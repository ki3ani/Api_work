from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100)

    
class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre, related_name="movies")
    rating = models.IntegerField( range(1,11))


class Series(models.Model):
    name = models.CharField(max_length =50)
    genre = models.ManyToManyField(Genre, related_name="series")
    rating = models.IntegerField( range(1,11))


class Movie_rating(models.Model):
    movie_rating = models.ForeignKey(Movie, related_name="movie")
    review = models.CharField(max_length=500)

class Series_rating(models.Model):
    series_rating = models.ForeignKey(Series, related_name="series")
    review = models.CharField(max_length=500)





