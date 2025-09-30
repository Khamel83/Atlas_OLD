# Money Stuff: What Does Payment for Order Flow Buy?

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Wed, 8 Dec 2021 13:19:58 -0500 (EST)
**Source:** inputs/saved_emails/Money Stuff What Does Payment for Order Flow Buy_Wed,_8_Dec_2021_13-19-58_-0500_(EST)_17d9b47153e02444.eml
**Processed:** 2025-08-24T19:13:08.430743














        PFOFI think there are two different intuitive models of payment for order flow. Let’s call them the Good Model and the Bad Model. The Good M














































      PFOF


I think there are two different intuitive models of payment for order flow. Let’s call them the Good Model and the Bad Model. The Good Model goes like this. Lots of retail investors go to their brokerage looking to buy XYZ stock, and lots of retail investors go to their brokerage looking to sell XYZ stock. XYZ is available on the stock exchange; you can buy it for $10.02 or sell it for $9.98. Those prices on the stock exchange are called the “national best bid and offer,” or NBBO, and are set essentially by market makers, high-frequency electronic traders who are in the business of buying from sellers and selling to buyers. The spread — the $0.04 difference between the buying price (the offer) and the selling price (the bid)[1] — is due to the fact that the market makers take lots of risk: If they buy stock on the stock exchange, probably some smart hedge fund is selling, and it will probably go down. So they need to buy at a fairly low price ($9.98) and sell at a fairly high price ($10.02) to compensate for this risk of “adverse selection,” this risk that whoever they trade with knows something that they don’t.If the brokerage just sends all of its customers’ orders to the stock exchange, they will buy at $10.02 and sell at $9.98, which is not so great. Also the brokerage will pay a little fee — customarily $0.003 per share — to the exchange for executing the order.But the market makers come to the brokerage and say: Look, we hate trading with all these hedge funds on the public stock exchange. So much adverse selection. If we could just trade with your delightful retail customers, who trade small lots and never know anything we don’t know, we would never lose money. So we could afford to charge them a much lower spread. So if you send your orders to us directly, we will let your customers buy at $10.01 and sell at $9.99. They will get a better price than they would on the stock exchange, but we will still make money. Not only that! We’ll make so much money that we can pay you some of it. We’ll give you $0.003 per share for your trouble. Instead of you paying an exchange to execute your customers’ orders, we’ll pay you to execute them. With that money, you can fund your business. It can replace commissions! You can offer free trades! Good deal for everyone.The Good Model has very intuitive market-structure economics. I have discussed it in more detail a few times, mainly here. The Bad Model goes like this. XYZ is available on the stock exchange, and the posted prices are in fact $10.02 to buy and $9.98 to sell. But only naive rubes pay those posted prices. There is a “real” price to buy XYZ, a savvy-customer price that you can get by knowing where XYZ is on sale. The real price is, say, $10.001 to buy and $9.999 to sell.[2] You have to be smart, you have to know about order types and hidden liquidity and dark pools, you can’t just send a market order to the big stock exchange and expect to get the real price. But lots of people are smart; there are smart order routers that are commercially available and that are good at finding the real price.High-frequency electronic traders, for instance, are smart, and know where to find the real price. They can easily buy XYZ for $10.001 and sell it for $9.999. Retail customers of retail brokerages are not particularly smart, and frankly the retail brokerages aren’t all that smart; they don’t know where to find the real price. All they know is that the posted price, the NBBO, is $9.98 / $10.02.So the electronic traders — the market makers — go to the brokerages and say: Look. Instead of sending your customers’ orders to the exchange, having them pay $10.02 and get $9.98 and you paying $0.003 in fees, send their orders to us. We’ll give them a better price; we’ll charge them $10.01 to buy and pay them $9.99 to sell. And we’ll even pay you $0.003 for your trouble. This is a good deal for the brokerage (it gets paid for order flow instead of paying for execution), and it looks like a good deal for the customers (they pay $10.01 instead of $10.02, etc.).But meanwhile the market makers are doing this very simple trade:	Customer comes to them to buy stock.	It sells them stock for $10.01.	It turns around and buys stock at the real price, $10.001.	It makes $0.009 in instant risk-free profit.	It pays $0.003 of that to the brokerage for the opportunity.The Bad Model is what pretty much everyone believes about payment for order flow. It is the explicit model of Michael Lewis’s “Flash Boys.” I have discussed it in more detail here, when we talked about an institutional brokerage that followed it more or less exactly and got in trouble with the Securities and Exchange Commission. The brokerage told its customers that it did smart routing to try to find them the best price. But it didn’t: It secretly sold their orders to market makers who filled the orders at a better-than-the-NBBO-but-worse-than-the-best-price price, and then went out and traded for themselves at the best price.[3]By the way, I call it the Bad Model, because people seem to think that it’s bad. Maybe that is unfair. Maybe I should call the Good Model the “Principal Model,” and the Bad Model the “Agency Model.” In the Principal (Good) Model, the market makers are essentially in the business of intermediating trades between retail customers in time: The economic theory of the market maker’s job is that it buys from retail sellers, waits, sells to retail buyers, and collects a small spread representing its relatively low risk of adverse selection.In the Agency (Bad) Model, the market makers are essentially in the business of finding good liquidity and selling it to retail: The economic theory of the market maker’s job is that it buys from retail sellers and immediately resells at a higher price because it knows where the higher prices are, but since the retail customer doesn’t know where the higher prices are the market maker is providing a useful service.I think that in the real world both of these models have to be somewhat true. That is, in the real world, what happens is that a market maker buys stock from a retail brokerage’s customers thousands of times each day, and sometimes it then turns around and sells the stock to that brokerage’s customers a minute later and collects a small spread (Good Model), and other times it turns around and sells the stock at the midpoint on a dark pool a millisecond later (Bad Model), and other times it does other things (sells the stock at the NBBO for risk management and loses money? I dunno) not really captured by either model. The market makers who internalize retail brokerage flow do not only do that; they also trade on public exchanges and dark pools and with institutional investors, and they manage their risk holistically and you cannot separate out which model they follow.Still, the two models do make different empirical predictions. In particular they make different predictions about what would happen if a retail brokerage — or every retail brokerage — stopped using payment for order flow and routing orders to market makers:	On the Good Model, internalizing retail orders allows them to get better prices than they could get in public markets, so getting rid of this model would lead to worse prices for retail.	On the Bad Model, internalizing retail orders allows them to get worse prices than they could get in the (“real”) public markets, so getting rid of this model would lead to better prices for retail, if retail brokers can do a good job of finding the real best public price.Last week Public, a retail stock brokerage, put out a Medium post titled “Delivering on Price Execution Without PFOF.” (Felix Salmon wrote about it here.) Earlier this year Public said that it would stop taking payment for order flow; instead, it routes its orders to public venues. Here’s how that’s going:The takeaway: The data available to us strongly suggests that Public delivers better execution quality on average to customers than our peer firms that accept PFOF from market makers. …We want our customers to get the best possible price on every single order. So, working with our partners at Apex Clearing, Instinet and the execution venues, we use smart order routing (“SOR”) software to locate the best price for each order available across 28 different lit exchanges and alternative trading systems (“ATSs”), and then route that order to the venue that offers the best price.When a customer submits an order to Public, the SOR first tries to execute that order at the “midpoint” price that is halfway between the Best Bid and Best Offer by scanning venues that are often not included in NBBO, including retail-specific lit venues and alternative trading systems that are designed to pair natural buyers and sellers at the midpoint.If we are unable to find a NBBO midpoint (or similar) execution during this first sweep, we route to the exchange with the best available posted price (often called the “inside quote”) as well as the highest likelihood of executing the order at or better than the NBBO. Most often, these are high-quality lit exchanges, including Nasdaq and IEX.This approach is working. We’re able to deliver better prices for our investors, in aggregate, than the PFOF-based model. This is based largely on delivering significantly better prices for a meaningful percentage of our investors’ orders.There are some statistics comparing execution quality and suggesting that Public gets better prices without the payment-for-order-flow model than it would with that model. Which suggests that the Bad Model of PFOF might predominate.Some caveats:	There are different ways to measure execution quality across lots of trades, none of the data is that transparent, and no study is ever really definitive. Some orders presumably get better execution with a PFOF/internalizer model, but others get better execution without it; Public’s aggregate numbers are good “based largely on delivering significantly better prices for a meaningful percentage of our investors’ orders.” I think that means something like “we trade at the midpoint” — $10.00 in my schematic examples above — “a lot of the time, which is way more price improvement than internalizers offer, but when we don’t get a midpoint fill we are more likely to end up trading at the NBBO, which is less price improvement than internalizers would offer.” 	This is not complete support for the Bad Model, because part of how Public gets good prices is by sending orders to “retail-specific lit venues,” that is, places for people who want to trade with retail due to, basically, the economic theory of the Good Model. “It is desirable to trade against retail,” the basic theory of the Good Model, does seem to be true.	Public doesn’t get paid for order flow, and in fact often pays exchanges to execute orders, which means that its business is not subsidized by PFOF, which makes it harder to offer free trading. (Public offers free trading, but gently requests tips.) If you think free trading is good then this is a drawback to getting rid of PFOF. (If you think free trading is bad and encourages gambling and churn, then this is a benefit!)Still all in all this does count as evidence for the Bad Model: You can find stock for sale at better prices than the NBBO, if you look for it, so you don’t have to use payment for order flow to get good execution for retail orders.






















































      Retail options


