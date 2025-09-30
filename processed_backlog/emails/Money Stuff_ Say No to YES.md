# Money Stuff: Say No to YES

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Thu, 30 Jun 2022 13:23:52 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Say No to YES_Thu,_30_Jun_2022_13-23-52_-0400_(EDT)_181b5a6bcbdd5fee.eml
**Processed:** 2025-08-24T19:13:11.251693














        Programming note: Money Stuff will be off tomorrow and Monday, back on Tuesday.YES!Here is a common pattern at a big investment bank. Some n











































          Programming note: Money Stuff will be off tomorrow and Monday, back on Tuesday.



      YES!



Here is a common pattern at a big investment bank. Some nerds in the derivatives lab cook up a derivative. To make it out of the lab and into production, the derivative will generally have a few attractive characteristics:
	It comes with a good intuitive story. “You are worried about X, and this derivative will protect you from X.” “You expect the market to do Y, and if the market does Y this derivative will make a lot of money.” “It would be extremely surprising if the market did Z, and this derivative will make money for you unless the market does Z.”	It has a pretty backtest. “Look at this chart: This derivative would never have lost money during your lifetime!” (Or only rarely, or not very much, or only in conditions you don’t expect to see again, etc.)	It has a good name. “Would you like to buy a YES? That is the name of our product, YES, it is an acronym, would you like to buy it?” The question suggests the answer, doesn’t it?	It builds in a lot of edge, so the bank can make a lot of money selling it.

And then the nerds go out and tell the bank’s salespeople “hey, we’ve got this product, it is called a YES, you should sell it because it makes us a lot of money” (Point 4). And they give the sales force a memo that contains a summary of the product’s intuitive story (Point 1), and the pretty backtest (Point 2), and the name of course (Point 3), and also probably a longer explanation of how the product works and what the risks are. And, ideally, the salespeople read the explanation and look at the backtest and figure out the moving pieces and talk to the derivatives nerds and get a good understanding of the product and sensibly advise clients on how to use the product to achieve their particular goals. 
But, in practice, some of the salespeople glance at the backtest and say “aha! This is a product that can never lose money,” and they like the name, and they go out and tell their clients “do you want a YES, it can never lose money,” and the clients believe them, and, uh:

The Securities and Exchange Commission [yesterday] announced that UBS Financial Services Inc. has agreed to pay approximately $25 million to settle fraud charges relating to a complex investment strategy referred to as YES, or Yield Enhancement Strategy.
According to the SEC’s order, UBS marketed and sold YES to approximately 600 investors through its platform of domestic financial advisors from February 2016 through February 2017. The order finds that, during this time, UBS did not provide its financial advisors with adequate training and oversight in the strategy, and although UBS recognized and documented the possibility of significant risk in YES investments, it failed to share this data with advisors or clients. As a result, the order finds, some of UBS’s advisors did not understand the risks and were unable to form a reasonable belief that the advice they provided was in the best interest of their clients. When investors suffered losses, many of them, along with their financial advisors, expressed surprise and closed their YES accounts.

The strategy is not that complex, but it is complex enough. It is an iron-condor-selling strategy: You sell some out-of-the-money puts and calls on a stock index, and then buy back further-out-of-the-money puts and calls. The result if that the market doesn’t move much, you collect some premium; if the market moves, you have some losses, though they are capped at around 10% to 20% of your position.
  [1]

This was cooked up by some nerds in the lab at Credit Suisse Group AG, and worked well enough at Credit Suisse that UBS hired the whole lab in 2015, “paying them upfront awards of approximately $50 million.” Then they pitched it to UBS’s financial advisers, who went out and sold it to clients:
UBS opened YES to new clients in February 2016. The YES Team conducted roadshows at UBS’s offices in California, Texas, and New York, among others, and pitched the strategy over the phone to financial advisors located across the country. The YES Team marketed the strategy as a way to enhance returns on an existing portfolio of securities. The YES Team generally explained to financial advisors and clients that historically the strategy had generated gains of approximately 3%-to-5% per year with worst-case historical losses of approximately 1% per year. The YES Team acknowledged that the strategy had experienced losses up to 11% in a single month but explained that this created a potential profit opportunity because they could try to sell options at premium prices, sometimes analogizing the program to writing “hurricane insurance.” As a result of these efforts, the number of client accounts increased by approximately 600 and the amount invested in YES increased by approximately $2 billion during the Relevant Period.
But, says the SEC, the advisers didn’t really know what they were selling:

