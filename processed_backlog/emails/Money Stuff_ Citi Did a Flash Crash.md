# Money Stuff: Citi Did a Flash Crash

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Tue, 3 May 2022 14:26:55 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Citi Did a Flash Crash_Tue,_3_May_2022_14-26-55_-0400_(EDT)_1808b2df596a046e.eml
**Processed:** 2025-08-24T19:13:04.119812














        Flash crashIf you are a person, and you own 100 shares of Company X stock, and you want to sell it, one way to do that would be to go to you














































      Flash crash


If you are a person, and you own 100 shares of Company X stock, and you want to sell it, one way to do that would be to go to your computer and log into your brokerage’s website and press the button to sell the stock at the market price. That will basically work. If the stock last traded at $100, you will probably sell your stock at a price very close to $100 per share, maybe $99.99 or $99.998 or whatever.If you are a trader at a big bank, and you own 100,000 shares of Company X stock, and you want to sell it, one way to do that would be to go to your computer and open your trading program and press the button to sell the stock at the market price. Oops! No, don’t do that. If you do that you might get  stories like this written about you:A sudden selloff in European stock markets just before 10 a.m. CET on Monday was fueled by a flash crash in the Nordic region, with traders and fund managers pointing toward a potential portfolio trade error.The OMX Stockholm 30 Index slumped as much as 8% in just five minutes before recovering most of the losses shortly after. The index was trading 1.1% lower as of 1:00 p.m. CET, roughly in line with a dip in broader markets.“It’s most certainly a ‘Nordic Flash Crash’,” said Joakim Bornold, savings economist at Soderberg & Partners, adding that equity markets can be very sensitive to erroneous trades despite safeguards.While it was not immediately clear what caused the short-lived slump, a spokesman for Nasdaq Stockholm said it wasn’t a technical glitch on their part. “Our first priority was to exclude technical issues in our systems, and our second priority was to exclude an external attack on our systems. We have now excluded both,” David Augustsson, spokesman for Nasdaq Stockholm, said.“It is very clear to us that the cause of this move in the market is a very substantial transaction made by a market participant,” he said, adding that Nasdaq will not cancel any trades made on the Nordic markets.Or  this one:Citigroup Inc.’s London trading desk was behind a flash crash that sent shares across Europe tumbling, dealing a fresh setback to the bank’s yearslong efforts to improve controls.A trader at the U.S. firm made a mistake “inputting a transaction,” Citigroup said late on Monday after a knee-jerk selloff in Swedish stocks in five minutes wreaked havoc in bourses from Paris to Warsaw. The bank said it identified the error “within minutes” and corrected it. The violent reaction saw the main European index lose as much as 3%, wiping out 300 billion euros ($315 billion) at one point. It revived questions how large financial firms can prevent such errors, and whether markets have sufficient safeguards in place.“The reality is that, despite all the fancy control systems, large parts of trading are still manual and human-driven, meaning the ‘fat finger’ isn’t just a metaphor,” said Oliver Scharping, a portfolio manager at Bantleon.I don’t really know what happened here, but I do want to lay out a minimal schematic story of a flash crash:	A Citi trader decided to sell large blocks of “a basket of shares that included many Swedish names” for some good reason (repositioning a portfolio, hedging some other trade, etc.).	The trader correctly typed the names and quantities of stocks to sell into the computer.	Then the trader hit the button to sell them.That’s it! I don’t mean to say that that’s what happened here, or that that’s the only explanation for a flash crash. But the way that a lot of modern electronic markets work is that if a large trader wants to sell a large position all at once, the market cannot handle it; simply sending a single large market order to sell the whole position at once would be a mistake. We have  talked about this before. The basic idea is that modern electronic markets operate on order books that do not reflect all of the supply or demand for a stock, or even very much of it. If you got all the people who trade Nordic stocks together in a big room — call it a stock exchange — and then a Citi trader walked into the room and said “hey I want to sell 100,000 shares of these stocks, who wants some,” enough of them would probably be interested at a price of, say, 1% below the last trade to get the deal done.But in modern markets there isn’t a room, and you don’t go to all the potential buyers and say “hey are you interested?” Instead, stock exchanges consist of computer programs to match up buy and sell orders. There will be orders resting on the order book at below the current stock price — some people will put in orders saying “I would buy some of this stock at 1% below the current price” — but there won’t be that many of them. If you think you would be happy to buy some of the stock at 1% below the current price, you don’t have much of an incentive to put in an order now. You can wait until it drops and then decide. (Maybe it dropped for a good reason and you don’t want to buy it anymore.)And so if you come to the exchange with an order to Sell Everything Now, the exchange won’t go around polling every potential trader saying “do you want to buy this stock?” Instead it will just look at the buy orders already on its book. And if you have a whole lot to sell, you’ll sell to everyone who wanted to buy down 1%, and everyone who wanted to buy down 2%, and so on, until you sell your last shares to people who wanted to buy down 8%. And then a minute later everyone will notice that they bought a bunch of stock but that nothing else changed, and so they will put in new orders to buy at prices that are slightly below where they were two minutes ago, and the stock will rebound almost all the way back to where it was before you cleared out the order book with your big trade.This is particularly true if things are otherwise quiet and there’s  no one around to buy:Scharping said lower volatility breaks in Nordic markets probably played a role, as did the bank holiday in the U.K., which left European stock markets with about a quarter less liquidity than normal.Again I don’t know if that’s the story here. Other explanations are possible. Maybe the Citi trader meant to sell 1,000 shares and accidentally typed in 1,000,000, in a true “fat finger” error. Or maybe the Citi trader sold a bunch of shares, and then momentum-following algorithms sold more shares, and then stop-loss orders were triggered forcing more sales, and then margin calls were triggered, etc., in a cascade of lower and lower prices. Possible!“The problem is not the mistake per se, but all the algorithms and stops that were triggered,” said John Plassard, a director at Mirabaud & Cie. “It shows the market is always vulnerable to human error and that algorithms and various CTAs are far too present in markets,” he added, referring to the commodity trading advisors that often use rapid systematic orders to pursue market trends. And you need some story like that to explain how selling Swedish stocks could cause “havoc in bourses from Paris to Warsaw.” But a basic story of “if you try to sell too many shares all at once the price will go down” seems like a decent starting place. “A very substantial transaction made by a market participant.”This is a story of market fragility, but on the other hand it is a small one. The market blipped down and then back up. The error wiped “out 300 billion euros ($315 billion) at one point” only in an abstract sense; the actual amount of stock traded at those lower prices was relatively small. And it’s a fixable problem: Banks generally have simple algorithms to do large trades, algorithms that space the trade out over a reasonable time, trying to trade, say, 10% of volume in any given period until they have sold all the stock they need to. If you hit the “Sell Carefully” button it’s fine. Hitting the “Sell Everything Now” button is the problem.






















































      SEC Crypto Cyber


