from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('lib/<string:ISBN>/', views.onebk, name='onebk')

]
