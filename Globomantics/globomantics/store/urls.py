from django.urls import path, re_path


from . import views


urlpatterns = [
	path('', views.index, name='index'),
	re_path(r'^\d+', views.detail, name='detail'),
	re_path(r'^electronics', views.electronics, name='electronics'),
	# re_path(r'^electronics', ElectronicsView2.as_view(), name='electronics'),
	# re_path(r'^electronics', ElectronicsView3.as_view(), name='electronics')
	# re_path(r'^electronics', EquipmentView.as_view(), name='electronics'),
]