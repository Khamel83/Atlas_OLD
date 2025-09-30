# Money Stuff: People Are Worried About the Basis Trade

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Thu, 14 Sep 2023 14:00:58 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff People Are Worried About the Basis Trade_Thu,_14_Sep_2023_14-00-58_-0400_(EDT)_18a94da938c7c15a.eml
**Processed:** 2025-08-24T19:13:05.145572














        Programming note: Money Stuff will be off tomorrow, back on Monday.A simple model of US Treasury bonds%3Cp%3EBoringly%2010-year%20Treasuries


































          Programming note: Money Stuff will be off tomorrow, back on Monday.



      Basis trade



A simple model of US Treasury bonds
  [1]
 could go something like:
	The US government borrows a lot of money and has a very long time horizon, so it wants to borrow a lot of money for terms of 10 or 20 or 30 years.	Lots of asset owners — pension funds, university endowments, people saving for retirement — also have a long time horizon and want to earn a safe return, so they want to lend the government money for terms of 10 or 20 or 30 years.

This is a nice and simple story. Pensions have long-dated liabilities (future pension payments), so they buy long-dated assets (long-term Treasuries) to match them, which means that they can buy Treasury bonds for long periods and hold them until they mature.
It is not a perfect story. If you run a pension fund, you probably do not just buy long-term Treasuries to cover your future liabilities. Treasuries are very safe assets, which means they don’t pay that much, and you want to get paid more. You probably invest in other stuff — “credit,” corporate bonds and private credit and asset-backed securities — to earn a bit more yield.
Much of this credit stuff, though, has shorter terms than 30 years; there is not that much 30-year corporate borrowing. If you buy a lot of seven-year corporate bonds, and you have very long-dated liabilities, there will be a mismatch. You are taking a lot of interest-rate risk: Sure those bonds pay a lot of interest now, but they mature in seven years, and if interest rates are lower in seven years you will earn less interest. If your liabilities are long term, you want to earn a lot of interest over the whole term. You want the duration of your assets to match the duration of your liabilities.
So you buy more duration with Treasury futures. Treasury futures are synthetic contracts that give you the interest-rate exposure of Treasury bonds but without putting up much cash upfront. You put up about  $3,900 and get economic exposure to $100,000 of Treasury bonds: If long-term Treasury prices go up by 1%, you make $1,000 on your initial $3,900. If interest rates go down, the price of Treasury bonds will go up, and you will make money, which will compensate you for your reduced future interest earnings.
This is a more nuanced story of what pension funds and other long-term asset managers do.
  [2]
 But our original simple story described a whole trade: Pensions bought Treasuries, and the government sold them, and the trade made sense for both of them. Now we have a trade that makes sense for pension funds, but who is on the other side? The government is not selling them Treasury futures.
  [3]
 
Instead, you need some intermediary to provide the service of transforming Treasuries (sold by the government) into Treasury futures (bought by pension funds). This service is called the “basis trade,” and the intermediaries are usually hedge funds and proprietary trading firms.
  [4]
 Here is a Wall Street Journal article about the basis trade, which has caused problems in recent years and is now making a comeback:

A popular way for hedge funds to profit from bond trading while minimizing their exposure to swings in the market, the basis trade exploits the price difference between Treasurys and Treasury futures. The resurgence is attracting fresh scrutiny from Wall Street because previous meltdowns have rattled global markets. ...
Hedge funds buy Treasurys, then bet against Treasury futures by selling contracts promising delivery of a bond on a specific date at a preset price. Instead of betting on the direction of bond markets, the trade seeks to take advantage of small differences in the securities’ prices. 
The trade works because large asset managers like pension funds often prefer buying Treasury futures that require less up-front cash than actual bonds. That tends to make the contracts slightly more expensive than the bonds, creating a window for speculators to take advantage.
  [5]
 Futures prices typically converge toward bond prices as their settlement date approaches.
The differences are small, so hedge funds juice returns by borrowing from big banks in the overnight funding markets—often putting little, if any, cash up front. Leverage can reach extreme levels: Hedge funds had more than $550 billion of Treasury trades at the end of last year backed by just $10 billion of their own money, Fed research found. 

The obvious objection is that if you have $550 billion of Treasuries backed by $10 billion of your own money, and the value of Treasuries drops by 2%, then all of your money is gone, you have to dump Treasuries, everyone else is dumping them at the same time and there is a crisis. This is an exaggeration, because if the value of Treasuries drops by 2% then probably you made 2% on your futures and you’re more or less fine, but still there is not a ton of margin for error, and mistakes have been made:

