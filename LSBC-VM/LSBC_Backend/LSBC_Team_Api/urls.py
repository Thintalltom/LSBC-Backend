from django.urls import path
from .views import (
    ClubCreateView, PlayerCreateView, CoachCreateView, ClubListView,
    ClubDeleteView, PlayerUpdateView, PlayerDeleteView, 
    CoachUpdateView, CoachDeleteView
)

urlpatterns = [
    path("clubs/", ClubCreateView.as_view()),
    path("clubs/list/", ClubListView.as_view()),
    path("clubs/<str:club_id>/", ClubDeleteView.as_view()),
    path("clubs/<str:club_id>/players/", PlayerCreateView.as_view()),
    path("clubs/<str:club_id>/coaches/", CoachCreateView.as_view()),
    path("players/<str:player_id>/", PlayerUpdateView.as_view()),
    path("players/<str:player_id>/delete/", PlayerDeleteView.as_view()),
    path("coaches/<str:coach_id>/", CoachUpdateView.as_view()),
    path("coaches/<str:coach_id>/delete/", CoachDeleteView.as_view()),
]
