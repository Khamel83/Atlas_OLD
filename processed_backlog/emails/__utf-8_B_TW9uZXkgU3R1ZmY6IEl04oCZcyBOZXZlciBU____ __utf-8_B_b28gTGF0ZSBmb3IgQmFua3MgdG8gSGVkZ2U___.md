# =?utf-8?B?TW9uZXkgU3R1ZmY6IEl04oCZcyBOZXZlciBU?=
 =?utf-8?B?b28gTGF0ZSBmb3IgQmFua3MgdG8gSGVkZ2U=?=

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Tue, 9 May 2023 13:49:53 -0400 (EDT)
**Source:** inputs/saved_emails/=utf-8BTW9uZXkgU3R1ZmY6IEl04oCZcyBOZXZlciBU=
 =utf-8Bb28gTGF0ZSBmb3IgQmFua3MgdG8gSGVkZ2U==_Tue,_9_May_2023_13-49-53_-0400_(EDT)_18801a33a12188db.eml
**Processed:** 2025-08-24T19:13:12.881232














        One question people have asked is: Why didn’t Silicon Valley Bank hedge its interest-rate risk? SVB, like other regional banks, got a lot of





































      Interest-rate hedging



One question people have asked is: Why didn’t Silicon Valley Bank hedge its interest-rate risk? SVB, like other regional banks, got a lot of deposits and invested them in long-term US government and agency bonds with fixed interest rates. As interest rates went up, those bonds lost value, eating through all of SVB’s equity. This was bad, people noticed, they withdrew their deposits, and SVB ran out of money. This was all pretty predictable, or at least a known risk. Why didn’t SVB hedge?
We have talked about a couple of answers to that question:
	SVB had expenses, and it needed to make money. It had to invest its depositors’ cash to make that money. In 2022, if it had been earning short-term interest rates on that cash, it would not have made enough money to cover its expenses.   The way that it made money was by investing at long-term interest rates, which were higher.
  [1]
 So it invested in long-term bonds, earned higher rates, and made enough money. “Hedging” would have meant swapping its long-term rates to short-term rates, which would have defeated its main purpose, making money. And in fact SVB did have some interest-rate hedges in place in early 2022; it took them off, though, to increase its profits. 	SVB thought that it was hedged: It was buying long-term bonds, yes, but it was funding those purchases with deposits. Those deposits are technically very short-term: Depositors could take their money back at any time, and eventually they did. But   it is traditional in banking to think of them as long-term, to think that the “deposit franchise” and the deep relationship between banker and customer would make customers unlikely to take their money out. SVB invested a lot in good customer service and good relations with its depositors; it also made loans to startups that required them to keep their cash on deposit at SVB. So it figured it had pretty long-term funding, and it matched that long-term funding with long-term assets. If it had swapped the assets to short-term rates, and then rates fell, it would lose money, and SVB thought that was the bigger risk. When SVB got rid of its interest-rate hedges in early 2022,  it did so because it had become “increasingly concerned with decreasing [net interest income] if rates were to decrease”: It worried that the hedges would hurt it if rates fell.

Those are, I think, the main answers. But there is one other sort of dumb accounting answer. Most of SVB’s interest-rate risk came in its portfolio of “held to maturity” bonds. The idea here is that SVB bought a lot of bonds and planned to hold them until they matured. If it did that, the bonds — which were mostly US-government backed and so very safe — would pay back 100 cents on the dollar. So SVB didn’t need to worry about mark-to-market fluctuations in their value. If interest rates went up, and the value of these bonds dropped from 100 to 85 cents on the dollar, SVB could ignore it, because the value would definitely go back up to 100, as long as it held the bonds to maturity. (The problem is that it couldn’t: There was a run on the bank long before the bonds matured.) 
This is a standard assumption in banking, that the bank is making loans or buying bonds and planning to hold them for life, so fluctuations in their market values don’t matter. And   bank accounting reflects this: Held-to-maturity bonds are held on the balance sheet at their cost, and fluctuations in their market values do not affect the bank’s balance sheet, or its income statement, or its regulatory capital. And thus for a while last year SVB was mark-to-market insolvent — if you subtracted its liabilities from the market value of its assets, you got a negative number — but its regulatory capital was fine, because regulatory capital doesn’t subtract that way.
But now add hedging. SVB had, call it, $120 billion of held-to-maturity bonds. When rates went up, they lost something like $15 billion of market value.
  [2]
 If SVB had fully hedged those bonds — if it had put on $120 billion notional amount of swaps, say — then the hedges would have perfectly offset that loss. But if rates had instead gone down, the hedges would have lost money. Obviously last year rates probably had more room to rise than to fall, but even a 0.25% decline in long-term interest rates could have cost SVB something like $2 billion in this scenario.
  [3]

Of course in that scenario its bonds would have gained $2 billion of market value, offsetting the loss on the hedges. But this is where the accounting is a problem. If you have a held-to-maturity bond, its fluctuations in value do not affect your income statement or balance sheet: When the market price of the bond goes up (or down), the book value of your assets does not go up (or down), and you do not have income (or loss) from the change. But if you have an interest-rate swap, its fluctuations in value do affect your income statement and balance sheet: When its market value goes up (or down), the book value of your assets goes up (or down), and you have income (or loss). An interest-rate derivative is sort of naturally a mark-to-market asset, and so changes in its value are reflected in income.
And so if SVB had hedged and rates had gone down, it would have reported a huge loss: A $2 billion loss on interest-rate derivatives would have wiped out more than all of  SVB’s profit last year. Hedging the held-to-maturity bond portfolio would have made SVB economically less risky, but it would have made its reported financial results far more volatile. The hedge would have made SVB look riskier. And banking is a business of confidence, so you don’t want to look riskier. (Also: The hedge would have made SVB’s regulatory capital more volatile, and banking is also a business of regulatory capital.)
Now, an obvious response is: “This is dumb, why should hedging make you look riskier?” And accountants are aware of that, and there is a thing called “hedge accounting” where you basically get to take some asset and the derivative that you use to hedge it, offset them against each other, and neutralize the accounting effect of fluctuations in their values. The hedge makes your financial statements look less risky, which makes sense.
The problem is that this is specifically not allowed for held-to-maturity assets.  PricewaterhouseCoopers explains:
The notion of hedging the interest rate risk in a security classified as held to maturity is inconsistent with the held-to-maturity classification under ASC 320,
  [4]
 which requires the reporting entity to hold the security until maturity regardless of changes in market interest rates. For this reason, ASC 815-20-25-43(c)(2) indicates that interest rate risk may not be the hedged risk in a fair value hedge of held-to-maturity debt securities. 
Again, here the accounting standards line up with the way banks have historically thought about themselves, which is basically that they are in the business of holding long-term assets for the long term. “Why would a bank hedge interest-rate risk on its held-to-maturity portfolio,” the accountants ask, “if it is just going to hold that portfolio to maturity?”
That said, you can hedge your bonds that you treat as “available-for-sale,” and if you do that you will get hedge accounting treatment, so your income statement (and capital) will look less volatile rather than more. (This is  what SVB was doing when it did have interest-rate hedges in place last year.) And if you are a US bank in spring of 2023, you will be keenly focused on the risk of rising interest rates, perhaps more keenly focused than you were back when interest rates were about to rise rapidly. Never too late I guess. Bloomberg’s Annie Massa reports:

Charles Schwab Corp. started using derivatives to hedge interest rate-related risk during the first quarter.
The derivatives had a notional value of $3.9 billion as of March 31, the Westlake, Texas-based company said in a regulatory filing Monday. 
Schwab, which runs both brokerage and bank businesses, has been ensnared in the tumult ravaging US regional banks after the Federal Reserve embarked on its most aggressive interest rate tightening cycle in decades last year. 
The firm confronted swelling paper losses on securities it owns and grappled with dwindling deposits as customers moved cash into accounts that earn more interest. Schwab executives have said those withdrawals will abate. The pace of cash withdrawals is already starting to slow, Chief Financial Officer Peter Crawford said in a recent statement.

It has $3.9 billion of swaps to  hedge $3.9 billion of available-for-sale securities, out of a total of about $141 billion of available-for-sale and $170 billion of held-to-maturity securities. 





























      Elsewhere in banks and interest-rate risk



We have   talked a few   times recently about two theories of banking, which I have boringly called Theory 1 and Theory 2. Theory 1 is a mark-to-market, legalistic approach: A bank uses short-term deposits to fund long-term assets, which makes it risky and fragile and particularly at risk from rising interest rates, which increase its cost of funding and decrease the value of its assets.
Theory 2 is a traditional, relationship-driven approach: A bank has a “deposit franchise” of long-term loyal customers, which gives it long-term rate-insensitive funding to invest in long-term assets, and it is at risk from falling interest rates, which decrease the amount of net interest margin it can earn on its assets. The problem, I have suggested, is that banks (and regulators) have traditionally thought in a Theory 2 sort of way, and modern financial markets, and the Fed’s rapid interest-rate increases, seem to have put us in a Theory 1 world.
In discussing Theory 2 I have sometimes cited a 2021 paper by Itamar Drechsler, Alexi Savov and Philipp Schnabl titled “Banking on Deposits: Maturity Transformation without Interest Rate Risk.” The abstract:
We show that maturity transformation does not expose banks to interest rate risk—it hedges it. The reason is the deposit franchise, which allows banks to pay deposit rates that are low and insensitive to market interest rates. Hedging the deposit franchise requires banks to earn income that is also insensitive, that is, to lend long term at fixed rates. As predicted by this theory, we show that banks closely match the interest rate sensitivities of their interest income and expense, and that this insulates their equity from interest rate shocks. Our results explain why banks supply long-term credit.
This is what I meant when I said, above, that SVB thought its interest-rate risk was hedged, and that its bigger risk was declining earnings if interest rates fell. If your deposits are insensitive to changes in short-term interest rates — because your long-term, loyal, relationship-driven customers are not checking the rate on their checking account every day — then you don’t want your assets to be very sensitive to rates (you don’t want to have very short-term investments), because then your income will be very volatile. Investing your sort-of-long-term deposits in actually-long-term assets is a way to reduce risk.
That’s the theory, Theory 2, but obviously things have not been working out that way recently. Drechsler, Savov and Schnabl have a new paper with Olivier Wang, titled “Banking on Uninsured Deposits.” The abstract:
Motivated by the regional bank crisis of 2023, we model the impact of interest rates on the liquidity risk of banks. Prior work shows that banks hedge the interest rate risk of their assets with their deposit franchise: when interest rates rise, the value of the assets falls but the value of the deposit franchise rises. Yet the deposit franchise is only valuable if depositors remain in the bank. This creates run incentives for uninsured depositors. We show that a run equilibrium is absent at low interest rates but appears when rates rise because the deposit franchise comes to dominate the value of the bank. The liquidity risk of the bank thus increases with interest rates. We provide a formula for the bank’s optimal risk management policy. The bank should act as if its deposit rate is more sensitive to market rates than it really is, i.e., as if its “deposit beta” is higher. This leads the bank to shrink the duration of its assets. Shortening duration has a downside, however: it exposes the bank to insolvency if interest rates fall. The bank thus faces a dilemma: it cannot simultaneously hedge its interest rate risk and liquidity risk exposures. The dilemma disappears only if uninsured deposits do not contribute to the deposit franchise (if they have a deposit beta of one). The recent growth of low-beta uninsured checking and savings accounts thus poses stability risks to banks. The risks increase with interest rates and are amplified by other exposures such as credit risk. We show how they can be addressed with an optimal capital requirement that rises with interest rates.
The new paper summarizes the previous paper, and Theory 2 generally:
Following Drechsler et al. (2021), we model a bank with a low “deposit beta” – a low sensitivity of deposit rates to the market interest rate. The bank then earns a deposit spread that rises with the interest rate. This is the source of its deposit franchise. The deposit franchise does not come for free: the bank pays an operating cost to maintain it. The deposit franchise is effectively an interest rate swap in which the bank pays fixed (the operating cost) and receives floating (the deposit spread). This swap has negative duration. The bank hedges it by investing in assets with positive duration; by holding long-term loans and securities.
But they add an increased likelihood of interest-rate-driven deposit outflows, and also the risk of runs by uninsured depositors:
The second reason for outflows is a run by uninsured depositors. Uninsured depositors have an incentive to run if the value of their claims exceeds the value of the bank if they do run. In standard models (Diamond and Dybvig, 1983) this is due to fire sales of the bank’s loans. There are no such fire sales in our model; the bank’s assets are fully liquid. Runs are instead due to the nature of the deposit franchise. When a deposit is withdrawn, the bank loses the stream of deposit spreads net of operating costs it would have earned on that deposit. In effect, the deposit franchise is subject to an extreme form of “fire sale”: its value is fully destroyed in a run. Moreover, since its value is increasing in interest rates, a run is more destructive – and hence more likely – at high interest rates.
This is sort of what you saw in the recent bank runs: Regional banks had financial assets (loans, bonds) whose market value fell due to rising interest rates until it was slightly less than their liabilities. On traditional banking theory, that’s survivable: The deposit franchise is itself valuable, and the combined value of the financial assets and the deposit franchise ought to have exceeded the liabilities, so the banks were solvent and valuable. But in practice the value of the deposit franchise evaporated overnight, leaving only a pile of financial assets that had lost value, funded by a bunch of short-term loans that came due.



      Narrow banking/shadow banking



Along these lines, I   wrote yesterday that the main risk of banking comes not from its assets (bonds, loans) but from its liabilities: If you fund your business with short-term loans (deposits) that can be withdrawn at any time, but you assume that your relationships with your lenders (depositors) are so good that they would never withdraw their money, you are liable to get in trouble. And we have talked about the possibility that, in a mark-to-market, no-relationships, Theory 1 sort of world, that funding model for banks wouldn’t work, or at least would become less popular. There is a set of ideas called “narrow banking” or the “Chicago plan,” in which:
	Deposits would not be used to fund loans or other long-term assets, but would just be parked at the Federal Reserve: Banking would be fully reserved, bank accounts would just be dollars, and they would not be used to make loans.	Loans would be equity-funded: People who wanted to take credit (or interest-rate) risk would invest their money in funds, and the funds would make loans (or buy bonds). But the investors in those funds would not be information-insensitive bank depositors who expected access to their money at any time; they would be conscious risk-takers. They would know what they were getting into: They would lock up their money for a long time and understand that they were taking the risk of any loan losses. Loans would effectively come from loan mutual funds, not from banks.

I   have suggested that some of this is really happening now. For one thing, a lot of US money market funds   kind of look like narrow banks (they just park money at the Fed’s reverse repo program), while there has been a huge rise in private credit funds that are equity-funded lenders, and that are displacing banks in some lending markets.
We talked yesterday about a  DealBook story about the rise of private credit, which worried that private credit funds are “not subject to the same regulations as banks, which allows them to take greater risks.” I thought that was the wrong thing to worry about; I wrote:
A private credit firm that raises money from investors in a locked-up fund, and uses that money to make idiotic loans that all go bust, is less risky than, well, a licensed bank that raises money from uninsured depositors and uses that money to buy safe US-government-backed bonds, like Silicon Valley Bank did.
That said, I added: “Though: A private credit fund that leverages its fund with short-term borrowing is riskier, more run-prone, more like a bank.” You could imagine private credit being very safe, very Chicago-plan, just taking long-term equity investments from people who want to take risks. But financial markets love leverage, and if you have a $1 billion loan fund, you might go to someone — say, a bank — and say “hey I have $1 billion of equity, lend me another $1 billion and I’ll go make $2 billion of loans with the money.” And then — if the money you borrowed from the bank is short-term or subject to margin calls — you have reintroduced a lot of the fragility of banking.
The details matter, though. A good, conservative, well-run bank might well fund $2 billion of long-term loans with $200 million of equity and $1.8 billion of short-term borrowing (deposits), which is just a lot more fragile than a private credit fund funding them with $1 billion of equity and $1 billion of borrowing. Even if the bank is making safer and more conservative loans than the private credit fund, it might be more fragile.
Anyway also yesterday the Fed released its  Financial Stability Report, and it directly discusses the financial-stability risks of private credit funds. The Fed, like me, is not that worried:

Since the 2007–09 financial crisis, private credit funds have experienced substantial growth, as the privately negotiated loans that they extend have become an increasingly important source of credit for some businesses, particularly middle-market companies. As of 2021:Q4, their assets under management (AUM) stood at $1 trillion, and the estimated “dry powder” (committed but uncalled capital) amounted to $228 billion (figure A). …
Investors in private credit funds are diversified institutional investors and high-net-worth individuals (figure B). Based on Form PF, as of 2021:Q4, public and private pension funds held about 31 percent ($307 billion) of aggregate private credit fund assets. Other private funds made up the second-largest cohort of investors at 14 percent ($136 billion) of assets, while insurance companies and individual investors each had about 9 percent ($92 billion). Given the rapid growth of private credit funds, these investors are increasingly indirectly exposed to the liquidity and credit risks of assets in private credit fund portfolios. 
Financial stability risks associated with investor redemptions from private credit funds appear low. Most private credit funds have a closed-end fund structure and typically lock up the capital of their investors (that is, limited partners) for 5 to 10 years. Those funds that are structured as hedge funds routinely restrict share redemptions of their investors through redemption notice periods, lockups, and gates. Thus, private credit funds engage in limited liquidity and maturity transformation. …
Risks to financial stability from leverage at private credit funds appear low. Indeed, most private credit funds are unlevered, with no borrowings or derivative exposures. A minority of funds, however, use modest amounts of financial or synthetic leverage. Figure C shows that the most levered funds (those at the 95th percentile) have borrowings-to-assets ratios of about 1.27 and derivatives-to-assets ratios of about 0.66. In the aggregate, private credit funds borrowed about $200 billion in 2021:Q4, mainly from U.S. financial institutions, and held about $200 billion of derivative gross notional exposure. Risks to lenders of private credit funds, typically banks, appear moderate due to the relatively modest amount of borrowings of private credit funds and their secured nature.
Overall, the financial stability vulnerabilities posed by private credit funds appear limited. Most private credit funds use little leverage and have low redemption risks, making it unlikely that these funds would amplify market stress through asset sales.

Are private credit funds making worse loans than banks are? Just the wrong question to ask! The right question is “can there be a run on private credit funds,” and the answer, so far, is “mostly no.”



      Active passive management



Bloomberg’s Ye Xie and Liz McCormick have sort of   a funny profile of Josh Barrickman, who runs Vanguard Group Inc.’s Americas bond indexing business. You might think that the guy running $1 trillion of bond index funds would not have to make a lot of decisions — “just buy the index” — but in fact the way you run a bond index fund is not by buying all the bonds in the index: There are too many, and many of them don’t trade that much. Instead you buy a lot of the bonds in the index, try to get a representative sample, try to track the index, and end up making a lot of decisions. You are in some sense much less active than an active bond manager, but on the other hand you run $1 trillion and they don’t:

That makes Barrickman exhibit A of a passive management revolution that’s reshaping the world of fixed-income, just as it did equities a decade ago. No longer dominated by traders making multimillion-dollar bets and eating what they kill, the real money is flowing to guys like him, whose decisions are increasingly rippling through markets.
“We do have size and scale, and that matters in the marketplace,” Barrickman said in an interview. “Tracking is job one, two and three,” he said, adding “if we can have a basis point a year, that’s a lot of real money.” …
Barrickman himself now oversees three of the world’s four largest bond funds, including the $298 billion Vanguard Total Bond Market Index Fund, according to data compiled by Bloomberg.
That means many of the decisions he makes, like which bonds to buy when trying to replicate his funds’ underlying benchmarks, can have big consequences for the market (the Vanguard Total International Bond Index Fund, for example, only holds roughly half the 13,000 bonds in the index it tracks.)
“We have to be, by definition, overweight some places and underweight others to build a sample,” Barrickman said. “We’re dealing in a market that forces us to take some active positions.”

If you run $1 trillion of indexed bond money and capture one basis point a year with your active decisionmaking, that’s $100 million of alpha. 



      Shaq is hiding from an FTX lawsuit



Sure   whatever:

Shaquille O’Neal is calling foul on the lawyers who chased him for months to serve a lawsuit accusing the basketball legend of duping investors in FTX crypto exchange.
Chucking legal documents at the front of O’Neal’s car as he drove quickly through the gates of his Georgia home doesn’t count as properly serving a lawsuit, his attorneys say.
The seven foot-one inch former Los Angeles Lakers star and NBA commentator known as Shaq is among numerous celebrities targeted in a suit claiming they funneled investors into a Ponzi scheme by promoting FTX’s unregistered securities.
O’Neal stood as a holdout among the group for not acknowledging receipt of the complaint despite what plaintiffs’ lawyers said were dozens of attempts to present it to him at known residences in Georgia and Texas and elsewhere, according to court filings. 

Seems like a blockchain could fix this.



      Things happen



PacWest, Western Alliance Slide as   Regional Bank Stocks Fall.  Betting Against Banks Brings Reward and Backlash. Regional Banks Will   Cut Bonuses While Big Firms Raise Incentive Pay. US lenders warned that  commercial property is ‘next shoe to drop.’ Concern Over TD  Anti-Money-Laundering Practices Helped Scuttle First Horizon Deal. Goldman to Pay $215 Million to End Case on   Underpaying Women. UBS to   Overhaul Board After Credit Suisse Deal. “Zoltan Pozsar, a widely followed Credit Suisse  markets guru, has left the bank.” Tempur Sealy to   Buy Mattress Firm for About $4 Billion. The  Supreme Court Case That Could Threaten the SEC’s Climate-Disclosure Rule. High-Tech Banks Grapple With a Rise in Old-Fashioned Crime:  Check Fraud. Ireland to propose creation of  sovereign wealth fund. Sri Lanka’s Creditors Hold Inaugural Debt Meet as China Observes. Why  Flossbar/Medbar Failed & What We Learned Along the Way. FTX Founder Sam Bankman-Fried  Seeks Dismissal of Criminal Charges. JPMorgan Ordered to   Pay Javice's Lawyers While They Sue Her. Spotify ejects thousands of AI-made songs in  purge of fake streams.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!

  [1] Another way to make money would have been to take less duration risk and more credit risk: to make, say, floating-rate loans to businesses. But SVB’s customer base
made that harder: In 2022, startups and VCs were flush with cash, so they parked a lot of deposits with SVB and didn’t need many loans. SVB couldn’t take credit risk to earn money, so it took duration risk.


  [2] In super rough numbers, SVB’s portfolio had a duration of about 6 years, the 10-year Treasury rate went up by about 2 percentage points from early 2022 through early 2023, so its $120 billion portfolio lost $120bn x 6 x 2% = $14.4 billion or so of value. This is not really right, but it’s the rough intuition.


  [3] See my fake math in the footnote above. Six years duration, $120bn notional, 0.25% move, $1.8 billion loss.


  [4] “ASC” stands for “Accounting Standards Codification,” and is the way the US Financial Accounting Standards Board codifies US generally accepted accounting principles.











            Follow Us













              Get the newsletter


















Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.








           You received this message because you are subscribed to Bloomberg's Matt Levine's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022







<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23ciplk5.5n9o/e3758b4d.gif" alt="" border="0" /></a>
