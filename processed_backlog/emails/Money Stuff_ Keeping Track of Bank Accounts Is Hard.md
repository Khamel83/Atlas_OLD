# Money Stuff: Keeping Track of Bank Accounts Is Hard

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Tue, 25 Jul 2023 13:39:53 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Keeping Track of Bank Accounts Is Hard_Tue,_25_Jul_2023_13-39-53_-0400_(EDT)_1898e23369e7794f.eml
**Processed:** 2025-08-24T19:13:12.194144














        There are two ways to think of the primary function of banks. One is a financial model: Banks borrow short-term to lend long-term, they prov





































      Banks are tech companies



There are two ways to think of the primary function of banks. One is a financial model: Banks borrow short-term to lend long-term, they provide credit intermediation, they pool risk-averse savings to finance risky investments, etc.; stuff we have  talked  about a  lot  around  here.
The other is an essentially technological, list-keeping model: Bank deposits are money, and the job of banks is to keep track of who has money, and move it around when one person wants to send money to another person.
Both of these functions are, of course, true and important. You could separate them conceptually: You could have one sort of company be in charge of keeping track of everyone’s money and doing payments, and a different sort of company be in charge of borrowing short-term to lend long-term, and of course there are examples of both. But in much of the world, for practical and also historical reasons, those functions are combined in banks. And my sense is that most bankers are mostly finance people, that they think mostly about borrowing short and lending long and the financial risks (credit, liquidity, interest rates) of that model. My sense is that most bankers do not come from the list-making world, that what gets them excited is not improving their list-keeping and number-moving technology.
And so the list-keeping technology of banks is not always on the cutting edge. Sometimes financial technology upstarts do have good ideas for improving payments mechanisms, because traditional bankers simply do not care enough about improving payments, because the technological aspects of their jobs are not what excite traditional bankers. And so you have fintech companies building better payments interfaces than the banks do. You have the US banking system’s slow move to real-time electronic payments, with the Federal Reserve’s FedNow instant payments system  rolling out last week to “35 early-adopting banks and credit unions.” And of course you have crypto, which is  in large part about building a system for keeping track of money that aims to be an improvement over banks. And you have proposals for  central bank digital currencies, which would take some ideas from crypto and use them to build a system for keeping track of the money without involving banks.
You could imagine the world going a different way. If you started from scratch in 2023, you might say “we should have a large well-run tech company that is in charge of keeping the databases of the money and moving numbers around in those databases, because that is what tech companies do, and then finance people could build all the borrowing-short-to-lend-long infrastructure on top of that.” Maybe the list-keeping tech company would also do the financial stuff, because its control of the lists and the payments would be an advantage in funding and lending, or maybe it would build open platforms and other, more specialized companies would do the funding and the lending. (Again, these questions are relevant to many crypto platforms.) And of course you would have to build a regulatory system to make all of this work fairly and robustly.
But in the actual world  here’s a funny Financial Times story about how Deutsche Bank AG bought Postbank, another German bank, in 2010 and then spent 13 years trying to figure out how to combine Postbank’s list of account holders with Deutsche Bank’s list of account holders:

Inside one of the lender’s buildings in Frankfurt, a 200-strong team of retail bankers and IT specialists were racing to complete the final 2,833 tasks needed to transfer the remaining data of German lender Postbank’s 12mn customers over to Deutsche’s computer systems.
As the meticulous plan, rehearsed several times in previous months, unfolded, an unsuspecting member of the team opened a dishwasher in mid-cycle, with the escaping steam setting off a smoke detector and forcing the evacuation of the building. Precious minutes were squandered before firefighters gave the all-clear.

The final 2,833 tasks! And:

The groundwork was laid just as the coronavirus pandemic struck Europe in the spring of 2020, when for the next 18 months more than 1,000 staff analysed the Postbank data, worked out how to move it and unearthed complications.
One stemmed from the fact that some Postbank clients were erroneously still listed as residents of defunct states such as Czechoslovakia or Yugoslavia, designations that Deutsche’s systems rejected. “In such a project, you not only have to deal with decades of data and history but also with junk data,” said Karsten Roesch, who ran the Unity project alongside Peschke.

I assume that there are people who work at, like, Stripe, who are rolling their eyes so hard at this that they have injured themselves. Not in a “combining two lists of bank accounts is trivial” way, but in a “well yes obviously you have to deal with defunct address data but why don’t you have people who are thinking about that” way. “We are a tech company,” some bankers are fond of saying, but not really.





























      Uninsured deposits



