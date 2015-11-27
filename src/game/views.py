from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .myDictionary import MyDictionary, dd
from .models import History, Score
from django.db.models import F

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return

class PlayData():
    def __init__(self, obj, word):
        self.obj = obj
        self.word = word

class PlayView(generic.ListView):
    template_name = 'game/play.html'
    context_object_name = 'History'

    def get_queryset(self):
        errWord = self.request.GET.get('errWord')
        errType = self.request.GET.get('errType')
        print('request: ', errWord, ", ", errType)
        return {'obj':History.objects.order_by('-updateDate')[0:10], 'errWord':errWord, 'errType':errType}

class ScoreView(generic.ListView):
    template_name = 'game/scoreboard.html'
    context_object_name = 'Score'
    
    def get_queryset(self):
        return Score.objects.order_by('-score')
    
def get_name(request):
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
                return HttpResponseRedirect('play?errWord='+ answer +'&errType='+'letterMissMatch')
        
        matchedList = History.objects.filter(text=answer)
        if len(matchedList) > 0:
            # print('matchedList: ', matchedList[0].updateDate)
            return HttpResponseRedirect('play?errWord='+answer+'&errType='+'AlreadyExist')

        if not dd.isExist(answer):
            # print('NotInDic: ', answer)
            return HttpResponseRedirect('play?errWord='+answer+'&errType='+'NotInDic')

        # db write
        p = History(text=answer, userId=request.user, updateDate= str(datetime.datetime.now()))
        p.save()
        
        # score update
        scores = Score.objects.filter(userId = request.user)
        if len(scores) <= 0:
            score = Score(score=1, userId=request.user, updateDate= str(datetime.datetime.now()))
            score.save()
        else:
            score = scores[0]
            score.score = F('score') +1
            score.updateDate = str(datetime.datetime.now())
            score.save()

        return HttpResponseRedirect('play')
        
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'play.html', {'form': forms.Form})
