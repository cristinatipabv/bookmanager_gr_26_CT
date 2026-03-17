from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from accounts.models import CustomUser
from books.forms import BookForm
from books.models import Book
from django.http.request import HttpRequest
# Create your views here.

#CRUD action
#Create, read, update, delete
def book_list(request: HttpRequest):
    #accesam db, extragem cartile si le afisam pe pagina html
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "books/home.html", context)

def create_book(request: HttpRequest):

    if request.method == "POST":
        # primim http post cand se apasa pe save

        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            #se salveaza in DB
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect("book_list")

    else:
        form = BookForm()
    context = {
        'form': form
    }
    return render(request, "books/book_form.html", context)



def delete_book(request: HttpRequest, pk: int):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    else:
        return render(request, "books/book_confirm_delete.html", {"book": book})

def update_book(request: HttpRequest, pk: int):
    # cartea care exista in DB
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form})

def check_book_count(request: HttpRequest):
    #count = len(Book.all()) # metoda asta este mai putin eficienta decat Book.objects.count()
    count = Book.objects.count()
    #book_count
    return render(request, "books/book_count.html", {"book_count": count})

        # HttpResponse("Hello World, this is my first web page!")

def user_books(request    : HttpRequest, pk: int):
# pk - id-ul userului
    user = get_object_or_404(CustomUser, pk=pk)
    books = user.books.all()
    return render(request, "books/home.html", {"books": books})

def search_books(request: HttpRequest):
    q = request.GET.get("q")

    if q is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(title__contains=q).all()
    print(books)

    return render(request, "books/home.html", {"books": books})


def simple_endpoint(request):
    return HttpResponse("{ 'content': 'Hello this is my response!'}", status=200)

