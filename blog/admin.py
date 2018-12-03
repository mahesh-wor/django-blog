from django.contrib import admin
from .models import Post , Tag 
# Register your models here.
admin.site.register(Post)  # from models class Post
#admin.site.register(Tags)
admin.site.register(Tag)
