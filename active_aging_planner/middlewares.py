from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """Middleware to require login for all views except login."""

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        path = request.path
        allowed_urls = [
            reverse('landing_page'),
            reverse('auth:login'),
        ]

        # Check if user is authenticated, if path is in allowed urls, or if path is related to admin pages or django live server.
        if (
            request.user.is_authenticated 
            or path.startswith('/__reload__/')
            or path.startswith('/admin/')
            or path in allowed_urls
        ):
            return self.get_response(request)
        
        return redirect('auth:login')
