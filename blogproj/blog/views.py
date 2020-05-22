from django.shortcuts import render
from .models import Blog
from .models import Movie
# Create your views here.

def home(request):
    blogs = Blog.objects
    movies = Movie.objects
    return render(request, 'home.html', {'BLOG':blogs, 'movies':movies})
