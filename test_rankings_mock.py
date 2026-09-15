from rankings import TeamWeek, rank_teams

mock_teams = [
    TeamWeek("Kit's Top-Notch Team", 3, 1, 452.3, 401.1, [98.2, 130.4, 121.7]),
    TeamWeek("g's Great Team", 3, 1, 470.8, 410.2, [140.1, 95.6, 150.2]),
    TeamWeek("NE Legendarios", 2, 2, 400.5, 415.0, [88.4, 92.1, 105.6]),
    TeamWeek("Marshall", 2, 2, 390.0, 380.4, [120.5, 110.2, 89.9]),
    TeamWeek("REPEAT", 1, 3, 370.2, 430.5, [70.1, 85.3, 60.2]),
    TeamWeek("Alex's Astounding Team", 1, 3, 385.6, 420.1, [100.2, 60.5, 95.0]),
    TeamWeek("mason's Magnificent Team", 4, 0, 480.9, 390.0, [110.4, 125.6, 135.2]),
]

for rank, team, score in rank_teams(mock_teams):
    print(f"{rank}. {team.team_name:28s} score={score:6.2f}  ({team.wins}-{team.losses}, PF {team.points_for})")
