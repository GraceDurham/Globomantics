from django.urls import path


from . import views

urlpatterns = [
	path('', views.index, name='index'),
	repath(r'^\d+', views.detail, name='detail'),

]