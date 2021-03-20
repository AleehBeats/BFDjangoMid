from django.shortcuts import render

# Create your views
from main.models import Book, Journal


def books_view(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context=context)


def journals_view(request):
    journals = Journal.objects.all()
    context = {
        'journals': journals
    }

    return render(request, 'journals.html', context=context)
