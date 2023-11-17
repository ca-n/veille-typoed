from django.db import models

from django.apps import apps

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)

    @property
    def tests(self):
        return apps.get_model('tests', 'Test').objects.filter(user=self).order_by('-date')
    
    def __str__(self):
        return self.username