from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm




def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # username = request.POST['username']
        # password = request.POST['password']
        # email = request.POST['email']
        # user = User.objects.create_user(username=username, password=password, email=email)
        # user.save()
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + user)
        return redirect('login')

    else:
        return render(request, 'SignUp.html',{'form':form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'Login.html')


@login_required()
def dashboard(request):
    users = User.objects.all()
    return render(request, 'Dashboard.html', {'users': users})


def logout(request):
    auth.logout(request)
    return redirect('login')
