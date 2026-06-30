# accounts/decorators.py

from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.profile.role == "ADMIN":
            return view_func(request, *args, **kwargs)

        messages.error(request, "Admin access required")
        return redirect('dashboard')

    return wrapper


def hr_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.profile.role == "HR":
            return view_func(request, *args, **kwargs)

        messages.error(request, "HR access required")
        return redirect('dashboard')

    return wrapper


def manager_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.profile.role == "MANAGER":
            return view_func(request, *args, **kwargs)

        messages.error(request, "Manager access required")
        return redirect('dashboard')

    return wrapper