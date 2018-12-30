from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .books_api import get_book
from .forms import BookSearchForm


def index(request):
    return render(request, 'books/index.html', {})


def success(request):
    context = {'user_name': "Onur Hunce"}
    return render(request, 'books/feedback.html', context)


@login_required
def user_profile(request):
    context = {'user_name': request.user}
    return render(request, 'books/user_profile.html', context)


@login_required
def search_book(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            results = []
            isbn_value = form.cleaned_data.get('isbn')
            title_value = form.cleaned_data.get('title')
            author_value = form.cleaned_data.get('author')
            if isbn_value:
                results = get_book(query_value=isbn_value, query_type='isbn')
            if title_value:
                results = get_book(query_value=title_value, query_type='title')
            if author_value:
                results = get_book(query_value=author_value, query_type='author')
            return render(
                request, 'books/feedback.html', {'results': results}
            )
    else:
        form = BookSearchForm()

    return render(request, 'books/search_book.html', {'form': form})
