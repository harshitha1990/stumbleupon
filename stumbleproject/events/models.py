from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Link(models.Model):
	CATEGORY_CHOICES=(
		('C','Coding'),
		('F','Fashion'),
		('W','Webdesigning'),
		('P','Photography'),
	)
	owner=models.CharField(max_length=100)
	category=models.CharField(max_length=1,choices=CATEGORY_CHOICES)
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=512)
	link=models.URLField(max_length=200)
	Date=models.DateField(auto_now_add=True)
	
#class shared(models.Model):
#	sharedto=models.CharField(max_length=512)
#	linkid=models.ForeignKey(Link)
#	Date=models.DateField(auto_now_add=True)aa
