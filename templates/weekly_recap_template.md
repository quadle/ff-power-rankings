# Weekly Recap — Prompt Template

Use this structure every week once `fetch_weekly_data.py` (standings + box scores/lineups)
has been pulled for the completed week. Feed the raw JSON plus the previous week's
power-rankings order into the write-up step.

## Required inputs
- This week's matchup results (final scores, home/away)
- Full starting lineups with actual points vs. projected points (to find over/underperformers)
- Last week's power rankings order (to compute up/down tick per team)
- Season-long standings (record, points for/against) for context

## Sections, in order

1. **Title**: `# 🏈 WEEK {N} RECAP — {League Name}`

2. **🏆 Best Team of the Week**
   - Team with the best combination of win + highest score (usually the top scorer, win required).
   - Call out 3-4 specific players who beat their projection and tie each one back to the
     draft-day decision that made them available (rookie pick, late-round flier, handcuff, etc).
   - If a past preseason take about this team was wrong, acknowledge it directly — self-aware
     callbacks land well.

3. **💀 Worst Team of the Week**
   - Team with the worst combination of loss + lowest score.
   - Call out which specific starters busted relative to projection.
   - Optional: an "honorable tough beat" shoutout for a team that scored well but still lost
     (high score + loss is a real, sympathetic storyline — don't roast those teams as hard).

4. **⭐ Standout Performers**
   - Top 8-10 individual scores across the whole league, ranked.
   - A short "biggest busts" list: studs who scored far under projection.

5. **📊 Power Rankings**
   - Full 1-N order for the week.
   - Each team gets a tick vs. last week's rank: `🔼 +N` / `🔽 -N` / `➖ 0`.
     (Ticks must always sum to zero across the league — it's a reordering of the same ranks.)
   - Tone: legit analysis first, then a sparing, sarcastic jab specifically aimed at the
     draft-day decision (or preseason take) that explains a bad week — not just "you lost."
   - Teams that lost narrowly or scored well despite losing get a lighter touch than teams
     that got blown out or started a real dud.

## Tone rules
- Mostly legit/analytical, funny in small doses — not a joke every line.
- Always ground jokes in an actual stat (projection vs. actual, a specific bench/start
  decision) rather than generic trash talk.
- Self-aware callbacks to previous weeks' picks/predictions are the best material.
