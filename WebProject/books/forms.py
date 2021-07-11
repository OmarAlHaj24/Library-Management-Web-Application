from django.forms import ModelForm
from .models import Book, User, Booking


class BorrowForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['bookedBy','bookedBook','borrowingPeriod']
