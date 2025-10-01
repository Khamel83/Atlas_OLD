# Numbers Game

**Source**: https://fiftytwo.in/story/numbers-game/
**Type**: article
**Created**: 2025-08-25T02:53:32.134295

---

# Numbers Game

### Big data already changed the way cricket was being watched. Now, machine learning is transforming the way it’s played.

 ![Numbers Game by Himanish Ganjoo; Illustration by Akshaya Zachariah for FiftyTwo.in](https://images.prismic.io/fiftytwo/9f6d0d00-5826-4d87-ad69-01ef2b9f20f9_68-Masthead+Desktop-Numbers+Game-fiftytwo_detail.png?auto=compress,format&rect=0,0,2281,1265&w=2280&h=1264)

[**himanish** ganjoo](/contributor/himanish-ganjoo/)  28 May 22

[Season Two](/tag/season-two/)

### Subscribe to our newsletter

Weekly updates with new Fifty Two stories

This is a story about cricket, but it starts at the Massachusetts Institute of Technology. In 2016, Muhammad Jehangir Amjad, originally from Rawalpindi, Pakistan, was in the fourth year of his PhD in operations research. His doctoral work involved using a statistical method called “synthetic control” to predict the “normal” progression of a series of data.

One of its everyday applications is in retail sales. Let’s assume a mobile phone store in Delhi decides to implement a discount policy. Call it an “intervention.” One way to estimate how this would affect sales would be to investigate a counterfactual: what was the likely outcome if the store had gone on conducting business as usual?

In this instance, the data set might comprise historic sales numbers from 50 other mobile phone stores in Delhi, ones that have not offered a discount. These numbers, fed into the model, comprise the “learning,” which is then used to predict the “usual” sales trajectory of the store.

These were the scenarios Amjad was playing around with. He was also playing cricket. It’s how he was coping with working on an advanced degree at one of the world’s most competitive universities, and a tragic personal loss. He revitalised the MIT Cricket Club and played all over the American Northeast. “If it wasn’t for the club and the team,” he told me, “I might not even have stayed on to finish the PhD.” (He bowled pace like his hero Wasim Akram.)

Devavrat Shah, Amjad’s graduate advisor, was naturally supportive of his inclination towards cricket. As the two South Asians bonded over finding a reliable stream to watch live cricket in America, their conversations took an academic turn. They concluded that predicting the path of a cricket innings could be somewhat similar to predicting sales.

That’s how Amjad’s research went in a new direction. He began applying his techniques to answer a question that cricket watchers are habitually obsessed with: where does the innings go from here?

The extent of number-crunching in cricket was once limited to calculating averages and strike rates, and predicting innings scores based on the current run rate. These are pen-and-paper calculations that can be sped up by computers. But over the past 15 years or so, advanced mathematical models like Amjad’s haven’t just accelerated what was already on the cards; they’ve transformed the way cricket is watched and analysed. They form the algorithmic basis for “machines” which then automatically “learn” patterns which are too complex to express using equations.

Take the projections of the final innings score on TV broadcasts, which rely on simple calculations using the current rate of scoring in an innings. They don’t consider factors like changing weather conditions, the quality of opposition players or historic innings totals at a particular ground. Machine learning models can account for all these and more, having been trained with mountains of data from past matches. You don’t have to spell out the relationship between a swinging pitch and a low-scoring innings. The machine learns that for itself.

The coming of 20-over cricket took these high-level models beyond score prediction. With its narrower margins of error and big money riding on player auctions, the short-format game added an inquiry that went beyond “Who’s winning?” Now, there was also the question of “How to win?”

Players, coaches and corporate houses were interested in the answer. Machine learning may still be a hot phrase for many ordinary fans. But in the world of cricket, it’s already serious business—and it is challenging the game’s long-established traditions.

Conventional cricket wisdom, for example, dictates that batters play it safe in the middle overs of a T20 innings, preserving their wicket for a late surge in the slog overs. But advanced machine learning models can now tell you exactly how much this can reduce a team’s winning chances. The data approach has even begun to influence Test cricket, historically the format most resistant to change. Teams use machine learning models to identify chinks in their own batter’s armour. The same analyses, when applied to opposition batters, informs bowlers where to pitch the ball to have the best chance of taking a wicket.

### Amjad’s Interventions

N

othing escapes the machine. Imagine a one-day match has reached the 30-over point. The batting team is getting ready for a final push of run-scoring. How much will they end up making? The answer is not straightforward. Jehangir Amjad’s model will not only predict the final score, but also chart exactly how the innings will progress.

Like his model, Amjad’s own path in the world of research was not linear. “Cricket was never the plan,” he told me. But when he thought he was onto something with his predictive model, he got in touch with Vishal Misra, then a professor of computer science at Columbia University. Misra also co-founded Cricinfo, the world’s biggest cricket website, in the 1990s. He shared the cricketing insights that helped Amjad adapt his model for cricket statistics.

Any cricket-watcher will tell you that games turn on the number of wickets that the batting side has in hand. Wickets and overs jointly form the “resources” available to a batting side. (The Duckworth-Lewis-Stern (DLS) system, which the International Cricket Council uses to revise targets in rain-affected games, recognises this joint dependence of the score on both wickets left and overs remaining. But the DLS is still a pen-and-paper model.)

Amjad, along with Misra, Devavrat Shah and Dennis Shen developed a new avatar of the synthetic control model: multi-dimensional robust synthetic control. Synthetic control could only consider one variable—runs—to predict the future of an innings; the multidimensional version could account for both wickets *and* runs.

> # “Before celebrating, I checked and double- and triple-checked my code. Just to see if there was anything in it that had caused a bug.”

Misra’s cricket connections provided the key to the “learning” that would fuel their new model: data from 4700 ODI matches. Runs and wickets counted as sequential data, balls bowled would represent “time” through which the score progressed, the “intervention” would be something like inclement weather. The counterfactual question: if you stopped an innings right now, how would the trajectory of run-scoring proceed?

Let’s go back to the match we were watching at the 30-over mark. Amjad’s method first considers the vast tranche of data, choosing only the innings which are “similar” in terms of the wickets lost at the 30-over point. It then attempts to learn exactly how similar the current innings is to all the innings in the chosen set. This “similarity” is not abstract: a weight is assigned to each match in the set using something called least squares regression.

The model expresses the degree of similarity in percentage. It shows, for instance, that the current game is two percent like that match from 1996 and four percent like one that took place a couple of months ago. It then predicts the trajectory of the final 20 overs of the current game by combining the trajectories of the final 20 overs of all such similar matches.

It’s an approach that automatically factors in the effect of a variety of externalities. A match being played in swinging conditions, for instance, is likely to feature a low rate of scoring at the start of the innings. The algorithm will automatically find similar matches, assigning them more weight in the final say.

One of the first matches on which Amjad tested his model was the quarterfinal clash between India and Australia at the 2011 Cricket World Cup. The “intervention” he used was a hypothetical stoppage in the Australia innings at the 40-over point.

Amjad was astounded by how closely the model’s prediction matched reality. “But before celebrating, I checked and double- and triple-checked my code,” he told me. “Just to see if there was anything in it that had caused a bug.”

### Frames of Reference

“

Who’s winning?” Sambit Bal, editor-in-chief of ESPNcricinfo, and his team were often faced with this question during the website’s live commentary of limited-overs games. Bal wanted to improve the quality of conversation among both casual fan groups and the website’s own journalists and experts.

The ESPNcricinfo team’s focus was the T20 format: they knew that conventional metrics couldn’t capture the complexity of T20. In Test matches, a simple counting of scores is enough to tell you who is in the driver’s seat. Direct comparisons of runs and wickets can convey a fair idea about the best and worst performers. In T20, however, the value of runs and wickets changes throughout the game. This boils down to the fact that teams use their batting resources differently in different phases. A run scored off a ball in the first over is about par, but the same outcome in the final over doesn’t reflect well on the batting team.

“We’ve always felt that conventional stats like averages, economy rates and strike rates didn’t adequately capture the essence of 20-over cricket,” S. Rajesh, senior stats editor at ESPNcricinfo, told me. In November 2018, ESPNcricinfo collaborated with Gyan Data, a firm based out of the Indian Institute of Technology, Madras, to develop a system for internal use called SmartStats.”We wanted metrics that would take into account match situation, pressure, quality of opposition, pitch conditions, quality of wickets taken.”

The goal of SmartStats is to provide a frame of reference for each performance. “For instance, why was a three-wicket haul greater than a five-for?” Rajesh said. “The idea is always to tell more interesting stories using these metrics."

ESPNcricinfo’s Forecaster tool aids the calculations for SmartStats by weighing runs and wickets by match context. The public-facing avatar of Forecaster was launched during last year’s Indian Premier League, the world’s glitziest franchise T20 competition. At each point during the game, the Forecaster, which appeared on the live scorecard on the website, furnished a projected score and a win probability for the batting team.

> # “For instance, why was a three-wicket haul greater than a five-for? The idea is always to tell more interesting stories using these metrics.”

To understand what makes the Forecaster more accurate than most prediction attempts, let’s go back to the basics of machine learning. Machine learning is the technique of feeding large amounts of data to algorithms that learn relationships between “features” to predict an outcome. A feature could be any property, including numbers, that describe a system.

A known set of feature-outcome combinations is first used to “train” the learning model in these relationships. Once trained, the model can predict the outcome for a set of features. In a cricket innings, typically, overs and wickets left might be the features in a simple model and the outcome is a final score.

ESPNcricinfo’s Forecaster sets itself apart from other predictive models by additionally making potential performance a feature. In the first stage, it employs a machine learning algorithm which uses the past performances of batters to predict how many balls they are expected to play and how quickly they are likely to score from a given situation. Also, it tries to predict which bowlers will bowl at what point, and what their expected returns are.

These predicted performances become the additional features of the Forecaster, which now studies not only the current state of the innings, but also future possibilities. Remember the graphic of projected final scores during a cricket broadcast? This panel is an upgraded version of that.

The win probability here can be used to weigh the value of runs scored or wickets taken by individual players. A run scored when the chances of winning are 90 percent is of less value than one scored when there is a 10 percent chance of winning. The quantification becomes particularly relevant for T20 matches. It scales raw runs and wickets to reflect their real value on the outcome of a match.

This means that ESPNcricinfo’s Most Valuable Player is often different from the official “Player of the Match,” a determination which still relies on conventional metrics. In an IPL 2022 game between the Punjab Kings and the Kolkata Knight Riders on 31 March, Umesh Yadav was adjudged Player of the Match for his four-wicket haul. But ESPNcricinfo’s MVP was Andre Russell, for his unbeaten 70 off 31 balls. The suite accounted for the fact that two of Yadav’s wickets had been of lower-order, non-specialist batters.

One question I had for Rajesh was whether ESPNcricinfo’s models could account for luck. Cricket statistics only record outcomes, but luck often plays a big role in determining a player’s performance and the result of a match. What if a catch is dropped? Where would the match have gone had that umpire given that one out?

The folks who put together Forecaster had thought through this. Rajesh explained with a real-life example. In an IPL match against Rajasthan Royals in October 2020, Kings XI Punjab’s Chris Gayle was dropped when he was on a score of 10. Gayle went on to score 87 more runs—off 54 balls—after the drop. The Luck Index algorithm constructed a hypothetical timeline, in which the extra balls faced by Gayle were distributed among the batters to come. Relying on expected performances based on recent form, the algorithm computed that the other batters would have scored 26 runs fewer than Gayle.

### Neighbours in Monte Carlo

T

he first T20 international, played in 2005, was far from a serious event. Players from New Zealand and Australia sported retro outfits and hairstyles, unsure of what to expect from a brand new format. “I think it is difficult to play seriously,” then Australian captain Ricky Ponting had remarked.

Fast forward to the 2020s. Ponting now has a plum coaching assignment with the Delhi Capitals in the IPL. Players are routinely auctioned to play in leagues which are watched by audiences around the world. In this ecosystem, assessing individual performance and impact is not just a media tool, but a business necessity. Bespoke analysis is in demand from team owners, sponsors, broadcasters and national selectors.

Nathan Leamon was director of coaching at Eton College when he heard that Andy Flower, then coach of the England men’s cricket team, was looking for an analyst to work for him. On his first trip with the England side to South Africa in 2009, Leamon built a Monte Carlo simulator for cricket: a machine that leverages the power of large numbers to evaluate the chances of winning. Not long after, he also built out a model to measure “impact.”

In 2015, a company called CricViz was founded on the back of these rudimentary tools. Today, CricViz works with teams across the globe: its clients include the Big Bash, the Australian T20 league; the Hundred tournament organised by the English cricket board; and the Royal Challengers Bangalore franchise in the IPL.

WinViz, the advanced form of Leamon’s Monte Carlo simulator, is now deployed in several international cricket broadcasts. In 2016, CricViz inked deals for WinViz with Channel 9 in Australia and Sky Sports in England. They also cracked a deal with the International Cricket Council for World Cups.

WinViz works by factoring the past batting and bowling performances of the players of both teams and running thousands of simulations of a given match. It first calculates the likelihood of a player scoring some runs or taking some wickets. Then, a team innings is built by randomly picking runs and wickets for all players using these likelihoods. A win is decided by counting the total runs made by the teams. Repeat this random process many times, and you get the average performance of the teams, presented as their percentage chances of winning.

While WinViz appeals to viewers, the Impact Model is geared towards team strategists. Like ESPNcricinfo’s Forecaster, the Impact Model first predicts the final score of an innings from a given point. Its features are current score, wickets left, balls left, ground conditions and some other factors which CricViz didn’t reveal to me because it is a trade secret.

All these features are fed into a “nearest neighbours” algorithm. Put simply, this algorithm finds the closest match situation to a given situation. These “close” neighbours are then gathered and averaged out to predict a final score. The Impact of a player is calculated by the change an action would have on the projected score.

If the projected score is 160, for instance, and the player hits a six, the final projected score might change to 163. The player’s Impact on the ball, then, is +3 runs. Added up, a player’s Impact can be calculated for a game, a season, or their whole career.

Freddie Wilde, CricViz’s head of performance analysis, gave me an instance of how Impact played out in real world strategising. CricViz’s model suggests that a wicket in the first six overs of a T20 game reduced the final score by eight to nine runs. That kind of margin is often the difference between winning and losing in the IPL. It would explain why certain IPL teams have recently been willing to shell out good money for bowlers who can pick up wickets with the new ball.

### Eats, Bowls and Leaves

B

all-by-ball data, the computation of Impact, score projections: all these statistics are based on numbers that record results. But there’s a layer of cricket statistics that takes granularity to the next level. Hawk-Eye and VirtualEye are two companies that use a setup of high frame-rate cameras to record the entire trajectory of each ball bowled in international matches. These cameras basically capture the life story of a delivery: from the time it leaves the bowler’s hand to the moment it strikes the bat or pad.

Nathan Leamon was quick to harness this goldmine of information. In his time as the England analyst, he collected the lengths of each delivery: the precise spot on the pitch where the ball bounces. He then divided the pitch into grids and calculated the average runs and wickets taken by deliveries in each grid. That’s how he worked out the best areas for his bowlers to land the ball in.

These ideas were formalised and modernised by Imran Khan, head of data science at CricViz, as “xR” and “xW.” The Expected Runs and Wickets model analyses each ball’s characteristics to predict two things: the chances of it being a wicket-taking delivery and the average runs that can be scored off it.

Each delivery is described by numbers charting its actual motion: where it pitched, how fast it was, how fast it came off the pitch, where it was released from, how much it swung in the air, how much it turned after bouncing, and so on. The depth and scale of this information is mind-boggling: since 2005, there have been more than 30 data points for a single delivery.

> # “It will always be a balance between numbers and broader observations, but I would expect numbers to be integrated more in the years ahead.”

All this data is then fed to a decision tree, a flowchart that intelligently sifts through each ball’s features by asking a series of yes-or-no questions. Based on the answers, it segregates deliveries into branches and bunches similar ones together. These are referred to as “leaves.” As a simple example, a decision tree might bunch together all balls that are faster than 140 km/h and swing more than 5 degrees in the air. When a ball of this kind is later fed to the system, it brings up this leaf where all such historic deliveries reside. That gives the analyst the average runs and wickets for a ball bowled in that leaf.

Because machine learning predictions are never perfect, the xR and xW models are not simple decision trees. To get the best result possible, ball tracking data is fed to a series of decision trees. At each stage, the algorithm calculates accuracy for each kind of delivery. The data is then fed to another decision tree, with a special focus on the kinds of deliveries offering the least accurate predictions. This technique is called “gradient boosting.” To perfect the prediction pipeline, Khan used a chain of thousand such trees, training it on more than 700,000 deliveries.

There is a further nuance to xW. Not only does it tell you the percentage chance of a wicket on that delivery, it also suggests which features of the ball are most important in determining its potency. The wicket-taking propensity of a delivery is based on a hierarchy: first, the location of the ball when it reaches the stumps, then the deviation from the pitch, and finally, the place on the pitch where the ball bounced.

The xW metric is already helping elite teams make selection decisions. Recently, the selectors of England’s men’s Test squad dropped spinner Dominic Bess from the team that toured the West Indies. Bess had been picking wickets on England’s tours of Sri Lanka and India. But, behind the scenes, CricViz analysts were supplying the team management with Bess’s xW numbers. These indicated that his wickets were lucky quirks: Bess’ record was likely unsustainable in the long run.

Tim Wigmore, one of the authors of *Cricket 2.0: Inside the T20 Revolution*, often uses CricViz’s xR and xW models in his pieces for *The Daily Telegraph*. “Data allows writers to prove—and sometimes to disprove—received wisdom about the game, and write more enlightening pieces,” Wigmore told me. “It will always be a balance between numbers and broader observations, but I would expect numbers to be integrated more in the years ahead.”

I

n an IPL 2022 match between Rajasthan Royals and Lucknow Super Giants on 10 April, R. Ashwin “retired out” so a more accomplished batsman could come to the crease. It was the first time that a batsman had voluntarily retired out in an IPL match. Watching from ESPNcricinfo’s offices in Bengaluru, writer Karthik Krishnaswamy saw the Forecaster total shoot up by seven runs.

Krishnaswamy was hopeful of data tools playing a big role in the future of cricket-watching and analysis. “It really gives you the ability to very easily and clearly communicate these things—the effect of one over, or sometimes one ball, on the direction of a match,” he said. “I think if that helps grow the understanding of T20 at a wider level, it will make it easier for coaches and players to accept the ideas of data nerds.”

“It’s just being closer to the truth, isn’t it?” writer and analyst Jarrod Kimber told me. Kimber recently wrote a detailed explanation of the logic of the retired out in T20 cricket. “Before, so much of cricket could be between players and administrators, based on their whims. Bowlers used to be finished because they lost a yard, batters would be dropped because they’d had a bunch of low-scoring wickets. Now, we can evolve beyond all that.”