Because there was no registration statement or other formal offering document associated with YES, financial advisors and clients were dependent on written materials prepared by UBS and documents associated with the account opening process. The first was a blast email prepared by the YES Team highlighting, among other things, that the strategy’s “worst year was down 1.02%.” The second was a 17-page slide deck. Beyond standard language along the lines of “[s]ignificant market moves either up or down may result in losses” and “[s]elling options involves a high degree of risk,” none of the written materials provided further explanation of the downside risk of YES. ...
Certain financial advisors and clients did not understand the significant downside risks of YES during the Relevant Period. Certain financial advisors understood from communications with the YES Team that the strategy could experience significant losses but believed that this created a profit opportunity under a hurricane insurance analogy. Certain clients who invested in YES during the Relevant Period would not have invested in YES had they known the significant downside risk, and believed their financial advisors would not have recommended YES had they appreciated those risks.

We have  talked about this product before; allegedly one broker told his client that “if the world came to an end tomorrow, you’d be the only one with any money left.” From selling S&P iron condors! Come on. Nobody in the derivatives lab would say anything like that. But something got lost in translation.
It’s hard. On the one hand, if you are a financial adviser, you want to give your clients good financial advice, which means understanding the nuances of the products you are selling them. On the other hand, if you are a financial adviser at a big brokerage, you want to give them a lot of financial advice, both because you will endear yourself to (some) clients by selling them lots of whizz-bang stuff that they can’t get anywhere else, and because you will endear yourself to your employer by selling stuff that makes a lot of money for your employer. And doing that tends to be easier if you don’t understand the nuances of the product. If your understanding of a product is limited to “this thing is called YES and it never goes down,” then you will be excited to sell it.























































      10b5-1s



One thing that I believe is that chief executive officers of public companies know more about their companies than outsiders do. I think this is obviously true: The CEO spends all day working at the company, everyone at the company reports to her, she sets the company’s strategy, she can get all the information she wants about the company, etc.; she is just clearly going to be more informed about the company than some random person, or even some hedge-fund analyst who covers the company closely.
But this is also a somewhat controversial thing to say in polite company. There is in US securities law a sort of polite fiction that the CEO of a public company only sometimes has “material nonpublic information” about the company. Right before the company releases earnings, when the CEO has seen the draft earnings release but it isn’t public yet, she has MNPI, but midway through the quarter she does not. If she is actively negotiating a merger with a competitor, she has MNPI, but if she just has occasional hypothetical chats with the competitor’s CEO then she does not. If the company just suffered a devastating hack that it hasn’t yet disclosed, she has MNPI, but if she is just reviewing weekly cybersecurity threat assessments she does not. Etc. (Not legal advice!) 
This polite fiction is important because it is what allows corporate executives to trade stock. If you said “well, yes, obviously CEOs always have inside information about their companies, after all they run those companies,” then any time a CEO traded her company’s stock she would be doing a crime. (It is illegal, in the US, for corporate insiders to trade while in possession of material nonpublic information.) So you say “oh no CEOs never have any material information about their company except at the end of the quarter, or when they’re doing a merger, or when they get hacked.” And then when things are normal — when the CEO just knows all sorts of inside information about her company, but none of it is big enough to rise to the level of “material nonpublic information” — then the CEO can trade. 
The way that this typically works is somewhat convoluted. Instead of just deciding to trade stock and then doing it, CEOs frequently set up Rule 10b5-1 trading plans. In a 10b5-1 plan, the CEO arranges with her broker to sell some prearranged number of shares of stock over some prearranged period. (Or to buy stock, though executives tend to do more selling than buying, since they are often paid largely in stock and need to turn it into money.) It could be “1,000 shares a day starting next month,” or some more complicated formula based on the price of the shares. But the idea is that you set up the Rule 10b5-1 plan in “normal” times — when the polite fiction says that you don’t have any MNPI — and then the plan operates automatically. So if you later get MNPI (because the quarter ends, or you start negotiating a merger), your broker keeps automatically selling stock for you, and you can say “what, I’m not insider trading, this is just the plan operating automatically.”
But the polite fiction isn’t true, so you can always get articles like this:

