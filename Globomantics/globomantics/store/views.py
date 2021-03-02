from django.core.exceptions import ViewDoesNotExist
from django.shortcuts import render
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
	return HttpResponse("Hello there, globomantics e-commerce store front coming here...")

def detail(request):
	return HttpResponse("Hello there, globomantics e-commerce store front detail pages coming here")

@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])
def electronics(request):

	items = ("Windows PC", "Apple Mac", "Apple iphone", "Lenovo", "Samsung", "Google")
	
	if request.method == 'GET':
		paginator = Paginator(items, 2)
		pages = request.GET.get('page', 1)
		
		try:
			items = paginator.page(pages)
		except PageNotAnInteger:
			items = paginator.page(1)
		return render(request, 'store/list.html', {'items':items})

	elif request.method == 'POST':
		return HttpResponseNotFound("Post method is not allowed")