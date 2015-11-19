from django.shortcuts import render
from django.views import generic
from django import forms
from django.http import HttpResponseRedirect
import datetime

from .models import History, Score

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return

class PlayView(generic.ListView):
    template_name = 'game/play.html'
    context_object_name = 'History'

    def get_queryset(self):
        return History.objects.order_by('updateDate')

class ScoreView(generic.ListView):
    template_name = 'game/scoreboard.html'
    context_object_name = 'Score'
    
    def get_queryset(self):
        return Score.objects.order_by('-score')
    
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        pk = request.POST['answer']
        p = History(text=pk, userId=request.user, updateDate= str(datetime.datetime.now()))
        p.save()

        return HttpResponseRedirect('play')
        
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'play.html', {'form': forms.Form})
