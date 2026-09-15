"""Power ranking engine: turns ESPN league standings/box scores into an ordered,
scored list of teams. Pure data-in/data-out so it can be unit-tested with mock data."""

from dataclasses import dataclass, field


@dataclass
class TeamWeek:
    team_name: str
    wins: int
    losses: int
    points_for: float
    points_against: float
    last_3_scores: list = field(default_factory=list)  # most recent last, e.g. [98.2, 110.4, 121.7]


def power_score(t: TeamWeek, league_avg_pf: float) -> float:
    """Blend of record, scoring efficiency, and recent form.
    Weights: 45% win pct, 30% points-for vs league average, 25% recent-3-week trend."""
    games = max(t.wins + t.losses, 1)
    win_pct = t.wins / games

    pf_per_game = t.points_for / games
    pf_component = (pf_per_game - league_avg_pf) / league_avg_pf if league_avg_pf else 0

    if len(t.last_3_scores) >= 2:
        trend = (t.last_3_scores[-1] - t.last_3_scores[0]) / max(t.last_3_scores[0], 1)
    else:
        trend = 0

    return round(win_pct * 45 + pf_component * 30 + trend * 25, 2)


def rank_teams(teams: list) -> list:
    """teams: list[TeamWeek]. Returns list of (rank, team, score) sorted best to worst."""
    games_played = [max(t.wins + t.losses, 1) for t in teams]
    league_avg_pf = sum(t.points_for / g for t, g in zip(teams, games_played)) / len(teams)

    scored = [(t, power_score(t, league_avg_pf)) for t in teams]
    scored.sort(key=lambda x: x[1], reverse=True)

    return [(i + 1, t, s) for i, (t, s) in enumerate(scored)]
