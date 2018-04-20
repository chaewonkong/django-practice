from django.db import models


class PostImage(models.Model):

	title = models.CharField(max_length=100)
	photo = models.ImageField(null=True)

	def __str__(self):
		return self.title