My basic view of U.S. Securities and Exchange Commission regulation of crypto projects is that we are in a somewhat eerie lull. It seems to me that there are a lot of projects in the crypto world that (1) are quite large, (2) have the backing of well-financed and respectable entities, and (3) are obviously illegal unregistered offerings of securities? The SEC under its previous chair, Jay Clayton, also seems to have thought that, and brought a lot of (sometimes pretty  aggressive) cases.The SEC under its current chair, Gary Gensler, as far as I can tell also thinks that, and has not brought a lot of high-profile cases. Some, though! The SEC has decided that  crypto lending programs are securities, and has moved to regulate them. But, like … governance tokens of decentralized finance projects are obviously equity securities?  Ponzicoins are obviously securities?  Fractionalized NFTs? Just … everything? I mean, this is not legal advice, and I guess a lot of lawyers disagree with me; maybe the SEC disagrees with me too. But my guess is that more stuff is coming. And when I say “more stuff” I do not mean hundreds of pages of notice-and-comment rulemaking designed to clarify what sorts of DeFi activities do and do not qualify as securities, and to help DeFi innovators comply with registration requirements. I mean enforcement actions in which the SEC will argue that various DeFi projects are illegal under existing rules.Anyway:The Securities and Exchange Commission today announced the allocation of 20 additional positions to the unit responsible for protecting investors in crypto markets and from cyber-related threats. The newly renamed Crypto Assets and Cyber Unit (formerly known as the Cyber Unit) in the Division of Enforcement will grow to 50 dedicated positions.Since its creation in 2017, the unit has brought more than 80 enforcement actions related to fraudulent and unregistered crypto asset offerings and platforms, resulting in monetary relief totaling more than $2 billion. The expanded Crypto Assets and Cyber Unit will leverage the agency’s expertise to ensure investors are protected in the crypto markets, with a focus on investigating securities law violations related to:	Crypto asset offerings;	Crypto asset exchanges;	Crypto asset lending and staking products;	Decentralized finance ("DeFi") platforms;	Non-fungible tokens ("NFTs"); and	Stablecoins.Notice that it’s all in the Division of Enforcement. As far as I can tell the Division of Writing DeFi Rules continues to have roughly zero dedicated position. The way you will know what SEC’s crypto rules are is that in like five years you will be able to look at a bunch of enforcement actions. Each enforcement action will begin by describing what the company did that was bad, and you’ll know that is illegal. Each settled enforcement action will end by describing what the company agreed to do to remedy the problem, and  you’ll know that is legal. And you’ll try to do the legal things and not do the illegal things and make your best guess about things that aren’t described in any of the enforcement actions. But it seems to me that the major enforcement actions are still mostly in the future, so good luck figuring it out now.











      Always Twitter


