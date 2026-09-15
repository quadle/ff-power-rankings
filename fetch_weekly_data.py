"""Pulls this week's league facts from ESPN into a plain JSON blob.
Kept deterministic and free of any write-up/commentary logic — the write-up step
(power rankings text) is a separate step so the numbers are always ground-truth
and only the prose is generated."""

import os
import json
import sys
from dotenv import load_dotenv
from espn_api.football import League

load_dotenv()


def fetch(week: int = None):
    league = League(
        league_id=int(os.environ["ESPN_LEAGUE_ID"]),
        year=int(os.environ["ESPN_SEASON_YEAR"]),
        espn_s2=os.environ["ESPN_S2"],
        swid=os.environ["SWID"],
    )

    target_week = week or max(league.current_week - 1, 1)

    standings = []
    for t in league.standings():
        standings.append({
            "team_name": t.team_name,
            "owner": (t.owners[0]["firstName"] if t.owners else t.team_name),
            "wins": t.wins,
            "losses": t.losses,
            "points_for": round(t.points_for, 1),
            "points_against": round(t.points_against, 1),
        })

    matchups = []
    try:
        for m in league.box_scores(target_week):
            home = getattr(m, "home_team", None)
            away = getattr(m, "away_team", None)
            matchups.append({
                "home_team": home.team_name if home else None,
                "home_score": round(m.home_score, 1) if home else None,
                "away_team": away.team_name if away else None,
                "away_score": round(m.away_score, 1) if away else None,
            })
    except Exception as e:
        matchups = []
        print(f"warning: could not fetch box scores for week {target_week}: {e}", file=sys.stderr)

    return {
        "league_name": league.settings.name,
        "week": target_week,
        "standings": standings,
        "matchups": matchups,
    }


if __name__ == "__main__":
    print(json.dumps(fetch(), indent=2))
