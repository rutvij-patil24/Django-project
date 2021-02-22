from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): # post model (basically a post table)
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	# timezone.now enables Django to update date whenever user updates his post
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	# author is foreign key of User table
	# on_delete=models.CASCADE will make Django to delete 
	# all posts if that user is deleted

	def __str__(self):
		return self.title




