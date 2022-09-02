from django.contrib import admin
from .models import Movies,Series,Rating

# Register your models here.

admin.site.register(Movies)
admin.site.register(Series)
admin.site.register(Rating)

