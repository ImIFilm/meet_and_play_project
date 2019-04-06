from django.db import models
from datetime import datetime 

class Game_Announcment(models.Model):
	""" doc to do"""
	sport = models.CharField("Sport", default="Sport",max_length=100)
	location = models.CharField("Location", default="Location",max_length=100)
	start_time = models.DateTimeField(default=datetime.now)
	end_time = models.DateTimeField(default=datetime.now)
	wanted_people = models.IntegerField()
	registered_people = models.IntegerField()
	price = models.FloatField(default=0)
	skill_level = models.CharField("Level of skills", default="Average", max_length=100)
	description = models.TextField("Description")

	

