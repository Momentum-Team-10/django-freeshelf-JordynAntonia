from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import URLField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.
    author = models.
    description = models.
    URL = models.
    created_at = models.