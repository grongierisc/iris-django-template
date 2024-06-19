from django.contrib import admin

# Register your models here.
from community.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
