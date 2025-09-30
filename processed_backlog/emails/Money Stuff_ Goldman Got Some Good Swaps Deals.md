# Money Stuff: Goldman Got Some Good Swaps Deals

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Tue, 11 Apr 2023 13:32:29 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Goldman Got Some Good Swaps Deals_Tue,_11_Apr_2023_13-32-29_-0400_(EDT)_1877161112ffcad0.eml
**Processed:** 2025-08-24T19:13:09.747807














        There are different ways to buy a stock index. You can just pay cash to buy all the stocks in the index. You can buy an exchange-traded fund





































      One-day lookback



There are different ways to buy a stock index. You can just pay cash to buy all the stocks in the index. You can buy an exchange-traded fund that holds all the stocks in the index. Or you can do an equity index swap: You sign a contract with a bank in which the bank promises to pay you the return on the index over some term. If the index is at 100 today, and you do a $10 million one-year swap with a bank, and then the index is at 108 in a year, then the bank pays you $800,000 (the index’s 8% return on the $10 million notional amount). If the index is at 93 in a year, you pay the bank $700,000.
The swap is approximately like the bank lending you the $10 million to buy the index: You don’t put up the $10 million upfront,
  [1]
 but you get back the return on $10 million worth of stock.
  [2]
 The bank charges you for that synthetic loan; the terms of the swap contract will say:
	The bank pays you any positive return on the index.	You pay the bank any negative return on the index, plus an interest rate. 

And so when you call up a bank to do a swap on some index, the bank will quote you a price consisting of the interest rate that you will pay — “3-month US dollar Libor plus 70 basis points,” for instance.
  [3]
 Or vice versa: You could sell a swap to the bank, if you want to get short the index; then the bank would pay you the interest rate and you’d pay the bank the return on the index. 
This makes the equity index swap roughly equivalent to buying the ETF: Either way, you make money when the index goes up, lose money when the index goes down, and pay some cost of funding to get the money, real or synthetic, that you use to buy the index.
At some high level of generality, buying an index using a swap and buying it using an ETF should be economically equivalent. But if you are an index trader at an investment bank, your entire job is to find places where they are not equivalent. Your job is to do the arbitrage — buying and selling the same index in two different ways — in such a way that you make a little bit of money. One simple way is: If you can borrow money at 2% to buy the ETF for cash, and then you can sell a one-year swap at a 2.1% financing rate, then you make a 0.1% profit.
  [4]
 Your profit is not about the index going up or down; you have hedged that out. (You bought the index for cash and sold it on swap.) Your profit is about the different interest rate.
There are better trades. Here is a good one, from a  Commodity Futures Trading Commission enforcement action against Goldman Sachs Group Inc. yesterday. Disclosure: I used to work at Goldman, I sold derivatives, and while I did not do or witness anything precisely like this, uh, let’s just say that this enforcement action brought a tear to this old derivatives structurer’s eye. This is good stuff!
  [5]
 Sure sure sure sure sure it is apparently illegal, but I cannot help but admire it.
