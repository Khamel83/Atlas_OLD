# The Most Shocking Result in World Cup History FiveThirtyEightDataLab | FiveThirtyEight

**Source:** inputs/New Docs/markdown/fivethirtyeight.com_datalab_the-most-shocking-result-in-world-cup-history.md
**Processed:** 2025-08-24T19:49:24.401828

# The Most Shocking Result in World Cup History FiveThirtyEightDataLab | FiveThirtyEight

**URL:** http://fivethirtyeight.com/datalab/the-most-shocking-result-in-world-cup-history/
**Date:** 2014-07-08 22:02:31

---

# The Most Shocking Result in World Cup History

Nate Silver, .Wp-Block-Co-Authors-Plus-Coauthors.Is-Layout-Flow, Class, Wp-Block-Co-Authors-Plus, Display Inline, .Wp-Block-Co-Authors-Plus-Avatar, Where Img, Height Auto Max-Width, Vertical-Align Bottom .Wp-Block-Co-Authors-Plus-Coauthors.Is-Layout-Flow .Wp-Block-Co-Authors-Plus-Avatar, Vertical-Align Middle .Wp-Block-Co-Authors-Plus-Avatar Is .Alignleft .Alignright • July 09, 2014

![The Most Shocking Result in World Cup History](https://fivethirtyeight.com/wp-content/uploads/2014/07/aptopix-brazil-soccer-wcup-brazil-germany.jpg?w=712)

We had Brazil favored to win Tuesday’s World Cup semifinal against Germany (even despite the absence of Neymar and Thiago Silva).

Time to eat some crow. That prediction stunk.

It’s not that a German win was all that unlikely. Germany had a 35 percent chance of victory, according to our model. But the 7-1 scoreline was truly shocking.

The Soccer Power Index (SPI) match-predictor (which uses a poisson distribution to estimate the range of possible scores) gave Germany only a 0.022 percent probability (about one chance in 4,500) of scoring seven or more goals. Likewise, SPI gave Germany a 0.025 percent probability (one chance in 4,000) of beating Brazil by six goals or more.

Statistical models can fail at the extreme tails of a probability distribution. There often isn’t enough historical data to distinguish a 1-in-400 from a 1-in-4,000 from a 1-in-40,000 probability. (This is some of the basis of Nassim Taleb’s book “The Black Swan.”)

We can, however, at least confirm that the match was an extreme outlier from the standpoint of past World Cup matches. There have been 833 matches played since the World Cup began in 1930. Based on the scoreline, this was the most unlikely result.

Although we don’t have SPI ratings before 2006, we can look at the Elo ratings, which are heavily correlated with SPI and contain data back to the 19th century. The Elo ratings (which we’ve updated manually since the start of the World Cup) had Brazil as a 65 percent favorite before Tuesday’s match, with most of that based on its (supposed) home-field advantage.

There’s nothing that noteworthy about a 65 percent favorite losing. Brazil lost as an 87 percent Elo favorite in the 1950 World Cup against Uruguay, for instance. And in the group phase of that World Cup, England lost to the United States with just a 7 percent chance of doing so by Elo’s estimation.

But both of those losses came by a single goal. The Elo formula also accounts for goal differential, although it discounts lopsided margins; scoring the seventh goal doesn’t count as much as scoring the second one. Teams exchange Elo points based on the score of the game and the pre-match odds.

Prior to Tuesday, the biggest shift in Elo points after a World Cup match came in 1958, when Czechoslovakia beat a heavily favored Argentina team by a 6-1 scoreline. That improved Czechoslovakia’s Elo rating by 85 points and lowered Argentina’s by the same margin (in the Elo system, the number of points exchanged between teams always equals zero).

The Germany-Brazil match ranks second by this metric; Germany’s six-goal win produced an 83-point rating shift in its favor.

As I mentioned, however, the Elo system discounts lopsided victories. Since it was the lopsidedness of the scoreline that made Tuesday’s match such an outlier, that somewhat defeats our purpose of placing the result in historical context.

So I ran an alternate version of the Elo ratings that includes no discount for scoring margin — every goal counts as much as the last. By this rendering, the Germany-Brazil match does rank well ahead of anything else.

There are still plenty of questions to ask about the match, and the model. To state the obvious, the loss of Neymar and Silva may have had a much larger impact than we accounted for. Not only do those players have enormous individual talent, they serve as the tactical anchors of Brazil’s offense and defense, respectively. Brazil’s defense appeared disorganized — then stunned, then demoralized.

Betting markets, which had the game at even odds going in, look a lot better than SPI and Elo in this instance.

But there was almost certainly some bad luck for Brazil. It had more shots than Germany in the match — I would never have guessed that while watching the game — and kept possession of the ball slightly more than half the time. Some of the goals that Brazil keeper Julio Cesar allowed were unavoidable, but he was not exactly Tim Howard in net. Even if our model had treated the teams as evenly matched going in, it would still have given Germany just a 1-in-900 chance of winning by six goals or more.

Germany’s win will also affect its odds in the World Cup final. Before Tuesday’s match, SPI had it rated just slightly ahead of the Netherlands but just slightly behind Argentina. But it will get a huge amount of credit for its overwhelming victory, and will likely enter the final as the SPI favorite unless the Argentines or the Dutch do something equally impressive.

CORRECTION (July 9, 10:35 a.m.): A previous version of the third table in this post, “Most Unexpected Scorelines in World Cup History,” incorrectly listed Switzerland defeating Turkey 7-0 in 1998 as the fourth-most unexpected scoreline. It should have listed Turkey defeating South Korea 7-0 in 1954. The table has been updated.

