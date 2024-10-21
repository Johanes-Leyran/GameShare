from django.db import models
from django.conf import settings


class Associate(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="From User",
        related_name="associates_to", 
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="To User",
        related_name="associates_from",
        on_delete=models.CASCADE
    )
    created_at = models.DateField(
        auto_now_add=True
    )
    RELATION_CHOICES = (
        ("follow", "FOLLOW"),
        ("block", "BLOCK")
    )
    relationship_type = models.CharField(
        max_length=15,
        choices=RELATION_CHOICES,
        verbose_name="Relationship Type"
    )

    class Meta:
        app_label = "accounts"
        unique_together = ('from_user', 'to_user', 'relationship_type')
