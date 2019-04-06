from django.shortcuts import render
from game_announcement.models import Game_Announcment

def home(request):
    announcements = Game_Announcment.objects.all()
    return render(request, 'game_annoucement/home.html', {'ann':announcements})

