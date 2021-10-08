from django.shortcuts import render

from .models import Movie
from reviews.models import Review
from actors.models import Actor

# Create your views here.
def movie_detail_view(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)
    cast = movie.actor_set.all()
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews, 'cast': cast})