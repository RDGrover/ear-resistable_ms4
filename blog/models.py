from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body_text = models.TextField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    comment = models.TextField(default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['created_at']

    def __str__(self):
        return 'This comment {} posted by {}'.format(self.comment, self.user)
