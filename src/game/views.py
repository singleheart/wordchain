from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from .gameRule import Game, GameScore

from .myDictionary import MyDictionary, dd
from .models import History, Score

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return

class ScoreView(generic.ListView):
    template_name = 'game/scoreboard.html'
    context_object_name = 'Score'
    
    def get_queryset(self):
        return Score.objects.order_by('-score')

gameRule = Game()
gameScore = GameScore()

class PlayView(generic.ListView):
    template_name = 'game/play.html'
    context_object_name = 'History'

    def get_queryset(self):
        gameScore.init(self.request.user)
        
        errWord = self.request.GET.get('errWord')
        errType = self.request.GET.get('errType')
        print('request: ', errWord, ", ", errType)
        
        if gameRule.isObserverMode(self.request.user):
            return {'obj':History.objects.order_by('-updateDate')[0:10], 'errWord':errWord, 'errType':errType, 'inObserverMode':True}
        else:
            return {'obj':History.objects.order_by('-updateDate')[0:10], 'errWord':errWord, 'errType':errType, 'inNormalMode':True}

def check_rule(request):
    gameScore.init(request.user)
        
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        answer = request.POST['answer']
        
        if len(answer) <= 0:
            return HttpResponseRedirect('play?errWord='+ ' ' +'&errType='+'Empty')
        
        # word chain validation check
        lastWords = History.objects.order_by('-updateDate')
        if len(lastWords) > 0:
            lastWord = lastWords[0]
            lastLetter = lastWord.text[-1]
            # print(lastWord, " : ", lastLetter)
            
            if lastLetter != answer[0]:
                # print('letterMissMatch: ', lastLetter, ", ", answer)
                if gameScore.update(request.user, gameScore.PENALTY_LASTLETTERMISSMATCH):
                    return HttpResponseRedirect('play?errWord='+ answer +'&errType='+'letterMissMatch')
                else:
                    return HttpResponseRedirect('play')
        
        matchedList = History.objects.filter(text=answer)
        if len(matchedList) > 0:
            # print('matchedList: ', matchedList[0].updateDate)
            if gameScore.update(request.user, gameScore.PENALTY_ALREADYEXIST):
                return HttpResponseRedirect('play?errWord='+answer+'&errType='+'AlreadyExist')
            else:
                return HttpResponseRedirect('play')

        if not dd.isExist(answer):
            # print('NotInDic: ', answer)
            if gameScore.update(request.user, gameScore.PENALTY_NOTINDIC):
                return HttpResponseRedirect('play?errWord='+answer+'&errType='+'NotInDic')
            else:
                return HttpResponseRedirect('play')

        if gameRule.isNoMoreWord(answer):
            print(request.user)
            gameRule.restart()
            return HttpResponseRedirect('play')

        # db write
        p = History(text=answer, userId=request.user, updateDate= str(datetime.datetime.now()))
        p.save()
        
        # score update
        gameScore.update(request.user, gameScore.ADD_CORRECT)

        return HttpResponseRedirect('play')
        
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'play.html', {'form': forms.Form})
