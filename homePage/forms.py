from django import forms 
from homePage.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput()) # ***** sign for password
    class Meta(): #in the database
        model = User
        fields = ('username','password','email')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your email'}),
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('occupation','company','location')
        widgets = {
            'occupation':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your occupation'}),
            'company':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your company'}),
            'location':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your location'}),
        }