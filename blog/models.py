from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length = 150, db_index = True)
    slug = models.SlugField(max_length = 150, db_index = True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ('name', )
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('blog:post_list_by_tag', args=[self.slug])


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/author/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

    def author_image(self):
        return format_html('<img src = "/media/%s" width="100" height="100" />' % (self.image))
    author_image.short_description = 'Image'
    author_image.allow_tags = True

    def get_absolute_url(self):
        return reverse ('blog:post_list_by_author', args=[self.slug])

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length=200)
    byline = models.CharField(max_length= 100)
    text = models.TextField()
    text2 = models.TextField(blank=True, null = True)
    text3 = models.TextField(blank=True, null = True)
    text4 = models.TextField(blank=True, null = True)
    midheading = models.CharField(max_length=100, blank=True, null = True)
    text5 = models.TextField(blank=True, null = True)
    bodyimage = models.ImageField(upload_to='blog/post/%Y/%m/%d', blank=True)
    imagecaption = models.CharField(max_length=100, blank=True, null = True)
    text6 = models.TextField(blank=True, null = True)
    text7 = models.TextField(blank=True, null = True)
    midheading2 = models.CharField(max_length=100, blank=True, null = True)
    text8 = models.TextField(blank=True, null = True)
    text9 = models.TextField(blank=True, null = True)
    midheading3 = models.CharField(max_length=100, blank=True, null = True)
    text10 = models.TextField(blank=True, null = True) 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE, null = True)
    headerimage = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True)
    


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    
    def get_tag_list(self):
        return (self.tag)
    
    def post_image(self):
        return format_html('<img src = "/media/%s" width="100" height="100" />' % (self.image))
    post_image.short_description = 'Image'
    post_image.allow_tags = True

    class Meta:
        ordering = ["-published_date"]

class About(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    p1 = models.TextField(null=True)
    p2 = models.TextField(null=True)
    p3 = models.TextField(null=True)
    image = models.ImageField(upload_to='blog/owner/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

    def owner_image(self):
        return format_html('<img src = "/media/%s" width="100" height="100" />' % (self.image))
    owner_image.short_description = 'Image'
    owner_image.allow_tags = True