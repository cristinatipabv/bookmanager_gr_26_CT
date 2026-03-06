from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from bookmanager import settings
from .import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create_book/', views.create_book, name='create_book'),
    path('check_book_count/', views.check_book_count, name='check_book_count'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('book/<int:pk>/update/', views.update_book, name='update_book'),
    path('api_simple_endpoint/', views.simple_endpoint, name='simple'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
