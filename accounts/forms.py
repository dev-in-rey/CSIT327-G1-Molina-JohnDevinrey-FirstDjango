from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class BootstrapFormMixin:
    def _apply_bootstrap_classes(self):
        for name, field in self.fields.items():
            css = field.widget.attrs.get("class", "")
            classes = css.split() if css else []
            if "form-control" not in classes:
                classes.append("form-control")
            if self.is_bound and self.errors.get(name):
                if "is-invalid" not in classes:
                    classes.append("is-invalid")
            field.widget.attrs["class"] = " ".join(classes)


class CustomAuthenticationForm(BootstrapFormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_bootstrap_classes()


class CustomerUserCreationForm(BootstrapFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "course")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_bootstrap_classes()


class ProfileUpdateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "course")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_bootstrap_classes()
