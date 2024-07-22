from django.contrib import admin
from .models import Tutorial_Post, Comment_Tutoria,Video_Post,Comment_Video

# Register your models here.
admin.site.register(Tutorial_Post)
admin.site.register(Comment_Tutoria)
admin.site.register(Video_Post)
admin.site.register(Comment_Video)