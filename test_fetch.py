import os
from dotenv import load_dotenv
from espn_api.football import League

load_dotenv()

league = League(
    league_id=int(os.environ["ESPN_LEAGUE_ID"]),
    year=int(os.environ["ESPN_SEASON_YEAR"]),
    espn_s2=os.environ["ESPN_S2"],
    swid=os.environ["SWID"],
)

print(f"League: {league.settings.name}")
print(f"Current week: {league.current_week}")
print()
print("Standings:")
for team in league.standings():
    print(f"  {team.team_name:25s} {team.wins}-{team.losses}  PF:{team.points_for:.1f}  PA:{team.points_against:.1f}")

print()
print(f"Box scores for week {league.current_week - 1 if league.current_week > 1 else 1}:")
scores = league.box_scores(league.current_week - 1 if league.current_week > 1 else 1)
for m in scores:
    print(f"  {m.home_team.team_name:20s} {m.home_score:6.1f}  vs  {m.away_score:6.1f} {m.away_team.team_name}")
