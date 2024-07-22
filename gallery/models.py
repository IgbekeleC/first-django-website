from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import os
from django.urls import reverse

# Create your models here.

CATEGORY = (
    ('Computer', 'Computer'),
    ('Smart Phones','Smart Phones'),
    ('Tablet','Tablet'),
    ('Accessories', 'Acessories'),
    ('Printer', 'Printer'),
    ('Health', 'Health'),

)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    description = models.TextField(max_length=300, null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    User = settings.AUTH_USER_MODEL
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    comment = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'



CATEGORY = (
    ('Web Apps', 'Web Apps'),
    ('Mobile Apps', 'Mobile Apps'),
    ('Desktop Apps', 'Desktop Apps'),
    ('Website', 'Website'),
    ('Graphic Design', 'Graphic Design'),
    ('Others', 'Others'),
)
class Project(models.Model):
    User = settings.AUTH_USER_MODEL
    project_name= models.CharField(max_length=500, null=True)
    project_no = models.CharField(max_length=20, null=True)
    client_name=models.CharField(max_length=200, null=True)
    project_category=models.CharField(max_length=100, choices=CATEGORY, null=True)
    status= models.CharField(max_length=50, null=True)
    team_lead = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.team_lead}-{self.client_name}'
    
class Account(models.Model):
    User = settings.AUTH_USER_MODEL
    customer= models.CharField(max_length=200, null=True)
    total_purchase=models.IntegerField(default=0, null=True)
    total_paid=models.IntegerField(default=0, null=True)
    total_balance=models.IntegerField(default=0, null=True)
    account_manager= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.account_manager}-{self.total_balance}'
    
    
    