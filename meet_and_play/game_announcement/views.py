from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from game_announcement.models import Game_Announcement, SPORT_CHOICES, SKILL_LEVEL_CHOICES
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

def home(request):
    announcements = Game_Announcement.objects.all()
    user_id = str(request.user.id)
    return render(request, 'game_announcement/home.html', {'ann':announcements, 'user_id': user_id })

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['sport'] and request.POST['location'] and request.POST['start_date'] and request.POST['end_date'] and request.POST['start_time'] and request.POST['end_time'] and request.POST['wanted_people'] and request.POST['skill_level'] and request.POST['price'] and request.POST['description'] :
            announcement = Game_Announcement()
            announcement.sport = request.POST['sport']
            announcement.location = request.POST['location']
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']

            st_t = str(start_date) +" "+ str(start_time)
            et_t = str(end_date) +" "+ str(end_time)

            announcement.start_time = datetime.strptime(st_t, "%Y-%m-%d %H:%M")
            announcement.end_time = datetime.strptime(et_t, "%Y-%m-%d %H:%M")            

            announcement.wanted_people = request.POST['wanted_people']
            #announcement.registered_people = 0
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
        return render(request, 'game_announcement/create.html', {'sport_choices': SPORT_CHOICES, 'skill_choices': SKILL_LEVEL_CHOICES })

def detail(request, game_announcement_id):
    announcement = get_object_or_404(Game_Announcement, pk=game_announcement_id)
    users_ids_list = announcement.joined_users()
    users_list = []
    is_user_signed = announcement.did_user_join(request.user.id)
    for uid in users_ids_list:
        users_list.append(User.objects.get(pk=int(uid)))
    return render(request, 'game_announcement/detail.html',{'announcement':announcement, 'users_list': users_list, 'is_user_signed': is_user_signed})

@login_required(login_url="/accounts/signup")
def join(request, game_announcement_id):
    announcement = get_object_or_404(Game_Announcement, pk=game_announcement_id)
    if announcement.did_user_join(request.user.id):
        announcements = Game_Announcement.objects.all()
        return render(request, 'game_announcement/home.html', {'ann':announcements, 'error':'You\'ve already joined this game'})
    if announcement.registered_people >= announcement.wanted_people:
        announcements = Game_Announcement.objects.all()
        return render(request, 'game_announcement/home.html', {'ann':announcements, 'error':'This game is already full!'})
    announcement.joined += str(request.user.id)
    announcement.joined += ';'
    announcement.registered_people += 1
    announcement.save()
    return redirect('/announcements/' + str(announcement.id))

@login_required(login_url="/accounts/signup")
def resign(request, game_announcement_id):
    announcement = get_object_or_404(Game_Announcement, pk=game_announcement_id)
    users_list = announcement.joined_users()
    users_list.remove(str(request.user.id))
    new_joined_list = ";"
    for u in users_list:
        new_joined_list += str(u.id)
        new_joined_list += ";"
    announcement.joined = new_joined_list
    announcement.registered_people -= 1
    announcement.save()
    return redirect('/announcements/' + str(announcement.id))