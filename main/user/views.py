from .forms import  UserForm, SignUpForm
from .models import User
from user.custom_permission import AdminRequiredJsonMixin

from django.views import View
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views.generic.edit import FormView, CreateView
from django import forms
from django.core.exceptions import ValidationError

class CustomLoginView(LoginView):
    template_name = "user/login.html"
    redirect_authenticated_user = True


class UserView(AdminRequiredJsonMixin, View):
    def post(self, request, id, *args, **kwargs):
        try:
            user_instance = User.objects.get(id=id)
            form = UserForm(request.POST, instance=user_instance)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": ["success"]})
            return JsonResponse(form.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": [e.__str__()]}, status=400)


class PatientUserForm(forms.ModelForm):
    """"""
    user_type = forms.CharField(initial="PT", show_hidden_initial=True, disabled=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ("email",  "first_name", "last_name", "user_type")


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class SignUpView(FormView, CreateView):
    form_class = PatientUserForm
    template_name = "user/signup.html"
    success_url = "/home"
