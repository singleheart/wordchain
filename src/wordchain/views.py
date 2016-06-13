from django.views import generic
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    
    def get_queryset(self):
        return
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/game")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
    
def logout(request):
    logout(request)