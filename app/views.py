from django.shortcuts import render
from django.http import HttpResponse
from app.models import Movie, Producer, Produces

# Create your views here.

def index(request):

	movies    = Movie.objects.all()
	producers = Producer.objects.all()

	context_dict = {'movies': movies,
	                'producers': producers}

	return render(request, 'app/base.html', context_dict)
