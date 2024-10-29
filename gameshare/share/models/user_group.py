from django.db import models
from django.conf import settings


class UserGroup(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="following_groups"
    )
    to_group = models.ForeignKey(
        "share.Group",
        related_name="members"
    )
    joined_at = models.DateField(
        auto_now_add=True
    )

    class Meta:
        app_label = "share"
        unique_together = ('user', 'to_group')
