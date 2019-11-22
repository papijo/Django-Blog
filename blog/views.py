from django.utils import timezone
from .models import Post, Tag, About, Author 
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def aboutus(request):

    about = get_object_or_404(About)
    
    return render(request, 'blog/staticpages/about.html', {
        'about': about,
    })

def contactus(request):
    return render(request, 'blog/staticpages/contactus.html')

def privacypolicy(request):
    return render(request, 'blog/staticpages/privacypolicy.html')


def post_list(request, tag_slug=None, author_slug = None):

    tag = None
    tags = Tag.objects.all()

    author = None
    authors = Author.objects.all()

    post = None
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tag=tag)

    if author_slug:
        author = get_object_or_404(Author, slug=author_slug)
        posts = Post.objects.filter(author=author)

    

    paginator = Paginator(posts, 1)
 
    # get the page parameter from the query string
    # if page parameter is available get() method will return empty string ''
    page = request.GET.get('page')
 
    try:
        # create Page object for the given page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'tag': tag,
        'tags': tags,
        'author': author,
        'authors': authors
    })
    


def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post})
