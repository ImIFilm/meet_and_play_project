from django.db import models
from datetime import datetime 
from enum import Enum

class SkillLevel(Enum):
	REC = "Recreational"
	AMA = "Amatuer"
	AVG = "Average"
	GOO = "Good"
	VGO = "Very Good"

class Sports(Enum):
	FOT = "Football"
	BAS = "Basketball"
	VOL = "Volleyball"

class Game_Announcment(models.Model):
	""" doc to do"""
	sport = models.CharField("Sport", max_length=100, choices=[(tag, tag.value) for tag in Sports])
	location = models.CharField("Location", default="Location",max_length=100)
	start_time = models.DateTimeField(default=datetime.now)
	end_time = models.DateTimeField(default=datetime.now)
	wanted_people = models.IntegerField()
	registered_people = models.IntegerField()
	price = models.FloatField(default=0)
	skill_level = models.CharField("Level of skills", max_length=100, choices=[(tag, tag.value) for tag in SkillLevel])
	description = models.TextField("Description")

	

