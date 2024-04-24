from django.shortcuts import render, redirect
from .models import Book


def index(request):
    title = 'Head page'
    template = 'books/index.html'
    book = Book.objects.all()
    context = {
        'title': title,
        'text': 'Text page',
        'book': book
    }
    return render(request, template, context=context)


def add(request):
    template = 'books/add.html'
    return render(request, template)


def addrec(request):
    a = request.POST['name']
    b = request.POST['title']
    c = request.POST['author']
    d = request.POST['description']
    e = request.POST['price']
    book = Book(name=a, title=b, author=c, description=d, price=e)
    book.save()
    return redirect('/')


def books_list(request):
    pass


def profile_edit(request):
    pass
