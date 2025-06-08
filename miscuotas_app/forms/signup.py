from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ..models import Curso

class SignUpForm(UserCreationForm):
    ROLE_CHOICES = [
        ('apoderado', 'Apoderado'),
        ('tesorero', 'Tesorero'),
        ('manager', 'Manager'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    nombre = forms.CharField(required=False)
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "role", "nombre", "curso")