from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
from django.conf import settings

class Game_Announcement(models.Model):
	""" doc to do"""
	SKILL_LEVEL_CHOICES = (
	('0', 'Recreational'),
	('1',  'Amatuer'),
	('2', 'Average'),
	('3',  'Good'),
	('4', 'Very Good'),
	)

	SPORT_CHOICES = (
		('0', 'Football'),
		('1',  'Basketball'),
		('2', 'Volleyball'),
	)

	sport = models.CharField("Sport", max_length=100, choices=SPORT_CHOICES)
	location = models.CharField("Location", default="Location",max_length=100)
	start_time = models.DateTimeField(default=datetime.now)
	end_time = models.DateTimeField(default=datetime.now)
	wanted_people = models.IntegerField()
	registered_people = models.IntegerField()
	price = models.FloatField(default=0)
	skill_level = models.CharField("Level of skills", max_length=100, choices=SKILL_LEVEL_CHOICES)
	description = models.TextField("Description")
	pub_date = models.DateTimeField(default=datetime.now)
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
