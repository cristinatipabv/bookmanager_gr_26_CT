from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'content', 'author',"image"]
        # fields = "__all__" => preia automat toate campurile din models, clasei respective
