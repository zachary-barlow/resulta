def get_team(data, idd):
  return [team for team in data if team['team_id'] == idd]