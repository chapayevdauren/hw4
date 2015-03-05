from django.db import models
from django.utils import timezone

class Post(models.Model):
	
	author = models.CharField(max_length=1000)
	title = models.CharField(max_length=1000)
	text = models.CharField(max_length=5000)
	pub_date = models.DateTimeField(auto_now_add=timezone.now)
	upd_date = models.DateTimeField(auto_now_add=timezone.now)
	is_public = models.BooleanField(default=False)


class Comment(models.Model):
	
	author = models.CharField(max_length=1000)
	text = models.CharField(max_length=5000)
	pub_date = models.DateTimeField(auto_now_add=timezone.now)
	post = models.CharField(max_length=1000)
		