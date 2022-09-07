from django.contrib import admin
from .models import Genre,Series,Movie,Movie_rating,Series_rating

# Register your models here.
admin.site.register(Genre)
admin.site.register(Series)
admin.site.register(Movie_rating)
admin.site.register(Movie)
admin.site.register(Series_rating)



