from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from users.forms import UserLoginForm, UserUpdate


# Create your views here


def create_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'users/create_user.html', context=context)


def user_update(request):
    try:
        user_ = User.objects.get(id=request.user.id)
    except Task.DoesNotExist:
        return redirect('home')
    form = UserUpdate(instance=user_)

    if request.method == 'POST':
        form = UserUpdate(request.POST, instance=user_)
        if form.is_valid():

            form.save()
            return redirect('user-profile')

    context = {'form': form}

    return render(request, 'users/user_update.html', context=context)


def profile(request):
    return render(request, 'users/user_profile.html')


def user_login(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(request, username=user_name, password=user_password)
            if user:
                login(request, user)
                return redirect('user-profile')

    context = {'form': form}

    return render(request, "users/user_login.html", context=context)


def user_logout(request):
    logout(request)
    return redirect('user-profile')

