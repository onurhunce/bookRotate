from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    isbn = models.CharField(max_length=100, null=True)
    publisher = models.TextField(max_length=100, blank=False)
    categories = models.TextField(max_length=500, blank=False)
    language = models.TextField(max_length=30, blank=False)
    genre = models.TextField(max_length=200, blank=False)
    pub_year = models.DateTimeField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)


class Library(models.Model):
    id = models.IntegerField(primary_key = True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, default="", related_name="library_user")


class ProfileSettings(models.Model):
    preferred_languages = models.TextField(max_length=500, blank=True)


class Review(models.Model):
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_user"
    )

    review_content = models.TextField(max_length=500, blank=False)


class Friend(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="relations_user_1"
    )
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="relations_user_2"
    )


class SwapStatuses(models.Model):
    status = models.TextField(max_length=20, blank=False)
    """
    Here we will have:
    1 -> request_sent
    2 -> request_accepted
    3 -> request_denied
    4 -> books_swapped
    5 -> books_returned
    6 -> request_removed
    """


class Swaps(models.Model):
    user_1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="swap_user_1"
    )
    user_2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="swap_user_2"
    )
    book_1 = models.ForeignKey(
        Library, on_delete=models.CASCADE, related_name="swap_book_1"
    )
    book_2 = models.ForeignKey(
        Library, on_delete=models.CASCADE, related_name="swap_book_2"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(SwapStatuses, on_delete=models.CASCADE)
    last_action_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="last_action_user"
    )
