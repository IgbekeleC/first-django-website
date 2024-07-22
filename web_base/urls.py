from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostListView
)
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('', views.home, name = 'home'),
    
    path('team_management/', views.team_management, name = 'team-mgt'),
    path('about/', views.about, name = 'website-about'),
    
    path('marketingsales/', views.marketingsales, name = 'market-sales'),
    path('businessdevelopment/', views.businessdevelopment, name = 'bus-dev'),
    path('appDev/', views.appDev, name = 'app-dev'),
    path('webdesign/', views.webdesign, name = 'web-design'),
    path('services/', views.services, name = 'website-services'),
    
    path('blog/', PostListView.as_view(), name = 'website-blog'),
    path('blog/user/<str:username>/', UserPostListView.as_view(), name = 'user_blog-post'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('blog/new/', PostCreateView.as_view(), name = 'post-create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    #path('blog/', views.blog, name = 'website-blog'),
    
    path('users/', views.userPage, name = 'users'),
    path('resources', views.resources, name = 'dashboard'),
    path('contact/', views.contact, name = 'contact'),
    path('team/', views.about, name = 'comp-team'),
    #path('subscribe/', views.subscribe, name='subscribe'),
    path('email_subscription/', views.email_subscription, name='email-subscription'),
    path('terms_and_conditions/', views.terms_and_conditions, name = 'terms-and-conditions'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)