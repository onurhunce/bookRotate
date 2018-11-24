import requests
import json

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"


def get_book(query_value, query_type):
    query = get_correct_query(query_type, query_value)
    url = f"{GOOGLE_BOOKS_API_URL}{query}"  # noqa
    response = requests.get(url)
    list_of_items = response.json()["items"]
    get_book_name_from_dict(list_of_items)


def get_correct_query(query_type, query_value):
    if query_type == "isbn":
        return f"?q=isbn:{query_value}&printType=books"  # noqa
    if query_type == "author":
        return f"?q=inauthor:{query_value}&printType=books"  # noqa
    if query_type == "title":
        return f"?q=intitle:{query_value}&printType=books"  # noqa


def get_book_name_from_dict(list_of_items):
    for item in list_of_items:
        print(item.get("volumeInfo"))
        print("\n\n\n")