Elon Musk has  agreed to buy Twitter Inc. for about $46.5 billion, which includes about $25.5 billion of money borrowed from banks (secured by Twitter and by Musk’s shares of Tesla Inc.) and about $21 billion of equity. Musk himself is on the hook for all of that $21 billion, but he is free to syndicate it. If he can find anyone else who wants a piece of Twitter, he’s welcome to sell it to them. He’s trying:Elon Musk is in talks with large investment firms and high net-worth individuals about taking on more financing for his $44 billion acquisition of Twitter Inc. and tying up less of his wealth in the deal, people familiar with the matter said. …The new financing, which could come in the form of preferred or common equity, could reduce the $21 billion cash contribution that Musk has committed to the deal as well as a margin loan he secured against his Tesla shares, the sources said. …Major investors such as private equity firms, hedge funds and high net-worth individuals are in talks with Musk about providing preferred equity financing for the acquisition, the sources said. Preferred equity would pay a fixed dividend from Twitter, in the same way that a bond or a loan pays regular interest but would appreciate in line with the equity value of the company. …Musk has also been in talks with some of Twitter's major shareholders about the possibility of them rolling their stake into the deal rather than cashing out, one of the sources said. Former Twitter Chief Executive and current board member Jack Dorsey is examining whether he will roll his take, one source added.Large institutional investors, such as Fidelity, are also in talks about rolling over their stake, according to the source.Musk has tweeted that he would try to keep as many investors in Twitter as possible as he takes the company private.I don’t really get the preferred equity idea? One problem with Twitter, as a leveraged-buyout target, is that it doesn’t generate that much cash. Just paying  the interest bill on the $13 billion that of debt that Musk plans to raise against Twitter will be tough with the company’s cash flow (Bloomberg shows estimated 2022 earnings before interest, taxes, depreciation and amortization of $1.57 billion), and he has to pay about another $1 billion on his Tesla margin loans. Preferred stock on Twitter will be junior to the debt, and the unsecured debt that he plans to raise on Twitter seems to have an interest rate north of 10%. He’s not going to raise billions of dollars of fixed-rate preferred at 15% and then pay out another billion dollars a year to preferred shareholders; that makes no sense.Perhaps he will raise convertible preferred, giving some investors an equity claim that is a bit senior to his own, without much or any cash dividend. hat makes a bit more sense, and is more common in private tech companies. It’s still weird here. Twitter is not some startup; if you are a potential investor, you are probably not that focused on an outcome like “Twitter is eventually sold at some price that pays off the debt but doesn’t fully return Musk’s investment.” (In which case a convertible preferred would be valuable.) Who would buy Twitter from Musk? Why would he sell it? I don’t know.Meanwhile the rollover equity idea is a long-standing dream of Musk’s. It’s  what he wanted with Tesla, back when he pretended he would take it private in 2018. The dream, for a lot of visionary tech startup founders, is:	Raise a lot of money from the deep liquid public capital markets, selling stock to giant institutions like Fidelity and also enthusiastic retail investors.[1]	Keep total control of your company and not have to listen to shareholders.	Get to choose your shareholders, so you can exclude annoying ones.	Ban short selling.	Not have a stock price that changes every day and makes you feel bad when it goes down.You can get some of these things in the public markets (dual-class stock mostly lets you keep control while raising public money), and you can get a lot of them in the private markets (all of them, really, except No. 1, and the private markets are pretty big and liquid these days), but I suppose you can always try to tweak it a little. Taking an existing public company and making it private while keeping a lot of the shareholders is one way to achieve the dream.There is something a little weird, though, about broadly marketing rollover equity in Musk Twitter to shareholders of Existing Twitter. Eventually there is going to be a proxy statement for this merger, and in effect Twitter’s board  will say to shareholders “you should take this deal because $54.20 in cash is more than Twitter’s stock is worth.” Meanwhile Musk is going out to potential equity investors and saying the opposite: “Chip in some money because this thing is worth more than $54.20.” If a select few of Twitter’s existing big shareholders — perhaps including Jack Dorsey, a board member who ran Twitter for years and voted for the deal — are offered the chance to stick around, and take it, then that undermines the logic of the deal. “Elon Musk can make Twitter vastly more valuable than $54.20 per share, but not for you” is not a great message for the board to send to most of its shareholders.Meanwhile, Twitter filed a Form 10-Q with new risk factors about how the deal with Musk  might undermine its business:Twitter Inc.’s $44 billion deal to be acquired by Elon Musk means it risks losing advertisers and employees, who may be concerned about the company’s uncertain future.Twitter said it may be difficult to attract and retain key people, and mentioned “the possibility that our current employees could be distracted, and their productivity decline as a result, due to uncertainty regarding the merger,” the company said in a regulatory filing Monday.In a sense, this doesn’t matter: As long as the deal closes, Twitter’s shareholders have no reason to care about employee retention or advertisers; they just get cashed out at $54.20 per share, and all this stuff is Musk’s problem. But of course if the deal doesn’t close then it’s the shareholders’ problem.


      Insider trading


