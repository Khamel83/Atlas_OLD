# New Powerball Odds Could Give America Its First Billion-Dollar Jackpot | FiveThirtyEight

**Source:** inputs/New Docs/html/fivethirtyeight.com_features_new-powerball-odds-could-give-america-its-first-billion-dollar-jackpot.html
**Processed:** 2025-08-24T19:14:01.994704

![](https://fivethirtyeight.com/wp-content/uploads/2015/07/ap_060927012462-lede.jpg?w=575)



Donald Diedrich, one of the 100 cheese company workers who won a Powerball jackpot worth $208.6 million in 2006.

Morry Gash / AP



Donald Diedrich, one of the 100 cheese company workers who won a Powerball jackpot worth $208.6 million in 2006.

Morry Gash / AP

New York state lottery commissioners approved a proposed rule Monday that would change [the Powerball lottery](http://www.cnbc.com/id/102813761) jackpot odds. Assuming the rest of the Powerball stakeholders get on board (and they have to in order to remain in the Powerball system), the move will make it even less likely that you could win the jackpot. The silver lining? There’s reason to believe that the size of that jackpot is about to get a whole lot bigger.

If those changes go through, the odds of winning the Powerball jackpot will go from about a 1 in 175 million chance to 1 in 292 million. Not great, right? Yes, but the chances of a Powerball win making some future player a billionaire are radically higher. Like, 7.5 times as high.

I’ve looked into the [odds of someone winning the Powerball before](https://fivethirtyeight.com/features/will-someone-win-the-powerball-jackpot-tonight/): There’s a pretty direct relationship between the advertised jackpot and how many tickets are sold. As a result, as the pot gets bigger, it’s harder for the jackpot to keep growing (because with all those tickets sloshing around someone is likely to win, which resets the pot). I used that dynamic to figure out the probability of one or more winners at any given advertised pot.

![hickey.lotto.5](https://fivethirtyeight.com/wp-content/uploads/2014/06/hickey-lotto-5.png)

The proposed change would render those calculations obsolete. Damn! But that’s probably a good thing, as the American people may finally get that billion-dollar lottery that has [eluded the nation for so long](https://en.wikipedia.org/wiki/Lottery_jackpot_records).

Based on a basic model I built that simulates Powerball jackpots over the next five years of play, the odds change makes a huge, huge difference. Under the old (1 in 175,223,510) odds, there was a billion-dollar lottery in **only 8.5 percent** of the simulated five-year periods. But under the new (1 in 292,201,338) odds, there was a billion-dollar lottery in **63.4 percent** of the simulated five-year periods.

If you’re just a casual player, those are the numbers to take away from this. Go start saving up for the Big One, because it may be on its way. But for the rest of you lottery nerds, I have a polynomial regression that I’m dying to tell you about.

To figure out the likelihood of a billion-dollar jackpot, I needed to first see how much a Powerball jackpot rises from one drawing to the next. Powerball jackpots reset at $40 million if someone wins, but otherwise rise with each drawing. Using historical data, I plotted the percent increase between each jackpot. There’s some variation in there because the lottery’s growth is determined by the number of people who bought tickets for each drawing. But since there’s a relationship between advertised jackpot and participation, there’s a pattern.

![hickey-datalab-powerballchange-2](https://fivethirtyeight.com/wp-content/uploads/2015/07/hickey-datalab-powerballchange-2.png)

That line you see is the polynomial regression I wanted to tell you about. The relationship between jackpot size and subsequent increase can’t be described as linear or even exponential because, though the growth looks exponential, the Powerball people have guaranteed that the jackpot rises at least $10 million between drawings, no matter how many tickets are sold. That meant I needed to use a polynomial regression to figure out the general trend of jackpot increases.1

Ideally, we’d be able to build a probability distribution at every single jackpot quantity to simulate the lottery. But that gets very complex very quickly, and we probably don’t have enough data at the high numbers to make that approach worthwhile. Instead, I used that polynomial trend line to make a slightly simpler model that could still help us see the way this change will affect the big picture.

Imagine a simpler lottery that behaves similarly to Powerball: the “Powerball-ish lottery.” Clever name, I know.

It starts at $40 million, as Powerball does. Then the second drawing goes to $50 million, and the third to $60 million.2 From there, I calculated the subsequent jackpots based on that growth rate we figured out earlier.

![hickey-datalab-powerballchange-1](https://fivethirtyeight.com/wp-content/uploads/2015/07/hickey-datalab-powerballchange-1.png)

Based on my assumptions, the 17th drawing would be the elusive billion-dollar lottery. It’s far from a perfect simulation of Powerball, obviously, but it’s the best we can do with what we have.

Under the current system it’s incredibly hard to get to 17 lotteries without somebody winning. The massive ticket sales we see for lotteries with jackpots of $400 million or so make it highly improbable that the jackpot can increase enough to cross the threshold. Check out this chart showing historical ticket sales:

![hickey.lotto.pball-UPDATED](https://fivethirtyeight.com/wp-content/uploads/2015/07/hickey-lotto-pball-updated.png)

But if the Powerball honchos lower the probability of winning a jackpot overall, it’s pretty likely that in the next couple of years we’ll have it.

To make that billion-dollar assertion, I assumed there’d be 520 Powerball drawings in the next five years (because there are [two drawings per week](http://www.lottoreport.com/powerballsales.htm) and 52 weeks in a year). In those 520 drawings, under the new proposed odds, a ticket would have a 1 in 292,201,338 chance of winning. So using numbers on how many people play at a given jackpot amount (using ticket sales data from [Lotto Report](http://www.lottoreport.com/powerballsales.htm)), I estimated the probability of at least one person winning in each round of the Powerball-ish lottery.
![jackpot table](https://fivethirtyeight.com/wp-content/uploads/2015/07/screenshot-2015-07-08-15-27-31.png)

|  |  | CHANCE THAT JACKPOT IS WON | |  |
| --- | --- | --- | --- | --- |
| JACKPOT | EST. TICKET SALES | CURRENT ODDS | PROPOSED ODDS |
| $40m | 14m | 8% | 5% |
| 50 | 16 | 8 | 5 |
| 60 | 17 | 9 | 6 |
| 72 | 19 | 10 | 6 |
| 85 | 21 | 11 | 7 |
| 98 | 23 | 12 | 8 |
| 114 | 27 | 14 | 9 |
| 130 | 30 | 15 | 10 |
| 148 | 33 | 17 | 11 |
| 169 | 37 | 19 | 12 |
| 193 | 44 | 22 | 14 |
| 223 | 56 | 27 | 17 |
| 265 | 75 | 35 | 23 |
| 331 | 100 | 43 | 29 |
| 464 | 160 | 60 | 42 |
| 892 | 504 | 94 | 82 |

Using that, I ran 100,000 simulations of the next five years of drawings with the old and new odds, and I tallied the number of times there was at least one billion-dollar lottery in the five-year period. In each drawing, if someone won it would reset to $40 million, and if nobody won then it would climb to the next tier.

In the end, 8.5 percent of the simulations with the old odds got a billion-dollar lottery, and 63.4 percent of the sims with the new odds did. If the people who run Powerball want larger jackpots, they’re going to get them.

That’s not necessarily what we’d expect in the real world. This doesn’t account for different lotto ticket sales after the odds change, and it doesn’t factor in other possible rule changes the people running Powerball might make. But in our Powerball-ish scenario, a little tweak made a huge difference in record-smashing lottos. You may not win as often, but whoever does has a decent shot at winning more money than ever.