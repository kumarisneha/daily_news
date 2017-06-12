import uuid

from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django import forms
from janitriapp.choices import INTEREST_CHOICES

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label=_("Email address"), required=True,
        help_text=_("Required."), widget=forms.TextInput(
            attrs={'value':'', 'placeholder':'Email Address', 'class': 'form-control input-md'}
            )
        )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password', 'class': 'form-control input-md'}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={'placeholder':'Confirm Password', 'class': 'form-control input-md'}
        ),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    interest = forms.ChoiceField(
        choices = INTEREST_CHOICES, 
        label=_("Select your interest"), initial='', 
        widget=forms.Select( attrs={'class': 'form-control input-md'}), 
        required=True,
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "interest")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        interest = self.cleaned_data["interest"]
        user.username = str(user.email).split('@')[0] + str(uuid.uuid4())
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.data["email"]
        user_obj= User.objects.filter(email= email)
        if len(user_obj) > 0:
            raise ValidationError("Email id already exist.") 
        return self.data["email"]