The basis trade had been subdued since a dash for cash in March 2020 forced hedge funds to rapidly unwind their positions, straining the market for Treasurys — meant to be the world’s easiest investment to buy and sell. …
During the 2020 Covid market crash, hedge funds’ unwinding of leveraged strategies including the basis trade spilled across markets, helping send the Dow Jones Industrial Average to its worst losses since 1987 and forcing the Fed to step in.

But now it is back:

The Fed’s fight against inflation and the U.S. government’s wave of borrowing reignited the trade, analysts say. Higher yields and worries about a recession have asset managers scooping up long-term bond futures. …
Given those uncertainties and with a potential recession up in the air, “it’s natural to see record hedging in the Treasury market,” said Agha Mirza, global head of rates and OTC products at CME Group.

If you are a pension fund, the 10-year Treasury is at a high-relative-to-recent-history 4.25%, and you worry it will go back down if there is a recession, then you will want to lock in a lot of that rate while earning more today on corporate credit. So you will load up on Treasury futures. And someone will sell them to you.
But you are a pension fund. The people selling you these futures are not. You have a long time horizon. They are doing this as a trade. They are in the business of buying a ton of Treasuries and selling a ton of Treasury futures when there is demand for the futures, and not doing that when there isn’t. They don’t have a giant pot of long-term locked-up pension money to buy Treasuries with. They have a little bit of their own cash ($10 billion), and a lot of borrowed money ($540 billion), to buy the Treasuries that they transform into futures.
So there is another intermediary here: When pensions are buying Treasury futures, they are buying them from hedge funds and prop trading firms that own the underlying raw materials (Treasuries) used to manufacture the futures. But those hedge funds need another raw material: the cash they use to buy the Treasuries. That money is mostly borrowed, in the repo market, where the hedge funds put up their Treasuries as collateral for short-term cash loans from banks and money-market funds and other investors looking to park cash somewhere safe for the short term. 
Again, our simple model at the beginning was that long-time-horizon pension funds buy and hold long-term bonds from the long-time-horizon government. The more accurate model is:
	The long-time-horizon government sells long-term bonds.	Those bonds are bought by short-time-horizon hedge funds using borrowed money.	The money is borrowed from short-time-horizon repo lenders.	The hedge funds use the bonds to manufacture Treasury futures, which they sell to long-time-horizon pension funds.

It all kinda works! The beginning makes sense, and the end makes sense, and the middle is efficient. It lets the pension funds be nimbler with their cash and lend to real businesses and get higher yields. But that efficiency comes with risk. The long-time-horizon government and the long-time-horizon pensions don’t really have to care about market movements; if they dealt with each other directly, they could just do the trade once and wait for it to mature 30 years later. Once you introduce highly leveraged short-term intermediaries, market movements can blow up the trade and lead to margin calls and forced selling.
We  talked last year about “liability-driven investment” at UK pension funds, which led to a brief meltdown in the gilt (UK government bond) market. The story there is different, but it has similar features: Pension funds, rather than matching their liabilities with long-dated gilts, bought things with higher returns and hedged their interest-rate risk with derivatives. This meant that if interest rates moved, the pensions got margin calls and could get blown up. I wrote:

This all makes total sense, in its way. But notice that you now have borrowed short-term money to buy volatile financial assets. The thing that was so good about pension funds — their structural long-termism, the fact that you can’t have a run on a pension fund: You’ve ruined that! Now, if interest rates go up (gilts go down), your bank will call you up and say “you used our money to buy assets, and the assets went down, so you need to give us some money back.” And then you have to sell a bunch of your assets — the gilts and stocks that you own — to pay off those margin calls. Through the magic of derivatives you have transformed your safe boring long-term pension fund into a risky leveraged vehicle that could get blown up by market moves.
I know this is bad but I find something aesthetically beautiful about it. If you have a pot of money that is immune to bank runs, over time, modern finance will find a way to make it vulnerable to bank runs. That is an emergent property of modern finance. No one sits down and says “let’s make pension funds vulnerable to bank runs!” Finance, as an abstract entity, just sort of does that on its own.

