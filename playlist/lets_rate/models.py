from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.


class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.genre}"

    
class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre, related_name="movies")
    rating = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.name}:{self.genre}:{self.rating}"


class Series(models.Model):
    name = models.CharField(max_length =50)
    genre = models.ManyToManyField(Genre, related_name="series")
    rating = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.name}:{self.genre}:{self.rating}"


class Movie_rating(models.Model):
    movie_rating = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie")
    review = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.movie_rating}:{self.review}"

class Series_rating(models.Model):
    series_rating = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="series")
    review = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.series_rating}:{self.review}"





