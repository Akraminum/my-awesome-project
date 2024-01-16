from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    title = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="users/avatar", default="users/avatar/default.png"  )
    birth_date = models.DateField(null=True)
    
    class Meta:
        app_label = "users"
        db_table = "auth_user"