The trick starts with the fact that in an equity index swap, the short party pays the long party the return on the index over the “strike price,” meaning roughly “the price of the index today.” So if the index is at 100 today, we can do a $10 million swap struck at 100, and then if the index is at 108 in a year I will pay you $800,000, etc. 
But customarily the strike price is actually the price of the index tomorrow: We sign the swap contract today, and then we set the strike price tomorrow, and then the swap pays the return over the strike price in a year or whatever the term is.  The CFTC explains:
Equity index swaps traditionally strike on a “T+1” basis. This means that the “strike” price, or “initial price,” of the swap equals the index value published the day after the parties agree to the trade. This one-day lag ensures that none of the components of the index that will form the initial valuation have priced at the time the swap is agreed upon, reducing the likelihood of potential information asymmetries regarding the projected index values.
So if you buy a swap today, ordinarily it starts tomorrow, to avoid any information asymmetries.
About those information asymmetries. Goldman’s trick was to trade T+0 swaps, that is, swaps that were struck based on that day’s index level. This doesn’t matter that much, if you trade US stock indexes in the US: If you trade an S&P 500 swap at 2 p.m., and it strikes based on that day’s S&P 500 closing level, you don’t know what that level will be. But Goldman traded T+0 swaps, in New York, on non-US indexes that closed before New York did:
Almost all the “same-day” equity index swaps at issue in this matter were swaps tied to the MSCI Europe Australasia and Far East (“EAFE”) Index (“EAFE Index Swaps”). The MSCI EAFE Index tracks a basket of stocks from Japan, Europe, Hong Kong, Singapore, New Zealand, and Australia, among others. The MSCI EAFE Index level (or, index price) is published once per day, in the early evening, New York time (“Index Settlement Value”). It is calculated by MSCI, using a formula based on the closing prices of the index’s component stocks. The foreign exchanges on which the component stocks trade, however, close hours before New York exchanges do—some before the New York trading day even begins. In other words, most of the component prices used to calculate the Index Settlement Value are stale—at least several hours old—by the time the Index Settlement Value gets published in New York.
If you trade a T+0 swap on the MSCI EAFE Index at 2 p.m. in New York, (1) the index price is not published yet, but (2) you already pretty much know what it will be, because all the stocks have closed already.
Also, though, you have a head start on knowing what tomorrow’s index price will be:
Though most of the component stocks in the EAFE Index trade on exchanges that close well before the New York markets do, there are other “proxy” instruments that generally track the market value of the components of the EAFE index and trade throughout the New York trading day. For example, there is an exchange traded fund (“ETF”) that tracks the MSCI EAFE Index. It trades on the NYSE throughout the New York trading day and reflects the market’s view of the real-time value of the basket of stocks in the corresponding index—despite the fact that the markets in which the underlying stocks trade may be closed.
So at 2 p.m. on Tuesday in New York, you can calculate that the MSCI EAFE index settlement price for Tuesday will be, say, 2,000 — a price that will be published Tuesday evening, but that reflects the index level as of Tuesday morning. But the ETF on that index trades all day in New York, and you can look at the trading price of the ETF at 2 p.m., and it might be above or below 2,000. If the broad market is rallying and people expect European and Asian stocks to trade up, then the ETF might trade at, say, 2,050. The CFTC says:
The result is twofold: (1) since most of the markets in which the underlying equities traded closed hours before the Index Settlement Value was published, sophisticated parties with the wherewithal and resources to access relevant market data could know—or have a very good approximation of—what the daily Index Settlement Value would be hours before that publication; and (2) during the New York trading day, the real-time market value of the components of the index, as reflected in proxy instruments like the EAFE ETF, can—and did— diverge from the projected Index Settlement Value. For example, during the New York trading day, the ETF and other proxies could be trading above (at a “premium” to) the projected Index Settlement Value. Or, the ETF and other proxies could be trading below (at a “discount” to) the projected Index Settlement Value.
There is a simple arbitrage: Sell the ETF at 2,050, buy the swap at 2,000, and collect the 50 points of difference. Trade the same index in two different ways at two different prices.
And that’s what Goldman did. It went out to swaps customers and said “hey we’ll pay you Libor plus 55 basis points for a regular-way T+1 swap, or, if you want, we can pay you Libor plus 90 basis points for a T+0 swap, that’s a good deal huh?” And some customers said yes:

For example, on January 21, 2016, Goldman told a client that Goldman could “bid” for a nine-month EAFE Index Swap. Specifically, Goldman said: “normal T[+]1 is 3mL+55 bid (+60 mid). for today's strike can show 3mL+91.” By bidding the same-day swap at a rate that appeared to be 31 basis points over the [pre-trade mid-market mark, i.e., the fair market price] for the T+1 swap, Goldman gave the client the impression that the same-day swap was a better deal for the client than the T+1 swap. It was not. Indeed, at the time, the EAFE index proxies were trading at a premium to the projected Index Settlement Value—meaning that the client would be selling the equity leg to Goldman at a below-market rate. Although Goldman offered the client a higher interest rate than the client would have received by trading a T+1 swap, Goldman’s higher same-day interest rate did not adequately compensate the client for the disadvantage on the equity leg. …
Goldman would only solicit or agree to a “same-day” swap when the client would be buying or selling the equity leg underwater and Goldman, conversely, would be selling or buying the equity leg at a level it could immediately cash in for a profit through the index proxy instruments. Yet, the “preferential” interest rates that Goldman offered clients to entice them to transact same-day did not fully compensate the clients for the disadvantage at which the client would start the equity leg.

And:
As a result, “same-day” swaps were particularly lucrative for Goldman. For example, on August 25, 2015, Goldman offered to enter a same-day swap with a client at an interest rate that, according to internal communications, was 15 basis points above what the client would have received in an analogous “T+1” swap. The client agreed to transact “same-day” at this seemingly preferential rate. The strike price the client received on the equity leg, however, was at least 60 basis points below market at or around the time of the agreement. As a result, Goldman traders estimated that they had earned a $1,620,000 profit that day on this swap and the corresponding index proxy trades alone. The client, for its part, thought it was getting a good deal; it did not understand why Goldman was offering the high interest rate.
The client thought it was getting a good deal, eh? Thought Goldman was just paying a little extra interest out of the goodness of its heart? 
Was this fraud? I mean, not exactly? The relevant pieces of information — the closing levels of the stocks in the index, the trading levels of the index ETF — were all public and pretty easy to get and calculate. Goldman wasn’t exactly tricking anyone into doing T+0 swaps. It wasn’t crossing the “1” out of the swap confirmation and writing in “0.” It would openly say “here is our price for a normal T+1 swap and here is our better price for a T+0 swap, don’t you want that one instead?” It’s, just, you know:
To be sure, the market prices of the index underliers, as well as projections of the end-of-day Index Settlement Value based on then-prevailing market prices of underliers (or, for underliers that had closed for the day, the closing prices), as well as the pricing of the index proxy instruments are publicly available. Parties with the resources and wherewithal to do so could, like Goldman, see when the proxy instruments were trading at a premium or a discount to the projected Index Settlement Value and, therefore, whether the projected Index Settlement Value was above or below the real-time market value of the components of the Index. Goldman’s clients, however—particularly, the ones to whom Goldman repeatedly returned to execute “same-day” swaps—rarely demonstrated such sophistication and often appeared to believe they were receiving an advantageous interest rate, with no strings attached.
Yes yes yes. If you are a DERIVATIVES SALESPERSON AT GOLDMAN SACHS, and you have a customer who APPEARS TO BELIEVE THAT HE IS RECEIVING AN ADVANTAGEOUS INTEREST RATE, FROM GOLDMAN SACHS, WITH NO STRINGS ATTACHED, you sure will repeatedly return to that customer to execute trades. That’s a real good customer! The customer who thinks that Goldman Sachs are charitable idiots who are giving him a good deal for no reason is going to be getting a lot of calls from Goldman Sachs. “Hey bud, got another great deal for you,” his Goldman salesperson will giggle to him, a dozen times a day.
Look, I do not want to be too generous about Goldman’s cleverness, or too ungenerous about its sharp elbows, but, just, if you think that you’re pulling a fast one on Goldman Sachs, you might be right, but maybe double-check to be sure? If you think that you are repeatedly pulling the same fast one on Goldman Sachs, man, you’d better be really sure.
But, right, it’s not exactly fraud, but it’s a little shady. Goldman definitely pushed these trades:

On another occasion, in January 2016, Goldman personnel asked a client: “any interest in [EAFE swaps]? We have an axe if you’re looking to put on more short exposure.” When the client, who had never traded “same-day” before responded with interest to sell $90 million notional, the Goldman salesperson quoted:
For Tomorrow’s strike: 3mL+50 bid (PTMM +53)for TODAY’s strike: 3mL+100
When the client responded with interest in the T+1 strike, the Goldman salesperson replied: “tomorrow’s strike? You’re not interested in today’s at the much better level?”—explicitly suggesting that the client would be better off trading same-day. Yet, the salesperson failed to disclose the disadvantage—that the client’s equity leg would start underwater, at a below-market strike price.

And did not explain why it liked them so much:
Furthermore, communications show that Goldman personnel believed that the less the clients understood about the economics of the same-day swaps, the more profit Goldman could make. As a Goldman trader told a Goldman salesperson, disclosing more detail about same-day swaps “makes it easier for them to squeeze us; we usually just say we have an axe.”
The CFTC concludes that Goldman’s comparison of its T+0 prices to the standard T+1 mid-market price was misleading, and that all of this violated Goldman’s obligation “to communicate with counterparties in a fair and balanced manner based on principles of fair dealing and good faith.” Which, yes, fine. It is a bit of a gray area, but if you are a big bank swaps dealer, and you are smarter than your clients, you cannot abuse that advantage too much; this apparently went too far. 





























      J&J



Earlier this year, Johnson & Johnson’s baby-powder division was thrown out of bankruptcy court for not being bankrupt enough. What happened is that J&J sold baby powder with talc in it, and people started suing J&J, alleging that the talc caused cancer. J&J has always denied these claims, but it lost some of these cases and had to pay huge damages. More cases were coming, and to get out ahead of them, J&J decided to go to bankruptcy court. It used a  “Texas two-step” merger to separate out its talc liabilities into a new subsidiary called LTL Management LLC, and then had LTL file for bankruptcy.
There are obvious benefits of this for J&J. For one thing, the bankruptcy filing would let J&J handle all of its talc claims in one case, instead of litigating against different plaintiffs in different courts. Also J&J presumably expected the result to be cheaper: Bankruptcy courts are in the business of working out negotiated plans to pay all similar claimants the same amount, while going to a bunch of jury trials in different courts ran the risk of getting a bunch of different multibillion-dollar verdicts. Juries sometimes award huge damages to send companies a message, while bankruptcy courts kind of don’t.
Still it is important not to overstate the benefits of the Texas two-step for J&J. The goal was to get into bankruptcy court and pay plaintiffs a negotiated amount, not to stiff them entirely. You could imagine using this approach to stiff the talc claimants entirely: Maybe J&J could have put all of its talc liabilities into LTL, given LTL no assets, filed for bankruptcy and said “sorry everyone, your lawsuits are now against LTL, which has no money.” Lots of people did, and I guess still do, imagine that that’s what J&J actually did. But it didn’t. Instead, J&J promised to provide financial support to LTL to pay any plausible amount of talc damages: If the LTL bankruptcy case ended up awarding talc plaintiffs $10 billion or $30 billion or $60 billion of damages, J&J would write a check for that amount to LTL, and LTL would have enough cash to pay the claims. J&J, which is a $400 billion public company with AAA credit ratings, agreed to provide this money in a Funding Agreement; the amount was capped at something like $61.5 billion, which let us assume was more than the talc plaintiffs will get.
So LTL filed for bankruptcy in New Jersey, and a bankruptcy judge concluded that this was all in good faith and allowed. Some talc claimants appealed, though, and in January an appeals court threw LTL out of bankruptcy. We  discussed the case, and the opinion, at the time.
The appeals court did not throw out the bankruptcy because it concluded that J&J was acting in bad faith or trying to stiff the claimants or anything like that. Instead, its objection was that LTL wasn’t bankrupt enough: Bankruptcy, the court said, is for companies that are insolvent or nearly insolvent or otherwise in financial distress, and LTL wasn’t, because J&J had promised to pay it up to $61.5 billion to pay all these claims. The  court wrote:

