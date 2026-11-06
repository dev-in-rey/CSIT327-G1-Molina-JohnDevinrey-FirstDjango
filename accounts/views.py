from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import (
    CustomerUserCreationForm,
    CustomAuthenticationForm,
    ProfileUpdateForm,
)
from .models import CustomUser


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "registration/login.html"


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomerUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Account created successfully! Please log in."


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        pk = kwargs.get("pk")
        if pk is not None and pk != request.user.pk:
            raise PermissionDenied("You cannot view another user's profile.")
        return super().dispatch(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("profile")
    success_message = "Your profile has been updated successfully!"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        if pk is not None and pk != self.request.user.pk:
            raise PermissionDenied("You cannot edit another user's profile.")
        return self.request.user
