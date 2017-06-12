# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
from janitriapp.choices import * 

class UserInterest(models.Model):
    user = models.OneToOneField(User)    
    interest = models.IntegerField(choices=INTEREST_CHOICES, default=1)   

class NewsWebsite(models.Model):
    title = models.TextField()
    interest = models.IntegerField(choices=INTEREST_CHOICES, default=1)
    url = models.URLField(unique=True)
    description = models.TextField(blank=True)
    
    