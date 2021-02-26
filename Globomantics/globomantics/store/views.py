from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello there, globomantics e-commerce store front coming here...")

def detail(request):
	return HttpResponse("Hello there, globomantics e-commerce store front detail pages coming here")


def electronics(request):
	if request.method == 'GET':
		print(request.headers)
		print("----------\n", request)
		return HttpResponse("Hello there, globomantics e-commerce store front Electronics page coming here soon")

	elif request.method == 'POST':
		return HttpResponse("Post method is not allowed")