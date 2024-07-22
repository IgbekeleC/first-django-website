from django.contrib import admin
from .models import Blog_Post, User, UserProfileInfo, Subscribers, MailMessage


# Register your models here.

admin.site.register(User)
admin.site.register(UserProfileInfo)
admin.site.register(Blog_Post)
admin.site.register(Subscribers)
admin.site.register(MailMessage)