Last week Vice published an article with the headline “I Lost $400,000, Almost Everything I Had, on a Single Robinhood Bet.” The bet was a $200-strike call option on Alibaba Group Holding Ltd. in February, when Alibaba was trading in the mid-$200s. Basically buying an in-the-money call option like that is a way to get a lot of leverage on a stock: You pay, say, $60 for an option on a share worth $240; you get four-to-one leverage, which is more than you can get in a U.S. margin account. Then if the stock goes up to $300, you get back $100, for a $40 profit on a $60 investment. If the stock goes down to $200 you get back nothing, for a $60 loss. “My thesis was I might not make a lot of money, but I won’t lose much,” says the article. “The downside seemed limited.” What? This person put $400,000 into this trade and lost all of it.Is this bad? I don’t know. It seems bad. How do you prevent it? At some level you might want each retail investor to have some trusted fiduciary financial adviser and have to run all of their trades through that adviser. You call up the adviser and say “hey I’d like to put all my money into Alibaba call options” and the adviser says “are you sure” and you say “yes” and she says “this is unbelievably dumb” and you say “nonetheless” and she says “I’ll let you put 10% of your money into Alibaba call options, max,” and you say “no I want all of it” and she says “nope” and her ruling is final. Obviously the market cannot actually work like this. You have to be able to do the dumb things that you want to do. Sometimes you shouldn’t, though.Today the Wall Street Journal has an article titled “Investors Are Using Robinhood, Other Platforms to Jump Into Options Trades, Worrying U.S. Regulators.” What can the regulators do about it? Well, one thing they can do is complain that you used to have to call someone to do an options trade:“Now, the ability to trade options is just a few clicks away, and investors can easily trade without direct contact with their brokers,” Securities and Exchange Commissioner Caroline Crenshaw said in a recent speech. “Given these changes in market access, it may be that the options account approval rules are due for a review.”She said that when the current options-approval rules were written—in 1980—investors had direct contact with a human broker who could explain the impact of various strategies and the risks they entailed.Which is a reasonable complaint! “A human broker” is not the same as “a trusted fiduciary financial adviser,” and if you called up a broker in the ’80s and said “put all my money in one call option” she might have said “sure chief” and taken the commission. There is some chance she would not have. That is sort of a crazy thing to do and she might have talked you out of it. She wants the commission, but if you lose all your money in a week then she’s not getting any more commissions out of you. Long-term greedy, etc. Still, complaining that things were better in the olden days is not really something useful that regulators can do about this. Instead they might tinker with options approval rules:Gaining approval to buy and sell options through some brokerages, such as Robinhood Markets Inc., is significantly easier than at others. Such discrepancies, combined with the recent trading surge, has left U.S. regulators questioning whether the rules governing individual investors’ access to the options market need to be revised.Because of the risks, brokers have long been required to perform extra due diligence before approving someone to trade options. This includes obtaining information about the customer’s financial background and investment experience, and making sure the customer has been apprised of the risks.Representatives from the Securities Industry and Financial Markets Association, a lobbying group for brokers and asset managers, have met with officials at Finra and the SEC in recent months to discuss potential changes. The group recommended standardizing the different levels that brokers use when approving customers to trade options. …Still, other brokers are much more rigorous in reviewing customers’ applications to trade options. Some large brokerages require investors to speak to a representative and answer questions about options trading before approving them to do more-complex trades. It can take days to review applications for the most basic level of options trading at some.Robinhood, by contrast, approves investors’ applications instantly if their responses to the questionnaire meet the company’s criteria.This does not strike me as all that useful either? The person in the Vice article did a very simple options strategy — just buying a call option, not a “more-complex trade” — and my impression is that he or she understood perfectly how the trade worked. “​​I would describe a call option as a leveraged bet on an underlying stock, which helps you increase the upside (or downside) of the bet you're trying to make,” the person wrote, accurately capturing how the trade operated and also how it blew up. The problem is not understanding; the problem is deciding to put 100% of your assets into one leveraged stock bet. It is not impossible to regulate against that! Make a rule that no one can buy options with more than 10% of their net worth or whatever. It just seems very hard politically. U.S. financial regulation just isn’t structured like that; rather than paternalistic limits on investment we have disclosure requirements. Disclosure does not seem sufficient to prevent people from losing all of their money on one call options trade. People like a gamble, and the system is set up to give them one.











      Fine yes