One misconception that people have about insider trading is that, to be guilty of insider trading in a company’s stock, you need to have inside information about the company. This is not true. Insider trading is, more or less, a crime of trading on misappropriated information. If you know something that is material to the stock, and you have some duty to keep that information confidential and not use it for yourself, then trading on it is insider trading.So, for instance, if a newspaper publishes a stock-picking column, and you get the column before it is published and buy the stocks it recommends, that is famously insider trading even if the columnist has no inside information about the companies. (It’s insider trading even if you are the columnist.) It’s not that you knew inside information about the company; it’s that you had information (1) that you weren’t supposed to have (or at least that you weren’t supposed to trade on) and (2) that moved the stock price.Or if you work at a company and get news about a merger and  buy your competitor’s stock, figuring that your competitor’s stock will go up on your merger news, that is also (arguably!) insider trading: You had information (about your company), you weren’t supposed to trade on it (under your company’s policies), and it was material to your competitor, in the simple sense that when the news came out the competitor’s stock went up.Or if you hack into the computer systems of a stock-picks newsletter and buy the stocks it is going to pick, you might not think that’s insider trading, but the Justice Department and Securities and Exchange Commission will. Here’s an email that David Stone allegedly sent to a buddy:I'm ok with sharing the weekly trades with you. I have used it so far to generate a significant amount of money and I'm sure you will be able to as well. There is a small possibility that what we are doing could be considered insider trading. [Advisor-1] uses only public information about to make its recommendations and even the recommendations are behind a paywall so it is a stretch to call it insider trading but it certainly behaves like it because it almost guarantees favorable price moves at a certain time. And here is the Justice Department press release:Damian Williams, the United States Attorney for the Southern District of New York, and Michael J. Driscoll, Assistant Director-in-Charge of the New York Field Office of the Federal Bureau of Investigation (“FBI”), announced today the unsealing of a complaint charging DAVID STONE with securities fraud in connection with an insider trading scheme. STONE was arrested yesterday and will be presented today in the United States District Court for the District of Oregon. … From 2020 up to his arrest in 2022, DAVID STONE exploited market-moving stock recommendations made by an investment recommendation service (“Advisor-1”) before those recommendations were released to paying subscribers. STONE, an information technology (“I.T.”) professional, accessed Advisor-1’s computing system without authorization and viewed information relating to Advisor-1’s recommendations before they were announced to Advisor-1’s paying subscribers.Advisor-1’s stock recommendations typically, but not always, lead to higher closing prices for the recommended stock as compared to the prior day’s closing price. By trading on those recommendations before they were announced, STONE was able to obtain significant profits unavailable to other market participants. In fact, since in or about November 2020, brokerage accounts associated with STONE traded ahead of Advisor-1 recommendations on more than a dozen occasions for approximately $3 million in gross gains.I don’t know who Advisor-1 is. I will say that the limit case here is if you hack into a pure pump-and-dump email list, someone who pumps stocks to a subscriber list based on no information or analysis at all but just to run a scam, and you buy the stocks he’s going to pump before he pumps them, then I think that is probably also insider trading? The point is the misappropriation and the materiality, not the quality of the information.


      The wrong Ma


