# Virgin America Is The Michael Jordan Of Airlines | FiveThirtyEight

**Source**: inputs/New Docs/html/fivethirtyeight.com_datalab_virgin-america-is-the-michael-jordan-of-airlines.html
**Type**: article
**Created**: 2025-08-25T02:53:52.052840

---

![](https://fivethirtyeight.com/wp-content/uploads/2015/03/gyi0000573426.jpg?w=575)



Two Virgin America planes taxi on the runway after arriving at San Francisco International Airport after their first flights from New York and Los Angeles in 2007.

Justin Sullivan / Getty Images

The Chicago Bulls won 88 percent of their games during the 1995-96 regular season, going 72-10 and claiming the best record in NBA history. Impressive, right? It’s hard to win that often in any field, let alone one with so much competition.

But there’s an airline that pretty much does exactly that. In 2014, Virgin America was faster than its competition on 87 percent of the routes they had in common.

This week, we rolled out our [fastest flights interactive](https://fivethirtyeight.com/interactives/flights/), which [seeks to place airlines on a level playing field](https://fivethirtyeight.com/features/fastest-airlines-fastest-airports/) by looking at what routes each one flew. It’s easier to avoid delays while flying out of Honolulu instead of Chicago, for instance. A fair comparison between the airlines ought to account for this, as ours does.

In the interactive, the [method](https://fivethirtyeight.com/features/how-we-found-the-fastest-flights/) of comparing airlines depends on [regression analysis](http://www.law.uchicago.edu/files/files/20.Sykes_.Regression.pdf). While there’s nothing particularly complicated about regression, there are [various ways it can go wrong](http://fredrikdeboer.com/category/popular-digital-writing/). It’s almost always worth it to sanity-check a regression result by applying another (ideally simpler) method to the same data.

So here’s a simple and fun one: We’ll compare airlines head-to-head, as though they’re basketball teams. For instance, American Airlines and United Airlines both fly from Chicago O’Hare to Oklahoma City. American flew the route about nine minutes faster, on average, in 2014, accounting for delays, cancellations and diversions.1 So it gets a “win” on that route, while United takes a “loss.”

We can run this comparison for every competitive route in the country.2 American and United often do battle, for instance — both have hubs at O’Hare and in Los Angeles. Among the 230 routes3 they had in common, American compiled a 148-82 win-loss record.

Here are the standings for every airline matchup:

[![silver-feature-flights-winloss](https://fivethirtyeight.com/wp-content/uploads/2015/03/silver-feature-flights-winloss2.png)](https://fivethirtyeight.com/wp-content/uploads/2015/03/silver-feature-flights-winloss2.png)

Some of the comparisons are incredibly lopsided. Alaska Airlines went 35-1 against Southwest Airlines. Virgin went 50-2 against United, 22-4 against American and 15-1 against JetBlue Airways, helping it to a 120-18 overall record. That was the best in the business: a Jordanesque 87 percent winning percentage.

That some airlines are so dominant against others suggests that there’s a lot of “signal” in this data set. After hundreds or thousands of flights on the same routes, luck — like happening to run into a thunderstorm when another airline doesn’t — doesn’t play a major role in on-time performance.

The head-to-head method still has some flaws. For instance, Frontier Airlines, which [rates as about average](https://fivethirtyeight.com/interactives/flights/) by our regression method, has a stellar 144-47 win-loss record. But that’s partly because it has a lot of routes in common with United and Southwest, two of our more poorly rated airlines.4

But overall the head-to-head comparison backs up our regression results. Hawaiian Airlines ranked fifth out of 10 airlines in our regression, for example. Those results are partly based on the many routes it flies within Hawaii (like from Honolulu to Hilo), on which it has little competition. But Hawaiian faces plenty of competition on routes from Hawaii to the U.S. mainland, and it went 21-15 against other airlines. That’s a perfectly decent record, but not exactly the ’96 Bulls.