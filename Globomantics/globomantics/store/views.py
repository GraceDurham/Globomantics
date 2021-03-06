from django.views import View
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.urls import path
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

from django.views.decorators.gzip import gzip_page
from django.views.generic import ListView, TemplateView
from django.views.decorators.http import require_http_methods


def index(request):
	return HttpResponse("Hello there, globomantics e-commerce store front coming here...")

def detail(request):
	return HttpResponse("Hello there, globomantics e-commerce store front detail pages coming here")

def logout(request):
	try:
		del request.session['customer']
	except KeyError:
		print("Error while logging out")
	return HttpResponse("Your logged out.")




@csrf_exempt
@cache_page(900)
@gzip_page
@require_http_methods(["GET"])

def electronics(request):
	items = ("Windows PC", "Apple Mac", "Apple iphone", "Lenovo", "Samsung", "Google")
	
	if request.method == 'GET':
		paginator = Paginator(items, 2)
		pages = request.GET.get('page', 1)
		name = "Sharu" # name of user logging into website hard coded but usually you make a database call to fetch creditionals or user name you want to display 
		try: 
			items = paginator.page(pages)
		except PageNotAnInteger:
			items = paginator.page(1)
		if not request.session.has_key('customer'): # Check if there is a session for that user if not than set a session key customer and value is their name
			request.session['customer'] = name
			print("Session value set")
		response = render(request, 'store/list.html', {'items':items})
		if request.COOKIES.get('visits'):
			value = int(request.COOKIES.get('visits'))
			print("Getting Cookie")
			response.set_cookie('visits', value + 1)
		else:
			value = 1
			print("Setting Cookie.")
			response.set_cookie('visits', value)
		return response 
	elif request.method == 'POST':
		return HttpResponseNotFound("Page Not Found")

class ElectronicsView(View):

	def get(self, request):
		items = ("Windows PC", "Apple Mac", "Apple iphone", "Lenovo", "Samsung", "Google")
		paginator = Paginator(items, 2)
		pages = request.GET.get('page', 1)
		self.process()

		try:

			items= paginator.pages(pages)
		except PageNotAnInteger:
			items= paginator.page(1)

		return render(request, 'store/list.html', {'items': items})


	def process(self):
		print("We are processing Electronics")


class ComputersView(ElectronicsView):
	def process(self):
		print("We are processing Computers")

class MobileView():
	pass

class EquipmentView(MobileView, ComputersView):
	pass

class ElectronicsView2(TemplateView):
	template_name = "store/list.html"

	def get_context_data(self, **kwargs):
		items = ("Windows PC", "Apple Mac", "Apple iphone", "Lenovo", "Samsung", "Google")
		context = {'items': items}
		return context


class ElectronicsView3(ListView):
	template_name = 'store/list.html' #1. Mention name of template file
	queryset = ("Windows PC", "Apple Mac", "Apple iphone", "Lenovo", "Samsung", "Google")
	#2 Show hard core data this will usually be a query to the database
	context_object_name = 'items'
	#3 Mention name of context object that will be used in the template file
	paginate_by = 2


	