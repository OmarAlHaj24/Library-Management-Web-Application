"""WebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Login import views as Login_views
from books import views as book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',Login_views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Login/logout.html'), name='logout'),
    path('', include('Login.urls')),
    path('lib/', book_views.libirary, name='libirary'),
    path('lib/<str:ISBN>/', book_views.onebk, name='onebk'),
    path('borrow/', book_views.borrow, name='borrow'),
    path('edit/<str:pk>/', book_views.edit, name='edit'),
    path('delete/<str:pk>/', book_views.delete, name='delete'),
    path('bookings/<str:pk>/', book_views.bookings, name='bookings'),
    path('about/', book_views.about, name='about'),

]
