from django.contrib import admin
from .models import Movie, MoreInfo, Rating, Actor

#admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #fields = ["title", "description", "year"]
    #exclude = ["description"]
    list_display = ["title", "imdb_rating", "year"]
    list_filter = ["year", "imdb_rating"]
    search_fields = ["title"]

admin.site.register(MoreInfo)
admin.site.register(Rating)
admin.site.register(Actor)
