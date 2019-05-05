from django import forms
from .models import Book


class BookSearchForm(forms.Form):
    title = forms.CharField(label='title', max_length=100, required=False)
    author = forms.CharField(label='author', max_length=100, required=False)
    isbn = forms.CharField(label='isbn', max_length=100, required=False)


class BookForm(forms.ModelForm):
    link = forms.URLField(label='link', required=False)
    class Meta:
        model = Book
        fields = ['title', 
                  'author', 
                  'isbn',
                   'publisher',
                   'categories',
                   'language',
                   'genre',
                   'pub_year',
                   'image_url']
