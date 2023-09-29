from django.urls import path
from . import views

app_name = 'dataentry'

urlpatterns = [
	path('', views.view_record, name='view_record'),

	path('single_record_information/<str:pk>/', views.single_record_information, name='single_record_information'),
 
	path('confirm_print/<str:pk>/', views.confirm_print, name='confirm_print'),
 
	path('al_razi/<str:pk>/', views.al_razi, name='al_razi'),
 
	path('noor_ul_ship/<str:pk>/', views.noor_ul_ship, name='noor_ul_ship'),
 
	path('al_gharbia/<str:pk>/', views.al_gharbia, name='al_gharbia'),
 
	path('badr_al_sama/<str:pk>/', views.badr_al_sama, name='badr_al_sama'),
]