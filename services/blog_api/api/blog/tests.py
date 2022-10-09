import os
import pytest

from django.contrib.auth.models import User

from .models import Post, Tag


@pytest.mark.django_db
def test_created_superuser(db, django_test_db_setup):
    default_user = User.objects.get(username=os.getenv("DJANGO_SUPERUSER_USERNAME", ""))
    assert default_user.is_superuser


# @pytest.mark.django_db
# def test_tag_create():
#     tag = Tag.objects.create(
        
#     )


# @pytest.mark.django_db
# def test_post_create():
#     ...
