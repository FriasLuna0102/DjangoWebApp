from django.shortcuts import redirect
from django.conf import settings

class RedirectIfNotAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if request.path == '/':
                return redirect('login')  # Redirige al login si no está autenticado
        response = self.get_response(request)
        return response
