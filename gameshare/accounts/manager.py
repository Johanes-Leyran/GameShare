from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _ 


class GamseShareUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields): 
        if not email:
            return ValueError(_("Email must be set"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if not password:
            return ValueError(_("Password must be set"))

        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(
            email=email, 
            password=password, 
            **extra_fields
        )
     
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields["is_staff"]:
            raise ValueError(_("Superuser must have staff privileges"))

        if not extra_fields["is_superuser"]:
            raise ValueError(_("Superuser must have superuser privileges"))

        return self.create_user(
            email=email, 
            password=password, 
            **extra_fields
        ) 