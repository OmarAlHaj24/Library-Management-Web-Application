from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('loggedin/', views.test, name='Logged-in'),
    path('update/', views.updateuser, name='update')
]
