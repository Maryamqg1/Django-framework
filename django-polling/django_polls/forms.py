# ======= forms for user creation (registeration)======

from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User

class  UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'email@example.com'
            }
        ),
    )
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Username'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {
                'class': 'form-input',
                'placeholder': 'Password1'
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'class': 'form-input',
                'placeholder': 'Password2'
            }
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
        