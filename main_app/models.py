from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length=100)
	release = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Show(models.Model):
	name = models.CharField(max_length=100)
	seen = models.BooleanField()

	def __str__(self):
		return self.name