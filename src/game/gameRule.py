from .models import History, Score
from django.db.models import F
from .myDictionary import MyDictionary, dd
import datetime


class Game:
    def __init__(self):
        return
    
    def restart(self):
        History.objects.all().delete()
        Score.objects.all().delete()

    def isEnd(self, word):
        # not in dic
        if not dd.isExistStartLetter(word[0]):
            return True
            
        # in dic, but in history
        words = dd.getSubWord(word[0])
        for word in words:
            matchedList = History.objects.filter(text=word)
            if len(matchedList) <= 0
                return False
        
        return True

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
    
    