Finance really does do that! 
But this is not just finance being a clever little scamp; there is something essential about it. Last week, Lev Menand and Josh Younger published a fantastic paper titled “Money and the Public Debt: Treasury Market Liquidity as a Legal Phenomenon.” Alexandra Scaggs wrote about it  at FT Alphaville, and Adam Tooze discussed it in  his newsletter, and I cannot really do justice to everything that is in it, but it is a good thing to read if you are thinking about the basis trade.
  [6]

It is basically a history of the US Treasury market from the perspective of how Treasuries are turned into money. The very simple story of Treasuries is “the government wants to borrow long-term, some people want to lend long-term, and they get matched up.” But that story has never been completely true: Treasuries are not just a long-term investment for pension funds and retirement savers; they are also the preeminent safe asset, which means that a lot of people who own Treasuries will have occasion to sell them to raise cash. There needs to be a buyer: When everyone wants to sell Treasuries for cash, there needs to be someone who can quickly come up with a lot of cash to buy all the Treasuries. Menand and Younger write:
The high degree of convertibility between Treasury securities and cash — the market’s “liquidity” — depends upon entities that can create new, money-like claims to buy Treasuries. Sometimes the government’s central bank has issued these claims directly, as in March 2020; other times these claims were issued by central bank-backed instrumentalities, such as banks and select broker-dealers. 
Who can “create new, money-like claims” to quickly buy any Treasury supply? The most obvious answer is “the central bank”: The Federal Reserve (1) creates dollars and (2) buys Treasuries, so it is a natural supplier of Treasury liquidity. But that is sort of a disfavored answer: Everyone understands that it is bad for a government to finance itself by printing money (it’s inflationary), so a system in which the Treasury sold all of its bonds directly to the Fed for newly created dollars would be bad.
But Menand and Younger argue “that American public finance has long been closely intertwined with the American monetary framework,” and they trace the history of (1) who could issue “money-like claims” to buy Treasuries and (2) how the government and the Fed supported those buyers and markets. The history has four parts:
	The national banking system, in which Congress chartered national banks to print money and use the money to buy Treasuries; here, “fiscal-monetary entanglement was relatively transparent.”	The Federal Reserve system, in which the Fed printed the actual dollars, while banks issued deposits (money-like claims) and, for some time, used a lot of the money to buy Treasuries.	The primary dealer system, in which banks stopped buying so many Treasuries, but primary dealers (investment banks) bought Treasuries and funded them in the repo market. Repo, Menand and Younger argue, is a money-like claim, a short-term safe place for cash investors to park their money, and it was created and supported by the Fed to allow primary dealers to efficiently provide liquidity for Treasuries.	The current system: After 2008, the primary dealer system atrophied (many big dealers became banks), and now Treasury liquidity comes from a combination of (1) actual banks, which can   fund Treasuries by issuing deposits, and (2) hedge funds, prop trading firms and other not-quite-primary-dealers that use the repo market to finance their Treasury trades.

In all of the later configurations, the Fed sits somewhere behind the market: When things go wrong, the Fed supports whoever (banks, primary dealers, now hedge funds) provides Treasury liquidity. They write:
Subsequent changes to market structure pushed substantial Treasury dealing further beyond the bank regulatory perimeter, leaving public finance increasingly dependent on high-frequency traders and hedge funds — “shadow dealers.” The near-money issued by these intermediaries proved highly unstable in 2020. Policy makers are now focused on reforming Treasury market structure so that Treasuries remain the world’s most liquid asset class. Successful reform likely requires a legal framework that, among other things, supports elastic intermediation capacity through balance sheets that can expand and contract as needed to meet market needs.
Treasuries can never be a pure long-term buy-and-hold investment for everyone; somebody needs to be ready to buy and sell them. That somebody will need short-term funding, and that short-term funding will create risks, and the Fed will have to stand behind the market to sort out those risks.





























      Arm IPO



