from django.db import models

from users.models import User

# Create your models here.

class Lang(models.Model):
    lang = models.CharField(max_length=2, primary_key=True)

    def __str__(self):
        return self.lang.upper()

class Word(models.Model):
    word = models.CharField(max_length=64)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)

    def __str__(self):
        return self.word

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    wpm = models.IntegerField()
    accuracy = models.DecimalField(max_digits=4, decimal_places=1)
    date = models.DateField()

    def __str__(self):
        return '{} - {} - {}'.format(self.user, self.lang,  self.date)