Here are  some words:Money manager Jason Ader will submit plans on Dec. 10 for a casino in the New York area that features what he said would be the world’s largest cryptocurrency trading floor and a landing pad for flying cars.Ader, a former casino analyst, said the project will also include an esports arena and space for events such as New York Fashion Week. The project could cost $3 billion or more, depending on the site, which has yet to be determined. Ader said he would prefer the location be in Manhattan.Just in general I will say that the broad trend toward legalization of gambling in the U.S. allows everyone to be a bit more honest about all of this. If “investing” is good and “gambling” is bad, then when you set up a crypto trading platform (or an options brokerage!) you have to mutter something about capital formation and hedging and funding decentralized competitors to incumbent internet giants, mutter mutter mutter. Whereas if everyone agrees that gambling is fun and good then you can just put a big crypto trading floor in your downtown Manhattan casino and everyone is like “ah yes cool casino.” 


      NFT Stuff


Here is a cartoon of Gollum sitting at a computer as Frodo explains to him: “So you can’t own the precious physically, but you can pay to have your name listed as its owner in an online distributed database.” On Twitter, Amit Kumar Goyal completes the joke: “You could make a NFT of destruction of the ring on Mt Doom and it would be more valuable.”Two points here. First, that previous paragraph is I think utterly inscrutable to any normal person in at least two completely different ways,[4] but I suspect like 90% of Money Stuff readers understood it instantly. Honestly you should all be ashamed of yourselves; I sure am.Second, I wrote the other day that “the basic innovation of crypto is the production of artificial scarcity,” and I added, somewhat sarcastically, “it is an interesting economic question whether this artificial production of scarcity could actually create value.” But consider the theory underpinning this joke. Frodo wants to throw the One Ring into the fires of Mount Doom in order to destroy it, because its existence is bad for the world. But owning the One Ring is very desirable, particularly for Gollum. It is a valuable thing with terrible externalities. Subjecting the One Ring to the “object-fire-token-money” cycle gives everyone what they want: The ring can be destroyed, saving the world, but Gollum still gets to own it and mutter about his precious.[5] Value creation by artificial scarcity!Here is a long Medium post from last month about Klima DAO, a crypto project that basically buys carbon offsets to push up their price, making them scarcer so that it is more expensive for public companies to pollute. (If they have shareholder pressure to be carbon-neutral, Klima forces them to pay more to offset their pollution, giving them incentives to pollute less.) Klima combines this with Olympus DAO-style crypto Ponzi economics so that the Klima people buying these offsets feel rich. Is this value creation by artificial scarcity? Is this taking a valuable asset with terrible externalities, burning it up in a volcano, and letting people feel like they own it anyway? I don’t know anything anymore, man, I’m just talking about a cartoon here.


      Things happen


