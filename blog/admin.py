from django.contrib import admin
from .models import BlogPost, Comments


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'body_text',
        'created_at',
        'updated_at',
    )

    ordering = ('created_at',)


admin.site.register(BlogPost, BlogPostAdmin)


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'comment',
        'post',
        'created_at',
    )
    search_fields = ('user', 'comment')
