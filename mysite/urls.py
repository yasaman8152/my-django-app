"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from courses import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.urls', 'blog'), namespace='blog')),
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
    path('categories/', include(('categories.urls', 'categories'), namespace='categories')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    #path('media/', include(('media.urls', 'media'), namespace='media')),
    #path('cart/', views.cart_view, name='cart'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 👇 این خطو حتما بعد از urlpatterns بذار:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)