from django import forms
from .models import Recipe
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


# Maqola qo'shish saxifasi uchun
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Recipe              # modelsdagi Recipe jadvalini olamiz
        fields = [                  # fields --> ko'rinishi kerak bo'lgan polyalar
            'title',
            'content',
            'photo',
            # 'is_published',
            'category',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Nomi'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Text'
            }),
            # 'is_published': forms.CheckboxInput(attrs={
            #     'class': 'form-check-input'
            # }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            })

        }

# kirish saxifasi uchun
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Foydalanuvchi ismi', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    }))
    password = forms.CharField(label='Parol', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol'
    }))



# Registratsiya saxifasi uchun
class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ism'
    }))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Familiya'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parolni qaytaring'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2') # fields --> ko'rinishi kerak bo'lgan polyalar

