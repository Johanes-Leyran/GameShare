from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Group(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True,
        help_text=_("Name of the group")
    )
    description = models.TextField(
        "Description",
        help_text=_("Description of the group")
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="owned_groups",
        help_text=_("Creator of the group") 
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        through="forum.UserGroup"   
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return NotImplementedError
