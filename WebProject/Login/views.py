from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm


# Create your views here.
def main(request):
    return render(request, 'Login/main.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'Login/register.html', {'form': form})


def login(request):
    return render(request, 'Login/login.html')


def logout(request):
    return render(request, 'Login/logout.html')


def test(request):
    return render(request, 'Login/test.html')


def updateuser(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('Logged-in')
    else:
        form = UserRegisterForm(instance=request.user)

    return render(request, 'Login/UpdateUser.html', {'form': form})
