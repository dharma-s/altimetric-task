from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    adhar_number = models.CharField(max_length=12, unique=True)
    registration_date = models.DateField(auto_now_add=True)
    assigned_mobile_number = models.CharField(max_length=10)
    # Specify a custom related name for user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Custom related name
        related_query_name='user'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions_set',  # Custom related name
        related_query_name='user'
    )

    def __str__(self):
        return self.username
