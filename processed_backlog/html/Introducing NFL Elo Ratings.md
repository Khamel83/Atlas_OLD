# Introducing NFL Elo Ratings

**Source:** inputs/New Docs/reader/fivethirtyeight.com_datalab_introducing-nfl-elo-ratings.html
**Processed:** 2025-08-24T19:14:20.910622

If you followed FiveThirtyEight’s coverage during the World Cup, you know that we’re big fans of the World Football Elo Ratings. They’re based on a relatively simple system developed by the physicist Arpad Elo to rate chess players. But they can be adapted fairly easily for other head-to-head competitions from baseball to backgammon.  
  
We thought we’d have a little fun and extend them to American football. In an accompanying post, you’ll find our initial Elo ratings for all 32 NFL teams (at this point, the ratings are based on a team’s standing at the end of last season, discounted slightly to reflect reversion to the mean). We’ve also developed a simulator program that plays out the NFL schedule thousands of times and projects a team’s likelihood of making the playoffs, based on a team’s record up to that point in time, its Elo rating, its remaining schedule and the NFL’s various tiebreaker rules. We plan to update these projections at the end of every week.  
  
But first (inspired somewhat by The New York Times’s personification of its election model, Leo), we thought we’d “interview” the Elo system about how it does its work.  
  
FiveThirtyEight: What are some of some of your best qualities?  
  
Elo: I’m simple, transparent and easy to work with. I can do a lot with a little, such as calculating point spreads and the probability of either team winning a game.  
  
Can I use you to beat Vegas?  
  
I wouldn’t try that. Vegas lines account for a much wider array of information than I do. When Nate backtested me, he found that I got 51 percent of games right against the point spread. That’s not nearly enough to cover the house’s cut, much less to make a living.  
  
We noticed that you have the Seattle Seahawks favored by 10 points in their Thursday-night game against the Green Bay Packers, while Vegas has the Seahawks as six-point favorites instead.  
  
That’s a perfect example. Has anything strange been going on with the Packers?  
  
Well, their star quarterback, Aaron Rodgers, was injured. Now he’s back!  
  
If this Mr. Rodgers fellow is as good as you say he is, that could account for the difference. I don’t know anything about him. I only keep track of the final scores, the dates of games and where the games were played.  
  
So what good are you?  
  
Think of me as a benchmark. I do a pretty good job of accounting for the basic stuff — wins and losses, margin of victory, strength of schedule. I also retain a memory from past seasons, so I know that the Jacksonville Jaguars aren’t as likely to win the Super Bowl as the Denver Broncos. Can we get to some more technical questions?  
  
Um … what are your parameters?  
  
That’s more like it. Like K, for instance; K is my favorite parameter.  
  
What makes K so special?  
  
K tells me how much to update my ratings after each game. In a sport like baseball, where there are lots of games, any one additional game doesn’t tell you all that much, so K takes on a low value. In the NFL, it’s much higher. Specifically, it’s the number 20. That may not mean anything to you, but if you set K a lot higher than that, I’d be a nervous wreck and bounce around too much from game to game. And if you made K much lower, I’d be hopelessly sluggish and too slow to notice changes in the quality of team’s play.  
  
I noticed the Detroit Lions have an Elo rating of 1467. What does that mean?  
  
An average team has an Elo rating of 1500 — so your Lions are not so hot. But it could be a lot worse. In 2009, the Lions got all the way down to a rating of 1223. Most NFL teams wind up in the range of 1300 to 1700.  
  
We’re still not quite sure how your ratings work. If you have one team at a 1650 and another at 1400, what does that mean?  
  
If it makes things easier, you can translate my ratings into a point spread. Take the difference in my ratings and divide by 25. It’s that simple.  
  
So, if one team is rated 250 Elo points higher than the other, that works out to a spread of 10 football points.  
  
Precisely.  
  
What about home-field advantage?  
  
I can account for that, too. Historically, it’s been worth about 65 Elo ratings points or 2.6 NFL points. Just add that to the point spread.  
  
What if you want to calculate a team’s probability of winning?  
  
