from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth import get_user_model
from .models import Blog_Post, User, Subscribers
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from .forms import SubscribersForm, MailMessageForm
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from gallery.models import Product, Order,Project, Account
from gallery.forms import ProductForm, OrderForm, ProjectForm, AccountForm
from django.contrib.auth.models import Group


def userPage(request):
    context = {}
    return render(request, 'web_users/userpage.html', context)


def blog(request):
    
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Subscription successful')
        return render(request, 'web_base/home.html')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
         
    context = {
        
        'posts' : Blog_Post.objects.all()
    }
    return render(request, 'web_base/blog.html', context)

class PostListView(ListView):
    model = Blog_Post
    template_name = 'web_base/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4
    
class UserPostListView(ListView): #used to get all the posts from a particular user
    model = Blog_Post
    template_name = 'web_base/user_blog_post.html'
    context_object_name = 'posts'
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog_Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Blog_Post

#@allowed_users(allowed_roles=['admin', 'superadmin'])
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog_Post
    fields = ['title','header_image','content' ]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog_Post
    fields = ['title', 'header_image','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Blog_Post 
    success_url = '/blog'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False          
    
def home(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Subscription successful')
        return render(request, 'web_base/home.html')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'web_base/home.html', context)

def about(request):
    return render(request, 'web_base/about.html')

def team_management(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Subscription successful')
        return render(request, 'web_base/home.html')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'web_base/team_mgt.html', context)


def services(request):
    return render(request, 'web_base/services.html')

def webdesign(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Subscription successful')
        return render(request, 'web_base/home.html')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'web_base/web_design.html', context)


def appDev(request):
    return render(request, 'web_base/app_dev.html')

def businessdevelopment(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Subscription successful')
        return render(request, 'web_base/home.html')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'web_base/bus_dev.html', context)
    

def marketingsales(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Subscription successful')
        return render(request, 'web_base/home.html')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'web_base/marketing_sales.html', context)
    

@login_required
#@allowed_users(allowed_roles=['admin', 'student','instructor', 'customer', 'superadmin'])
def resources(request):
    User = get_user_model()
    product = Product.objects.all()
    product_count = product.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    product_quantity = Product.objects.filter(name='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('gallery-products')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    
    
    return render(request, 'web_base/resources.html', context)

def contact(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Subscription successful')
        return render(request, 'web_base/home.html')
    else:
        form = SubscribersForm()
    context = {
        'form':form,
    }
    return render(request, 'web_base/contact.html', context)



def email_subscription(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to mail list')
            return render(request, 'web_base/email_subscription.html')
    else:
        form = MailMessageForm()
    context={
        'form':form,
    }
    return render(request, 'web_base/email_subscription.html', context)

def terms_and_conditions(request):
    
    return render(request, 'web_base/terms_and_conditions.html')

