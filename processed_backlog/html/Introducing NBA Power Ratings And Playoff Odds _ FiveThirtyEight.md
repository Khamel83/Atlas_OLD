# Introducing NBA Power Ratings And Playoff Odds | FiveThirtyEight

**Source:** inputs/New Docs/html/fivethirtyeight.com_datalab_introducing-nba-power-ratings-and-playoff-odds.html
**Processed:** 2025-08-24T19:13:46.295154

![](https://fivethirtyeight.com/wp-content/uploads/2015/01/ng1_7778.jpg?w=575)



Stephen Curry of Golden State Warriors after making the game-winning shot against the Orlando Magic on Dec. 2 at Oracle Arena in Oakland, California.

Noah Graham / NBAE / Getty Images

Starting this week, with the help of basketball analytics experts [Jeremias Engelmann](https://twitter.com/jerryengelmann) and [Steve Ilardi](http://psych.ku.edu/people/faculty/ilardi_stephen.shtml), we’re rolling out weekly NBA power rankings fueled by ESPN’s [Real Plus-Minus](http://www.espn.com/nba/story/_/id/10740818/introducing-real-plus-minus) player ratings. These power ratings predict how well each team will perform over the coming week of games; we’ll also list each team’s projected end-of-season win total and its odds of making the playoffs.

If you want to read more about how these ratings work, scroll below the rankings.

![paine-RPM-power-rankings.0119_NEW](https://fivethirtyeight.com/wp-content/uploads/2015/01/paine-rpm-power-rankings-0119_new1.png)

**Q:** What do these ratings mean?

**A:** They represent each team’s projected [per-100 possession](http://hangtime.blogs.nba.com/2013/02/15/the-new-nba-comstats-advanced-stats-all-start-with-pace-and-efficiency/) performance — schedule-adjusted and relative to league average — for the coming week, taking into account the quality of players on each roster, as well as injuries and expected minute allocations.

**Q:** How is player quality measured?

**A:** Using ESPN’s [Real Plus-Minus](http://www.espn.com/nba/story/_/id/10740818/introducing-real-plus-minus) (RPM), which attempts to isolate each player’s contribution to the team’s scoring margin while on the court by adjusting for the quality of his teammates and opponents faced. While the version of RPM [listed at ESPN.com](http://www.espn.com/nba/statistics/rpm/_/sort/RPM) is a single-season metric, these power ratings use the more predictive multiyear version of RPM.

**Q:** Where do the rosters come from?

**A:** ESPN’s [depth charts](http://www.espn.com/nba/depth) and [injury wire](http://www.espn.com/nba/injuries).

**Q:** Who generates the projected minute allocations?

**A:** [Jeremias Engelmann](http://stats-for-the-nba.appspot.com), the creator of Real Plus-Minus, provides the minute projections for each team.

**Q:** How are these different from other computer power ratings available, such as the [Hollinger Power Rankings](http://www.espn.com/nba/hollinger/powerrankings)?

**A:** Most power ratings are, to some extent or another, backward-looking; they can only generate ratings using inputs from games the team has played. Given a large enough — and relevant enough — sample of played games, this is usually not a problem. But in the case of early-season rankings, or when a team experiences roster changes midseason (via trades or injuries), it takes time for traditional power ratings to catch up to the team’s new quality.

These RPM power ratings, however, are based on the talent of the players on hand for each team. The advantage of this approach is that when a player is added to or subtracted from a team, a talent-based rating can adjust immediately, without waiting for new games to be played. In other words, injuries, trades and signings are instantly accounted for in these rankings.

The other side of that coin is that, barring personnel changes, these ratings aren’t going to change drastically from week to week. RPM player talent estimates have a strong grounding in [Bayesian statistics](http://en.wikipedia.org/wiki/Bayesian_inference); and for veteran players, their [prior](http://en.wikipedia.org/wiki/Prior_probability) rating carries a good deal of weight. So, while a team’s “statement win” in a given week might have a tangible effect on human or even recency-weighted computer power rankings, it’s unlikely to move the needle much with these ratings.

**Q:** Why look at only the next week?

**A:** The ratings can also be modified to use long-term minute projections for players who are injured but will return later in the season. For now, though, we’ve chosen to use the short-term version to get a good snapshot of where each team stands.

**Q:** What are the projected wins and playoff odds?

**A:** Those are generated via the aforementioned long-term RPM talent ratings, rather than the short-term numbers from the power rankings themselves. The long-term ratings are used to simulate every remaining game in the 2014-15 schedule, and the simulated results are added to the NBA’s actual standings. Expected wins are the average number of wins for the team at the end of the season across the simulations; playoff probability shows the percentage of simulations in which the team qualified for the postseason.

**Q:** How good are these ratings?

**A:** It’s hard to say, as this type of analysis — using aggregated player talent ratings to estimate team strength — doesn’t have a long track record. However, RPM itself (or at least its predecessor, xRAPM) is [consistently](http://ascreamingcomesacrossthecourt.blogspot.com/2013/10/2013-retrodiction-how-player-metrics.html) the single [most predictive](http://www.apbr.org/metrics/viewtopic.php?t=8196&p=15343#p15334) advanced metric available to the public. And the FiveThirtyEight [preseason projections](https://fivethirtyeight.com/features/2014-nba-preview-the-rise-of-the-warriors/), which used a similar methodology, are performing well in a [prediction contest](http://apbr.org/metrics/viewtopic.php?p=22167#p22167) against other metrics.