from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='list'),
    path('category/<slug:slug>/', views.category_detail, name='detail'),
]
