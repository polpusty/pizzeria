from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetails(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    address = models.CharField(
        max_length=511
    )
    phone = models.CharField(
        max_length=12
    )
