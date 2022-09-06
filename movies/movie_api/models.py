from django.db import models

# Create your models here.
class Rating(models.Model):
    movie_rating = models.IntegerField(range(1,0))
    series_rating = models.IntegerField(range(1,10))
    best_scene = models.CharField(max_length=1000)
    worst_scene = models.CharField(max_length=1000)
    favourite_actor = models.CharField(max_length=200)
    review = models.CharField(max_length=1000)
   
 

    def __str__(self):
        return f"{self.review}"    

class Movies(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=500)
    length = models.IntegerField()
    description = models.CharField(max_length=500)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name="my_movie_rating")

def __str__(self):
    return f"{self.name}"


class Series(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=500)
    season = models.IntegerField()
    episodes = models.IntegerField()
    description = models.CharField(max_length=1000)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name="my_series_rating")
    price = models.DecimalField(decimal_places=2,max_digits=8)


    def __str__(self):
        return f"{self.name} : {self.season} : {self.rating}"


