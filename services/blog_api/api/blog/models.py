from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image


STATUS = (
    (0, "DRAFT"),
    (1, "PUBLISH")
)


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=240, unique=True)
    slug = models.SlugField(max_length=240, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    full_img = models.ImageField(upload_to="full_imgs")
    thumb_img = models.ImageField(upload_to="thumb_imgs")
    tags = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        if (self.full_img):
            t_img = Image.open(self.full_img).copy()
            t_img.thumbnail(settings.THUMBNAIL_SIZE, Image.ANTIALIAS)
            t_img.save(settings.MEDIA_ROOT / "thumb_imgs" / self.full_img.name)
            self.thumb_img = "thumb_imgs/{}".format(self.full_img.name)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
