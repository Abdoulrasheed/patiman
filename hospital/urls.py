from django.urls import path
from . import views


urlpatterns = [
	path('', views.homePage, name='home_page'),
	path('student/search/', views.search, name='search'),
	path('student/add', views.addPatient, name='add_patient'),
	path('student/detail', views.get_student_detail, name="search_detail"),
]