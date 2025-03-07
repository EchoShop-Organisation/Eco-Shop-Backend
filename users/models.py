from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Fix the reverse accessor clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_profiles",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_profiles",
        blank=True
    )
