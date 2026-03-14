import pytest
from books.models import Book
from django.contrib.auth import get_user_model
User = get_user_model()


@pytest.mark.django_db

def test_book_creation():
    book = Book.objects.create(
        title="test book 1",
        content="test content here 1",
        author="test",

    )

    assert book.title == "test book 1"
    assert book.content == "test content here 1"

@pytest.mark.django_db
def test_book_creation_with_user():
    user = User.objects.create(username="test1")
    book = Book.objects.create(
        title="test book 1",
        content="test content here 1",
        author="test",
        user=user

    )

    book2 = Book.objects.create(
        title="test book 2",
        content="test content here 2",
        author="test",
        user=user

    )

    assert book.title == "test book 1"
    assert book.content == "test content here 1"
    assert book.user.username == "test1"
    assert len(user.books.all()) == 2
