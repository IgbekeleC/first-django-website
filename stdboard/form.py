from django import forms
from .models import Comment_Tutoria, Video_Post, Comment_Video

class TutorialCommentForm(forms.ModelForm):
    class Meta:
        model = Comment_Tutoria
        fields = ['body']

class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = Comment_Video
        fields = ['body']
        
class VideoForm(forms.ModelForm):
    class Meta:
        model= Video_Post
        fields= ["caption", "video", "description"]
