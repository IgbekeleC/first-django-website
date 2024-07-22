from django import forms
from .models import Subscribers, MailMessage
#from django.contrib.auth.forms import UserCreationForm

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email',]
        
class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'