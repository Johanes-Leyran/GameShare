from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class GameShareUser(AbstractUser):
    email = models.EmailField(
        unique=True, 
        help_text=_("The email for your account")
    )
    username = models.CharField(
        max_length=120,
        unique=True,
        help_text=_("The username for your account")
    )
    show_adult_content = models.BooleanField(
        default=False,
        help_text=_("Show adult contents to the user")   
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]