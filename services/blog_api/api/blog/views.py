from django.shortcuts import render
from django.db.models import Count


from .models import Post, Tag


def render_posts(request):
    return render(
        request,
        "posts.html",
        context={
            "posts": Post.objects.filter(status=1).order_by("-created_on")[:3]
        }
    )


def render_post_detail(request, slug):
    return render(
        request,
        "post_detail.html",
        context={
            "post": Post.objects.get(slug__iexact=slug)
        }
    )


def render_tags(request):
    return render(
        request,
        "tags.html",
        context={
            "tags": Tag.objects.annotate(posts_count=Count("post")).order_by("-posts_count").all()
        }
    )


def render_tag_detail(request, slug):
    return render(
        request,
        "tag_detail.html",
        context={
            "tag": Tag.objects.get(slug__iexact=slug)
        }
    )
