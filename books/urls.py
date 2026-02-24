from django.urls import path
from .import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create_book/', views.create_book, name='create_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('hello/', views.hello_world, name='hello_world'),
    path('api_simple_endpoint/', views.simple_endpoint, name='simple'),

]

