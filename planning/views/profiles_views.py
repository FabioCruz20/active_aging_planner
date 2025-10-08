from django.shortcuts import render

def profile_view(request):
    """View para o perfil do usuário."""
    return render(request, 'profiles/profile.html')