Ahahaha  in possibly related news:

The largest US banks have been rushing to restate their financials in order to minimise how much they may have to pay to cover the cost of the failures this year of Silicon Valley Bank and Signature Bank. ...
The FDIC regularly assesses banks with a fee for providing deposit insurance, but in May, it proposed a special assessment for this year’s major failures.
The fees were computed based on banks’ uninsured deposits, as $15.8bn of the $18.5bn cost of the SVB and Signature bailouts were due to the coverage of accounts larger than the FDIC’s normal $250,000 insured limit. Most of those accounts were with large banks.
The corporation wanted to apply the assessment based on the value of the banks’ uninsured deposits at the end of 2022. ...
Analysts at S&P Global noted in a report that an unusually high number of banks in the past six months had restated their uninsured deposits as of the end of last year. S&P said 55 banks this year had restated their fourth-quarter figure, compared with just 14 in the same quarter the prior year. S&P said the majority of the restatements resulted in lower uninsured deposits.
Bank of America had the largest restatement, cutting its uninsured deposits by $125bn, or nearly 14 per cent, according to the report. Based on its lower uninsured deposits, S&P said BofA’s special assessment would drop to $1.95bn, down from $2.26bn. ...
BofA declined to comment. It had told S&P it had improperly characterised some of the bank’s own cash as customer deposits, resulting in the restatement. A source close to BofA told the Financial Times that the restatement was made in early May, days before the FDIC released the framework for its proposed assessment.

The FDIC is   not pleased; it published a Financial Institution Letter objecting to some of the adjustments the banks have made:
The FDIC observed that some insured depository institutions (IDIs) are not reporting estimated uninsured deposits in accordance with the instructions to the Consolidated Reports of Condition and Income (Call Report). For example, some institutions incorrectly reduced the amount reported to the extent that the uninsured deposits are collateralized by pledged assets; this is incorrect because in and of itself, the existence of collateral has no bearing on the portion of a deposit that is covered by federal deposit insurance. Additionally, some institutions incorrectly reduced the amount reported on Schedule RC-O by excluding intercompany deposit balances of subsidiaries.
You might naively think that if you asked one of the largest banks in the US “how much money do you have from depositors with more than $250,000 at your bank,” it could spend, you know, a few hours looking at the data and get back to you with an answer that was accurate to within 10%. But you’d be wrong!



      The APE arb



AMC Entertainment Holdings has two types of stock: common shares (ticker AMC) and AMC Preferred Equity Units (ticker APE). These are supposed to be economically equivalent, but they trade at very different prices. The common stock closed at $5.85 yesterday; the APEs closed at $1.80. AMC has announced plans to convert the APEs into common stock; the formula is somewhat complicated but roughly speaking each APE would turn into 0.88 common shares.
  [1]
 If the common stock is really worth $5.85, then an APE should be worth about $5.16. If the APEs are really worth $1.80, then each common share should be worth about $2.04. Or pick some numbers in the middle. The point is, the $5.85/$1.80 disparity seems odd.
Of course the disparity exists because, as we have discussed a lot,   including yesterday, AMC common shareholders sued to stop AMC from converting the APEs into common, and a court has held up the proposed conversion. The shareholder plaintiffs and AMC have reached a settlement, but the court has not approved the settlement yet; on Friday, the judge, Delaware Vice Chancellor Morgan Zurn, rejected the settlement because it gave AMC too broad a release from legal liability. (This is what we discussed yesterday.) AMC and the plaintiffs pretty much immediately sent back a revised settlement, crossing out the broad release and thus answering the judge’s objections.
Now what? Well, the good news (for AMC, and for the APEs) is that the judge   will consider the revised settlement quickly:

AMC Entertainment Holdings Inc. and shareholders leading litigation against the theater chain can immediately renew their efforts to get court approval for a settlement that would let the company convert its APE units into common stock, a judge said Monday.
Vice Chancellor Morgan T. Zurn, who stunned analysts by rejecting the original agreement July 21, said the deal approval process can resume without a delay that would let AMC’s passionate retail investors file new objections. “The narrowed release does not adversely affect the putative class,” she said in a letter to both sides of the court fight, suggesting the new deal could be approved in August. ...
Zurn, writing Monday for Delaware’s Chancery Court, said she was sensitive to AMC’s recapitalization needs, which the company has called urgent as recently as Sunday, when CEO Adam Aron published an open letter stressing the risk of “financial collapse.” AMC previously requested a ruling “before the capital markets go quiet in August,” the judge noted.

