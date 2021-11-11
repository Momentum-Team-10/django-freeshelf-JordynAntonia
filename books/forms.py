from django import forms
from django.db.models import fields
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "description",
            "URL",
            "created_at",
            "data"

        ]