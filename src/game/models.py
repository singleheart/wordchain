from django.db import models

# Create your models here.

class History(models.Model):
    userId = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    updateDate = models.DateTimeField('date published')
    
class Score(models.Model):
    userId = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    updateDate = models.DateTimeField('date published')
    