The bad news is that it is still not quite certain that she will approve the revised settlement, or when. It answers the objections that she raised on Friday, but her opinion on Friday did not say “this settlement is fine except for this one thing”; it just raised the one thing. I think the settlement is fine, and the special master appointed by Vice Chancellor Zurn to review the settlement found it was fine, but it’s up to her, and she hasn’t ruled yet one way or the other. (The  Chancery Daily newsletter, for one, is skeptical that Vice Chancellor Zurn has an opinion ready approving the settlement: “If she had the whole thing done, why would she have held it back?”)
AMC’s common shares and its APEs have always been meant to be one-for-one (or, now, one-for-0.88) substitutes for each other, always meant to merge into each other eventually. And so there is an arbitrage: Hedge funds can buy APEs (for $1.80 or whatever), sell 0.88 common shares short (for $5.85 per share, or $5.16 per 0.88 shares), and pocket the roughly $3.36 profit when the APEs convert.
  [2]

And they have done that — for a long time — and it has been   an absolute nightmare for them:

Investors betting on the conversion were shorting shares of the common stock and snapping up AMC’s preferred units on the expectation that the price gap between the pair would vanish as the deal goes through, allowing them to capture the spread.
While it was supposed to be a straightforward bet — with traders expecting to reap a windfall in a short period of time — it hasn’t played out that way.
The expensive cost to short the meme stock’s common shares, paired with the volatility given its retail-trader following, also kept the spread wider than $2 since the APEs were distributed last year.

The problem is that, to short AMC common shares, you have to borrow them, and that’s expensive, with short sellers paying something north of 800% annualized to borrow the common, according to S3 Research data. Call that rate 20% per month, or about $1 per month per common share, which eats pretty rapidly into your $3.36 profit. The conversion was   supposed to happen in March; now the best case is August. It has been an unpleasant trade.
Incidentally, this is why the gap exists between the common stock and APE prices. Some of it is due to uncertainty — maybe Vice Chancellor Zurn will reject the settlement and never allow the APEs to convert — but most of it is probably due to limits to arbitrage. If you notice the gap and say “hey, these APEs are trading at a huge discount to the common, I bet that gap will close,” that’s fine, but you can’t actually make that bet economically.
  [3]
 Arbitrageurs can’t really close the gap between the share classes: They tried, and got burned.
It’s still a bit of a weird gap. If you are an AMC shareholder, you could always sell your AMC shares and buy APEs: If you are not short selling, you don’t need to borrow the stock, so you can easily swap into the APEs. Sell one AMC share for $5.85 and buy three APEs, with some change left over; the APEs will eventually convert back into common shares (probably! not certainly! not legal or investing advice!) and you’ll get free extra shares. But:
	A lot of AMC shareholders are meme-stock believers who do not want the APEs to convert into common stock, are trying to prevent it, don’t believe it will happen, and therefore have no reason to bet on the gap closing.	If you are an institutional AMC shareholder, sure you can sell your common shares and buy many more APEs. But if you instead hold the common shares, you can make a lot of money lending them out: Those super-expensive stock-borrow costs paid by short sellers end up getting paid (largely) to the share owners who lend out their common shares. The common stock has a higher price than the APEs in part because it is worth more: The common stock comes with share-lending cash flows, while the APEs do not.




      iRobot



