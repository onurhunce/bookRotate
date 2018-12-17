from django import forms


class BookSearchForm(forms.Form):
    title = forms.CharField(label='title', max_length=100, required=False)
    author = forms.CharField(label='author', max_length=100, required=False)
    isbn = forms.CharField(label='isbn', max_length=100, required=False)
