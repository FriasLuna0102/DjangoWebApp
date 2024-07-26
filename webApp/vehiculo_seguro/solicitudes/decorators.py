from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group

def agente_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.groups.filter(name='Agentes').exists():
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