We   talked a couple of weeks ago about the mechanics of a public-company merger. Specifically, I pointed out that public-company acquisitions don’t generally have price adjustments for changes in the target’s financial situation between signing and closing. If you sign an agreement in April to buy a public company for $54.20 per share, expecting it to have $1 billion in cash at closing, and then when the deal closes in October it only has $900 million in cash, you don’t get to knock a dollar or two off the purchase price. The company is less valuable at closing than you thought it would be, but there’s not a lot you can do about it. This is partly because, when you sign an agreement to buy a public company, the company needs to have a shareholder vote to approve the deal, and the shareholders need to know what they are voting on. If the price can change at the last minute, it’s hard to do the vote.
That said, there are limits: If the company’s cash goes from $1 billion to $0, perhaps there has been a “material adverse effect” that gives you the right to get out of the deal. Or if the company decides to pay its chief executive officer a $1 billion special bonus for being such a great CEO, that might not be “in the ordinary course of business,” which would also give you a right to get out of the deal. The merger agreement will say things like “the company can’t pay bonuses outside of the ordinary course of business without the buyer’s permission,” and so if the company wants to pay a big bonus it will have to ask you first, and you can say no and preserve the cash for yourself.
Similarly, if you expect the company to have some money at closing, but it runs through its money too fast and has to borrow more money to stay afloat, that will reduce the value of the company to you, and you probably do get to do something about it. The  merger agreement will say something like “the Company will not … create, incur, assume, guarantee, endorse, suffer to exist or otherwise be liable with respect to any indebtedness for borrowed money.” Between signing of the merger agreement and closing, the target company can’t go around borrowing money without your permission. That would change the deal.
And the way that works in practice is that, if the company does need to borrow money, it will come to you for permission, and you will say something like “well I see that you need the money, but this makes your company worth less than I thought it would be, so I want a price reduction.” And then you will just   negotiate a price reduction in exchange for your permission:

IRobot Corp. tumbled after Amazon.com Inc. lowered the price it’s paying for the Roomba maker to $51.75 per share from $61 per share.
IRobot has entered into a $200 million financing facility to fund its ongoing operations, the companies said in a statement. That prompted Amazon to change the price to offset the planned increase in iRobot’s net debt.
IRobot shares fell about 8.9% to $42.73 as markets opened in New York, while Amazon was largely unchanged.

Note that that price is well below $51.75, because “since Amazon announced the transaction last August, the Federal Trade Commission and European regulators have been probing the deal.” Here are iRobot’s  filing announcing the amendment, and the press release saying that “the change in price per share is expected to be largely offset by the planned increase in iRobot’s net debt under the new financing facility.” Largely offset: The company has about 27 million shares outstanding, so the $9.25 per share price reduction is worth about $250 million, which is more than $200 million. But if the company you are buying comes to you and says “hey uh bad news we’re out of cash and need to borrow more, that’s okay right,” you are going to exact a price for saying yes.



      Multistrategy funds



Here are two ways to run a hedge fund:
	Be a charismatic genius investor. Pick some companies that you think are good, buy their stocks, hold them for a fairly long term, maybe do a bit of activism to improve their performance. Pick some companies that you think are bad, short their stocks, maybe do a bit of short activism to get everyone to see their flaws. Have a concentrated portfolio of a dozen or so names, bet big with conviction, hope you’re right.	Hire like 30 genius investors and scientifically analyze their investing styles and track records to break down exactly how they add value. Pay them only to do that: Hedge out all of their exposure to the broad stock market, and to factors like value and momentum, so that they are not getting paid just for owning stocks in a bull market (or owning tech stocks in a tech bubble), but only for picking exactly which stocks will outperform which other stocks. Because everything is hedged, they won’t benefit from broad market movements, and they probably won’t make all that much of a return. But because everything is hedged, you can leverage it a lot: You can take $1 of investor capital, buy $10 of good stocks, short $10 of bad stocks, and if the good stocks are up 10% and the bad ones are up 8% then you have a 20% return on capital.

Crudely speaking, the first approach was the popular image of hedge-fund management for much of its history, and the second approach — the “multi-manager” or “multistrategy” fund or “pod shop” — has become increasingly dominant in recent years. There are reasons for this. For one thing, the pod shops, with their scientific performance measurement, can more convincingly promise their clients that they are delivering uncorrelated returns, that they are good rather than just lucky. Also, clients like that they are more institutional and less reliant on one charismatic genius, which makes them less susceptible to succession drama. Also, there is reason to think that the skills of (1) making investment decisions, (2) charming clients and (3) running the operations of a company are all pretty separate, and the multi-manager funds can hire people who are good at making investment decisions, let them do that, and have someone else handle the rest of it.
At FT Alphaville, Rupak Ghose points out another important aspect of pod shops, which is that they are structurally much better clients for banks:

Many of the most successful equity long/short managers of recent decades — such as Viking, Lone Pine, TCI, Lansdowne, and Egerton — had very different investment styles from the dominant multi-strategy shops. The former had more concentrated investment portfolios and less churn, and were closer to long-only growth funds than multi-strategy “pods”. (Remember, capital is often pulled away from a “pod” when it is down 5 per cent, and the “pod” closed altogether if it is down 10 per cent.)
Commissions to sellside banks and data vendors are consequently much larger for pod shops. Similarly, equity long/short funds tend to deploy leverage that is order of magnitudes lower than multi-strategy and systematic firms that are in vogue today, meaning the industry’s AUM packs a greater punch.

