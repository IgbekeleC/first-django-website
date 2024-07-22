from django import forms
from .models import Product, Order, Project, Account


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'order_quantity']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = '__all__'