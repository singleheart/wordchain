from django.db import models

# Create your models here.

class Score(models.Model):
    userId = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    updateDate = models.DateTimeField('date published')
    