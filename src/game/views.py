from django.shortcuts import render
from django.views import generic

from .models import Score

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
    
