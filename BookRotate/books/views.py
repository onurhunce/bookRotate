from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .books_api import get_book, get_correct_query
from .forms import BookSearchForm, BookForm


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
            res=[]
            part = ''

            isbn_value = form.cleaned_data.get('isbn')
            title_value = form.cleaned_data.get('title')
            author_value = form.cleaned_data.get('author')

            if isbn_value:
                part = get_correct_query(query_type='isbn', query_value=isbn_value)
                res.append(part)
            if title_value:
                part = get_correct_query(query_type='title', query_value=title_value)
                res.append(part)
            if author_value:
                part = get_correct_query(query_type='author', query_value=author_value)
                res.append(part)

            que=','.join(res)
            query = f"?q={que}&printType=books"
            results=get_book(query=query)

            return render(
                request, 'books/feedback.html', {'results': results}
            )
    else:
        form = BookSearchForm()

    return render(request, 'books/search_book.html', {'form': form})
