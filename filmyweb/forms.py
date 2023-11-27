from django.forms import ModelForm
from .models import Movie, MoreInfo, Rating, Actor

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'premier', 'imdb_rating', 'poster']

class MoreInfoForm(ModelForm):
    class Meta:
        model = MoreInfo
        fields = ['time', 'genre']

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['review', 'stars']

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'surname']
