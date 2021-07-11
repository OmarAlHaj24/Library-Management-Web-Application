import django_filters
from .models import *
from django_filters import DateFilter


class Search(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = "__all__"
