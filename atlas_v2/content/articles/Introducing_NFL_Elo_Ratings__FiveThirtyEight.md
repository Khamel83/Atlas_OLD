# Introducing NFL Elo Ratings | FiveThirtyEight

**Source**: inputs/New Docs/html/fivethirtyeight.com_datalab_introducing-nfl-elo-ratings.html
**Type**: article
**Created**: 2025-08-25T02:53:44.963404

---

If you followed FiveThirtyEight’s [coverage](https://fivethirtyeight.com/features/updated-elo-ratings-for-world-cup-teams/) during the World Cup, you know that we’re big fans of the [World Football Elo Ratings](http://www.eloratings.net/). They’re based on a relatively simple system developed by the physicist [Arpad Elo](http://www.nytimes.com/1992/11/14/obituaries/prof-arpad-e-elo-is-dead-at-89-inventor-of-chess-ratings-system.html) to rate chess players. But they can be adapted fairly easily for other head-to-head competitions from [baseball](http://www.baseballprospectus.com/article.php?articleid=5247) to [backgammon](http://usbgf.org/ratings-stats-mission-and-policy/).

We thought we’d have a little fun and extend them to American football. In [an accompanying post](https://fivethirtyeight.com/features/nfl-week-1-elo-ratings/), you’ll find our initial Elo ratings for all 32 NFL teams (at this point, the ratings are based on a team’s standing at the end of last season, discounted slightly to reflect reversion to the mean). We’ve also developed a simulator program that plays out the NFL schedule thousands of times and projects a team’s likelihood of making the playoffs, based on a team’s record up to that point in time, its Elo rating, its remaining schedule and the NFL’s [various tiebreaker rules](http://www.nfl.com/standings/tiebreakingprocedures). We plan to update these projections at the end of every week.

But first (inspired somewhat by The New York Times’s [personification](http://www.nytimes.com/newsgraphics/2014/senate-model/methodology.html) of its election model, Leo), we thought we’d “interview” the Elo system about how it does its work.


Elo: I’m simple, transparent and easy to work with. I can do a lot with a little, such as calculating point spreads and the probability of either team winning a game.


I wouldn’t try that. Vegas lines account for a much wider array of information than I do. When Nate [backtested](http://en.wikipedia.org/wiki/Backtesting) me, he found that I got 51 percent of games right against the point spread. That’s not nearly enough to cover the [house’s cut](http://en.wikipedia.org/wiki/Vigorish), much less to make a living.


That’s a perfect example. Has anything strange been going on with the Packers?


If this Mr. Rodgers fellow is as good as you say he is, that could account for the difference. I don’t know anything about him. I only keep track of the final scores, the dates of games and where the games were played.


Think of me as a benchmark. I do a pretty good job of accounting for the basic stuff — wins and losses, margin of victory, strength of schedule. I also retain a memory from past seasons, so I know that the Jacksonville Jaguars aren’t as likely to win the Super Bowl as the Denver Broncos. Can we get to some more technical questions?


That’s more like it. Like *K*, for instance; *K* is my favorite parameter.


*K* tells me how much to update my ratings after each game. In a sport like baseball, where there are lots of games, any one additional game doesn’t tell you all that much, so *K* takes on a low value. In the NFL, it’s much higher. Specifically, it’s the number 20. That may not mean anything to you, but if you set *K* a lot higher than that, I’d be a nervous wreck and bounce around too much from game to game. And if you made *K* much lower, I’d be hopelessly sluggish and too slow to notice changes in the quality of team’s play.


An average team has an Elo rating of 1500 — so your Lions are not so hot. But it could be a lot worse. In 2009, the Lions got all the way down to a rating of 1223. Most NFL teams wind up in the range of 1300 to 1700.


If it makes things easier, you can translate my ratings into a point spread. Take the difference in my ratings and divide by 25. It’s that simple.


Precisely.


I can account for that, too. Historically, it’s been worth about 65 Elo ratings points or 2.6 NFL points. Just add that to the point spread.


That’s pretty easy, too, although you’ll need a [formula](http://www.eloratings.net/system.html) for it. In a game between Team A and Team B, Team A’s win probability is equal to:

Pr(A) = 1 / (10^(-ELODIFF/400) + 1)

Where ELODIFF is Team A’s Elo rating minus Team B’s Elo rating.


Yes. One of my more appealing properties is that a team’s Elo rating will always improve after it wins and always decline after it loses. How much it improves will depend on how much of a favorite or an underdog it was.


I can predict where you’re going with that question. I’ll admit that I didn’t have the New York Giants rated so highly compared to the New England Patriots. But the Giants’ Elo rating improved a lot after they won that game — more than the Patriots’ would have if they’d won instead. I may have my flaws, but unlike a lot of you human beings, I know how to fix them. The lower a team is rated, the easier for it to gain ground by proving me wrong.


Affirmative. I took some inspiration from the soccer ratings, which account for goal differential in addition to the game result. But this is one of the more complicated parts.

For the NFL, I start by adding one point to team’s margin of victory and then take its [natural logarithm](http://mathworld.wolfram.com/NaturalLogarithm.html). Then I multiply that result by the *K* value. That means I’m more moved by big wins than narrow ones, although there are diminishing returns. I’m not so impressed by the fifth touchdown when a team is ahead 28-0.


It would be, but that isn’t all there is to it. We haven’t talked about my autocorrelation problem. It’s a little embarrassing.


Autocorrelation is the tendency of a time series to be correlated with its past and future values. Let me put this into football terms. Imagine I have the Dallas Cowboys rated at 1550 before a game against the Philadelphia Eagles. Their rating will go up if they win and go down if they lose. But it should be 1550 after the game, on average. That’s important, because it means that I’ve accounted for all the information you’ve given me efficiently. If I expected the Cowboys’ rating to rise to 1575 on average after the game, I should have rated them more highly to begin with.

It’s true that if I have the Cowboys favored against the Eagles, they should win more often than they lose. But the way I was originally designed, I can compensate by subtracting more points for a loss than I give them for a win. Everything balances out rather elegantly.

The problem comes when I also seek to account for margin of victory. Not only do favorites win more often, but when they do win, they tend to win by a larger margin. Since I give more credit for larger wins, this means that their ratings tend to get inflated over time.


Possibly. You may want to reconsider [what you wrote about Germany](https://fivethirtyeight.com/features/germany-may-be-the-best-national-soccer-team-ever/).


It isn’t complicated in principle. You just have to discount the margin of victory more when favorites win and increase it when underdogs win. The formula for it is as follows:

Margin of Victory Multiplier = LN(ABS(PD)+1) \* (2.2/((ELOW-ELOL)\*.001+2.2))

Where PD is the point differential in the game, ELOW is the winning team’s Elo Rating before the game, and ELOL is the losing team’s Elo Rating before the game.

It’s a little ugly, but we all have our vices.


I take their rating from the end of last season and discount it slightly. Specifically, I revert it to the mean by one-third. Remember that the mean Elo rating is 1500. So, if a team finished last season with a rating of 1800, I’ll revert it to 1700 when the new season begins. This whole notion of “season” is strange to me, by the way. We don’t have them in chess.


Technically speaking, a game affects my ratings forever once it’s played, just with a smaller and smaller weight that gradually diminishes to almost nothing over time. But, yes, for the time being, my ratings are mostly about who was good last season. Games toward the end of the season will count more, especially games during last year’s playoffs.


[How about a nice game of chess](https://www.youtube.com/watch?v=NHWjlCaIrQo)?

*See the [Week 1 Elo ratings and playoff odds](https://fivethirtyeight.com/features/nfl-week-1-elo-ratings/).*