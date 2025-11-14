from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='list'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('course/<int:id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
]