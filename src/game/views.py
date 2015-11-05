from django.shortcuts import render
from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return