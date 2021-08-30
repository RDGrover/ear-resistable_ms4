from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'body_text',
        'created_at',
        'updated_at',
    )

    ordering = ('updated_at',)

admin.site.register(BlogPost, BlogPostAdmin)
