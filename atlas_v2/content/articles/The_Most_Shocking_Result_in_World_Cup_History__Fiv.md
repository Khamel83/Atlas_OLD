# The Most Shocking Result in World Cup History | FiveThirtyEight

**Source**: inputs/New Docs/html/fivethirtyeight.com_datalab_the-most-shocking-result-in-world-cup-history.html
**Type**: article
**Created**: 2025-08-25T02:53:47.440446

---

![](https://fivethirtyeight.com/wp-content/uploads/2014/07/aptopix-brazil-soccer-wcup-brazil-germany.jpg?w=575)



Brazil’s Marcelo during Tuesday’s World Cup semifinal between Brazil and Germany at the Mineirao Stadium in Belo Horizonte, Brazil.

Francois Xavier Marit / AP

We [had Brazil favored](https://fivethirtyeight.com/features/world-cup-semifinal-crib-notes-brazil-vs-germany/) to win Tuesday’s World Cup semifinal against Germany (even [despite the absence](https://fivethirtyeight.com/features/how-neymars-injury-affects-brazils-chances-at-the-world-cup/) of Neymar and Thiago Silva).

Time to eat some crow. That prediction stunk.

It’s not that a German win was all that unlikely. Germany had a 35 percent chance of victory, according to our model. But the 7-1 scoreline was truly shocking.

The Soccer Power Index (SPI) match-predictor (which uses a [poisson distribution](http://en.wikipedia.org/wiki/Poisson_distribution) to estimate the range of possible scores) gave Germany only a 0.022 percent probability (about one chance in 4,500) of scoring seven or more goals. Likewise, SPI gave Germany a 0.025 percent probability (one chance in 4,000) of beating Brazil by six goals or more.

Statistical models can fail at the extreme tails of a probability distribution. There often isn’t enough historical data to distinguish a 1-in-400 from a 1-in-4,000 from a 1-in-40,000 probability. (This is some of the basis of Nassim Taleb’s book “[The Black Swan](https://www.youtube.com/watch?v=BDbuJtAiABA).”)

We can, however, at least confirm that the match was an extreme outlier from the standpoint of past World Cup matches. There have been 833 matches played since the World Cup began in 1930. Based on the scoreline, this was the most unlikely result.

Although we don’t have SPI ratings before 2006, we can look at the [Elo ratings](https://fivethirtyeight.com/features/how-fivethirtyeights-world-cup-predictions-compare-to-other-ratings/), which are [heavily correlated with SPI](https://fivethirtyeight.com/features/how-fivethirtyeights-world-cup-predictions-compare-to-other-ratings/) and contain data back to the 19th century. The Elo ratings (which we’ve [updated manually](https://fivethirtyeight.com/features/updated-elo-ratings-for-world-cup-teams/) since the start of the World Cup) had Brazil as a 65 percent favorite before Tuesday’s match, with most of that based on its (supposed) home-field advantage.

There’s nothing that noteworthy about a 65 percent favorite losing. Brazil lost as an [87 percent Elo favorite](http://www.eloratings.net/system.html) in the 1950 World Cup against Uruguay, for instance. And in the group phase of that World Cup, England lost to the United States with just a 7 percent chance of doing so by Elo’s estimation.

![eatcrow1](https://fivethirtyeight.com/wp-content/uploads/2014/07/eatcrow1.png)

But both of those losses came by a single goal. The Elo formula also accounts for goal differential, although it discounts lopsided margins; scoring the seventh goal doesn’t count as much as scoring the second one. Teams exchange Elo points based on the score of the game and the pre-match odds.

Prior to Tuesday, the [biggest shift in Elo points](http://www.eloratings.net/Upsets.htm) after a World Cup match came in 1958, when [Czechoslovakia beat a heavily favored Argentina team by a 6-1 scoreline](https://www.youtube.com/watch?v=E1F5t-G-3W4). That improved Czechoslovakia’s Elo rating by 85 points and lowered Argentina’s by the same margin (in the Elo system, the [number of points](http://www.eloratings.net/system.html) exchanged between teams always equals zero).

The Germany-Brazil match ranks second by this metric; Germany’s six-goal win produced an 83-point rating shift in its favor.

![eatcrow2](https://fivethirtyeight.com/wp-content/uploads/2014/07/eatcrow2.png)

As I mentioned, however, the Elo system discounts lopsided victories. Since it was the lopsidedness of the scoreline that made Tuesday’s match such an outlier, that somewhat defeats our purpose of placing the result in historical context.

So I ran an alternate version of the Elo ratings that includes no discount for scoring margin — every goal counts as much as the last. By this rendering, the Germany-Brazil match does rank well ahead of anything else.

![eatcrow3](https://fivethirtyeight.com/wp-content/uploads/2014/07/eatcrow31.png)

There are still plenty of questions to ask about the match, and the model. To state the obvious, the loss of Neymar and Silva may have had a much larger impact than [we accounted for](https://fivethirtyeight.com/features/how-neymars-injury-affects-brazils-chances-at-the-world-cup/). Not only do those players have enormous individual talent, they serve as the tactical anchors of Brazil’s offense and defense, respectively. Brazil’s defense appeared disorganized — then stunned, then demoralized.

Betting markets, which had the game at even odds going in, look a lot better than SPI and Elo in this instance.

But there was almost certainly some bad luck for Brazil. It had [more shots than Germany in the match](http://www.fifa.com/worldcup/matches/round=255955/match=300186474/statistics.html) — I would never have guessed that while watching the game — and kept possession of the ball slightly more than half the time. Some of the goals that Brazil keeper Julio Cesar allowed were unavoidable, but he was [not exactly Tim Howard in net](https://fivethirtyeight.com/features/tim-howard-lost-but-he-just-had-the-best-match-of-the-world-cup/). Even if our model had treated the teams as evenly matched going in, it would still have given Germany just a 1-in-900 chance of winning by six goals or more.

Germany’s win will also affect its odds in the World Cup final. Before Tuesday’s match, SPI had it rated just slightly ahead of the Netherlands but just slightly behind Argentina. But it will get a huge amount of credit for its overwhelming victory, and will likely enter the final as the SPI favorite unless the Argentines or the Dutch do something equally impressive.