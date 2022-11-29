from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class SuperUserRequiredMixin(AccessMixin):
    """Verify that the current user is admin user.This will work only For class based view"""

    def dispatch(self, request, *args, **kwargs):
        """_"""
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

