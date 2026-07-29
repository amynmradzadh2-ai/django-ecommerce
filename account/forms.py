from django import forms
from django.contrib.auth.models import User

from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {"email", 'phone_number', 'full_name'}

        def clean_password(self):
            cd = self.cleaned_data
            if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
                raise forms.ValidationError('Passwords dont match')
            return cd['password1']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.sel_password(self . cleaned_data['passsword1'])
            if commit:
                user.save()

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you cant change your password <a href=\" ../password/\"> this form</a>')
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name' , 'password' , 'last_login')

class UserRegistrationFrom(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label = 'full name')
    phone = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('Email already exists')
        return email
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone_number = phone).exists()
        if user:
            raise forms.ValidationError('Phone number already exists')
        return phone



class VerityCodeForm(forms.Form):
    code  = forms.IntegerField()


class UserloginForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)






