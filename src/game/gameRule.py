from .models import History, Score
from django.db.models import F
import datetime


class Game:
    def __init__(self):
        return
    
    def restart(self):
        History.objects.all().delete()
        Score.objects.all().delete()


class GameScore:
    INIT_SCORE = 100
    ADD_CORRECT = 10
    PENALTY_LASTLETTERMISSMATCH = -10
    PENALTY_NOTINDIC = -10
    PENALTY_ALREADYEXIST = -5
    
    def __init__(self):
        return
    
    def init(self, userName):
        scores = Score.objects.filter(userId = userName)
        if len(scores) <= 0:
            score = Score(score=GameScore.INIT_SCORE, userId=userName, updateDate= str(datetime.datetime.now()))
            score.save()
            
    def update(self, userName, scoreDelta):
        scores = Score.objects.filter(userId = userName)

        score = scores[0]
        score.score = F('score') + scoreDelta
        score.updateDate = str(datetime.datetime.now())
        score.save()
    
    