from django.shortcuts import get_object_or_404, render

from .models import Group, Post


LIST_LENGHT: int = 10


def index(request):
    posts = Post.objects.all()[:LIST_LENGHT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:LIST_LENGHT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