We cannot agree LTL was in financial distress when it filed its Chapter 11 petition. The value and quality of its assets, which include a roughly $61.5 billion payment right against J&J and New Consumer, make this holding untenable. …
From these facts—presented by J&J and LTL themselves—we can infer only that LTL, at the time of its filing, was highly solvent with access to cash to meet comfortably its liabilities as they came due for the foreseeable future. It looks correct to have implied, in a prior court filing, that there was not “any imminent or even likely need of [it] to invoke the Funding Agreement to its maximum amount or anything close to it.”

That is, the problem is not that J&J put its talc liabilities into a box, undercapitalized the box to stiff claimants, and then had the box file for bankruptcy. The problem is that J&J put its talc liabilities into a box, overcapitalized the box to make sure that it was able to pay claimants, and then had the box file for bankruptcy. The court concluded that the overcapitalized box was not allowed to file for bankruptcy.
You see the solution, right?
No, I’m kidding. The obvious, ironic solution is for J&J and LTL to tear up the Funding Agreement and have LTL file for bankruptcy again with no money in it. “Sorry,” J&J would say to the talc plaintiffs, “but the court said we couldn’t file for bankruptcy with enough money to pay you, so we’re not gonna pay you.” There are problems with this solution, though. The point of the LTL structure is to come to some sort of negotiated settlement with enough plaintiffs to get a bankruptcy court to sign off on it (and bind the rest of the plaintiffs), and you can’t get a negotiated settlement with no money for victims. People will just keep suing and arguing that the bankruptcy is in bad faith, the Texas two-step merger is invalid, etc., and some of them will probably win. You can’t really get away with this approach, even if it sort of technically works.
Still the basic idea is right: J&J has to have LTL file for bankruptcy again, but with less money, so that it looks more bankrupt. And so, Bloomberg’s Steven Church and Jef Feeley  reported last week:

On Tuesday, just hours after a judge officially ended that first effort, J&J tried the gambit again. The company put the same subsidiary that had been tossed out of bankruptcy court back into Chapter 11, this time with a plan to pay $8.9 billion to resolve the decades-old cancer claims. The move has already drawn the ire of some victim lawyers and raised eyebrows among legal scholars, who are asking why this time will be any different. …
In the new case, J&J argues this one is different because they have support from many more cancer victims. That shows the company is acting in good faith, and the new case also meets a test set by the appeals court in Philadelphia, lawyers for the bankrupt subsidiary said in court documents filed Tuesday.

Here is the (new)  bankruptcy docket, and here is the “Debtor’s Statement Regarding Refiling of Chapter 11 Case” explaining why J&J thinks this time will be different. The simple version of it is that there is no longer a Funding Agreement in which J&J — the huge public company — agrees to pay all of LTL’s talc liabilities up to some enormous cap.
  [6]
 Instead, there is a Support Agreement in which J&J agrees to pay LTL’s talc liabilities, but only when LTL is in bankruptcy. That is, before it files for bankruptcy, LTL has limited resources to pay the talc liabilities, and might be insolvent or at least distressed. So it can file for bankruptcy. But once it is in bankruptcy, it can draw on J&J’s resources to pay those claims. From the statement:
These new financing arrangements resolve the concerns that led the Third Circuit to conclude the Debtor’s first chapter 11 case had to be dismissed. … Under the new financing arrangements, J&J’s support is only available in bankruptcy and only if approved by this Court. … As a result, J&J’s balance sheet and liquidity were no longer available to the Debtor before the filing of this second chapter 11 case. J&J’s support, which was always intended to facilitate, not frustrate, a bankruptcy filing by the Debtor now serves its intended purpose.
Get it? LTL might not have enough money to pay all the talc claims, so it can file for bankruptcy, at which point (but no sooner!) J&J will give it enough money to pay all the talc claims. Unless LTL is kicked out of bankruptcy court again, in which case J&J won’t give it enough money to pay all the talc claims. It is both a clever response to the appeals court’s complaint — “you said LTL wasn’t bankrupt enough, so we made it more bankrupt” — and also a threat: “There is enough money to pay everyone, but only if you let us do it in bankruptcy.”



      Research



A slight oversimplification of the rules is that in, in the US, it is illegal for brokers to charge clients money directly for investment research, while in the EU it is illegal for brokers not to charge clients money directly for investment research. In the US, brokers provide research for “free,” and clients compensate them for the research by doing trades with them and paying commissions for the trades. The EU dislikes the  potential conflicts of interest in that model,
  [7]
 so in the 2018 Markets in Financial Instruments Directive it banned it: Clients have to pay for research explicitly. In the US, though, charging people for research might make you an “investment adviser,” requiring separate registration with the Securities and Exchange Commission and creating awkward new fiduciary obligations.
For the last five years the SEC has sort of waived this conflict, telling US brokers that they can comply with Mifid (by charging European clients directly for research) without registering as investment advisers. But now that is ending. The  Financial Times reports:

After July 3, US broker-dealers are set to lose the protection of a five-year “no action” letter from the Securities and Exchange Commission that covered them against having to register as investment advisers. …
Without that protection they face a choice of registering, moving research teams into already registered affiliates, or potentially cutting off clients bound by Mifid regulations from research produced in the US.
“Banks are talking to each other and to their clients. It’s already causing disruption,” said one person involved in the behind-the-scenes discussions. …
Banks have resisted investment adviser status because it would restrict them from some activities including principal trading, and could hinder their ability to offer bespoke research, according to people with experience of the rules. The costs and complications of reorganising to register would depend on each bank’s individual arrangements, but were not insurmountable, they added.

It is a strange little conflict? One way to read the situation is that the SEC doesn’t mind forcing brokers to register their research arms as investment advisers with fiduciary duties to the research customers. The SEC has historically been a little suspicious of sell-side investment research, and the main suspicion is that sometimes research analysts seem to  recommend stocks for reasons other than that they think the stocks will go up. (To  maintain corporate access, for instance, or historically to  win investment banking business.) It would be hard for the SEC to write new rules saying that research analysts are fiduciaries for the people who read their reports, but it’s possible that European regulators have done that work for the SEC.



      Oxy



You could have a model of carbon emissions that goes like this:
	As the world becomes more concerned about carbon emissions, it will become increasingly expensive, illegal, undesirable or impossible to drill, sell or use oil.	Unless we find some way to make all the carbon emissions disappear, in which case oil is fine.

In that model, the biggest beneficiaries of carbon-capture technology will be oil companies, because in that model oil is basically a complement to carbon capture technology. If carbon capture works, you can sell lots of oil; if not, you can’t.
So if you are building promising carbon-capture technology, the way to monetize it is to buy stock in oil companies, or just to be an oil company. The Wall Street Journal  reports on Occidental Petroleum Corp.:

It is spending more than $1 billion to build the first in a planned fleet of plants using direct-air capture to pull the CO2 out of the air, a budding technology with fuzzy economics. Bolstering the move are generous tax incentives included in the climate package President Biden signed into law last year that cover up to 45% of Occidental’s expected initial costs per metric ton. 
Chief Executive Vicki Hollub, who has the blessing of the company’s largest investor, Warren Buffett, said the plan will help it reach net-zero emissions on all its operations, its own energy use and its customers’ use of its products, by 2050, and allow it to keep investing in oil extraction. …
Ms. Hollub told The Wall Street Journal in August that Occidental’s efforts on carbon capture and on becoming a net-zero emitter would allow it to keep up its investments in oil and gas. She warned that underinvestment in fossil fuels, which she says will be needed for years even amid the broader transition to clean energy, will lead to a scarcity of supplies. In contrast, she said, other oil majors such as BP PLC and Shell PLC have shrunk their oil segment and invested in renewables.
Oil companies will have to find ways to remove as much carbon dioxide as they emit “if they want to be the last producer standing in the world,” Ms. Hollub said.

In the abstract, it is a hard problem to get people to pay for clean air and low carbon emissions: Clean air and stable temperatures benefit everyone, and it’s hard to charge them all; there are free-rider problems. A lot of modern financial and regulatory engineering — emissions regulations, carbon-credit trading, ESG investing, etc. — goes into fixing this problem, putting a price on carbon emissions so that someone will pay for fixing them. Saying “we’re gonna ban oil companies unless oil companies find a way to capture carbon” is in some ways a simpler approach.



      Things happen



Collapse of SVB, Signature Bank Tests the FDIC’s  Executive Reserve Corps. Big US banks expected to report  deposit flight in upcoming earnings. Infinity Q Founder Velissaris Gets   15 Years in Prison for Asset-Value Fraud.   Elizabeth Holmes Will Have to Wait Out Her Appeal in Prison. Former Twitter Executives Sue Platform for  Unpaid Fees.   Winklevoss Twins Lend $100 Million to Their Gemini Crypto Platform. A Little-Known  Stablecoin Gets Big Help From World’s Largest Crypto Exchange. Citadel’s   Ken Griffin Gives $300 Million to Harvard University. “Mr. Christiansen says his farm has been met with  ridicule over his manure’s cost since the Goop mention.”
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!

  [1] You put up some margin, there are collateral terms, etc.; sometimes this   lands people in trouble but it doesn’t concern us here.


  [2] One way for this to work is that the bank buys $10 million of actual stock or ETF, with its own money, and pays you the return. The bank is hedged, long the stock and short the swap. In single-stock swaps it is customary to think of the trade this way, "the bank buys the stock and pays you the return via a swap," though that's not necessarily what happens; the bank could hedge with another swap, or not hedge at all.


  [3] The London interbank offered rate is being phased out as a benchmark interest rate, so I guess now they’d quote you the Secured Overnight Financing Rate, but in 2015 and 2016, the period relevant here, it was Libor.


  [4] I am ignoring various risks and complications here, including credit risk, capital, etc., but never mind.


  [5] It is loosely related to the concept in the section header here, the “one-day lookback.” In various contexts you can have an option where you have the right to exercise the option on any day and get the price that day. The option contract might say “Bank can exercise the option as of some date (the ‘Exercise Date’) by delivering a notice by close of business on the Exercise Date.” *Or*, it might say “Bank can exercise the option as of some date (the ‘Exercise Date’) by delivering a notice by close of business on the following business day.” Those sentences are almost the same! The difference seems boring and administrative, a matter of convenience, something a lawyer or back-office person would care about but not a trader. Nope! Having a one-day lookback on an option — deciding on Tuesday whether to exercise at Monday’s price — can be incredibly valuable; it is an extra little option on an option. (Consider the   Bed Bath & Beyond Inc. convertible preferred stock sale, where a ton of the economics were baked into the 10-day lookback on the conversion price.) There are, uh, times when the derivatives salesperson at the bank pays more attention to this sentence than the customer does.


  [6] There *is* a Funding Agreement in which a LTL’s direct parent company, a J&J subsidiary named Johnson & Johnson Holdco (NA) Inc., agrees to fund LTL’s liabilities. I don’t know enough about Holdco’s capitalization to know how valuable that funding is, but presumably it is capitalized thinly *enough* that LTL can argue it is in financial distress. Meanwhile the Support Agreement (with the J&J public-company parent) backstops that agreement, but only when LTL is in bankruptcy.


  [7] Roughly: When a fund company uses research and pays for it with commissions, the fund’s *clients* pay the commissions (trading costs are charged to the fund) but arguably the fund’s *managers* get the benefits of the research (it is part of their expenses of managing the fund). When the fund company has to pay for the research directly, either the management company eats the cost, or it explicitly and transparently passes it on to its customers.











            Follow Us













              Get the newsletter


















Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.








           You received this message because you are subscribed to Bloomberg's Matt Levine's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022







<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cij95y.5ind/dc02065c.gif" alt="" border="0" /></a>
