import os
import pytest

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import RequestFactory
from django.utils.text import slugify

from .models import Post, Tag
from .views import (
    render_post_detail,
    render_posts,
    render_tag_detail,
    render_tags
)


@pytest.mark.django_db
def test_superuser_exists(db, django_test_db_setup):
    default_user = User.objects.get(
        username=os.getenv("DJANGO_SUPERUSER_USERNAME", "")
    )
    assert default_user.is_superuser


@pytest.mark.django_db
def test_tag_create():
    tag = Tag.objects.create(
        title="computers",
        slug="computers"
    )
    assert tag.title == "computers"
    assert tag.slug == "computers"


@pytest.mark.django_db
def test_tag_str_method():
    tags = Tag.objects.all()
    for tag in tags:
        assert tag.title == str(tag)


@pytest.mark.django_db
def test_tags_view():
    path = reverse("tags")
    request = RequestFactory().get(path)
    response = render_tags(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_tag_detail_view():
    tags = Tag.objects.all()
    for tag in tags:
        path = reverse("tag_detail", kwargs={"slug": tag.slug})
        request = RequestFactory().get(path)
        response = render_tag_detail(request, tag.slug)
        assert response.status_code == 200


@pytest.mark.django_db
def test_post_str_method():
    posts = Post.objects.all()
    for post in posts:
        assert post.title == str(post)


@pytest.mark.django_db
def test_posts_view():
    path = reverse("posts")
    request = RequestFactory().get(path)
    response = render_posts(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_view():
    posts = Post.objects.all()
    for post in posts:
        path = reverse("post_detail", kwargs={"slug": post.slug})
        request = RequestFactory().get(path)
        response = render_post_detail(request, post.slug)
        assert response.status_code == 200


@pytest.mark.django_db
def test_post_create():
    post = Post.objects.create(
        title="Porcupine Enjoying Being Petted Like a Dog Delights Internet",
        slug=slugify("Porcupine Enjoying Being Petted Like a Dog Delights Internet"),
        author=User.objects.get(
            username=os.getenv("DJANGO_SUPERUSER_USERNAME","")
        ),
        content="The clip of Charlie the prehensile tailed porcupine was first shared on TikTok by Jawnie Payne—who uses the handle zookeeperjawnie—in June 2021, and has since been posted again on the popular Reddit forum r/aww where it has gained over 82,000 upvotes and hundreds of comments.",
        status=1,
        full_img="full_imgs/charlie_porcupine.jpeg",
    )
    post.tags.add(Tag.objects.get(title="nature"))
    assert post.title == "Porcupine Enjoying Being Petted Like a Dog Delights Internet"
    assert str(post) == "Porcupine Enjoying Being Petted Like a Dog Delights Internet"
    assert post.thumb_img == "thumb_imgs/charlie_porcupine.jpeg"
    assert post.status == 1
    assert post.tags.first().title == "nature"


@pytest.mark.django_db()
def test_adding_new_tag_to_post():
    tag = Tag.objects.create(
        title="animals",
        slug="animals"
    )
    post = Post.objects.first()
    post.tags.add(tag)
    assert post.tags.last().title == "animals"


@pytest.mark.django_db()
def test_removing_tags_from_post():
    post = Post.objects.first()
    post.tags.remove()
    assert post.tags.all().count() == 0