A Wall Street Journal analysis of 75,000 prearranged stock sales by corporate insiders, using a comprehensive compilation of the data, shows that about a fifth of them occurred within 60 trading days of a plan’s adoption. The timing in aggregate made the trades more profitable: On average, those trades preceded a downturn in share price more often than when insiders waited longer to trade, the analysis found.
Collectively, insiders who sold within 60 days reaped $500 million more in profits than they would have if they sold three months later, according to the analysis, which examined trades from 2016 through 2021 and adjusted returns to remove the effect of sector-wide moves in the market.
For those who waited 120 days or more after adopting a plan, roughly half sold before a downturn and half before a stock upturn, suggesting that the sellers reaped no unusual gains after more time had passed.

One way to read this is that corporate executives know more about what will happen at their companies in the next 60 days than the market does, though their informational advantage erodes after 120 days. Really it is a bit more complicated than that. For one thing, executives probably sell stock more to buy houses or pay tuition than to make tactical bets on market prices, so you might not expect their sales to be informative even if they do know more than everyone else. Some research has found that insider buying is informative (CEOs buy their own stock because they think, with reason, that it will go up), but insider selling is not informative (CEOs sell their own stock for liquidity reasons, not because they think it will go down). Still, if you are a corporate executive and you decide you need to sell stock this month, that does seem to increase the likelihood that next month will be bad.
Anyway there is an obvious solution to this problem, if it’s a problem. You can abandon the polite fiction that CEOs don’t have material nonpublic information, and replace it with a time delay. A CEO who decides to sell stock today, or next week, knows something that the market doesn’t. A CEO who decides today “I am going to sell stock in four months” does not. The stock price might be higher or lower in four months; she doesn’t know. After she sells, the stock might go up or down; she doesn’t know that either. In four months she’ll know stuff that the market doesn’t, but if she makes the decision today it is probably an uninformed decision. That is both intuitive, and what the Journal’s analysis shows.
Also this is exactly what the US Securities and Exchange Commission wants to do. Late last year, the SEC proposed amendments to Rule 10b5-1 to “require a Rule 10b5-1 trading arrangement entered into by officers or directors to include a 120-day mandatory cooling-off period before any trading can commence under the trading arrangement after its adoption.” (We  talked about the proposal in December.) You sign up a plan today, but it can’t start trading for four months. You know stuff now that the market doesn’t know, but four months from now the market will know it, so you aren’t insider trading. 












      Bailouts



One thing that sometimes happens in financial markets is that a firm runs into a liquidity crisis. It has borrowed a lot of money short-term to fund long-term investments, but its short-term lenders have gotten spooked and have pulled their financing, and it can’t sell its long-term investments fast enough or at a high enough price to pay them back. When that happens, a classic solution is for some bigger and better-capitalized firm with an appropriately long-term horizon to buy the troubled firm or its assets. “We know that these assets are good,” the bigger firm might think, “so we will buy them at a discount, solve the liquidity crisis and get rich.” That is sort of the point of being a big and well-capitalized firm: You are a bit boring in the boom times, but then in the bust you can go around scooping up lots of good assets cheap.
But this is all pretty schematic, and in real life it is not always the case that a liquidity crisis is just, or primarily, a liquidity crisis. If some firm runs into a liquidity crisis and can’t pay back its short-term debt and calls up a big well-capitalized firm for help, the big well-capitalized firm has to go look at its assets and see what’s going on. Sometimes the big firm will crack open the books and conclude “yes, these assets are great, your lenders are spooked for no reason, it’s an amazing buying opportunity for us” and buy them. Other times the big firm will crack open the books and find a crayon drawing of a billion-dollar bill and say “ah, yes, that’s your problem right there” and walk away. Sometimes the liquidity crisis is well deserved.
Anyway!

