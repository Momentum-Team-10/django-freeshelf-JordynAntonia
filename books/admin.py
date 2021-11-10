from django.contrib import admin
from books.models import Book, User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(Book)
admin.site.register(User, UserAdmin)