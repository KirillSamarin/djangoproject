from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    phone_number = forms.CharField(max_length=20, required=False, label="Номер телефона")
    country = forms.CharField(max_length=60, required=False, label="Страна")
    avatar = forms.ImageField(required=False, label="Аватар")

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name',
                  'phone_number', 'country', 'password1', 'password2']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять только из цифр")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует")
        return email

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1']