Crypto exchange operator FTX looked at making a deal with troubled crypto lender Celsius but ultimately walked away, two people with knowledge of the matter told The Block.
FTX began talks with Celsius about providing financial support or making an acquisition but decided against proceeding after looking at Celsius's finances, the sources said. Celsius had a $2 billion hole in its balance sheet and FTX found the company difficult to deal with, one of the sources said.
Celsius did not respond to The Block's request for comment.
Celsius has been fighting for survival since freezing all withdrawals on June 12, citing "extreme market conditions." Clients' funds have remained stuck ever since.

See if I was looking for a bailout I would want to be easy to deal with but that is just me.



      Tether



Ahahaha come on:

The public face of crypto’s biggest stablecoin, Tether chief technology officer Paolo Ardoino, laid down the gauntlet this week to hedge funds who are shorting the $66bn market cap token.
Over 12 tweets on Monday, he decried “FUD, troll armies, clowns etc” and said that Tether was “the only stablecoin that is proven with fire under extreme pressure”, referring to the $17bn in redemptions it has processed in May and June.
“Eventually these hedge funds, that borrowed and shorted billions of USDt will need to buy them back. What will happen then?,” he warned.

I mean … they’ll … buy them back … at $1? Like that’s the point? Of Tether? What are we doing here? Like if you see a stock go from $10 to $100 and think “hahaha this is a great short” and short it at $100, one thing that might happen is that there might be a short squeeze and the stock might go to $400 and stay there. If that happens, (1) you will have to buy it back at $400 and lose tons of money, and (2) the people who own the stock will say things like “yes!” and “haha gotcha” and “this is exactly what we wanted.” But if you see Tether trading at $0.9988 and you think “hahaha this is a great short” and short it at $0.9988, it seems implausible that there will be a short squeeze and Tether will go to, like, $2. The point of a stablecoin is to be worth $1! If Tether goes to $2, the people who own it will say things like “what?” and “oh dear” and “this is not supposed to happen.” It’s not a useful stablecoin if it trades very far from $1. If you are short Tether and it stays near $1, you will lose money, because you are paying money to borrow Tether and short it. But you’re losing a little money every day; the problem is not, like, you sold it at $0.9988 and now you have to buy it back at $1.00. That costs you $0.0012!



      MicroStrategy



If you are MicroStrategy Inc., and you were a small software company, and then you pivoted to become a giant leveraged sack of Bitcoins with a small software company hanging off of it, and then the price of Bitcoin went way down, what are you going to do about it? Like if you run a hedge fund, or Tesla Inc., and you buy some Bitcoins and the trade moves against you, you can say “oops, our bad, sorry we burned some of your money, moving on.” But if you run a company that was a regular company but that has now turned Bitcoin into its whole identity, that is a trickier move. Your shareholders are all Bitcoiners, your debts are all secured by Bitcoin, you are a Bitcoin company now, and there is no face-saving way out of the trade. This also applies to El Salvador. Anyway:
On June 29, 2022, MicroStrategy Incorporated (“MicroStrategy”) announced that, during the period between May 3, 2022 and June 28, 2022, MicroStrategy acquired approximately 480 bitcoins for approximately $10.0 million in cash, at an average price of approximately $20,817 per bitcoin, inclusive of fees and expenses. As of June 28, 2022, MicroStrategy, together with its subsidiaries, held an aggregate of approximately 129,699 bitcoins, which were acquired at an aggregate purchase price of approximately $3.98 billion and an average purchase price of approximately $30,664 per bitcoin, inclusive of fees and expenses.
The good news is that, if it keeps going down and they keep buying, that average price will keep getting lower.



      Ethics



