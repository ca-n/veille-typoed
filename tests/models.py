from django.db import models

from users.models import User

# Create your models here.

class Test(models.Model):
    username = models.CharField(max_length=20)
    wpm = models.IntegerField()
    accuracy = models.DecimalField(max_digits=4, decimal_places=1)
    date = models.DateField()

    def __str__(self):
        return "{} - {} wpm - {}".format(self.username, self.wpm, self.date)