The standard mechanism of the initial public offering is:
	A company hires some banks to sell some shares to the public for the first time.	The banks and company get together and come up with some estimate of value and then go out and market the shares at some price range based around that estimate.	They go out to investors, pitch the company, and get orders at different prices.	The goal is to be “oversubscribed,” to have orders for many more shares than they are selling, so that there is demand for the shares once they start trading. The bankers want some investors not to get the shares that they asked for, so that they have to go out and buy them in the market the next day, so that the investors who did get shares have someone to sell to. They want a healthy market, with supply and demand.	The banks work for the company (they get paid a fee by the company), but they have mixed loyalties. The investors who buy the shares are also customers of the banks, often big customers who pay the banks a lot of fees and do a lot of trades with the banks. The banks want their corporate client to be happy, but they also want their investor clients to be happy.	This tension is the point of the IPO: Companies hire banks to do IPOs because the banks have relationships with investors, because the banks are in a web of favors and obligations with the investors that they can use to sell the shares. If the banks were not somewhat looking out for the investor clients, they would not be able to effectively sell the corporate client’s shares. “No conflict, no interest.”	Anyway, at the end of the process the banks come to the company and say, like, “we have gotten a lot of good orders, and we are three times oversubscribed at $53 per share, and five times oversubscribed at $52, and 10 times oversubscribed at $51, and 15 times oversubscribed at $50, so let’s price at $51.”	And then the client says “wait you said we have orders to buy three times the shares we are selling at $53 per share, and you want us to sell the shares at $51? Isn’t that leaving a lot of money on the table?”	And then the bankers say “you don’t understand how this works, it is in your long-term interests and also our long-term interests for the stock to trade well, for it to go up after this offering is complete, and so we want to make sure there’s enough demand. It would be a disaster if the stock dropped on the first day. You will be a long-term repeat user of the capital markets, you will come back to investors for money, you will pay your employees in stock, you want the stock to be attractive and trade up; you don’t want to take every last penny today at the expense of long-term investor relationships.”	This advice is basically not wrong, though it probably implies that investors have longer memories than they actually do.	The company is like “fine $51.”	The stock doubles the next day.

Sorry, actually, this was the standard mechanism of IPOs a few years ago, when big “IPO pops” (where the stock doubles the day after the company goes public) were common, which led to companies trying things like   direct listings to leave less money on the table. The standard mechanism of IPOs now is like:
	A company calls some banks about selling some shares to the public for the first time.	The banks are like “ehhh kind of a rough IPO market right now, better wait.”

There is a middle ground; some companies are still going public these days. But the IPO market is still a bit shaky, and everyone is more sensitive about not knocking it over.   For instance:

SoftBank Group Corp. satisfied its ambitions for Arm Holdings Plc by raising $4.87 billion in the year’s biggest initial public offering, while resisting the temptation to try for more.
A smooth trading debut from the chip designer on Thursday could help revive a weak IPO market and provide a boost for upcoming listings from companies like Instacart Inc. and Birkenstock Holding Ltd. At the IPO price, Arm is valued at about $54.5 billion, according to Bloomberg News calculations.
Arm’s offering was oversubscribed more than 10 times, people with knowledge of the matter have said, which means investor interest exceeded supply at the price range of $47 to $51 a share and could help buoy the stock once trading begins.
In setting the price for the IPO, Masayoshi Son, SoftBank’s founder, chairman and chief executive officer, signaled that he was unwilling to push things too far even if it meant leaving a bit of money on the table.
In the final price-setting meeting Wednesday, some bankers and executives made the case for a higher price, with some of the debate centering on whether $52 made sense, people familiar with the matter said, asking not to be identified because the meeting was private. Son joined the discussion and chose $51, saying it wasn’t worth risking a healthy debut for $100 million or so in additional proceeds, they said.

The bankers told him to go with $52 and he said “nah let’s do $51,” the exact opposite of every 2019 IPO. Arm opened for trading today at 12:19 p.m. with   a price of $56.10, then rose a bit in early trading. A nice IPO pop: Up a bit, but not so much that you’re embarrassed about the money you left on the table.
To be fair, it is Masayoshi Son, who is a particularly long-term repeat user of the capital markets. The Financial Times  noted last week:

As well as retaining more than 90 per cent of a company that Son believes will underpin the future of computing, SoftBank will also be able to lean on the newly listed company as a big source of financing. ...
“SoftBank has been wanting to monetise Arm for years,” said Kirk Boodry, an analyst at Astris Advisory. “Arm is a quality asset, with punchy revenues and good margins. They can hold on to and still have the cash to use in other areas — in that respect it’s a perfect replacement for Alibaba.”

