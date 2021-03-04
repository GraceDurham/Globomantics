from django.urls import path, re_path


from . import views
from .views import ElectronicsView

urlpatterns = [
	path('', views.index, name='index'),
	re_path(r'^\d+', views.detail, name='detail'),
	#re_path(r'^electronics', views.electronics, name='electronics')
	re_path(r^'electronics', ElectronicsView.as_view(), name='electronics'),

]