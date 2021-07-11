from django.shortcuts import render
from .models import Book
from .filters import Search
from django.http.response import Http404


# Create your views here.


def libirary(request):
    Books = Book.objects.all()
    searchFilter = Search(request.GET, queryset=Books)
    Books = searchFilter.qs
    context = {'Books': Books, 'searchFilter': searchFilter}
    return render(request, 'books/lib.html', context)


def onebk(request, ISBN):
    try:
        book = Book.objects.get(pk=ISBN)
    except Book.DoesNotExist:
        return Http404("Doesn't Exist")
    return render(request, 'books/onebk.html', {'book': book})
