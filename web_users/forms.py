from django import forms
#from django.forms import ModelForm
#from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    instructor = 'instructor'
    student = 'student'
    customer = 'customer' 
    
    usertype = [
        (instructor, 'instructor'),
        (student, 'student'),
        (customer, 'customer'),
    ]
    
    usertype = forms.ChoiceField(required=True, choices=usertype)
    
    
    class Meta:
        User = get_user_model()
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

        labels = {
        'password1':'Password',
        'password2':'Confirm password',
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        User = get_user_model()
        model = User
        fields = ['username','first_name','last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
     class Meta:
        model = Profile
        fields = ['image']    

