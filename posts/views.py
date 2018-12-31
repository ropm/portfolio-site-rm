from django.shortcuts import render
from .models import Posts

# Create your views here.
def postsView(request):
    posts = Posts.objects.all()[:10]    #first 10 posts

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts.html', context)

def details(request, id):
    postbyid = Posts.objects.get(id=id)

    context = {
        'post': postbyid
    }
    return render(request, 'details.html', context)