If you sell $5 billion of a $54 billion company and keep the other $49 billion so you can borrow against it later to raise cash, you care a lot more about the long-term value of the company than you do about maximizing today’s sale price.
Byrne Hobart also  points out that “Arm has a long list of strategic investors in the chip industry who have committed to taking a stake in the company,” and that “a large chunk of [the shares sold in the IPO] will be locked up by these buyers.” This is probably good for the stock price (a lot of the big investors in the IPO won’t be selling the first day), which means that Son could probably get away with being more aggressive in pricing. On the other hand, it means that if he’s more aggressive in pricing he’s getting more money for SoftBank at the expense of Arm’s strategic customers. Ordinarily in an IPO, the banks have relationships with the investors and want to make the investors happy, but the issuer is less interested in that goal. Here Arm probably has stronger relationships with the investors than the banks do.



      Executive pay accounting



If you are the board of directors of a small ambitious company that intends to disrupt and remake the whatever industry, but has not done so yet, probably the way you should pay your chief executive officer is (1) give her enough cash to pay her rent and (2) promise to make her very rich if the company actually works out. The exact mechanics of that promise are flexible, but one pretty standard approach is:
	Give her a reasonable cash salary; and	Award her a huge slug of stock options, at the beginning of the journey to disrupting and remaking the industry, that will be worth, like, $5 billion if the company ends up being worth $50 billion. But if the company ends up being worth $0, they’ll be worth zero. And if the company just sort of muddles along doing okay but never really disrupts or remakes anything, they will also be worth zero: They will only pay off if the company gets really big. They are a stretch goal, a huge reward for huge success; they are not meant to reward the CEO comfortably for modest success, but to encourage her to take big swings.

This is not the only way to do it, and boards that try to do it this way do not always follow through rigorously. (If the company does okay-but-not-great, but the CEO is doing her best and the board likes her, they might modify her options or give her more so that she still gets rich without real success.) But the appeal of this approach is obvious, grounded in theory, aligned with shareholders and not uncommon. In the state of the world where the CEO gets rich, the shareholder have also gotten rich, which is what the shareholders want.
But the accounting is weird. As a matter of accounting, what happens is that you give the CEO a one-time grant of options whose payout is something like “$5 billion if the company gets to $50 billion and $0 if it stays under $5 billion,” or whatever, and then an accountant throws that into a Black-Scholes calculator and computes that the options have a fair market value, now, of $100 million or whatever, and then you disclose that value as the CEO’s “compensation” for “this year” in your securities filings. And then journalists cheerfully report that your CEO gets “paid” $100 million “per year,” and that she is one of the highest-paid CEOs in the country despite your company being kind of small and not having had much success.
And you say, well, of course we are small and haven’t had much success; the point of the options grant is to change that. The options will cost you $5 billion if the company works out great and $0 if it doesn’t. They didn’t “really” cost you $100 million now, and the CEO certainly didn’t get $100 million now: The calculated fair market value of the options today might be $100 million, but she can’t sell them, and she will never get any value for them unless the company succeeds. The $100 million value is, crudely, the $5 billion value of the options in the success case times the 2% chance of achieving it.
  [7]
 It’s “worth” $100 million in expectation, but 98% of the time it will end up worth zero.
We  talked in July about an article titled “Meet the CEOs Who Pull In More Than $100 Million a Year,” and I made some of these points, particularly about the CEO of “CS Disco, a cloud-services provider that caters to attorneys and [had] a market capitalization of about $500 million.” Giving the CEO of a $500 million company $100 million in annual pay seems odd,
  [8]
 but of course CS Disco didn’t do that. They gave him a big one-time grant of options with a $109 million fair market value, but the options (1) have a strike price of $32 and (2) vest at prices starting at $150 and going up.
  [9]
 The $32 strike price was the company’s initial public offering price, but by the time we talked about it the stock was at $8.40 and, I wrote, “the most likely value of this $109 million pay package is zero dollars.”
There’s an update today:

A big payday doesn’t always keep a chief executive employed.
Just over a year after CS Disco shareholders approved a CEO pay package worth nearly $110 million — one of the biggest of 2022 — the company’s co-founder and chief executive, Kiwi Camara, resigned with little explanation.
His departure, disclosed in a securities filing on Monday, could mean Camara loses the stock options that made up nearly all of the pay package. Camara couldn’t be immediately reached for comment. 
CS Disco shares fell nearly 20% Tuesday following the disclosure. Shares in the company, which provides software used by lawyers, are trading below $8 after going public at $32 in July 2021. …
Under the terms of his employment agreement and equity awards, Camara would forfeit the 4.37 million options he received in May last year if he departed before the company met certain stock-price targets, ranging from $150 to $900 a share. CS Disco hasn’t traded above about $66 a share, a level it last reached in 2021.

