from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('about/', views.aboutus, name = 'aboutus'),
    path('contactus/', views.contactus, name = 'contactus'),
    path('privacypolicy', views.privacypolicy, name = 'privacypolicy'),
    #path('blog/<tag_slug>/', views.post_list, name = 'post_list_by_tag'),
    url(r'^tags/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    url(r'^authors/(?P<author_slug>[-\w]+)/$', views.post_list, name='post_list_by_author'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail')
]