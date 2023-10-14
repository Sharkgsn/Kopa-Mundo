from django.urls import path
from .views import TeamsView, TeamViewDetail

urlpatterns = [
    path("teams/", TeamsView.as_view()),
    path("teams/<int:team_id>/", TeamViewDetail.as_view()),
]
