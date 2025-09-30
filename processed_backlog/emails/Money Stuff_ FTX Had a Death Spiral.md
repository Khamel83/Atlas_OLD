# Money Stuff: FTX Had a Death Spiral

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Wed, 9 Nov 2022 15:14:52 -0500 (EST)
**Source:** inputs/saved_emails/Money Stuff FTX Had a Death Spiral_Wed,_9_Nov_2022_15-14-52_-0500_(EST)_1845e0836cc1c297.eml
**Processed:** 2025-08-24T19:13:08.307544














        So how could this happen? I don’t know, but let me speculate a little bit.Let’s start with Coinbase. Coinbase Global Inc. runs a cryptocurre














































      FTX



So how could   this happen? I don’t know, but let me speculate a little bit.
Let’s start with Coinbase. Coinbase Global Inc. runs a cryptocurrency exchange. When FTX.com, one of the largest crypto exchanges, was instantaneously vaporized yesterday,  Coinbase put out a statement, the gist of which was “don’t worry, we are not going to be instantaneously vaporized.” The part that I want to focus on is this paragraph:
There can’t be a “run on the bank” at Coinbase. As you can review in our publicly filed, audited financial statements, we hold customer assets 1:1. Any institutional lending activity at Coinbase is at the discretion of the customer and backed by collateral. We have no gating for client loan recalls or withdrawals.
The way it works is roughly that you open an account and send dollars to Coinbase, and then you tell Coinbase “I’d like to buy some Bitcoin with those dollars,” and Coinbase buys Bitcoin and holds on to it for you and  charges you a fee for that transaction. You can check your account balance, and Coinbase says “you have 0.5 Bitcoin” or whatever. That 0.5 Bitcoin is, in the general case, held by Coinbase; it has possession of the Bitcoin.
  [1]
 But it is held in a custody account for you.  Coinbase says:

Your funds are your funds, and your crypto is your crypto: Coinbase maintains internal systems, like a bank or a broker. Our fully audited ledger identifies your account, your fiat and crypto holdings, and tracks your account activity in real time. There’s never a situation where customer funds could be confused with corporate assets.
We will never repurpose your funds: We do not lend or take any action with your assets, unless you specifically instruct us to. Many banks and financial institutions use customer funds for commercial purposes including lending and trading, meaning that they often hold only a fraction of their customer assets at any given time. Coinbase always holds customer assets 1:1. This means that funds are available to our customers 24 hours a day, 7 days a week, 365 days of the year.

The analogy is: Imagine a weird sort of bank. You come to the bank with $100 in paper bills, and you deposit it in the bank, and the bank takes your paper bills and sticks them in an envelope with your name on it. Then it sticks the envelope in a vault, and if at any point you ask for your money back, it opens the vault and hands you your envelope. This sounds like a bad business model: The bank needs to pay for real estate and tellers and vaults, and it is not doing anything with your money. But the other weird thing about this bank is that, every day, you come in and say “hey I’d like to exchange my dollars for euros” or “my euros for pounds” or whatever, and each time you do that the bank charges you a dollar. So you have $100, which you exchange for €99, which you exchange for £98, which you exchange for $97, etc.,
  [2]
 paying the bank $1 each time. If all of the bank’s customers do this every day, then the bank makes plenty of money to pay for real estate and tellers and vaults and executive bonuses, without doing anything else with your money. It just takes the $100 out of your envelope and replaces it with €99, etc., always keeping exactly the right amount of money (in whatever currency you like that day) in exactly your envelope.
  [3]

And then if one day every single customer walked into the bank at the same time and said “we would like our money back,” the bank would just hand them all their envelopes. Don’t get me wrong, this would be a catastrophe for the bank: If everyone took their envelopes back, then presumably they would stop changing money at the bank and paying fees, and the bank would stop making money, and it would no longer be able to pay for real estate or tellers or vaults or executive bonuses. It would go out of business in fairly short order. But it would not go out of business that minute. It would actually have enough money to give all the customers their money back, because it kept all the customers’ money in their own envelopes the whole time.
No actual bank works that way. Real banks take deposits but don’t keep the money in envelopes; they lend it out.
  [4]
 Most classically, they borrow short to lend long, taking checking deposits that can be withdrawn at any time, and using them to make long-term mortgages. This makes them vulnerable to runs,  Diamond-Dybvig, It’s a Wonderful Life, etc., everyone knows all this.
But in theory a cryptocurrency exchange could work that way, and at a high level of generality Coinbase sort of does.
  [5]
 Historically — not so much now, but until early this year anyway — cryptocurrencies were volatile and exciting and people were jazzed to trade them a lot, so you could make a lot of money by just charging fees without doing anything else with customer assets. And that is a run-proof business. If everyone takes their money out at once, you have the money.
But then one day a customer comes to you and says “I have $10,000, but I am really bullish on Bitcoin, so I would like to buy $20,000 worth of Bitcoin. Why don’t you lend me $10,000 so I can buy $20,000 of Bitcoin, so I can get more excitement?” This is called a margin loan.
Or — equivalently — a customer comes to you and says “I have $20,000 of Bitcoin in my account, and I need some cash this month. I don’t want to sell my Bitcoin, because I am a true believer and also do not want to realize gains for tax purposes. Could you just lend me $10,000, secured by my $20,000 of Bitcoin? You know I’m good for it: If I don’t pay you back, you can sell my Bitcoin and pay yourself back from the proceeds.” 
You might just say “no, that’s dumb, Bitcoin is volatile, buying $10,000 of Bitcoin is plenty of excitement.” (In fact Coinbase  shut down margin trading in 2020.) But your competitors probably offer loans, and it is tempting for you to do it too. So you say, sure, fine, I’ll take your $10,000 and put $20,000 of Bitcoin in your account.
But where do you get the money that you are lending to the customer? Well, you have to borrow it too. Ordinarily the way that you will borrow it is by putting up the customer’s Bitcoin as collateral to your lender, just as the customer puts up its Bitcoin as collateral to you. If the customer defaults, you still have to pay your lender (and then you get the Bitcoin back and can sell it to pay off your customer’s liability to you); if you default, the lender sells the Bitcoin.
But who are the lenders? Oh, various possibilities. But one general point is that while some customers will want to borrow dollars to buy Bitcoin, other customers will want to borrow Bitcoin. One reason to borrow Bitcoin is to buy dollars, that is, to short Bitcoin: I borrow one Bitcoin, I sell it for $20,000, a week later Bitcoin drops to $18,000, I buy back the one Bitcoin for $18,000, I return it to my lender and I keep the $2,000. There are variations on this trade (I borrow Bitcoin and sell it for Ethereum, betting on the relative value between the tokens, etc.). It is necessarily a leveraged trade; I can’t short Bitcoin without borrowing it.
  [6]

If you are a crypto exchange, this is a nice opportunity. You have Customer A who has Bitcoin and wants to borrow dollars, and Customer B who has dollars and wants to borrow Bitcoin. (By “dollars,” for a crypto exchange, I mostly mean “dollar-denominated stablecoins,” though potentially also dollars.) You take some of Customer A’s Bitcoin and lend it to Customer B, and you take some of Customer B’s dollars and lend them to Customer A. Each of them is overcollateralized — you only lend Customer A half the value of her Bitcoin, and you only lend Customer B half the value of his dollars — so you feel pretty safe. And they both pay you interest.
But there are risks. One day Customer A might come in, pay off her dollar loan, and ask to take her Bitcoin back. You don’t have her Bitcoin, or not all of them anyway; some of them are with Customer B. Customer B owes them to you — ultimately you’re good for it — but you don’t have them now. There is a timing problem.
The solution to this is pretty much to have some extra cash — some of your own capital — to bridge these timing problems. Eventually you’ll get the rest of the Bitcoin back from Customer B, but for now you just pay Customer A out of your own Bitcoin stash.
But the timing problem is also connected to a real economic risk. If the price of Bitcoin falls by 90%, Customer B will be thrilled. He will come to you and say “here’s my Bitcoin back, I’d like to withdraw my dollars.” But you don’t have his dollars, or not all of them; half of them are with Customer A. Your dollar loan to Customer A is now underwater: You loaned her 50% of the value of her Bitcoin, but Bitcoin fell by 90%, so she owes you more than her collateral is worth. You call her up and ask her for more money — a “margin call” — but she, sensibly, doesn’t answer the phone.
  [7]
 You have to pay Customer B out of your own capital, and you don’t get it back from Customer A. You've just lost money. Actually that’s the best outcome. The worst outcome is that you don’t have enough capital, you go bankrupt, and Customer B does not get his money back.
Everyone knows this, which is why crypto exchanges — and securities broker-dealers, who have the same basic business model — spend most of their time thinking about risk management. Before the price of Bitcoin drops too far, you will be calling up Customer A for more margin, and if she doesn’t answer the phone you will liquidate her position to pay back the loan you made. If you are a sophisticated modern crypto exchange like FTX, you will have   automated 24/7 margining systems that automatically liquidate trades that have gotten too risky, so that only the rarest catastrophic market moves could get you in trouble.
But sometimes market moves are catastrophic, and in particular, sometimes securities broker-dealers and crypto exchanges will have “run on the bank” risks. If everyone knows that you are in this situation — that you have a lot of Bitcoin collateral and Bitcoin prices are falling — people will expect you to have to liquidate your Bitcoin collateral, so they will expect Bitcoin prices to fall, so they will sell Bitcoin, which will cause Bitcoin prices to fall, which will cause your long-Bitcoin customers to default, which will cause you to liquidate Bitcoin at lower and lower prices, etc., until you are bankrupt.
Now let’s add one more crypto element. If you are a crypto exchange, you might  issue your own crypto token. FTX issues a token called FTT. The attributes of this token are, like, it entitles you to some discounts and stuff, but the main attribute is that FTX periodically uses a portion of its profits to buy back FTT tokens. This makes FTT kind of like stock in FTX: The higher FTX’s profits are, the higher the price of FTT will be.
  [8]
 It is not actually stock in FTX — in fact FTX is a company and has stock and venture capitalists bought it, etc. — but it is a lot like stock in FTX. FTT is a bet on FTX’s future profits.
But it is also a crypto token, which means that a customer can come to you and post $100 worth of FTT as collateral and borrow $50 worth of Bitcoin, or dollars, or whatever, against that collateral, just as they would with any other token. Or something; you might set the margin requirements higher or lower, letting customers borrow 25% or 50% or 95% of the value of their FTT token collateral.
If you think of the token as “more or less stock,” and you think of a crypto exchange as a securities broker-dealer, this is completely insane. If you go to an investment bank and say “lend me $1 billion, and I will post $2 billion of your stock as collateral,” you are messing with very dark magic and they will say no.
  [9]
 The problem with this is that it is wrong-way risk. (It is also, at least sometimes,  illegal.) If people start to worry about the investment bank’s financial health, its stock will go down, which means that its collateral will be less valuable, which means that its financial health will get worse, which means that its stock will go down, etc. It is a death spiral. In general it should not be possible to bankrupt an investment bank by shorting its stock. If one of the bank’s main assets is its own stock — is a leveraged bet on its own stock — then it is easy to bankrupt it by shorting its stock.
The worst case is something like:
	You have 100 Customer As who are long Bitcoin on margin: They each have 1 Bitcoin in their accounts and owe you $10,000.	You have 100 Customer Bs who are short Bitcoin on margin: They each have $20,000 in their account and owe you 0.5 Bitcoin.	You have loaned 50 of the Customer As’ Bitcoins to the Customer Bs, and $1 million of the Customer Bs’ dollars to the Customer As. You keep the other 50 Bitcoins and $1 million as collateral.	Your accounts show that you owe clients 100 Bitcoins and $2 million, and that they owe you back 50 Bitcoins and $1 million, and you have 50 Bitcoins and $1 million on hand, so everything balances.	You have one Customer C who says “hi I would like to borrow 50 Bitcoins and $1 million, I will secure that loan with 150,000 FTT, each of which is worth $20.”	You say “sure, sounds good,” and hand over all your collateral.	Now you have 150,000 of FTT, worth $3 million, as collateral (and no Bitcoins or dollars).	Your accounts show that you owe clients 100 Bitcoins and $2 million and 150,000 FTT, and they owe you back 100 Bitcoins and $2 million, and you have 150,000 FTT of collateral, so everything balances.

But then if the value of FTT drops to zero, you have nothing. You have no Bitcoins to give to the customers to whom you owe Bitcoins, no dollars to give to the customers to whom you owe dollars. You just have to call up Customer C and say “hey we need all those dollars and Bitcoins back.” But Customer C will not want to give you back all those valuable dollars and Bitcoins in exchange for now-worthless FTT. Also the fact that Customer C had all that FTT in the first place is not a great sign. It is an FTT whale, and FTT is now worthless. Has it been borrowing elsewhere against FTT? Are all those debts coming due? 
Now let’s add a few more FTX-specific elements. One is that FTX is  an exchange for levered traders, offering products like perpetual futures and leveraged tokens that build in margin lending. So whereas the basic model of Coinbase is “they buy Bitcoin for you and put it in an envelope,” the basic model of FTX has to be “they lend you money to buy crypto and then make use of your crypto to get the money.” In financial terms, they have to rehypothecate your collateral; you can’t expect them to just keep it in an envelope if they’re lending you the money to buy it.
The other is that FTX is closely associated with a hedge fund called Alameda Research. Sam Bankman-Fried founded Alameda to do crypto arbitrage and market-making trades, and then he founded FTX to basically have a better exchange for Alameda to trade on. Alameda has lots of FTT, and  last week Coindesk reported on its balance sheet; the gist of that report was “wow its balance sheet is mostly FTT”:

The financials make concrete what industry-watchers already suspect: Alameda is big. As of June 30, the company’s assets amounted to $14.6 billion. Its single biggest asset: $3.66 billion of “unlocked FTT.” The third-largest entry on the assets side of the accounting ledger? A $2.16 billion pile of “FTT collateral.”
There are more FTX tokens among its $8 billion of liabilities: $292 million of “locked FTT.” (The liabilities are dominated by $7.4 billion of loans.)

That is not in itself a reason for a run on FTX! It might be a reason for the price of FTT to go down, if you think that Alameda has too much of it and might need to sell it.
The reason for a run on FTX is that you think that Alameda is, in my terminology, Customer C. The reason for a run on FTX is if you think that FTX loaned Alameda a bunch of customer assets and got back FTT in exchange. If that’s the case, then a crash in the price of FTT will destabilize FTX. If you’re worried about that, you should take your money out of FTX before the crash. If everyone is worried about that, they will all take their money out of FTX. But FTX doesn’t have their money; it has FTT, and a loan to Alameda. If they all take their money out, that’s a bank run.
And all of this is self-fulfilling: If you are worried about FTX’s business, then the price of FTT should go down. If the price of FTT goes down, then FTX’s business is riskier, because it has less collateral. If, say, the operator of the biggest crypto exchange gently raises one eyebrow and says “FTT, eh?” that can be enough to topple FTX. FTT goes down, leaving FTX undercapitalized, leading to customer withdrawals, leading to ruin.
Anyway it is still early and confusing but that seems to be the story of FTX. Coindesk reported on Alameda’s FTT exposure, and then Changpeng “CZ” Zhao, the founder of Binance Holdings Ltd., the largest crypto exchange, raised eyebrows by  tweeting that Binance would sell its FTT holdings “due to recent revelations.” People worried that this would tank the price of FTT and put pressure on FTX, so they started   withdrawing money from FTX. FTX didn’t have the money, and Bankman-Fried  started calling around asking for a loan or a bailout. Eventually he called CZ himself, and  they announced a non-binding letter of intent for   Binance to acquire FTX and make customers whole. Bankman-Fried’s fortune   basically vanished, as did his “  emperor aura.” Venture capital investors in FTX — which last raised money at a $32 billion valuation — are  probably getting zeroed, the price of  FTT collapsed, and now   regulators are investigating.
In this description I have drawn on Twitter threads from  Jon Wu,  Lucas Nuzzi and an anonymous “Wassie Lawyer,” who make arguments along these lines, as well as this Substack post from  Byrne Hobart. But the most informed view is probably that of CZ himself, who tweeted this morning:

Two big lessons: 
1: Never use a token you created as collateral. 
2: Don’t borrow if you run a crypto business. Don't use capital "efficiently". Have a large reserve.
Binance has never used BNB for collateral, and we have never taken on debt.

“Never use a token you created as collateral” suggests, to me, that FTX accepted its FTT token as collateral, probably from Alameda, probably in exchange for borrowing assets that it owes to customers. And that that went wrong in roughly the way I have outlined.
One other point here is that if this is the story, then it is not a liquidity crisis but a solvency one. That is, the problem is not a timing mismatch, in which FTX’s customers asked for their cash back but FTX did not have enough ready cash because it had long-term but money-good loans out. The problem is that FTX took its customers’ money and traded it for a pile of magic beans, and now the beans are worthless and there’s a huge hole in the balance sheet.   On that note:

Changpeng Zhao moved fast when Sam Bankman-Fried’s FTX.com was on the brink, offering to take it over and stem any further crypto contagion.
Within hours, he was forced to reconsider. 
For starters, Binance executives quickly found themselves staring into a financial black hole -- a gap between liabilities and assets at FTX that’s probably in the billions, and possibly more than $6 billion, according to a person familiar with the matter. 
On top of that, US regulators are circling FTX, investigating whether the firm properly handled customer funds, as well as its relationship with other parts of Bankman-Fried’s crypto empire, Bloomberg News reported Wednesday. 
It makes for a tricky decision for Zhao, known in the crypto world as CZ: Follow through with rescuing his onetime top rival and shoulder the financial and regulatory burdens, or let FTX crumble and sort through the potential wreckage? Zhao himself admits there was no “master plan” to take over FTX.
His answer, at least for now, is that the financial hole appears too deep. Binance is unlikely to follow through on its takeover of FTX, according to the person familiar, who wasn’t authorized to publicly discuss the matter.

Seems bad.























































      WhatsApp



Do you think that there is a big financial firm in the US that got through the entire pandemic without any employees doing any business over WhatsApp or text messages from their personal phone? It seems somewhat unlikely. So much business is about personal relationships, and texting and WhatsApp can feel more personal than your firm email account. And since you were not visiting clients in person during the pandemic, or sitting in your office, you might have been a bit more inclined to use your personal cell phone to communicate.
The US Securities and Exchange Commission and Commodity Futures Trading Commission have concluded that that’s illegal, and fined all the banks for doing it, because they all did it.   The fine is $200 million per bank (SEC and CFTC combined). I mean, there’s a little bit of differentiation, but not too much. Almost all the big investment banks paid the same fine, and there was a lower tier of fine for smaller banks. Nobody cares very much about how culpable each bank is, or how many bad messages it sent. (With one exception: Bank of America Corp. paid a bit more for being a bit more culpable.) It is just a weird sort of one-off tax on big banks, like a backdoor windfall profits tax. “WhatsApp, everyone pay $200 million.” Okay.
Anyway  private equity is next:

Financial regulators are looking at the biggest private equity firms’ use of WhatsApp and other messaging apps for work, in a signal that the US is ramping up its push to police Wall Street’s electronic communications. 
Apollo Global Management Inc., Carlyle Group Inc. and KKR & Co. said in regulatory filings this week that they received letters from the Securities and Exchange Commission on their use of electronic messaging for business.

Just a weird business all around. Everybody used WhatsApp and now everybody writes checks.












      Oh Elon



 Huh:

Tesla Inc. Chief Executive Officer Elon Musk sold at least $3.95 billion of the electric-vehicle maker’s shares just days after closing his buyout of Twitter Inc.
Musk unloaded 19.5 million shares, according to regulatory filings on Tuesday in New York, his first disposals since August. The documents didn’t indicate that the transactions were pre-planned.
The world’s richest person followed through with his takeover of the social-media platform in October, after spending months trying to get out of it. In August, Musk had said he was done offloading Tesla stock and that it was important to avoid an “emergency sale” of the shares in case he was forced to close the Twitter acquisition and struggled to bring in additional equity partners.

What is he doing with the money? Some possibilities:
	He used 100% of the proceeds of his previous sales to pay for Twitter, and now is selling more to pay his year-end tax bill on those previous sales.	He got to closing and realized he didn’t actually have enough cash to pay for Twitter, so  someone loaned him the money for a week and now he is paying it back.	Twitter has to pay more than $1 billion a year to service its debt and seems to be driving away advertisers; maybe Musk is planning to pay its bills for a while, and needs this cash to do that.	Having closed the deal for Twitter and spent a few days wreaking havoc, Musk has gotten bored and moved on to some other expensive hobby, which we will hear about in due time.	Index funds?

One popular, odd theory of Musk’s deal for Twitter is that he just wanted to diversify his Tesla holdings. Simply selling billions of dollars of Tesla stock would have upset his fans, driven down the stock price and undermined his image as a committed true believer. But selling billions of dollars of Tesla stock to fund a weird quest to buy Twitter would … I mean, be a distraction at least.
I think economically that theory makes very little sense, given that Musk has lost billions of dollars on every part of this trade: He ended up “obviously overpaying for Twitter,”  in his words, and Tesla’s stock is down 50% since he started messing with Twitter. But it sure has been a distraction! If you are a Tesla shareholder, or anyone else really, it is hard to care that much about Elon Musk dumping $4 billion of Tesla stock in November 2022. He just has so much else going on.



      Things happen



Barclays Joins Rivals in   Culling Investment-Banking Staff. Tiger Global Slashes Value of  Private Tech Bets by Billions, Documents Show. Opposition shadows  Cerberus windfall from Albertsons supermarket deal. Twitter says  user growth has picked up since Elon Musk took over. EDF Employees Challenge   Chairman’s Role in $10 Billion Buyout. Tyson Foods CFO Arrest Adds to  Governance Challenges for Board. National Park Service Asks Visitors to  Please Stop Licking Toads. Martin Shkreli tells Do Kwon “Jail is not that bad.”
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!

  [1] Coinbase does offer a noncustodial wallet where you can trade on Coinbase and hold your Bitcoins yourself.


  [2] This is sort of a dumb joke but presumably a new generation is coming up just intuitively assuming that $1 = €1 = £1, which is very convenient. In the olden days the values were all different!


  [3] In this dumb model I am eliding the *exchange* function and just assuming the bank acts as principal, though in fact Coinbase mostly operates as an exchange. So really it is like I want to trade dollars for euros and you want to trade euros for dollars so the bank takes $100 from me and gives $99 of it to you (and keeps $1) and takes €100 from you and gives €99 of it to me (and keeps €1).


  [4] The lower bound is that they take it and lend it to the Federal Reserve, which is called “narrow banking” and basically as good as keeping it in envelopes, but which is   strongly disfavored by US authorities.


  [5] I want to be careful to say that I am not an expert on Coinbase’s business models and do not want to, like, endorse it. Don’t go put all your money in Coinbase because I said so or anything! And in fact Coinbase does have other revenue models besides charging trading fees, some of which are more run-vulnerable than what I say in the text. (Most notably, there *are* loan products. “We provide retail and commercial loans to qualified customers secured by their crypto asset holdings on our platform, which exposes us to the risk of our borrowers’ inability to repay such loans,” says a risk factor in  Coinbase’s Form 10-K.) But Coinbase’s claims this week, and its securities filings, suggest that the dominant business model is boringly segregating customer money and charging fees.


  [6] Well, I can, using futures, but futures are just a synthetic form of the leveraged transaction in the text. If I short Bitcoin at $20,000 via futures and put up $4,000 of collateral, that is a leveraged trade; if Bitcoin goes above $24,000 then my collateral is gone. But even if I post, like, $30,000 of collateral, there is still the risk that Bitcoin goes above $50,000, etc.


  [7] As a legal/contractual matter, you may or may not have “recourse” against her — you may or may not be able to sue her for the extra money— but as a practical matter you are a crypto exchange, don’t count on getting that money back.


  [8] In modern US stock markets, buybacks are the principal way of returning profits to shareholders, meaning that the connection between stock prices and corporate profits is in practice “when there are profits the company buys back stock” — just like with FTT.


  [9] They’ll probably lend you like $100 against $200 of their stock, in an ordinary-course transaction; they just won’t do too much of it.











            Follow Us













              Get the newsletter



























Like getting this newsletter?
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022


















<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23chngxi.5hxa/5620d242.gif" alt="" border="0" /></a>
