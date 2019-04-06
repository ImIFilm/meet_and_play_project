from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:game_announcement_id>', views.detail, name='detail'),
    path('<int:game_announcement_id>/join', views.join, name='join'),
    path('<int:game_announcement_id>/resign', views.resign, name='resign'),
]