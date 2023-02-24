from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta:
        fields = ('username','email','first_name','last_name','password1','password2','designation')
        widgets = {
            'designation':forms.RadioSelect,
        }
        model = User