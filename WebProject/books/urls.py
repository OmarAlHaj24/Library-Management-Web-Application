from django.urls import path

from . import views

from . import views
app_name = 'books'

urlpatterns = [
    path('lib/<str:ISBN>/', views.onebk, name='onebk'),
    path('bookings/', views.bookings, name='bookings'),
    path('borrow/', views.borrow, name='borrow'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('about/',views.about,name='about'),
]
