from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.urls import reverse


# Create your models here.


class Tutorial_Post(models.Model):
    User = settings.AUTH_USER_MODEL
    title = models.CharField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to="profile_pics/")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('tutorial-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']   
    
class Video_Post(models.Model):
    User = settings.AUTH_USER_MODEL
    caption = models.CharField(max_length=500)
    video = models.FileField(upload_to='video/%y')#, null=True, verbose_name="")
    description = models.TextField(max_length=500, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #url = EmbedVideoField()
    
    #def __str__(self):
        #return self.caption + ": " + str(self.video)
    
    def __str__(self):
        return self.caption
    
    class Meta:
        ordering = ['-date_posted']
         
       
    
    
class Comment_Tutoria(models.Model):
    User = settings.AUTH_USER_MODEL
    post = models.ForeignKey(Tutorial_Post, related_name='comments', on_delete=models.CASCADE )
    user = models.CharField(max_length=100, null=True)
    body = models.TextField(max_length=255, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.user)
    
    class Meta:
        ordering = ['-date_posted']
        
class Comment_Video(models.Model):
    User = settings.AUTH_USER_MODEL
    post = models.ForeignKey(Video_Post, related_name='comments', on_delete=models.CASCADE )
    user = models.CharField(max_length=100, null=True)
    body = models.TextField(max_length=255, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.user)
    
    class Meta:
        ordering = ['-date_posted']