That’s pretty easy, too, although you’ll need a formula for it. In a game between Team A and Team B, Team A’s win probability is equal to:  
  
Pr(A) = 1 / (10^(-ELODIFF/400) + 1)  
  
Where ELODIFF is Team A’s Elo rating minus Team B’s Elo rating.  
  
Let’s say Team A wins. Its Elo rating will improve?  
  
Yes. One of my more appealing properties is that a team’s Elo rating will always improve after it wins and always decline after it loses. How much it improves will depend on how much of a favorite or an underdog it was.  
  
So, like after the 2008 Super Bowl …  
  
I can predict where you’re going with that question. I’ll admit that I didn’t have the New York Giants rated so highly compared to the New England Patriots. But the Giants’ Elo rating improved a lot after they won that game — more than the Patriots’ would have if they’d won instead. I may have my flaws, but unlike a lot of you human beings, I know how to fix them. The lower a team is rated, the easier for it to gain ground by proving me wrong.  
  
Do you also account for margin of victory?  
  
Affirmative. I took some inspiration from the soccer ratings, which account for goal differential in addition to the game result. But this is one of the more complicated parts.  
  
For the NFL, I start by adding one point to team’s margin of victory and then take its natural logarithm. Then I multiply that result by the K value. That means I’m more moved by big wins than narrow ones, although there are diminishing returns. I’m not so impressed by the fifth touchdown when a team is ahead 28-0.  
  
That seems simple enough.  
  
It would be, but that isn’t all there is to it. We haven’t talked about my autocorrelation problem. It’s a little embarrassing.  
  
Go on. “Autocorrelation”? Was that the weird David Cronenberg movie?  
  
Autocorrelation is the tendency of a time series to be correlated with its past and future values. Let me put this into football terms. Imagine I have the Dallas Cowboys rated at 1550 before a game against the Philadelphia Eagles. Their rating will go up if they win and go down if they lose. But it should be 1550 after the game, on average. That’s important, because it means that I’ve accounted for all the information you’ve given me efficiently. If I expected the Cowboys’ rating to rise to 1575 on average after the game, I should have rated them more highly to begin with.  
  
It’s true that if I have the Cowboys favored against the Eagles, they should win more often than they lose. But the way I was originally designed, I can compensate by subtracting more points for a loss than I give them for a win. Everything balances out rather elegantly.  
  
The problem comes when I also seek to account for margin of victory. Not only do favorites win more often, but when they do win, they tend to win by a larger margin. Since I give more credit for larger wins, this means that their ratings tend to get inflated over time.  
  
Is this also a flaw with the soccer Elo ratings?  
  
Possibly. You may want to reconsider what you wrote about Germany.  
  
So, how do you correct for this?  
  
It isn’t complicated in principle. You just have to discount the margin of victory more when favorites win and increase it when underdogs win. The formula for it is as follows:  
  
Margin of Victory Multiplier = LN(ABS(PD)+1) \* (2.2/((ELOW-ELOL)\*.001+2.2))  
  
Where PD is the point differential in the game, ELOW is the winning team’s Elo Rating before the game, and ELOL is the losing team’s Elo Rating before the game.  
  
It’s a little ugly, but we all have our vices.  
  
I see that you have ratings for this year’s teams, but they haven’t played any games yet! How does that work?  
  
I take their rating from the end of last season and discount it slightly. Specifically, I revert it to the mean by one-third. Remember that the mean Elo rating is 1500. So, if a team finished last season with a rating of 1800, I’ll revert it to 1700 when the new season begins. This whole notion of “season” is strange to me, by the way. We don’t have them in chess.  
  
For now, the ratings are all about which teams were good last year?  
  
Technically speaking, a game affects my ratings forever once it’s played, just with a smaller and smaller weight that gradually diminishes to almost nothing over time. But, yes, for the time being, my ratings are mostly about who was good last season. Games toward the end of the season will count more, especially games during last year’s playoffs.  
  
Thanks for taking the time! So, you’re saying we should take the Seahawks?  
  
How about a nice game of chess?  
  
See the Week 1 Elo ratings and playoff odds.