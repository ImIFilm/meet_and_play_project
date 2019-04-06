from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:game_announcement_id>', views.detail, name='detail'),
    path('<int:game_announcement_id>/upvote', views.upvote, name='upvote'),
]