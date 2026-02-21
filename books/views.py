from django.shortcuts import render, redirect
from django.http import HttpResponse
from books.forms import BookForm
from books.models import Book
from django.http.request import HttpRequest
# Create your views here.


def book_list(request: HttpRequest):
    #accesam db, extragem cartile si le afisam pe pagina html
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "books/home.html", context)

def create_book(request: HttpRequest):
    if request.method == "POST":
        # primi http post cand se apasa pe save

        form = BookForm(request.POST)
        if form.is_valid():
            #se salveaza in DB
            form.save()
            return redirect("book_list")

    else:
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, "books/book_form.html", context)

def hello_world(request):
    return render(request, "books/home.html")

        # HttpResponse("Hello World, this is my first web page!")

def simple_endpoint(request):
    return HttpResponse("{ 'content': 'Hello this is my response!'}", status=200)

