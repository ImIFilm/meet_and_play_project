from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from game_announcement.models import Game_Announcement
from django.utils import timezone

def home(request):
    announcements = Game_Announcement.objects.all()
    return render(request, 'game_announcement/home.html', {'ann':announcements})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['sport'] and request.POST['location'] and request.POST['start_time'] and request.POST['end_time'] and request.POST['wanted_people'] and request.POST['registered_people'] and request.POST['skill_level'] and request.POST['price'] and request.POST['description'] :
            announcement = Game_Announcement()
            announcement.sport = request.POST['sport']
            announcement.location = request.POST['location']
            announcement.start_time = request.POST['start_time']
            announcement.end_time = request.POST['end_time']
            announcement.wanted_people = request.POST['wanted_people']
            announcement.registered_people = request.POST['registered_people']
            announcement.skill_level = request.POST['skill_level']
            announcement.price = request.POST['price']
            announcement.description = request.POST['description']

            announcement.pub_date = timezone.datetime.now()
            announcement.creator = request.user
            announcement.save()
            return redirect('/announcements/' + str(announcement.id))
        else:
            return render(request, 'game_announcement/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'game_announcement/create.html')

def detail(request, game_announcement_id):
    announcement = get_object_or_404(Game_Announcement, pk=game_announcement_id)
    return render(request, 'game_announcement/detail.html',{'announcement':announcement})

@login_required(login_url="/accounts/signup")
def upvote(request, announcement_id):
    if request.method == 'POST':
        announcement = get_object_or_404(Game_Announcement, pk=announcement_id)
        announcement.votes_total += 1
        announcement.save()
        return redirect('/announcements/' + str(announcement.id))
