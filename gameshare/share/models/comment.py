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
        default=None,
        related_name="comment_childrens"
    )
    # TODO: add liking system for the comment
    # TODO: add editing and history system 
    text_content = models.TextField()
    comment_at = models.DateField(
        auto_now_add=True
    )    
