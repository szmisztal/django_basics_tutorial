from django.db import models

class MoreInfo(models.Model):
    genre_list = {
        (0, 'Another'),
        (1, 'Horror'),
        (2, 'Comedy'),
        (3, 'Sci-Fi'),
        (4, 'Drama')
    }
    time = models.PositiveSmallIntegerField(default = 0, null = True, blank = True)
    genre = models.PositiveSmallIntegerField(default = 0, choices = genre_list, null = True, blank = True)

class Movie(models.Model):
    title = models.CharField(max_length = 64, blank = False, unique = True)
    year = models.PositiveSmallIntegerField(default = 2000)
    description = models.TextField(default = '')
    premier = models.DateField(null = True, blank = True)
    imdb_rating = models.DecimalField(max_digits = 4, decimal_places = 2, null = True, blank = True)
    poster = models.ImageField(upload_to = "posters", null = True, blank = True)
    more = models.OneToOneField(MoreInfo, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return f"{self.title} ({self.year})"

class Rating(models.Model):
    stars_list = {
        (0, '*'),
        (1, '**'),
        (2, '***'),
        (3, '****'),
        (4, '*****')
    }
    review = models.TextField(default = '', blank = True)
    stars = models.PositiveSmallIntegerField(default = 0, choices = stars_list, null = True, blank = True)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.stars_list}"

class Actor(models.Model):
    name = models.CharField(max_length = 32)
    surname = models.CharField(max_length = 32)
    movies = models.ManyToManyField(Movie, related_name = 'actor')

    def __str__(self):
        return f"{self.name} {self.surname}"

