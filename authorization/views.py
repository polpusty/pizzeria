from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm, UserDetailsForm
from .models import UserDetails

User = get_user_model()


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect(request.GET.get('next', 'home'))

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form_register = RegisterForm(request.POST)
        form_user_details = UserDetailsForm(request.POST)

        if form_register.is_valid() and form_user_details.is_valid():
            user = User.objects.create_user(**form_register.cleaned_data)
            user_details = UserDetails(user=user, **form_user_details.cleaned_data)
            user_details.save()
            return redirect('login')

    else:
        form_register = RegisterForm()
        form_user_details = UserDetailsForm()

    return render(request, 'register.html', {'form_register': form_register, 'form_address': form_user_details})


@login_required()
def logout_user(request):
    logout(request)
    return redirect('home')
