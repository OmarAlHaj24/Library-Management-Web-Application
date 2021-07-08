from django.shortcuts import render, redirect
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# Create your views here.
def main(request):
    return render(request,'Login/main.html')


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request,'Login/register.html',{'form':form})

def login(request):
    return render(request,'Login/login.html')

def logout(request):
    return render(request,'Login/logout.html')

def test(request):
    return render(request,'Login/test.html')
