from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('scoreboard/<str:league>/<slug:start_date>/<slug:end_date>/', views.scoreboard, name='scoreboard'),
]