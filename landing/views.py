from django.shortcuts import render

def landing_page(request):
    """
    View para a landing page com efeito parallax.
    """
    return render(request, 'landing/index.html')
