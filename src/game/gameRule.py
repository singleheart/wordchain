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

    def isNoMoreWord(self, word):
        # not in dic
        if not dd.isExistStartLetter(word[-1]):
            return True
            
        # in dic, but in history
        words = dd.getSubWord(word[0])
        for word in words:
            matchedList = History.objects.filter(text=word)
            if len(matchedList) <= 0:
                return False
        
        return True

    def isObserverMode(self, userName):
        scores = Score.objects.filter(userId = userName)
        if len(scores) > 0:
            score = scores[0]
            if score.score <= 0:
                return True
                
        return False

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
            
    def getWinnerByScore(self):
        scores = Score.objects.all()
        if len(scores) <=1:
            return None
        
        scores = Score.objects.filter(score__gt=0)
        if len(scores) == 1:
            return  scores[0].userId
        
        return None

    def restart(self):
        History.objects.all().delete()
        Score.objects.all().delete()
        
    def update(self, userName, scoreDelta):
        scores = Score.objects.filter(userId = userName)

        score = scores[0]
        score.score = F('score') + scoreDelta
        score.updateDate = str(datetime.datetime.now())
        score.save()
        
        # if score is negative value,
        # check the result
        scores = Score.objects.filter(userId = userName)
        score = scores[0]
        
        if score.score <= 0:
            winner = self.getWinnerByScore()
            if winner is not None:
                print("Winner: ", winner)
                self.restart()
                return False
            else:
                print("No winner...")
                
        return True