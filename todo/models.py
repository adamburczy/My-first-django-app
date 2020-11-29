from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

class Task(models.Model):
    title = models.CharField(max_length=30, unique=True)
    notes = models.TextField(max_length=150)       # TypeError: expected string or bytes-like object
    created = models.DateField(auto_now_add=True)  # add start as, start of task, default = created maybe
    deadline = models.DateField(default=None)      # add status: not started yes, ongoing, finished
    #STATUS_CHOICES = [
     #   ('not started yet', 'not started yet'),
      #  ('ongoing', 'ongoing'),
       # ('finished', 'finished')
    #]
    #status = models.CharField(choices=STATUS_CHOICES,
     #                         max_length=20,
      #                        default='ongoing')

    def __str__(self):
        return self.title




















