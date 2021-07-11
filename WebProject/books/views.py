from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Book, Booking
from .filters import Search
from django.http.response import Http404
from .forms import BorrowForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def libirary(request):
    un = request.user.username
    Books = Book.objects.all()
    searchFilter = Search(request.GET, queryset=Books)
    Books = searchFilter.qs
    context = {'Books': Books, 'searchFilter': searchFilter, 'username': un}
    return render(request, 'books/lib.html', context)


def onebk(request, ISBN):
    try:
        book = Book.objects.get(pk=ISBN)
    except Book.DoesNotExist:
        return Http404("Doesn't Exist")
    return render(request, 'books/onebk.html', {'book': book})

@login_required(login_url='/login')
def bookings(request, pk):

    un = User.objects.get(username=pk)
    Books = Booking.objects.filter(bookedBy__username__contains=un)
    context = {"Bookings": Books, 'username': un}
    return render(request, 'books/bookings.html', context)

def borrow(request):
    form = BorrowForm()
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lib')
    context = {'form': form}
    return render(request, 'books/borrow.html', context)

@login_required(login_url='/login')
def edit(request, pk):
    borrowed = Booking.objects.get(id=pk)
    form = BorrowForm()
    if request.method == 'POST':
        form = BorrowForm(request.POST, instance=borrowed)
        if form.is_valid():
            form.save()
            return redirect('/lib')
    context = {'form': form, 'booking':borrowed}
    return render(request, 'books/edit.html', context)

@login_required(login_url='/login')
def delete(request, pk):
    booking = Booking.objects.get(id=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('/lib')

    context = {'Booking': booking}
    return render(request, 'books/edit.html', context)
