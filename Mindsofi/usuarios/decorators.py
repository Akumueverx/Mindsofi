from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def role_required(allowed_roles=[]):
    """
    Decorador para vistas que comprueba si un usuario tiene uno de los roles permitidos.
    Redirige a su propio dashboard si no tiene permiso.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # Si el usuario no está autenticado, el decorador @login_required se encargará
            if not request.user.is_authenticated:
                return redirect('login')

            # Los superusuarios tienen acceso a todo
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            if request.user.rol in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                # Si no tiene el rol, lo redirigimos a su dashboard correspondiente
                return redirect('redirect_dashboard')
        return _wrapped_view
    return decorator