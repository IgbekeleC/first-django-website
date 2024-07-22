from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import os
from django.urls import reverse


# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class User(AbstractUser):
    pass


class UserProfileInfo(models.Model):
    
    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes
    bio = models.CharField(max_length=500)
    instructor = 'instructor'
    student = 'student'
    customer = 'customer'
    
    usertype = [
        (instructor, 'instructor'),
        (student, 'student'),
        (customer, 'customer'),
    ]
    usertype = models.CharField(max_length=10, choices=usertype, default=student)

    def __str__(self):
        return self.user.username


class Blog_Post(models.Model):
    
    title = models.CharField(max_length=200)
    header_image = models.ImageField(null=True, blank=True, upload_to="profile_pics/")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    
    def __str__(self):
        return self.title



    
