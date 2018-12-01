from django.shortcuts import render


def index(request):
    context = {
        'user_name': "Onur Hunce",
    }
    return render(request, 'books/index.html', context)
