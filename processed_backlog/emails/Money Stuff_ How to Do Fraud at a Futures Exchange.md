# Money Stuff: How to Do Fraud at a Futures Exchange

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Tue, 13 Dec 2022 14:50:52 -0500 (EST)
**Source:** inputs/saved_emails/Money Stuff How to Do Fraud at a Futures Exchange_Tue,_13_Dec_2022_14-50-52_-0500_(EST)_1850d0b983057754.eml
**Processed:** 2025-08-24T19:13:12.823151














        I.Here is how you run a futures exchange: You offer some bets on some propositions, say, whether Bitcoin will go up or down. Some people com














































      Oh Sam



I.
Here is how you run a futures exchange:
	You offer some bets on some propositions, say, whether Bitcoin will go up or down.	Some people come and take the long side of the bet (betting that Bitcoin will go up) and others take the short side (betting that it will go down).	In a sense, they are betting against each other, but they never meet and are not betting against each other directly. Instead, you — the exchange — are on the other side of all of their bets. You pay out the winners and collect from the losers. They all take your credit, not each other’s. The point of the exchange is to be a trustworthy central counterparty for all the bets.	They all have to start by depositing some money in their accounts, so you can be confident they’ll pay up on the bets. Let’s say the deposit is $2,000 per Bitcoin bet, long or short.
  [1]
 This is called “initial margin.”	Each day,
  [2]
 you check if Bitcoin went up or down.	If it went up, you take some money out of the accounts of the short bettors and put it into the accounts of the long bettors.
  [3]

	If it went down, you take some money out of the accounts of the long bettors and put it into the accounts of the short bettors.	If a bettor’s account gets too low (because Bitcoin has moved against her), say below $1,000, you call her up and ask her to deposit more money.
  [4]
 This is called “variation margin.” If she doesn’t do it, you close out her bet at a loss.	If a bettor’s account gets really high (because Bitcoin has moved in her favor), she can withdraw some of the money in her account. If I bet on Bitcoin when it is at $17,000, depositing $2,000 of initial margin, and it goes up to $30,000, then I have $15,000 in my account. (My initial $2,000 plus $13,000 of market moves.) You might let me withdraw, say, $12,000 of it, leaving $3,000 in the account in case Bitcoin falls again.	If a bettor’s account ever gets below zero — if Bitcoin has moved so far against her so quickly that you didn’t have time to ask for more money or close out her bet, and now she owes more on the bet than she has in her account — then that’s bad. You still have to pay out the winner on the bet, but you can’t collect from the loser. (You can call and ask her for more money, but she might have made herself scarce.) You have to pay the winner out of your own — the exchange’s — money. If you don’t have enough money, then that’s really bad. Then you can’t pay out all your customers on the amounts in their accounts.

I want to make a few points about this model. First, it is really common and traditional. There are lots of futures exchanges; we have, for reasons,   talked a   lot this year about the London Metals Exchange, and the above description basically covers the LME if you substitute “nickel” or “aluminum” for “Bitcoin.”
Second, notice that in this model there are no Bitcoins at all. Some of your customers are long Bitcoin and some are short Bitcoin but you, the exchange, never have to have any Bitcoins. There are no Bitcoins in the customers’ accounts, or in yours. You just sit in the middle of some bets between the customers. You hold onto some money for them — the amount they deposited as collateral for their bets, customarily called “margin” — but you don’t keep the underlying thing, the Bitcoin that they are betting on, in a safe.
  [5]
 You can trade nickel futures on the London Metals Exchange, but the LME does not own any nickel.
  [6]
 
Third, this model is at its core about offering leveraged trading on Bitcoins: It’s a way for people to bet on Bitcoin going up without paying the full $17,000-ish that you’d need to buy a Bitcoin, since they only have to put up $2,000 of margin in Step 4, which is less than $17,000. And it’s a way for people to bet on Bitcoin going down, which is a necessarily leveraged trade: To bet against Bitcoin, you either need to borrow a Bitcoin and sell it or do a futures trade; there is no simple unlevered way to just hold negative one Bitcoin.
And so this model generalizes to doing margin trading on the actual underlying asset. Instead of saying “deposit $2,000 to bet on Bitcoin using futures,” you could say “deposit $2,000 and we’ll lend you the other $15,000 to buy a Bitcoin.” Or, instead of saying “deposit $2,000 to bet against Bitcoin using futures,” you could say “deposit $2,000 and we’ll lend you a Bitcoin to sell for dollars.” Then the exchange probably would have some Bitcoins; certainly, the first customer’s account would show that she owned a Bitcoin. But it wouldn’t have that many Bitcoins, because these trades would more or less offset: The exchange would borrow Bitcoins from the long customer to lend to the short customer, and borrow dollars from the short customer to lend to the long one. Economically this ends up looking quite a lot like the futures exchange, where the core business is sitting between customers’ bets with each other rather than holding on to customers’ assets for them.
Fourth, and most important, this is really risky. This is not a business of   taking customers’ money and holding onto it for them; this is a leveraged financial institution. If prices move too far in one direction too quickly, some of your customers will owe you more money than they have in their accounts. If you are unable to collect from them — because they have gone bankrupt or otherwise — then you still owe money to the other customers who do have money in their accounts. If you don’t have enough to pay them, then you go bankrupt and they don’t get paid.
II.
Here is how you manage the risks at a futures exchange:
	You charge a lot of initial margin. When people make bets on your exchange, you make them put up a reasonable amount of money to make sure that they’re good for it.	You tailor the initial margin to the riskiness of the bets. If people are betting on very volatile and illiquid things, they have to put up more money than if they are betting on very stable and liquid things. You look at historical price moves to satisfy yourself that the bets won’t move by more than the amount that customers have in their accounts.	You might tailor the initial margin to the size of the bets. If people are making huge bets, they might have to put up more money per contract than if they are making small bets.	You monitor variation margin carefully. If a position moves against a customer and she doesn’t put up more money, you close out her bet quickly so that she never ends up with a negative balance.	You are careful about letting customers take money out. If some small illiquid token called MattCoin is trading at $1, and I take a long position on 10,000 MattCoin futures, posting $1,000 of initial margin, and then 20 minutes later MattCoin trades up to $7, then I have $60,000 of gains and my account balance is $61,000. I might call you up and say “hey I’d like to withdraw half of that money.” And you might say something like “meh, no, let’s wait a while and see if this $7 price is for real.” What you don’t want is for me to withdraw $30,000 and then have MattCoin drop back to $1 immediately. Then you’d call me up and ask for the $30,000 back and I would probably have spent it. And now my account would have a balance of negative $30,000, oops.

This is absolutely the core of the business; what a futures exchange is is a business that manages these risks. And at a high level it is all very well-known stuff.
Take FTX, for instance, the crypto derivatives exchange founded by Sam Bankman-Fried; its name comes from the words “futures exchange.” Here is FTX’s help page  describing how it calculates margin for futures contracts. The calculation is based on a margin factor that is customized for each coin (depending on its volatility and liquidity) and the square root of position size. And here is  a Twitter thread that Bankman-Fried wrote in October, which I   discussed last week, about how FTX’s risk engine carefully takes into account position sizes and unusual market moves, so that if you own a ton of one token that goes up a lot very rapidly, FTX will not let you take money out right away. FTX knew all of the things about how to manage the risks of a futures exchange, and described its risk management in thoughtful and sensible ways.
But while this is all well-known stuff, it is not easy. Sometimes prices do move further and faster than you anticipated, and you have huge problems. We have talked a lot about the LME because   that’s what happened at the LME: Nickel prices shot up, traders who were short had negative balances, and there was just not enough money to pay out the traders who were long. The LME solved this in a messy and unsatisfying way, basically shutting down trading for a while and canceling some trades until prices went back down again. The traders who were long made money on paper, but then the LME took it away from them, because risk-managing a futures exchange is hard.
III.
Here is how you do fraud at a futures exchange:
	You set up a futures exchange.	You advertise, and also have, all of the standard risk-management stuff, with thoughtful margining and liquidation. You make the exchange look safe.
	You also do a lot of trades on the exchange with your own money.	Without telling anyone, you exempt yourself from all the risk-management stuff.	If your bets move in your favor and your account gets bigger, you take the money out to spend on luxury condos or political campaign contributions or venture capital.	If your bets move against you and your account gets smaller, or negative, you don’t put more money back in, and you don’t close out your bets. You just let your negative balance accrue and don’t worry about it.

In the long run, if you bet on volatile things, you will win some and lose some. But if you keep taking money out when you win, and don’t put money back in when you lose, then you will take out a lot of actual money to spend on stuff, and your account at your own exchange will become very negative. If you win a billion dollars and take it out to spend, and then you lose it again and don’t put it back, then on net nothing has happened (everybody’s bets are flat), but you have effectively transferred $1 billion of money from the exchange — ultimately, from other customers — to yourself. 
This is fraud for three reasons. First, in Step 2, you advertised that you had good risk management, but you had bad risk management. Again, the risk management is the whole business of a futures exchange; people are putting their money at your exchange because they expect it will not disappear because you told them that you managed the risks, but you were lying. You tricked customers into putting money at your exchange.
Second, it is fraud because it very predictably transfers money from your customers to you. Again, if stuff goes up, you take money out; if it goes down, you don’t put money back in; in the long run stuff goes up and down, so you will extract money from the exchange. Once you have extracted enough money, there will not be enough left for the other customers. You tricked customers into putting money at your exchange, and then you took it for yourself.
Third, it could be fraud because you might be tempted to speed the process along. You might say, well, look, if my account goes up I can take money out, and then if it goes down again I can ignore it, so I want stuff that will go up and down rapidly. So you might find a MattCoin — a small illiquid token — to bet on, then pump up its price so you can withdraw a lot of money, then walk away whistling as it collapses.
Or more to the point you can create your own token, sell a little of it into the market to establish a market price, keep 97% of it for yourself, and make markets in the token to keep the market price up. Then you go to your own exchange and say “hey I have billions and billions of dollars worth of this token, can I borrow against it?” And then the exchange says “sure, that seems fine,” because (1) you run the exchange and (2) you have exempted yourself from any sort of thoughtful risk management. “You own 97% of a token that really only you trade, and you want to put up that token as collateral to borrow billions of dollars of real money against its suspect market value? Sure, no problem,” the exchange says to you, not because that is a sensible trade but because you are doing fraud.
One more point here. Eventually this collapses. Eventually your balance at your own exchange gets really negative, and customers try to withdraw their money, and you don’t have enough to give to them, because you ended up transferring too much of it to yourself and spending it. Customers notice, there is a “run on the bank,” and your exchange ends up in bankruptcy. 
That’s bad! But you have an excuse! The excuse is that you were a futures exchange, a levered financial institution, and that is hard. You made some mistakes, of risk management and credit extension. You should have liquidated some customers more quickly; you should have extended less credit against their weird illiquid tokens. But these are not always easy calls, and sometimes even traditional futures exchanges mess it up. This wasn’t fraud, you can say; it was just a series of mistakes.
In other words, this is a good way to do fraud because what looks like “stealing customer money for yourself” can instead be characterized as “making unfortunate mistakes in the complicated nuanced business of extending leverage to certain customers.” Those certain customers are you, yes, but mistakes happen.
IV.
Yesterday   Sam Bankman-Fried was arrested in the Bahamas on US charges of doing fraud at FTX, his Bahamas-based crypto futures exchange, and Alameda Research, his affiliated crypto trading firm. Here is  the indictment that US federal prosecutors filed against him in New York; here are civil fraud cases filed by the  US Securities and Exchange Commission and the  Commodity Futures Trading Commission.
There is a lot going on here, but I want to focus on the simple story I laid out above. FTX was mainly a crypto futures exchange. The CFTC says:
FTX offered trading in a large variety of digital assets, including digital commodities such as bitcoin, ether, tether, and others. FTX operated primarily as a derivatives exchange and offered trading in various types of options, futures, swaps, perpetual swaps, and other digital commodity derivative products. FTX allowed customers to place buy (long) and sell (short) orders in an electronic order book, and matched customer orders via its “trading engine” or “matching engine.” FTX also offered a number of additional services related to the trading of digital asset products. For example, FTX operated a peer-to-peer (P2P) margin lending program where customers could offer margined and leveraged offerings to one another.
And like any serious futures exchange it advertised, and had, a sophisticated risk-management system. The SEC says:
In addition to generally promoting the benefits of automated risk engines, Bankman-Fried repeatedly claimed that FTX’s own risk engine was especially sophisticated and carefully calibrated. In a submission to the Commodity Futures Trading Commission, FTX touted its automated system, claiming that it calculated a customer’s margin level every 30 seconds; and that if the collateral on deposit fell below the required margin level, FTX’s automated system would sell the customer’s portfolio assets until the collateral on deposit exceeded the required margin level.
Meanwhile though Alameda — which was co-founded and 90% owned by Bankman-Fried — was trading on FTX and exempted from all of this. The CFTC says:

Alameda was exempt from FTX’s “auto-liquidation” risk engine functions, which would automatically liquidate (sell) a customer’s open position when their “Maintenance Margin Fraction” fell below a certain determined level. All customers who took on too much leverage or risk on FTX would thus be auto-liquidated by the exchange. Alameda was exempt from this—it could not be liquidated on FTX Trading under any conditions. This exception was hard coded into FTX’s system. This advantage was not publicly disclosed during the Relevant Period. The existence of this and other advantages directly contradicted public statements made by and on behalf of Defendants.
Alameda’s account on FTX also had a special designation in the FTX Trading code, labeled as an “allow negative flag,” which allowed Alameda to execute a transaction even if it did not have the funds available in its account to do so. Alameda also had an essentially unbounded credit limit in the FTX database. On at least one occasion during the Relevant Period, Alameda had reached a previously-set borrowing limit for its FTX account. In response, Bankman-Fried directed FTX personnel to raise the borrowing limit to a level that would be unlikely to ever be exceeded. On information and belief, FTX personnel ultimately raised Alameda’s borrowing limit to be many tens of billions of dollars. Alameda’s borrowed funds could also be withdrawn from FTX. These features, in combination, allowed Alameda unlimited ability to borrow and withdraw and digital assets directly from FTX Trading to put towards its off-platform activities.

And the SEC adds:
All of these special privileges were afforded to Alameda—and only Alameda—at Bankman-Fried’s direction, and all were hidden from investors. These privileges permitted Alameda to draw on FTX customer assets to a virtually unlimited extent for its own uses. Because its own FTX trading account was able to maintain a negative balance of billions of dollars, unbacked by sufficient collateral, Alameda was able to divert billions of dollars in FTX customer assets. Alameda did just that in 2022.
Much of this money went to pay off Alameda’s other lenders: Alameda was a trading firm that made risky bets, some of those bets lost, and it owed money to lenders; it paid them with money it withdrew from FTX. Some of it, though, went to “pay hundreds of millions of dollars in ‘loans’ to Bankman-Fried and other FTX executives, as well as hundreds of millions more to fund additional venture investments.”
Also, as we have   discussed a few   times, Alameda borrowed huge amounts of money secured by rickety FTX-created tokens like FTT and Serum, tokens that Alameda owned most of and whose market price was mostly set by Alameda. “The collateral Alameda deposited on FTX consisted largely of illiquid, FTX-affiliated tokens, including FTT,” says the SEC. And the CFTC says:

One of Alameda’s most significant holdings was the FTT digital asset. FTT was the FTX “exchange token” and could be used to obtain discounted trading fees for transactions on FTX Trading. On information and belief, Alameda did not pay to acquire its FTT holdings. …
Alameda’s FTT holdings were a significant portion of its balance sheet and a significant portion of all FTT in circulation. Alameda valued its FTT holdings on its balance sheet at the market price at which FTT was traded, without applying any discount to reflect that it could not have sold its significant FTT holdings into the marketplace without causing a sharp reduction in its trading price. ...
Alameda relied on its significant holdings of FTT and similar illiquid tokens, valued at the market value of the asset without discount, as collateral to support a number of large loans from various digital asset lending platforms. During the Relevant Period, Alameda took out a large number loans, at times totaling as much as $10 billion in notional value during the Relevant Period.

Eventually the market got concerned about FTT and those third-party lenders called in their loans to Alameda, so:
In approximately May and/or June 2022, Alameda was subject to a large number of such margin calls and loan recalls. It did not have sufficient liquid assets to service its loans. Instead, at the direction of Bankman-Fried, Alameda greatly increased its usage of FTX customer funds to meet its external debt obligations. Alameda was able to rely on its undisclosed ordinary-course access to FTX credit and customer funds to facilitate these large withdrawals, which were several billion dollars in notional value.
I   have assumed that Alameda ended up borrowing billions of dollars from FTX secured by its illiquid weird FTX-affiliated tokens like FTT, and today’s charges sort of suggest that but aren’t clear. Instead, Alameda seems to have borrowed billions of dollars from other lenders secured by those weird tokens (which is weird!), and then when those lenders got nervous Alameda paid them back with money that it borrowed from FTX. Since it could more or less do that unsecured — it could just have a negative account balance! — it doesn’t matter very much whether it put up the FTT tokens as collateral.
In fact, there was also a bizarre, enormous, unsecured, no-interest loan that FTX made to Alameda and documented as basically an accounting glitch. The SEC:

From the start of FTX’s operations in or around May 2019 until at least 2021, FTX customers deposited fiat currency (e.g., U.S. Dollars) into bank accounts controlled by Alameda. Billions of dollars of FTX customer funds were so deposited into Alameda-controlled bank accounts. ...
Alameda did not segregate these customer funds, but instead commingled them with its other assets, and used them indiscriminately to fund its trading operations and Bankman-Fried’s other ventures.
This multi-billion-dollar liability was reflected in an internal account in the FTX database that was not tied to Alameda but was instead called “fiat@ftx.com.” Characterizing the amount of customer funds sent to Alameda as an internal FTX account had the effect of concealing Alameda’s liability in FTX’s internal systems.

Basically if you deposited $100 at FTX through Alameda, then (1) Alameda kept the $100 to use for its own purposes, (2) FTX credited $100 to your account and (3) FTX recorded an offsetting $100 loan to Alameda. But “characterizing the amount of customer funds sent to Alameda as an internal FTX account had the effect of concealing Alameda’s liability in FTX’s internal systems”: It was sort of recorded as a loan, but not for purposes of FTX’s risk-management systems. (It was not so much recorded as a loan as it was   recorded as a “hidden, poorly internally labled ‘fiat@’ account,” in Bankman-Fried’s own words.) And “Alameda was not required to pay interest on the liability reflected in the ‘fiat@ftx.com’ account.”
The alleged fraud here is mostly these sorts of things: having a system that funneled money from customers to Alameda, in the form of a limitless line of credit and exemption from liquidation.
But — as we have also   discussed   before — another important element of the alleged fraud is that FTX advertised good risk management and had bad risk management. Bankman-Fried has been going around on a weird media tour whose essential message is “I made mistakes and was careless, sorry,” presumably thinking that that is a defense to fraud charges, that “carelessness” and “fraud” are entirely separate categories.
  [7]
 The SEC is having none of it:

Bankman-Fried repeatedly touted FTX’s automated risk mitigation protocols— which he called FTX’s “risk engine”—to the public, and prospective investors, as a safe and reliable way for crypto asset trading platforms to manage risk. … In addition to generally promoting the benefits of automated risk engines, Bankman-Fried repeatedly claimed that FTX’s own risk engine was especially sophisticated and carefully calibrated. ...
Bankman-Fried thus misled FTX’s investors by representing that its risk engine would protect FTX customer funds and would limit FTX’s exposure to any single customer, while failing to disclose that Bankman-Fried had personally directed that the engine not apply to one of its largest customers.
As Bankman-Fried acknowledged in a network television interview on or about December 1, 2022: “I wasn’t even trying, like, I wasn’t spending any time or effort trying to manage risk on FTX.” Bankman-Fried continued: “What happened, happened—and, if I had been spending an hour a day thinking about risk management on FTX, I don’t think that would have happened.”

If you attract customers and investors by saying that you have good risk management, and then you lose their money, and then you say “oh sorry we had bad risk management,” that is not a defense against fraud charges! That is a confession!

















































































      Everything is securities fraud



By the way! If you run a crypto exchange, and you steal your customers’ money, is that securities fraud? That is a hard question. I think that the US Securities and Exchange Commission   would mostly say:
	Most crypto tokens are securities,	You did a fraud about the tokens,	So you did securities fraud.

But that interpretation is not free from doubt. Some crypto tokens (Bitcoin, etc.) are clearly not securities, and with the rest it is debatable; the SEC has to fight over this interpretation in court. Going after a crypto exchange for securities fraud for stealing its customers’ money is, legally, a stretch for the SEC. The Department of Justice can go after the exchange for wire fraud, and the CFTC can go after a crypto futures exchange for commodity futures fraud, but the SEC might feel a bit left out.
Unless the crypto exchange sold stock. If the crypto exchange raised money from investors by selling them stock, well, the stock is clearly a security. And if it didn’t tell the investors, as it sold them the stock, “hey by the way we are stealing money from our customers,” then the investors were defrauded. 
This is the theory that we talk about all the time around here, that “everything is securities fraud.” If a company does a bad thing, and it didn’t tell its shareholders about it, then it deceived the shareholders and that’s fraud. Ordinarily this theory applies only to public companies, but if you’re a high-profile enough private company and you raised a lot of money from outside investors while doing bad stuff and not telling them about it, then I guess that’s good enough. 
And so  the SEC’s case against Bankman-Fried is a little silly because, although he allegedly defrauded customers out of billions of dollars, the SEC is vindicating the rights of the venture capitalists who supported him:
According to the SEC’s complaint, since at least May 2019, FTX, based in The Bahamas, raised more than $1.8 billion from equity investors, including approximately $1.1 billion from approximately 90 U.S.-based investors. In his representations to investors, Bankman-Fried promoted FTX as a safe, responsible crypto asset trading platform, specifically touting FTX’s sophisticated, automated risk measures to protect customer assets. The complaint alleges that, in reality, Bankman-Fried orchestrated a years-long fraud to conceal from FTX’s investors (1) the undisclosed diversion of FTX customers’ funds to Alameda Research LLC, his privately-held crypto hedge fund; (2) the undisclosed special treatment afforded to Alameda on the FTX platform, including providing Alameda with a virtually unlimited “line of credit” funded by the platform’s customers and exempting Alameda from certain key FTX risk mitigation measures; and (3) undisclosed risk stemming from FTX’s exposure to Alameda’s significant holdings of overvalued, illiquid assets such as FTX-affiliated tokens. The complaint further alleges that Bankman-Fried used commingled FTX customers’ funds at Alameda to make undisclosed venture investments, lavish real estate purchases, and large political donations.
The allegations are that he stole customer money, but he didn’t tell the shareholders about that as he was raising money from them, so really he stole their money too. So the SEC gets its piece of the action. 
We talked last year about an everything-is-securities-fraud case against Goldman Sachs Group Inc.; there, the allegations were that (1) Goldman did some fraud while selling mortgage collateralized debt obligations, (2) it didn’t tell shareholders that it was doing fraud while selling CDOs, so (3) it was doing fraud on the shareholders too.   I wrote:

As I often write, this theory can turn anything bad that a public company does into securities fraud: A company will put out some generic statements saying that it is good, follows the law, has a code of ethics, etc.; then it will turn out that the company secretly does bad things, breaks the law, has unethical executives, etc.; the stock will drop (because the bad things are bad for the company); the shareholders will sue, saying “you said you were good, we believed you, we bought the stock, but you were bad and we lost money.” And so climate change and sexual harassment and lax customer data protections and mistreatment of orcas can all be transmuted into securities fraud. 
Here the underlying bad deed that was transmuted into securities fraud was also securities fraud—Goldman said it put customers first, then it did a fraud on the Abacus CDO buyers, then it got caught, then its stock dropped—but that is just a coincidence. If instead of defrauding the Abacus CDO buyers Goldman had murdered them, that would not have been securities fraud with respect to the Abacus CDO buyers (it would have been murder), but it would still have been securities fraud with respect to Goldman’s shareholders (if the stock dropped after Goldman was charged with murder).

Similarly, here, the underlying bad deed was (allegedly) running a fraud at a crypto exchange, which certainly looks like securities fraud, but might not actually be. But it doesn’t matter; if you have shareholders, any sort of fraud is also securities fraud.












      Wirefraud



I don’t know how true  this is — Bankman-Fried denied it, and it sounds sort of too good to be true — but it is enough up my alley that I have to pass it along:

Members of the inner circle of power at collapsed cryptocurrency exchange FTX formed a chat group called "Wirefraud" and were using it to send secret information about operations in the lead up to the company's spectacular failure.
On the eve of the first big hearing in the US Congress this week that will investigate FTX's collapse, The Australian Financial Review has learnt that FTX founders Sam Bankman-Fried and Zixiao “Gary” Wang, along with FTX engineer Nishad Singh and former Alameda Research chief executive Caroline Ellison, used a chat group on Signal in the hope that the information would remain hidden.
On Monday (Tuesday AEDT) Mr Bankman-Fried denied being part of the chat saying, “If this is true then I wasn't a member of that inner circle (I'm quite sure it's just false; I have never heard of such a group).”

Don’t … don’t name your group chat Wirefraud? I mean I guess if you work for the US Attorney’s office you can do it, but even then I might go with “Stoppingwirefraud” just to be safe.



      Put spreads



I
wrote yesterday that “big serious players in crypto are long crypto volatility at a small scale, but short crypto volatility at a large scale,” and: “You are long a put spread I guess.” Like three people emailed to point out that really I mean a ratio put spread: You make money if stuff goes down a little, but lose money if it goes down a lot, which is not true of a simple 1-to-1 put spread. I appreciate that my readers care about the specifics of derivatives metaphors.



      Things happen



Brokers braced for big overhaul of US  stock trading rules. Goldman to Cut Hundreds More Jobs as   Consumer Unit Scaled Back. Sears Hometown Stores Files Bankruptcy to Liquidate Merchandise. WeWork’s Once Robust Cash Reserves Have Dwindled, Raising Chances of Default. Twitter   Disbands Independent Trust and Safety Council.   SpaceX Tender Offer Is Said to Value Company at $140 Billion. Tesla Investors Voice Concern Over Elon Musk’s  Focus on Twitter. Former top Twitter official forced to leave home due to threats amid ‘Twitter Files’ release. Binance Is Trying to Calm Investors, but Its Finances Remain a Mystery. Binance temporarily halted withdrawals of stablecoin USDC as investor concerns mount after FTX collapse.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!

  [1] Actual margin levels in crypto are more complicated but FTX US offered  10% initial margin on spot trades; FTX International tended to  offer higher leverage.


  [2] I am simplifying; in fact you could — and FTX did — mark to market far more frequently than that.


  [3] I am ignoring funding payments, where one side of a futures contract gets a little extra money each day even if the price of the underlying thing has moved against them.


  [4] This step is optional; it is standard in traditional financial markets but   FTX advertised that it never did margin calls, just moved to liquidation if margin levels got too low. Of course the bettor could voluntarily deposit more money before hitting the liquidation trigger, without a phone call.


  [5] In the general case, you could accept Bitcoin *as* margin, and it is reasonable for crypto futures exchanges to accept widely used liquid cryptocurrencies as collateral. It would be weirder for a metals exchange to accept metals as margin, though I guess not crazy.


  [6] There are some complexities there, in that metals futures can be physically settled and there is a   physical delivery mechanism that involves transferring metals in LME-approved warehouses.  But “the LME does not own or operate warehouses, nor does it own the material they contain. It simply authorises warehouse companies and the warehouses they operate to store LME-registered brands of metal, on behalf of warrant holders, and issue LME warrants through their London agent for material delivered into their approved warehouses.”


  [7] The CFTC says: “In the days and weeks since Bankman-Fried resigned from the companies, he has continued to make widespread public statements, provide explanations, and make admissions, including in live interviews. Several of his statements admit key facts pled herein.”











            Follow Us













              Get the newsletter



























Like getting this newsletter?
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022


















<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23chueuz.5jhb/47aee7a2.gif" alt="" border="0" /></a>
