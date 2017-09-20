# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100) #the name of Blog
    category = models.CharField(max_length = 50, blank = True) #the tag of Blog
    date_time = models.DateTimeField(auto_now_add = True) #the date of Blog
    content = models.TextField(blank = True, null = True) # the content of Blog

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
