# Create your views here.
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from author.models import Author
from .models import Book
from .forms import BookForm
from order.models import Order


def all_books(request):
    books = Book.get_all()
    return render(request, 'book/all_books.html', {'books': books})



def book_detail(request, book_id=None):
    book_id = request.POST.get('book_id')
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_detail.html', {'book': book})

def filter_books(request):
    books = Book.objects.all()
    author_name = request.GET.get('author')
    title = request.GET.get('title')
    if author_name:
        try:
            # books = books.filter(authors__name__icontains=author_name)
            author = Author.objects.get(name=author_name)
            books = author.books.all()
        except Author.DoesNotExist:
            messages.warning(request, f"No books found by author '{author_name}'")
    if title:
        books = books.filter(name__icontains=title)
        if not books.exists():
            messages.warning(request, f"No books found by title '{title}'")
    return render(request, 'book/filter_books.html', {'books': books})


def user_books(request, user_id=None):
        user_id = request.POST.get('user_id')
        orders = Order.objects.filter(user_id=user_id)
        books = [order.book for order in orders]
        return render(request, 'book/user_books.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.data
            author = Author.get_by_id(data.get('author'))
            Book.create(name=data.get('book_name'),
                        description=data.get('description'),
                        count=data.get('count'),
                        authors=author,
                        date_of_issue=data.get('date_of_issue'),
                        year_of_publication=data.get('year_of_publication'))
            return redirect('/books/')
    authors_all = Author.get_all()
    form = BookForm()
    return render(request, 'book/form_book.html', {'form': form, 'authors': authors_all})


def edit_book(request, book_id):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.data
            author = Author.get_by_id(data.get('author'))
            edit_book = Book.get_by_id(book_id)
            edit_book.update(name=data.get('book_name'),
                             description=data.get('description'),
                             count=data.get('count'),
                             authors=author,
                             date_of_issue=data.get('date_of_issue'),
                             year_of_publication=data.get('year_of_publication'))
            return redirect('/books/')
    form = BookForm()
    authors_all = Author.get_all()
    book = Book.get_by_id(book_id)
    return render(request, 'book/form_book.html', {'book': book, 'form': form, 'authors': authors_all})



def delete_book(request, book_id):
    book = Book.get_by_id(book_id)
    for author in book.authors.all():
        if len(author.books.all()) == 1:
            Author.delete_by_id(author.id)
    Book.delete_by_id(book_id)
    return redirect('/book/')


