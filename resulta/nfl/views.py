from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


import requests
from nfl.static.scripts.helpers import get_team
import json
from datetime import datetime
# import asyncio

API_KEY = '74db8efa2a6db279393b433d97c2bc843f8e32b0'

# Create your views here.
def index(request):
  return JsonResponse({'message': 'Hello WOrld'})


async def scoreboard(request, league, start_date, end_date):

  url_score = 'https://delivery.chalk247.com/scoreboard/{}/{}/{}.json?api_key={}'.format(league, start_date, end_date, API_KEY)
  url_rank = 'https://delivery.chalk247.com/team_rankings/{}.json?api_key={}'.format(league, API_KEY)

  data = requests.get(url_score).json()
  ranks = requests.get(url_rank).json()
  # urls = [url_score, url_rank]

  games = data['results'][start_date]['data']
  ranks = ranks['results']['data']
  frm = []

  for game in games.keys():
    ateam = get_team(ranks, games[game]['away_team_id'])[0]
    bteam = get_team(ranks, games[game]['home_team_id'])[0]

    date = games[game]['event_date'].split(' ')
    dates = date[0].split('-')

    frm.append({
      'event_id': games[game]['event_id'],
      'event_date': dates[2]+'-'+ dates[1] + '-' + dates[0],
      'event_time': date[1],
      'away_team_id': games[game]['away_team_id'],
      'away_nick_name': games[game]['away_nick_name'],
      'away_city': games[game]['away_city'],
      'away_rank': ateam['rank'],
      'away_rank_points': '{0:.4g}'.format(float(ateam['points'])),
      'home_team_id': games[game]['home_team_id'],
      'home_nick_name': games[game]['home_nick_name'],
      'home_city': games[game]['home_city'],
      'home_rank': bteam['rank'],
      'home_rank_points': '{0:.4g}'.format(float(bteam['points'])),
    })

  return JsonResponse(frm, safe=False)



def rankings(request, league):
  return HttpResponse({'message': 'Hello WOrld'})