from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import URLField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Author(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(max_length=100)
    URL = models.JSONField(null=True)
    created_at = models.DateField()
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name
