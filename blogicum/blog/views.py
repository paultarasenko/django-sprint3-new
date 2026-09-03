from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .constants import POSTS_LIMIT
from .models import Category, Post


def published_posts(manager=Post.objects):
    return manager.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )


def index(request):
    post_list = published_posts()[:POSTS_LIMIT]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(published_posts(), pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    post_list = published_posts(category.post_set)
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
