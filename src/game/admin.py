from django.contrib import admin

# Register your models here.

from .models import History, Score

admin.site.register(History)
admin.site.register(Score)