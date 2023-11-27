from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, MoreInfo, Rating, Actor
from .forms import MovieForm, MoreInfoForm, RatingForm, ActorForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, MovieSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def all_movies(request):
    all = Movie.objects.all()
    return render(request, 'movies.html', {'my_movies': all})

@login_required
def new_movie(request):
    new = True
    form_movie = MovieForm(request.POST or None, request.FILES or None)
    form_more_info = MoreInfoForm(request.POST or None)
    form_rating = RatingForm(request.POST or None)
    form_actor = ActorForm(request.POST or None)

    if form_movie.is_valid() and form_more_info.is_valid():
        movie = form_movie.save(commit = False)
        more = form_more_info.save()
        movie.more = more
        movie.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form': form_movie, 'form_more_info': form_more_info, 'new': new,
                                               'form_rating': form_rating, 'form_actor': form_actor})

@login_required
def edit_movie(request, id):
    new = False
    movie = get_object_or_404(Movie, pk = id)
    reviews = Rating.objects.filter(movie = movie)
    actors = Actor.objects.filter(movies = movie)

    try:
        more_info = MoreInfo.objects.get(movie = movie.id)
    except MoreInfo.DoesNotExist:
        more_info = None

    form_movie = MovieForm(request.POST or None, request.FILES or None, instance = movie)
    form_more_info = MoreInfoForm(request.POST or None, instance = more_info)
    form_rating = RatingForm(request.POST or None)
    form_actor = ActorForm(request.POST or None)

    if request.method == 'POST':
        if 'stars' in request.POST:
            rating = form_rating.save(commit = False)
            rating.movie = movie
            rating.save()
    if request.method == 'POST':
        if 'name' and 'surname' in request.POST:
            actor = form_actor.save(commit = False)
            actor.save()
            movie.actor.add(actor)
            movie.save()

    if form_movie.is_valid() and form_more_info.is_valid():
        movie = form_movie.save(commit = False)
        more = form_more_info.save()
        movie.more = more
        movie.save()
        return redirect(all_movies)

    return render(request, 'movie_form.html', {'form': form_movie, 'form_more_info': form_more_info,
                                               'reviews': reviews, 'form_rating': form_rating,
                                               'new': new, 'form_actor': form_actor, 'actors': actors})

@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk = id)

    if request.method == "POST":
        movie.delete()
        return redirect(all_movies)

    return render(request, 'delete.html', {'movie': movie})

