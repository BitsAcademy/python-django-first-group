from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
BOOK_CATEGORY = (('eng', 'ENGINEERING'), ('doc', 'DOCTOR'),\
 ('csit', 'CSIT'), ('arc', 'ARCHITECT'), ('ca', 'CHARTERED ACCOUNT'))

class Book(models.Model):

	name = models.CharField(max_length=40)
	author = models.CharField(max_length=30, null=True)
	publication = models.CharField(max_length=30, null=True)
	page = models.IntegerField(null=True, blank=True)
	published = models.DateTimeField(null=True)
	category = models.CharField(max_length=20, choices=BOOK_CATEGORY, null=True, default='eng')

	def __str__(self):
		return self.name


class Student(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	faculty = models.CharField(max_length=20)
	batch = models.CharField(max_length=20)
	contact_no = models.CharField(max_length=15, null=True)

	def __str__(self):
		return '{}: faculty:{}'.format(self.user, self.faculty)

class BookRecord(models.Model):
	name = models.ForeignKey(Student, on_delete=models.CASCADE)
	book = models.ManyToManyField(Book)
	issued_date = models.DateTimeField(auto_now_add=True)
	returned = models.BooleanField(default=False)
	return_date = models.DateTimeField(blank=True, null=True)

	def save(self):
		if self.returned:
			self.return_date = datetime.datetime.now()
		super(BookRecord, self).save()

	def __str__(self):
		return('{}'.format(self.name))

