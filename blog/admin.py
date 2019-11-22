from django.contrib import admin
from .models import Tag, Author, Post, About

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(About)
