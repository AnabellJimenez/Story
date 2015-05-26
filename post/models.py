from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	
	post_title = models.CharField(max_length = 100)
	post_text = models.TextField(max_length = 200)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.post_text

class Comment(models.Model):

	post = models.ForeignKey(Post)
	comment_text = models.CharField(max_length = 200)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.comment_text

class Picture(models.Model):
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)

class Gallery(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length = 100)
	post = models.ForeignKey(Post)
	pic_url = models.TextField(max_length = 200)
