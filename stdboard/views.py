from django.shortcuts import render, redirect,get_object_or_404
#from django.http import HttpResponseRedirect
#from requests import Request, request
from django.core.paginator import Paginator
from .models import User ,Tutorial_Post, Video_Post, Comment_Tutoria, Comment_Video
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
#from .decorators import unauthenticated_user, allowed_users, admin_only
from web_base.decorators import unauthenticated_user, allowed_users, admin_only
#from hitcount.views import HitCountDetailView
from stdboard.form import TutorialCommentForm, VideoForm, VideoCommentForm
from web_base.forms import SubscribersForm
from django.contrib import messages


# Create your views here.



@login_required
#@allowed_users(allowed_roles=['admin', 'student']) 
def videofile(request):
    video = Video_Post.objects.all()
    paginator = Paginator(video, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        vform = VideoForm(request.POST)
        if form.is_valid() and vform.is_valid():
            vform.save()
            form.save()
        messages.success(request, 'video uploaded successfully')
        messages.success(request, 'Subscription successful')
        return render(request, 'stdboard/video.html')
   
    else:
        vform = VideoForm()
        form = SubscribersForm()

    return render(request, 'stdboard/video.html',{'page_obj': page_obj, 'video' : video, 'vform':vform, 'form':form})    


@login_required
#@allowed_users(allowed_roles=['admin', 'student'])
def tutorial(request):
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
        'posts' : Tutorial_Post.objects.all()
    }
    return render(request, 'stdboard/tutorial.html', context)

class PostListView(ListView):
    model = Tutorial_Post
    template_name = 'stdboard/tutorial.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4
   
class UserPostListView(ListView): #used to get all the posts from a particular user
    model = Tutorial_Post
    template_name = 'stdboard/tutorial_user.html'
    context_object_name = 'posts'
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Tutorial_Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Tutorial_Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Tutorial_Post
    fields = ['title', 'image','content' ]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Tutorial_Post
    fields = ['title', 'image', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Tutorial_Post 
    success_url = '/dashboard'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  

@login_required
#@admin_only
def create_forum(request):
    
    context = {}
    return render(request, 'stdboard/forum_discuss.html', context)

@login_required
def tcomment(request):
    t_comment = Comment_Tutoria.objects.all()
    if request.method == 'POST':
        t_form = TutorialCommentForm(request.POST)
        if t_form.is_valid():
            t_form.save()
        messages.success(request, 'comment posted successfully')
        return render(request, 'stdboard/tutorial.html')
   
    else:
        t_form = TutorialCommentForm()
    context = { 
        't_form':t_form
        }
    return render(request, 'stdboard/tutorial.html', context)

@login_required
def vcomment(request):
    video_comment = Comment_Video.objects.all()
    if request.method == 'POST':
        v_form = VideoCommentForm(request.POST)
        if v_form.is_valid():
            v_form.save()
        messages.success(request, 'comment posted successfully')
        return render(request, 'stdboard/video.html')
   
    else:
        v_form = VideoCommentForm()
    context = {
        'v_form':v_form
        }
    return render(request, 'stdboard/video.html', context)
    
    
    