Speaking of information that is material to a company without being about that company:Alibaba shares sold off on Tuesday following a Chinese state media report that an individual surnamed “Ma” had been detained, pushing down Chinese technology stocks that had been expected to rally on the promise of support from Beijing.Shares in the Chinese ecommerce giant fell as much as 9.4 per cent at the open in Hong Kong following the report. The shares later pulled back to be down about 1 per cent after China’s state broadcaster CCTV amended its one-sentence dispatch to indicate the individual was not Alibaba’s billionaire founder Jack Ma.If you knew about the other Ma’s arrest in advance and you shorted Alibaba’s stock, etc.


      BS


Uh, I don’t know, here’s a paper:What is the effect of seemingly impressive verbal financial assertions that are presented as true and meaningful but are actually meaningless; that is, financial pseudo-profound bullshit? We develop and validate a novel measurement scale to assess consumers’ ability to detect and distinguish financial bullshit. We show that this financial bullshit scale captures a unique construct that is only moderately correlated with related constructs such as financial knowledge, numeracy, and cognitive reflection. Consumers particular vulnerable to financial bullshit are more likely to be young, male, have a higher income, and be overconfident with regards to their own financial knowledge. The ability to detect and distinguish financial bullshit also predicts financial well-being while being less predictive of consumers’ self-reported financial behavior, suggesting that susceptibility to financial bullshit is linked to affective rather than behavioral reactions.They basically surveyed people online and asked them to rate the “meaningfulness” of aphorisms about finance, some of them “generated by searching for actual quotes related to the financial domain” and others generated “by using bullshit generators like www.makebullshit.com.” People who rated the “fake” ones higher than the “real” ones were more likely to be young, male and overconfident, though honestly even Googling real quotes about finance is not necessarily the best way to order your affairs. The real profound statements include:Every time you borrow money, you are robbing your future self. — Nathan W. MorrisInflation is taxation without legislation. — Milton FriedmanWealth is not his that has it, but his that enjoys it. — Benjamin FranklinSure. The fake pseudo-profound ones include:Money eases the costs of those who borrow.Good investors spread large shares beyond size.Freedom and space transform the abstract meaning of money.I kind of like the fake ones? Money really does ease the costs of those who borrow!


      Things happen


Russia Dodges Default as Some Investors  Receive Dollar Funds. BP Takes $25.5 Billion Hit From Russia Exit. Lessor Avolon Writes Off $304 Million on  Planes Tied to Russia. Spirit Airlines Rejects JetBlue Bid, Sticks With Frontier Deal. EU Accuses Apple of Abusing Mobile-Payment Market Power. PayPal Helped Spur  EU Antitrust Complaint Against Apple Payments. Facing a Wheat Crisis, Countries Race to Remake an Entire Market on the Fly. U.S. Allowed to  Seize Megayacht With Russia Owner in Dispute. Russian tycoon Tinkov claims he was forced to sell bank stake after denouncing ‘crazy war.’ Chelsea sale hits snag over fears Roman Abramovich wants £1.6bn loan repaid. Morgan Stanley Raided in Frankfurt in  Tax Fraud Investigation. “Things were going well at Credit Suisse, until we blew up the business.”If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] Musk seemed enthusiastic, though vague, about  letting retail shareholders roll over into a private Tesla, but that never made sense and he has not mentioned it for Twitter. 










            Follow Us













              Get the newsletter



























Like getting this newsletter?
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022


















<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cgf76b.5sss/4ef7de18.gif" alt="" border="0" /></a>
