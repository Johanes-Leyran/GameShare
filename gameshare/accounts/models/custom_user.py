from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ..manager import GamseShareUserManager


class GameShareUser(AbstractUser):
    # we don't need these two in our custom user
    first_name = None
    last_name = None

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
        "show adult content",
        default=False,
        help_text=_("Show adult contents to the user")   
    )
    # handles the following and follower shit of the user
    associates = models.ManyToManyField(
        "self",
        through="accounts.Associate",
        symmetrical=False
    )
    user_post = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username"
    ]
    
    objects = GamseShareUserManager()
   
    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return NotImplementedError