Yes, right, he had a deal that would pay him a lot of money if he could get the stock up above $150, and when it became clear that that was not going to happen, he left, leaving behind a pay package that was manifestly worth zero dollars.
  [10]

In some sense that is the disadvantage of paying your CEO like this: If she takes a big swing and misses and the stock falls rather than rising, she will give up, because there is no hope of achieving the milestones that you set for her. But in another, more accurate, sense that’s why you set the milestones! You wanted the company to take a big swing and disrupt its industry, and if it doesn’t work out you don’t want the CEO sitting around comfortably collecting a big check.



      Don’t put it in email



One fact of antitrust law is that if you are an executive at a big company, or at a medium-sized company contemplating a merger, you will think things like “we need to grow our market share” or “we need to grind our competitors into dust,” but if you say stuff like that — particularly, if you say it in writing, in emails or memos or presentations — antitrust regulators might find it and sue to break up your company or stop the merger or whatever, and they will use your words to prove that you are doing anti-competitive things to become a monopoly. This is not intuitively obvious to you at all: You are just a normal competitive businessperson looking to do more business; surely trying to gain market share is good for competition, not bad. But there are forms of words, ways of expressing things, that look bad to antitrust regulators, and there are others that don’t, and most normal people don’t know which are which.
  [11]

Antitrust lawyers do, though, so it is common in mergers for the antitrust lawyers to sit down with their clients and say “here are the words not to use, and here are the words to use instead.” And if you work at a company that gets big enough organically, and that starts looking a little monopolish, at some point it will hire some antitrust lawyers who will also have that talk with everyone. 
But there is a problem, which is that the talk also uses the bad words. The talk itself looks suspicious! If you are going around telling people not to use the bad words, that suggests a guilty conscience; you tell people not to say “crush the competition” because you know that your plans to crush the competition are monopolistic. Or that’s what antitrust regulators will argue. Also  the talk is probably in writing:

Alphabet Inc.’s Google is on trial in Washington DC over US allegations that it illegally maintained a monopoly in the online search business. Executives of the Mountain View, California-based behemoth have known for years that the company’s practices are under a microscope, and have encouraged its employees to avoid creating lasting records of potential problematic conduct, government lawyers allege. …
As far back as 2003, Google managers circulated unambiguous instructions on phrases to avoid to ensure they don’t come across like monopolists.
We “have to be sensitive about antitrust considerations,” Google Chief Economist Hal Varian wrote in a July 2003 memo, unearthed by government lawyers who are suing Alphabet. “We should be careful about what we say in both public and private.”
One phrase to avoid, Varian said: “Cutting off their air supply.” He was referring to a quip used years earlier by then-Microsoft Corp Chief Executive Officer Steve Ballmer, when his company was under federal antitrust scrutiny.
Another no-no, according to a 2009 Varian missive: “Market share.” Instead, when referring to Google’s portion of the search market, use the term “query share.” Penny Chu, the recipient of Varian’s email, responded in the affirmative. “Yes, absolutely.” Such instructions constitute “the one big thing I remember from all that Legal training,” Chu wrote, ending the sentence with a sideways smiley. …
During the trial, [Justice Department lawyer Kenneth] Dintzer pressed Varian on the question of “antitrust training” at Google. When Varian said he couldn’t remember whether he’d taken it, Dintzer tried to jog his memory. “Avoid references to markets or market shares or dominance,” Dintzer said, citing an internal document.

It really is a hard problem to solve. One option is you hire the antitrust lawyers and they walk door to door, visiting every person’s office and having an in-person chat impressing on everyone the importance of using the good words and not the bad words. Maybe the antitrust lawyers, like, dress up in hooded robes and play terrifying sound effects and generally try to put on a memorable theatrical presentation (with nothing in writing!) to scare everyone into remembering not to use the bad words. People are gonna forget, and then you have to remind them, not in writing, never in writing. You show up at their office in the robe again, with a scythe, and you point a bony finger at them and in a booming desolate voice you shout “IT’S QUERY SHARE.” Still, even if you never put it in writing, the regulators could ask about it at trial.
Really this stuff should be taught in college, so that every company can wash its hands of it. The last semester at Wharton everyone should have to take a class called Don’t Put It In Email that is just, like, “we know that when you go out into the world you will occasionally engage in legally ambiguous actions, here are some best practices for not getting in trouble over them, some forms of words and communications methods not to use and some others to use instead.” Then the college is responsible for the “don’t put it in email” instruction, but not for the legally ambiguous actions (Wharton is not starving Google’s competitors of oxygen), while the companies are responsible for the legally ambiguous actions but not for any trainings that look like evidence of a guilty conscience.



      Things happen



