from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'proTrack/home.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("Usuario autenticado correctamente")  # Mensaje de depuración
                return redirect('proTrack:dashboard')
            else:
                print("Error de autenticación")  # Mensaje de depuración
        else:
            print(form.errors)  # Mensaje de depuración
    else:
        form = AuthenticationForm()
    return render(request, 'proTrack/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'proTrack/dashboard.html')
