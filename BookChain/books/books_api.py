import requests
import json
import base64
import argparse
import io

from google.cloud import vision
from google.cloud.vision import types


GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
GOOGLE_VISION_API_URL = "https://vision.googleapis.com/v1/images:annotate"
GOOGLE_BOOKS_API_KEY = ""


def get_book(query):
    url = f"{GOOGLE_BOOKS_API_URL}{query}"  # noqa
    response = requests.get(url)
    list_of_items = response.json()["items"]
    return get_book_name_from_dict(list_of_items)


def get_correct_query(query_type, query_value):
    if query_type == "isbn":
        return f"isbn:{query_value}"  # noqa
    if query_type == "author":
        return f"inauthor:{query_value}"  # noqa
    if query_type == "title":
        return f"intitle:{query_value}"  # noqa


def get_book_name_from_dict(list_of_items):
    names = []
    for item in list_of_items:
        title = ''
        authors = ''
        categories = ''
        published_date = ''
        link = ''
        if item.get("volumeInfo"):
            title = item["volumeInfo"].get("title")
            authors_list = item["volumeInfo"].get("authors")
            if authors_list:
                authors = ','.join(authors_list)
            categories_list = item["volumeInfo"].get("categories")
            if categories_list:
                categories = ','.join(categories_list)
            link = item["volumeInfo"].get("previewLink")
            published_date = item["volumeInfo"].get("publishedDate")
            book_dict = {
                'title': title,
                'authors': authors,
                'categories': categories,
                'link': link,
                'published_date': published_date,
            }
            names.append(book_dict)
    return names


def post_image_to_vision_api():
    url = f"{GOOGLE_VISION_API_URL}?key={GOOGLE_BOOKS_API_KEY}"  # noqa
    print("url is::: ", url)
    image = open(
        '/home/onur/Works/BookChain/bookchain/scripts/image.jpg', 'rb'
    )
    b64_string = base64.b64encode(image.read())
    request_data = {
        "requests": [
            {
                "image": {
                    "content": b64_string},
                "features": [{
                    "type": "LABEL_DETECTION",
                    "maxResults": 1
                }
                ]
            }
        ]
    }

    response = requests.post(
        url,
        request_data,
        headers={'content-type': 'application/json'}
    )
    print("response is:::", response)
    print("response text is:::", response.text)
    print("response json is:::", response.json())


def use_vision_client():
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    print("client is:: ", client)
    image_file = open(
        '/home/onur/Works/BookChain/bookchain/scripts/image.jpg', 'rb'
    )
    # Loads the image into memory
    with io.open(
        '/home/onur/Works/BookChain/bookchain/scripts/image.jpg', 'rb'
    ) as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    labels = response.text_annotations
    for label in labels:
        print(label.description)