Being really scientific about performance measurement tends to mean trading a lot and borrowing a lot of money, both of which make you a good client of banks. Buying a dozen stocks, shorting four more, and holding them for years makes you less exciting for the banks. 



      Too much trading



If you are a retail stock investor, which is better:
	Sometimes trading stocks for a bit, on your lunch break at work, or	Trading stocks all night, sometimes looking up from your brokerage website to see the sun rising?

I mean! Intuitively, if you like trading stocks, trading stocks all night long might be more fun than having to fit it into the workday. But if you are having fun trading stocks all night long, you are probably making less money? I would guess?
That is just a guess. Here’s “Trading Hours and Retail Investment Performance” by Ed deHaan and Andrew Glover:
This paper examines the effects of stock market access, and in particular trading hours, on retail investment performance. We find that plausibly exogenous increases in trading hours are associated with meaningful declines in retail investors’ capital gains, as reported on tax returns for the U.S. population. Our results indicate that increasing trading hours exacerbates retail investors’ tendencies to trade “too much,” leading to declines in portfolio performance. Our findings inform discussions among academics, practitioners, and regulators about the potential detrimental effects of decreasing barriers to entry for retail investors in trading markets.
“We find that a one-hour decrease in waking trading hours is associated with a 3.9 percentage point increase in investment performance,” they write, though to be fair they are talking about trading during “normal productive waking hours”: They use time-zone discontinuities to argue that investors who are at work during more of the market’s hours have more trading time, and those investors do worse than investors (say in California) who get to their desks after the market has already been going for a while.
I don’t know if that answers my question? Another way to put that is that investors who have more time to trade outside of normal working hours — who have to wake up early to feed their obsession — do better than the ones who can only trade during working hours. But they do write:
The generalizability of our empirical findings warrants discussion. Our setting limits access in the first hour(s) of regular trading, when volume, volatility, spreads, and adverse selection are especially high. Adverse selection and spreads are often even higher outside of regular hours (Barclay & Hendershott 2004), and recent research finds that news-driven volatility is now also higher out-of-hours than during the day (Boudoukh et al. 2019). Thus, our findings from the first hour(s) of regular trading should be informative about the likely effects of increasing retail investors’ out-of-hours trading access. 
Yeah no the market is not going to be efficient if you are trading at midnight, but efficient is maybe not what you want.



      Things happen



UBS to Pay $387 Million in Credit Suisse-Tied   Archegos Fines. US security officials scrutinise Abu Dhabi’s $3bn  Fortress takeover. Lazard Launches New Arm Focused on Capital Raising. The World Tied $3.5 Trillion-Plus of Debt to  Inflation — The Costs Are Now Adding Up. The Little Known   Metals Giant that Rules a Global Market. Leon Black’s $158 Million   Payments to Epstein Spark Senate Probe.  Lyft CEO David Risher’s Efforts to Turn the Company Around: Cheaper Rides, Fewer Distractions. TCW to Buy  Engine No. 1’s ETF Unit in First Deal for CEO Katie Koch. TikTok’s Next Plan for U.S. Dominance: Selling Made-in-China Goods. TikTok is adding  text posts.   Musk Explains Why He’s Axing Twitter Name, Iconic Bird Logo.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!

  [1] More specifically, each APE would convert into common on a one-for-one basis, but common shareholders will get a settlement payment of an additional one share for every 7.5 shares they hold now. So 75 common shares will turn into 85 new common shares, while 75 APEs will turn into 75 new common shares, a 0.8824 ratio.


  [2] The current ratio is a result of the settlement, and the original hedge ratio would have been one for one, but never mind that. You could have put this trade on   almost a year ago, when AMC first issued the APEs, and, feh.


  [3] “What about derivatives?” Ehh, derivatives prices incorporate stock borrow costs; if you bought a $5.50 August put and sold a $5.50 August call you’d pay about $1.20 net at a spot price of around $5.25, per Bloomberg data, which translates into losing about $1 a month anyway.











            Follow Us













              Get the newsletter


















Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022







<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cj5x1l.5je3/5991ed58.gif" alt="" border="0" /></a>
