from django.urls import path

from . import views

urlpatterns = [
  path('scoreboard/<str:league>/<slug:start_date>/<slug:end_date>/', views.scoreboard, name='scoreboard'),
]