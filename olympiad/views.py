from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.set_unusable_password()
            user.save()
            return redirect('main')
        else:
            return render(request, 'register.html', {'form': form, 'errors': 'Произошла ошибка'})
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def main(request):
    return render(request, 'main.html')


