from django import forms  # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationform  # type: ignore

class UserCreationForm(UserCreationForm):
    