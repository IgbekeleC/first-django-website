from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from stdboard import views
from django.contrib.auth import views as web_base_views
from django.contrib.auth import views as stdboard_views
from django.conf import settings
from django.conf.urls.static import static
from web_users import views as web_user_views
from stdboard import views as stdboard_views
from stdboard.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
    )

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('web_base.urls')),
    path('', include('gallery.urls')),
    
    #path('userpage/', web_user_views.userPage, name='user-page'),
    path('register/', web_user_views.register, name='register'),
    path('profile/', web_user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='web_users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='web_users/logout.html'), name='logout'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='web_users/password_reset.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='web_users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='web_users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='web_users/password_reset_complete.html'), name='password_reset_complete'),
    
   
    path('video/', views.videofile, name = 'video'),

    
    path('tutorial/', stdboard_views.tutorial, name='tutorial'),
    path('tutorial/', PostListView.as_view(), name = 'tutorial'),
    path('tutorial/user/<str:username>/', UserPostListView.as_view(), name = 'tutorial-user'),
    path('tutorial/<int:pk>/', PostDetailView.as_view(), name = 'tutorial-detail'),
    path('tutorial/new/', PostCreateView.as_view(), name = 'create-tutorial'),
    path('tutorial/<int:pk>/update/', PostUpdateView.as_view(), name = 'update-tutorial'),
    path('tutorial/<int:pk>/delete/', PostDeleteView.as_view(), name = 'delete-tutorial'),
    
    path('tcomment/', views.tcomment, name='tcomment'),
    path('vcomment/', views.vcomment, name='vcomment'),
    path('create_forum/', stdboard_views.create_forum, name='forum'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
