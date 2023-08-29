import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from .validators import validate_min_length

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    institution_name = models.CharField(max_length=255, verbose_name='Наименование учебного заведения')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона', validators=[validate_min_length])

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )


