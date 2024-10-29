from django.db import models
from django.conf import settings


class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_comments"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL
        null=True,
        default=None
    )
    # TODO: add liking system for the comment
    text_content = models.TextField()
    comment_at = models.DateField(
        auto_now_add=True
    )    
