from django.core.exceptions import ViewDoesNotExist
from django.shortcuts import render
from django.urls import path
from django.views.generic.base import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
	return HttpResponse("Hello there, globomantics e-commerce store front coming here...")

def detail(request):
	return HttpResponse("Hello there, globomantics e-commerce store front detail pages coming here")

@csrf_exempt
@cache_page(900)
@require_http_methods(["GET"])

class ElectronicsView(View):

	def get(self, request):
		items = ("Windows PC", "Apple Mac", "Apple iphone", "Lenovo", "Samsung", "Google")
		paginator = Paginator(items, 2)
		pages = request.GET.get('page', 1)


		try:

			items= paginator.pages(pages)
		except PageNotAnInteger:
			items= paginator.page(1)

		return render(request, 'store/list.html', {'items': items})

class ElectronicsView2(TemplateView):
	template_name = "store/list.html"

	def get_context_data(self, **kwargs):
		items = ("Windows PC", "Apple Mac", "Apple iphone", "Lenovo", "Samsung", "Google")
		context = {'items': items}
		return context

	