How   Sam Bankman-Fried’s Elite Parents Enabled His Crypto Empire. Fund Giants Muscle In on the $1.5 Trillion   Private Credit Party. ‘Almost All Loans Are Bad’ — Why  Banks Aren’t Lending. After $16bn judgment, Burford’s next battle will be  making Argentina pay. Inside Exxon’s Strategy to  Downplay Climate Change. Goldman Sachs Fires Transaction Banking Chief Moorthy, Other Leaders Over   Lapses. Caesars Entertainment   Paid Millions to Hackers in Attack. X   Unlikely to Win Back Advertisers Before Holiday Season. X Corp. Agrees to Try to Settle Lawsuits Over   Mass Layoffs. Is Chainalysis blockchain tracing “  junk science”?  Gemini Earn Users Could Expect Nearly Full Recovery in Genesis Bankruptcy, DCG Says. Billionaire   Divorces Spur Crackdown by China’s Market Regulator. Golf Digest on weird trading in the stock of a  micro-cap putter company.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!

  [1] Boringly 10-year Treasuries are called “notes” and 20- and 30-years are called “bonds” but let’s not worry about that.


  [2] It is not, like, accurate in all respects or anything; this is still a very stylized version of one portion of what is going on with the basis trade.


  [3] Not only because, like, that would be weird, but because the government is in the Treasury market to borrow actual money, and the point of Treasury futures is that they do not involve much upfront cash. If you sell $100,000 of Treasury bonds you get $100,000; if you sell $100,000 of Treasury futures you don’t really get any cash to use immediately.


  [4] Again, I am writing a very stylized schematic story of the basis trade. In the real world futures are used by lots of investors for lots of reasons, people are naturally long futures while others are naturally short, etc.; this is really only part of it. But I think the intuitions here are interesting.


  [5] The phrase I would use here is not "a window for speculators to take advantage" but rather "a form of compensation for people who do the work of manufacturing futures out of Treasuries."


  [6] This is a bit tangential to the main points in the text, but the paper explains the basis trade as a way for hedge funds to, like, reserve bank balance sheet: “Second, to the extent that SLR and other regulations drove their internal economic incentives when managing balance sheet capacity, bank-affiliated intermediaries often allocated it on a ‘use it or lose it’ basis. In other words, leverage budgets that were allocated to specific entities but, if they were left underutilized, were downsized in favor of more active clients during regular reviews. That motivated hedge funds and other major consumers of leverage to find ways to utilize leverage allocations without taking much market risk. In other words, it became costly not to use one’s access to bank balance sheet, for fear that access would not be available when needed. Cash/Treasuries basis trades, which are most commonly constructed as a ‘short’ in futures and a repo-financed ‘long’ in one or several bonds from that contract’s deliverable basket, rely on leverage but have a theoretically bounded payoff with minimal market risk in a relatively wide range of market conditions. That made them fit for purpose as a placeholder position to secure future access to balance sheet as needed.”


  [7] Obviously Black-Scholes doesn’t work this way but we don’t have to care about that.


  [8] Come to think of it, that's
the rough order of magnitude of Jimmy Levin’s pay at Sculptor Capital Management Inc. and Sculptor’s market cap, but that’s because publicly traded hedge fund companies really are odd.


  [9] They also vest on a change of control, making this functionally a big golden parachute.


  [10] Well, “Camara made about $500,000 in salary last year and just under $1 million, all cash, in 2021.” Still the pile of hopeless options was not an incentive to stay.


  [11] I don’t really either, though I have at times in my life seen some lists. My vague impression is that a lot of words like “market share” are bad because a lot of  fights in antitrust are about market definition. The government will say that you are dominant in the market for social media, and   you will say “no we are a tiny fraction of the market for human interaction,” and you’ll argue about what the relevant market is. But if your employees were sending around memos like “we need to increase our market share, we’re currently 35% of social media and want to get to 40%,” then the government can say “see, that’s the correct market.”











            Follow Us













              Get the newsletter


















Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022







<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cjh4ge.66jr/56d7dec2.gif" alt="" border="0" /></a>
