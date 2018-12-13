from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    languages = models.ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
            choices=[(language, language) for language in
                           settings.AVAILABLE_LANGUAGES]
        ),
        size=8,)




class Swaps(models.Model):
	user_1 = models.ForeignKey(User, on_delete=models.CASCADE)
	user_2 = models.ForeignKey(User, on_delete=models.CASCADE)
	book_1 = models.ForeignKey(Library_Books, on_delete=models.CASCADE)
	book_2 = models.ForeignKey(Library_Books, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	status  = models.ForeignKey(Swap_Statuses, on_delete=models.CASCADE)
	last_action_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Swap_Statuses(models.Model):
	"""
	Here we will have:
	1 -> request_sent
	2 -> request_accepted
	3 -> request_denied
	4 -> books_swapped
	5 -> books_returned
	6 -> request_removed
	"""
	status = models.TextField(max_length=20, blank=False)


class Library(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# owned_book = models.For(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Books, on_delete=models.CASCADE)
	# shelf = models.ForeignKey(Shelves, on_delete=models.CASCADE)


class Books(models.Model):
	name = models.TextField(max_length=500, blank=False)
	categories = models.TextField(max_length=500, blank=False)
	author = models.TextField(max_length=200, blank=False)
	language = models.TextField(max_length=30, blank=False)
	genre = models.TextField(max_length=200, blank=False)
	year = models.DateTimeField(auto_now_add=True)



class Relations(models.Model):
	user_one =  models.ForeignKey(User, on_delete=models.CASCADE)
	user_two =  models.ForeignKey(User, on_delete=models.CASCADE)
	action = models.TextField(max_length=20, blank=False)
	relation_status = models.TextField(max_length=20, blank=False)
	action_by = models.ForeignKey(User, on_delete=models.CASCADE)



