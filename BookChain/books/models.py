from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class ProfileSettings(models.Model):
    preferred_languages = models.TextField(max_length=500, blank=True)


class Book(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.TextField(max_length=500, blank=False)
    isbn = models.TextField(max_length=500, blank=False)
    publisher = models.TextField(max_length=500, blank=False)
    categories = models.TextField(max_length=500, blank=False)
    author = models.TextField(max_length=200, blank=False)
    language = models.TextField(max_length=30, blank=False)
    genre = models.TextField(max_length=200, blank=False)
    year = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField()


class Review(models.Model):
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    reviewee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewee"
    )

    review_content = models.TextField(max_length=500, blank=False)


class Friend(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="relations_user_1"
    )
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="relations_user_2"
    )


class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # owned_book = models.For(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # shelf = models.ForeignKey(Shelves, on_delete=models.CASCADE)


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
