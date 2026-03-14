import pytest
from books.models import Book
from django.contrib.auth import get_user_model
from django.test.client import Client
from django.urls import reverse


User = get_user_model()

# pytest fixture
# obiecte pre-initializate

@pytest.fixture
def user(db):
    user = User.objects.create_user(
        username='test1',
        email='test1@test.com',
        password='python2026'
    )
    return user

@pytest.fixture
def logged_in_client(client: Client, user) -> Client:
    client.login(username="test1", password="python2026")
    return client

@pytest.fixture
def book_obj(user):
    book = Book.objects.create(
        title="Book1",
        content="Test Content22",
        author="Tester Author",
        user=user
    )
    return book



@pytest.mark.django_db
def test_book_create(logged_in_client: Client):
    response = logged_in_client.post(
        reverse("create_book"),
        {
            "title": "Book1",
            "author": "Tester1",
            "content": "Test Content11",

        }

    )

    assert response.status_code == 302
    assert Book.objects.count() == 1

@pytest.mark.django_db
def test_book_delete(logged_in_client: Client, book_obj: Book):
    # book id here:
    book_id = book_obj.pk
    response = logged_in_client.post(
        reverse("delete_book", kwargs={"pk": book_id})
    )

    assert response.status_code == 302
    book_search = Book.objects.filter(pk=book_id).all()
    assert (len(book_search)) == 0

@pytest.mark.django_db
def test_book_update(logged_in_client: Client, book_obj: Book):
    book_id = book_obj.pk
    response = logged_in_client.post(
        reverse("update_book", kwargs={"pk": book_id}),
        {
            "title": "Book15",
            "author": "Tester101",
            "content": "Test Content1100",
        }
    )
    assert response.status_code == 302
    # refresh manual
    book_obj.refresh_from_db()
    assert book_obj.title == "Book15"
    assert book_obj.author == "Tester101"
    assert book_obj.content == "Test Content1100"




# explicatie cum se foloseste "->" intr-o functie:
# def func1(x: int, y: int) -> int:
#     result = x+y
#     return x + y
