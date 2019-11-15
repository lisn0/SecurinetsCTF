 
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField, CaptchaTextInput
import re
# from account.models import Person

def username_validate(value):
    username_re = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]{2,18}$')
    if not username_re.match(value):
        raise ValidationError('Username Format error')
    elif User.objects.filter(username=value).exists():
        raise ValidationError('This account already exists')


class UserForm(forms.ModelForm):
    # field password override that in Person
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Please enter a 6-18 digit password'}
        ),
        min_length=6,
        max_length=18,
        label="password",
        required=True,
        error_messages={
            'required': 'Please enter your password',
            'min_length': 'Password is too short',
            'max_length': 'Password is too long',
        }
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Please enter your password again'}
        ),
        min_length=6,
        max_length=18,
        label="Repeat the password",
        required=True,
        error_messages={
            'required': 'Please enter your password again',
            'min_length': 'Password is too short',
            'max_length': 'Password is too long',
        }
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Please enter your username'}
        ),
        validators=[username_validate],
        error_messages={
            'required': 'Please fill in the username',
            'max_lengh': 'max 30',
            'min_length': 'min 5',
        },
        label='Username',
        max_length=30,
        min_length=5,
        required=True
    )


    # verify password
    def clean_confirm_password(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        re_password = re.compile('^[a-zA-Z]\w{5,17}$')
        if password != confirm_password:
            raise forms.ValidationError('Two passwords are inconsistent')
        if (not re_password.match(password)) or (not re_password.match(confirm_password)):
            raise forms.ValidationError('Passwords begin with a letter and can only contain letters, numbers, and underscores')
        return cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password',)


# class BasePersonForm(forms.ModelForm):
#     institute = forms.CharField(
#         widget=forms.Select(
#             choices=(
#                 (u'ISI', 'ISI'),
#             ),
#             attrs={'class': 'form-control', 'placeholder': 'Please select a college'},
#         ),
#         label='college',
#         max_length=15,
#         required=True,
#         error_messages={
#             'required': 'Please select a college'
#         }
#     )
#
#     class Meta:
#         model = Person
#         fields = ('institute',)
