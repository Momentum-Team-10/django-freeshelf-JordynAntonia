
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def list_books(request):
    books = Book.objects.all().order_by("title")
    return render(request,"books/list_books.html",{"books": books})

@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect("show_book", pk=book.pk)
    else:
        form = BookForm()

    return render(request, "books/add_book.html", {"form": form})



def show_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/show_book.html", {"book: book"})



def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.PATCH)
        # if form.is_valid()



def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "Delete":
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST)
    return render(request,"books/delete_book.html", {"book:book"})