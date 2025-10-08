from django.shortcuts import render, redirect
from django.contrib import auth, messages

# Create your views here.

def login_view(request):
    """View para login de usuários"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard:index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'authentication/login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('auth:login')