from django.db import models
from django.conf import settings


user_model = settings.AUTH_USER_MODEL

class Associate(models.Model):
    from_user = models.ForeignKey(
        user_model,
        verbose_name="From User",
        related_name="associates_to", 
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        user_model,
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
        constraints = [
            models.UniqueConstraint(fields=[
                "to_user", 
                "relationship_type", 
                "from_user"
                ],
                name="associate must be unique!"
            )
        ]

    def save(self, *args, **kwargs):
        if(self.to_user == self.from_user):
            raise KeyError("a user cannot have associates to itself")
        
        super().save(*args, **kwargs)