These Real Estate and Oil Tycoons Avoided Paying Taxes for Years. Evergrande Crisis Is  No Lehman Moment for Rising Chinese Markets. GameStop’s Stock Price Holds Steady—For Meme Stock. Crypto Chiefs Face Democrat Skeptics, GOP Supporters at  House Hearing. Denmark Plans to Sell Its First  Sovereign Green Bond in January. Martin Shkreli’s Former Company Ordered to Pay $40 Million in Settlement Over Price-Gouging Case. How Amazon Outage Left Smart Homes  Not So Smart After All. Space Tourist Billionaire to  Hand Out Cash While Orbiting Earth. Just in Time for Christmas: Knitwear Fit for a T. Rex. If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] That is, the offer is the price that a price-insensitive liquidity-taking market order would buy at. It’s the price a market maker would sell at. The bid is the price that a market maker buys at, and you sell at.[2] These are very silly numbers; I mean to gesture schematically at a distribution where much of the time you can trade at the midpoint (buy at $10.00, sell at $10.00) but sometimes you trade at some spread. None of this stuff is deterministic; it is all “if you do a lot of trades this is how it averages out.”[3] Actually as far as I can tell there the market makers reversed the order of that, trading for themselves at the best price and *then* filling the customer order at a worse price, which seems much worse! In general the Bad Model does not require that the market makers engage in *front-running*, that is, buying for themselves before filling the customer. It just requires that they have confidence that they can trade elsewhere at low risk.[4] Maybe not that different; I feel like “Lord of the Rings” knowledge is subsumed into a lot of online nerd domains.[5] Of course Gollum loses the actual magical attributes of the ring that make it precious to him but if he is addicted enough to the internet maybe he doesn’t mind.










            Follow Us













              Get the newsletter



























Like Money Stuff? | 
Get unlimited access to Bloomberg.com, where you'll find trusted, data-based journalism in 120 countries around the world and expert analysis from exclusive daily newsletters.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022


















<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cfgn8a.5nfl/118fd640.gif" alt="" border="0" /></a>
