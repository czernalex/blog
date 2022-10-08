from django.contrib import admin

from .models import Tag, Post


class TagAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    search_field = (
        "title",
    )
    prepopulated_fields = {
        "slug": ("title",)
    }


class PostAdmin(admin.ModelAdmin):
    exclude = ("thumb_img",)
    list_display = (
        "title",
        "slug",
        "author",
        "status",
        "created_on",
        "full_img",
        "thumb_img",
    )
    list_filter = (
        "status",
    )
    search_filed = [
        "title",
        "content",
    ]
    prepopulated_fields = {
        "slug": ("title",)
    }


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
