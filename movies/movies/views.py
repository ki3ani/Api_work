from django.http import JsonResponse
from .models import Movie
from serializers import MovieSerializer



def movie_list(request):

    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse(serializer.data, safe=False)
    