We  talked the other day about how, to become a certified public accountant, you have to take an ethics exam. You take this take-home open-book online multiple-choice ethics exam after passing four other grueling exams about accounting, and it seems to be taken less seriously than some of the other elements of becoming an accountant. To the extent that a bunch of accountants at Ernst & Young cheated on it, and the US Securities and Exchange Commission caught them and fined E&Y $100 million for not turning in the cheaters.
I suggested that a regulatorily imposed multiple-choice ethics exam is maybe not the best way to instill a sense of ethics in a profession.
A reader pointed me to this paper, by Margaret Forster, Tim Loughran and Bill McDonald at Notre Dame, about “Commonality in Codes of Ethics.” From the abstract:
We create a database of company codes of ethics from firms listed on the Standard & Poor’s 500 Index and, separately, a sample of small firms. The SEC believes that “ethics codes do, and should, vary from company to company.” Using textual analysis techniques, we measure the extent of commonality across the documents. We find substantial levels of common sentences used by the firms, including a few cases where the codes of ethics are essentially identical. We consider these results in the context of legal statements versus value statements. While legal writing often mandates duplication, we argue that value-based statements should be held to a higher standard of originality. Our evidence is consistent with isomorphic pressures on smaller firms to conform.
The examples are fun; popular sentences include “Theft, carelessness, and waste have a direct impact on the company’s profitability,” “We seek competitive advantages through superior performance, never through unethical or illegal business practices,” “Remember that it is your supervisor’s responsibility to help solve problems,” “Stealing proprietary information, possessing trade secret information that was obtained without the owner’s consent, or inducing such disclosures by past or present employees of other companies is prohibited,” and “It may help to get others involved and discuss the problem.”
It turns out that when the US Securities and Exchange Commission mandated a code of ethics for public companies, they … copied each others’ answers. Just like the accountants did! I feel like there is a deep lesson here about ethics mandates. 



      Things happen



Grayscale Suing SEC After Its  Bitcoin ETF Is Rejected. Did  Razzlekhan and Dutch Pull Off History’s Biggest Crypto Heist? Spirit Air Board Pushes Shareholders Meeting on Frontier Bid for Second Time. Treasury market reforms draw flak from funds and high-speed traders. Private Lenders Are Offering  Cheaper Debt Than Wall Street Banks. Megadeals buoy global M&A despite pullback from record 2021.  Romance Scams Explode, Leaving Broken Hearts and Millions Lost. Hedge Fund Viking Global Seeks to Raise $1 Billion to Back
Cash-Hungry Startups. Putin: Western leaders would look ‘disgusting’ topless. Beer Made From Recycled Toilet Water  Wins Admirers in Singapore. Anchovies are reportedly raining from the sky across San Francisco. 
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!

  [1] The SEC explains: “YES is an options overlay strategy designed to generate income from an existing portfolio of securities and is managed on a discretionary basis. YES generally sells short term out-of-the-money European style put and call options on the S&P 500 and hedges those positions by purchasing below-market puts and above-market calls with the same duration – an options trading strategy known as an ‘Iron Condor.’ Clients participate in YES by pledging as collateral for those options trades a portfolio of existing securities held at UBS with a view towards enhancing returns on their existing portfolio. YES is a short volatility strategy and thus has the potential to generate modest returns during periods of low market volatility; however, unbeknownst to certain clients who opened YES accounts during the Relevant Period and certain UBS financial advisors who recommended YES during the Relevant Period, the strategy could -- and eventually did – suffer losses during periods of high market volatility.”











            Follow Us













              Get the newsletter



























Like getting this newsletter?
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022


















<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cgt37y.5y6q/b356b0d4.gif" alt="" border="0" /></a>
