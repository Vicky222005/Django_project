from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomuserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
