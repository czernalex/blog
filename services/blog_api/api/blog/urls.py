from django.urls import path

from .views import render_posts, render_post_detail, render_tags, render_tag_detail


urlpatterns = [
    path("", render_posts, name="posts"),
    path("tags/", render_tags, name="tags"),
    path("<slug:slug>/", render_post_detail, name="post_detail"),
    path("tags/<slug:slug>/", render_tag_detail, name="tag_detail"),
]
