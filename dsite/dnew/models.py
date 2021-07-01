from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	mobile = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.username

