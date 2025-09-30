# JPMorgan Fights Tesla Over Warrants

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Tue, 16 Nov 2021 13:04:53 -0500 (EST)
**Source:** inputs/saved_emails/JPMorgan Fights Tesla Over Warrants_Tue,_16_Nov_2021_13-04-53_-0500_(EST)_17d29ee63e664458.eml
**Processed:** 2025-08-24T19:13:05.090243







        WarrantsCompanies sometimes issue convertible bonds. A convertible bond is a bond that can be converted into stock. Normally the conversion














































      Warrants


Companies sometimes issue convertible bonds. A convertible bond is a bond that can be converted into stock. Normally the conversion is at a fixed price that is above the price of the stock when the convertible is issued. In 2014, Tesla Motors Inc. (now Tesla Inc.) sold $1.38 billion of 7-year convertible bonds with a 1.25% coupon and a conversion price of $359.87, a 42.5% premium above its stock price of $252.54 at the time. (At the same time, it sold another $920 million of 5-year convertibles with a 0.25% coupon and the same 42.5% conversion premium, though I will not discuss those bonds further here.[1]) When the bonds matured seven years later (this March 1), Tesla’s stock was trading at $718.43. But in between Tesla had done a 5-for-1 stock split, making the effective conversion price of the bonds about $71.97. One $1,000 bond converted at maturity into about $10,000 worth of stock. All the convertible bondholders converted by the time the bonds matured — some long before — and were happy and we will not talk about them anymore.[2]When a company issues a convertible bond, often it thinks: “This is fine, but I want a higher conversion premium. I don’t want people to be able to convert into my stock at 42.5% above my current stock price, because I think my stock will go up a lot. I want, like, a 100% conversion premium. I want to do a convertible that doesn’t dilute my stock unless my stock goes up a whole lot.” But this is hard to do, in the convertible bond market; convertible-bond investors don’t want to buy super-high-premium convertibles. So companies sometimes do what is called a “call options overlay,” or a “call spread,” or a “bond hedge and warrant transaction,” with their investment banks. In effect they buy an option from the banks (the “bond hedge”) that mirrors the conversion option in the convertible: In this case, Tesla’s $1.38 billion 7-year convertible would convert into about 3.8 million shares of stock, so Tesla bought a 7-year option on 3.8 million shares with a strike price of $359.87. (Those 3.8 million shares automatically became 19 million shares after the stock split.) And then they sell the banks a separate option (the “warrant”) at a higher strike price: In this case, Tesla sold the banks a 7ish-year warrant with a strike price of $560.6388, a 122% premium above the stock price when it issued the convertible bonds.[3] The overall result is that the company has effectively issued a synthetic high-premium convertible: If the stock goes up 80% or 100%, it will issue some shares on the convertible but get them back from the bond hedge; it only “really” issues shares if the stock goes up more than 122% and the warrant is in the money.[4]So Tesla’s banks owned warrants to buy Tesla stock. One of those banks was JPMorgan Chase & Co. Disclosure! Another one of those banks was Goldman Sachs Group Inc. I used to work at Goldman Sachs, on the convertible bonds and corporate equity derivatives desk, doing exactly these trades, though I was long gone by the time of the Tesla deal (I left in 2011).The banks, of course, hedge these warrants. Roughly speaking the way you hedge a warrant is that you sell a portion of the underlying stock; as the stock goes up you sell more, and as it goes down you buy some back.[5] The more often you do that — the more you buy low and sell high — the more money you make. So you want the stock to be volatile, to bounce around a lot, because every time it bounces around you make money. The volatility of the underlying stock is an important input to the options calculators that the banks use to figure out how much to pay for the warrant.When you do a deal like this, one thing that you worry about is a merger. The value of the warrant comes in large part from the volatility of the stock. Tesla’s stock is volatile, so the banks paid a lot for its warrants. (A total of about $390 million combined for these warrants plus other warrants related to the five-year convertible bond.) If Tesla were to be acquired for, say, $420 a share, it would stop being volatile; its stock would be worth $420 per share forever. Not only that, but it would stop being volatile — at least, it would become a lot less volatile — as soon as the merger was announced; it would trade close to the deal price ($420) and be pinned there until the deal was completed or abandoned. The merger might be sort of good for you — the stock probably jumps up on the merger news, and you are long an option — but it’s not that good; you were hedged, so you don’t have a huge windfall from the stock going up. What you have is a loss in warrant value from the reduced volatility.When you are a bank doing a deal like this, and you worry about things, you put provisions in the contract to protect you against them. These warrants are over-the-counter options done under an International Swaps and Derivatives Association form agreement; the banks write the agreements, and they give the banks a lot of protections against risks. Basically if the banks identify some risk that they worry about, the contract will say “if the risk happens the bank can adjust the terms of the agreement to preserve the fair value to the bank.” (Generally if something good happens that makes the warrant more valuable for the bank, the bank won’t adjust to reduce that fair value.) You can read the form warrant agreement that Tesla’s banks signed here, though it doesn’t say much; mostly it works by reference to the ISDA Equity Derivatives Definitions. And so, in particular, it is standard for these warrants to have an adjustment provision in case of a corporate event like an acquisition. This provision tends to give the bank broad discretion to adjust the terms of the warrant to keep the value the same. The bank can “make such adjustment to the exercise, settlement, payment or any other terms” of the warrant as it “determines appropriate to account for the economic effect on the [warrant] of [the announcement of a merger] (including adjustments to account for changes in volatility, expected dividends, stock loan rate or liquidity ...).”[6] In practice what that means is that if you are bopping along with the warrant, and one day it is worth, say, $400 million, and the next day the company announces a merger and the volatility flatlines, you fire up your options calculator and figure out how to get the warrant back to being worth $400 million. If the lower volatility causes the warrant’s value to drop to $250 million, then you lower the strike price of the warrant until it’s worth $400 million again. A warrant with a strike price of $450 is worth a lot more than a warrant with a strike price of $560; the extra value from lowering the strike price can make up for the reduced value from flattening the volatility.I do not think I am giving away any huge secrets here when I say that, if a client gives its bank broad discretion to adjust a complex transaction to preserve value for itself, and the bank uses that discretion, the client will end up annoyed. The client will announce a merger, it will have a party, it will be well pleased, and then its bank will show up and say “hey remember that warrant we did a few years ago? Yeah you owe us an extra $150 million on that. Due to volatility. I can show you the model but you won’t understand it.” The bank might even be acting in good faith! But. You know. The client will be upset, and also the banker on the trade just made her whole year’s revenue target with that adjustment, weird how that works.[7]This is a story about Tesla and Tesla, you might notice, has not been acquired.[8] But you may remember that time that Elon Musk, the chief executive officer and major shareholder and memelord of Tesla, spent a couple of weeks  pretending on Twitter that he was going to take Tesla private at $420 per share. If he had taken Tesla private, JPMorgan (and Tesla’s other banks) would definitely have adjusted their warrants and demanded a big payday. He did not do that; it was all pretend. But he did say he would.And when he said that, in August 2018, JPMorgan said, well, okay, that's an announcement of a merger, we get to adjust the warrants. So it did:Following its standard practice, JPMorgan determined the economic effect of Tesla’s announcement by looking to the resulting change in the average implied volatility of publicly listed options on Tesla’s common stock with a maturity and strike price similar to the 2021 Warrants. ... In this case, JPMorgan looked at the average implied volatility prior to the announcement (from June 25 through August 6) and compared it to the average implied volatility after the announcement (from August 7 through August 15). Based on these calculations, JPMorgan concluded that the average implied volatility dropped by 12.41 points, a reduction of 26.4%.Next, consistent with its standard practice, JPMorgan determined that the appropriate adjustment to account for this economic effect would be a change to the strike price of the 2021 Warrants that preserved their fair value in light of this reduction in average implied volatility, keeping all other pricing inputs constant. Following a methodology that takes into account the differences between the bespoke 2021 Warrants and the listed Tesla options for which implied volatility data is publicly available—a methodology that, like the use of an average implied volatility, would tend to result in adjustments more favorable to Tesla— JPMorgan determined that the strike price had to be reduced from $560.6388 to $424.66 (the “First Adjustment”) to maintain the same fair value for the 2021 Warrants as they had before the Announcement Event. JPMorgan made the First Adjustment effective August 15 and modified its hedge positions the same day.The day before Musk’s tweet, Tesla closed at $341.99 and JPMorgan had out-of-the-money warrants to buy Tesla stock for $560.5388. The week after Musk’s tweet, Tesla closed at $338.69 and JPMorgan had warrants to buy the stock for $424.66. Tesla’s stock price was about the same, but JPMorgan’s warrants were much closer to being in-the-money. That was a big improvement!Of course it was an improvement meant to offset the reduced volatility in Tesla’s stock caused by Elon Musk pretending he was going to take Tesla private. Except that ... except that ... having a CEO pretend to take the company private makes it way more volatile? That’s a wild thing to do! If your CEO is the sort of wild man who will do pretend mergers because he’s bored on Twitter then your stock will be volatile! I mean, yes, Tesla’s expected volatility was reduced for a bit in the week or so after Musk made his announcement, when some people thought he might actually take the company private at $420 per share. But then it went up again as they realized (1) no he wouldn’t and (2) he’s the sort of guy who would joke around about that. In general Tesla has been more volatile since Musk’s tweet than it was before; in the long run, Musk’s tweet made JPMorgan’s warrant much more valuable.[9] But the warrant gave JPMorgan the right to adjust as soon as Tesla announced an acquisition, so it did. Well … did Tesla announce an acquisition? Sure I dunno whatever. Here’s what JPMorgan says:At the time, Mr. Musk was not only Tesla’s CEO, but also the chair of its board of directors and its largest shareholder. In a Form 8-K filed on November 5, 2013, Tesla had identified Mr. Musk’s personal Twitter account as a source of material public information about the company and encouraged investors to review that account. Because the tweet violated Nasdaq rules requiring at least 10 minutes’ advance notice before a listed corporation publicly disclosed a going-private transaction, Nasdaq temporarily halted trading in Tesla’s stock following Mr. Musk’s tweet, evidencing that the exchange considered the tweet to constitute an announcement by the company itself.After Mr. Musk’s tweet, Tesla’s Chief Financial Officer, its head of communications, and its General Counsel drafted an email—attributed to Mr. Musk—detailing the going-private plan. The email was sent to Tesla employees and published the same day on both Mr. Musk’s Twitter account and Tesla’s blog (which Tesla had also designated as a source of material public information about the company). In the email, and in a series of tweets responding to his Twitter followers, Mr. Musk elaborated on his plans to take Tesla private. He concluded in a tweet that “Investor support is confirmed. Only reason why this is not certain is that it’s contingent on a shareholder vote.”That same day, in response to various inquiries from research analysts, Tesla’s head of investor relations confirmed that Mr. Musk’s tweet signified a “firm offer” to take Tesla private that was “as firm as it gets.” Man, what a weird time that was; all that stuff happened. I feel like … I knew he was kidding? I feel like the market kind of knew he was kidding? (The stock went up 11% on his tweets, but not all that close to the supposed $420 deal price.) I feel like JPMorgan knew he was kidding? But they saw a deal announcement, of a sort, and they adjusted their warrant to make it worth a lot more money.A few weeks later, on Aug. 24, Tesla confirmed that Musk was just kidding, and JPMorgan dutifully adjusted the warrant again. Weirdly, though, it did not adjust it all the way back:JPMorgan had to determine the actual economic effect of Tesla’s second announcement. JPMorgan thus employed the same methodology as it had for its First Adjustment, comparing the average implied volatility before the second announcement (from August 16, the first day after the effective date of the First Adjustment, through Friday, August 24) to the average implied volatility after that announcement (from Monday, August 27 through August 29).Based on these calculations, JPMorgan concluded that the average implied volatility increased by 5.74 points, or 14.3%, as a result of the August 24 announcement, and determined that increasing the strike price to $484.35 was the appropriate adjustment to maintain the same pre-announcement fair value for the 2021 Warrants.So because Elon Musk spent three weeks in 2018 pretending he would take Tesla private, JPMorgan lowered the strike price of its warrants by about $75. (These are pre-split prices; post-split, that’s about a $15 difference, and JPMorgan calculates the split-adjusted strike price as $96.87.) Tesla, understandably, disagreed with all of this:After receiving notice from JPMorgan of the Second Adjustment on August 29, Tesla protested that no adjustment should be necessary at all because it had so quickly abandoned its going-private plans. Consistent with its obligations under the Agreements, JPMorgan shared a written explanation describing its calculations, including supporting market data and quotations, and held several conference calls with Tesla to explain its calculations. Tesla did not provide any specific objection to JPMorgan’s explanations on these calls, and following these calls, Tesla did not communicate further with JPMorgan regarding the Adjustments for six months. …Tesla sent a letter to JPMorgan about the 2021 Warrants on February 13, 2019 arguing that the Adjustments made by JPMorgan pursuant to the terms of the Warrants were “unreasonably swift and represented an opportunistic attempt to take advantage of changes in volatility in Tesla’s stock.” Tesla’s letter, however, did not dispute that Announcement Events had occurred, did not challenge any of the specific calculations or supporting materials JPMorgan had provided six months earlier, and did not offer any support for its assertion that JPMorgan’s methodology was unreasonable. If it is not obvious by now, I am quoting from the lawsuit that JPMorgan filed against Tesla in federal court yesterday. The warrants expired in June and July of this year; they were very in-the-money no matter what strike price you use (Tesla’s stock has been on a tear since 2018), but JPMorgan and Tesla used two different strike prices. JPMorgan demanded a lot of shares based on its adjusted strike price, Tesla gave it fewer shares based on an unadjusted price, and JPMorgan sued Tesla for a difference of 228,775 shares, which it converted to $162.2 million of cash.[10]I don’t know! I can see Tesla’s point here. Was JPMorgan being opportunistic in lowering the strike price of its warrants by $75 for three weeks of a pretend going-private transaction that actually increased the volatility of Tesla’s stock and the value of JPMorgan’s warrants? Yes, of course. The harm that JPMorgan was guarding against — losing the value of its warrant because a merger crushed the volatility of Tesla’s stock — obviously did not happen, and obviously was not going to happen, and really the exact opposite happened and Elon Musk’s nonsense made Tesla’s stock more volatile. But the letter of the contract let it adjust the warrant to offset that imagined harm, so it did.On the other hand it is not a great defense to be like “when our CEO makes corporate announcements nobody should listen to him.” JPMorgan might not have actually believed Elon Musk when he said he was going to take Tesla private. But it’s weird for Tesla to argue that. He’s the CEO! If he says he’s going to take Tesla private, Tesla is kind of committed to that position.It’s worth saying that JPMorgan was one of four banks that acted as Tesla’s counterparties on the warrant transactions for this convertible bond deal. Did the other banks adjust their warrants to give themselves more shares for Musk’s pretend going-private deal? Apparently not. Here’s a grudging footnote in JPMorgan’s complaint:Tesla also claimed that none of its three other warrant dealers had made similar adjustments. But Tesla has never substantiated that claim. Moreover, even if it were true, it has no bearing on whether JPMorgan acted in good faith, or whether its methods for calculating the adjustment were commercially reasonable. Tesla’s other warrant dealers generally held fewer warrants, and thus had less exposure, than JPMorgan. In addition, according to Tesla’s August 24 blog post, two of Tesla’s other warrant dealers were advising Mr. Musk on his going-private proposal. The third dealer may have been under consideration to serve as financial advisor to the special committee of Tesla’s board, but even if it was not involved in the going-private transaction, that dealer was working on a major financial transaction with Tesla that closed on or about August 21, 2018, just days before the going-private transaction was publicly abandoned. Thus, each of the other dealers may have been privy to non-public information about the going-private transaction, or otherwise may have declined to adjust their warrants for business reasons having nothing to do with the contractual terms or the reasonableness of JPMorgan’s adjustments. On the one hand, sure, fair, the other banks could have had thought “we should adjust these warrants” and had other reasons for deciding not to. On the other hand, if one bank adjusts its warrants to be worth an extra $162 million, and the other three don’t, that does tend to undermine the one bank’s position. The other three banks saw Musk’s tweets too; they just let it go.Speaking of “business reasons,” with cases like this it is fun, for me at least, to imagine the discussions within the bank. Like there is some banker at JPMorgan who covers Tesla, and who is not particularly in the weeds of the equity derivatives book. And this coverage banker was just cheerfully going about her business, planning to meet with Tesla and pitch some mergers and financing deals, when some nerd in equity derivatives called and said “hey, heads up, we’re in a dispute with Tesla about how we calculate the adjusted strike price of the warrants we did in 2014.” And the coverage banker was probably like “I don’t know what those words mean but this sounds very trivial, this is a huge company with huge prospective revenue, don’t antagonize them, just do them a favor and calculate the adjusted strike price the way they want.” And then the derivatives banker said “no you don’t understand it’s $162 million.”And then the coverage banker presumably … fainted? Like, obviously people very high up at JPMorgan had to sign off on filing this lawsuit, and presumably the coverage bankers advocated against it, but they had absolutely no leg to stand on because it takes a whole lot of banking revenue to compete with the $162 million that the equity derivatives nerds are planning to collect from Tesla. And now Tesla presumably hates JPMorgan and doesn’t return the coverage banker’s phone calls, and JPMorgan has decided as a matter of corporate policy to do this anyway because very few clients are worth $162 million.






















































      Everything is securities fraud


Say it with me now!Ohio’s attorney general is suing Meta Platforms Inc., formerly known as Facebook Inc., alleging the company misled the public about how it controlled its algorithm and the effects its products have on children.The lawsuit, filed on behalf of Meta investors and the Ohio Public Employees Retirement System, seeks more than $100 billion in damages and demands that Meta make significant changes so as to not mislead investors again, Ohio Attorney General Dave Yost said in a statement. …The lawsuit alleges that between April 29 and Oct. 21, 2021, Facebook and its executives violated federal securities law by intentionally misleading the public about the negative impact of its products on minors in an effort to boost its stock and deceive shareholders.“Facebook said it was looking out for our children and weeding out online trolls, but in reality was creating misery and divisiveness for profit,” Mr. Yost, a Republican, said.Here is the complaint. You  know the drill by now. Facebook said some generic things about how it was good:Throughout the Class Period, the Company repeatedly assured investors that it has “the most robust set of content policies out there” and touted the aggressive steps it takes to ensure the safety and security of its users by preventing misinformation and harmful content from spreading through its platforms. Facebook also stated that it was committed to keeping people safe and assured investors that it enforces its content policies evenly across all users. And investors, reassured by those statements, assumed that Facebook was good and bought its stock. But in fact it was bad:Thousands of recently leaked internal Facebook documents paint a remarkably different picture. Those documents show that Defendants were acutely aware that the products and systems central to Facebook’s business are riddled with flaws that sow dissention, facilitate illegal activity and violent extremism, and cause significant harm to users, but Facebook lacks the will or ability to correct them. Despite this knowledge, Facebook opted to maximize its profits at the expense of the safety of its users and the broader public, exposing Facebook to serious reputational, legal, and financial harm.And, when the facts (that Facebook was bad) came out, the stock went down:From the date of the first article published by The Wall Street Journal on September 13, 2021 to The Wall Street Journal article published on October 21, 2021 that raised concerns about the accuracy and reliability of the Company’s user metrics, Facebook’s stock price declined by $54.08 per share, or over 14%, representing a decline of more than $150 billion in Facebook’s total market capitalization.If you were the attorney general of Ohio and you were interested in “looking out for our children,” it is not obvious that the right mechanism for that would be to try to recover billions of dollars of damages for Meta shareholders? Those shareholders are the ones who enjoyed the profits that Facebook was allegedly maximizing “at the expense of the safety of its users and the broader public.” Arguably if you are a state attorney general you should be protecting the broader public from Meta and its owners, not trying to recover more money for Meta’s owners. But this ship has sailed, nobody thinks it’s weird, everything is securities fraud.And, sure, fair. Imagine the attorney general of Ohio trying to sue Meta on behalf of children who were negatively impacted by using Facebook and Instagram. He’d have to find the children in Ohio who used Facebook and Instagram, and figure out how sad Facebook and Instagram made them. It would be hard to turn that into a damages claim, especially one with a big dollar number; how much is a child’s sadness worth in dollars? He could seek an injunction — not “pay us money” but rather “change your policies to be nicer to children” — but that would require him to figure out what the right policies are, which is not easy! But if bad documents come out of Facebook and the stock goes down by $150 billion, then that’s a big lawsuit with clear victims (the shareholders) and clear damages ($150 billion). And if Facebook wants to avoid lawsuits like that, well, it can figure out what policies to write so that its stock doesn’t drop again.Byrne Hobart writes that “everything is securities fraud” is “partly a result of how efficiently markets aggregate and share information: it's hard to directly measure the effect of corporate malfeasance on sales or employee retention, especially over long periods. But stock prices react fast, and they represent a guess about the long term. So if you want to know exactly how bad some piece of news was, the only way to rephrase that is ‘how bad was it for shareholders?’”I do not disagree with this but  it continues to be just a weird way to structure a society. Here you have the top law enforcement officer of a state saying that Facebook did things that were bad for society in order to maximize profits for its shareholders. “How bad were those things, for society,” you might ask the attorney general, and his only answer is to measure how much they cost the shareholders. If Facebook harms society, and as a result its stock goes down by $150 billion, society sends it a $150 billion bill.











      The Elon show


Well  there you go:Elon Musk exercised options and offloaded more Tesla Inc. shares, continuing a streak of sales that helped tank the stock last week by the most since March 2020.  The world’s richest person disposed of more than 934,000 shares on Monday for about $930 million, according to regulatory filings. That adds to the $6.9 billion he already sold last week, just after he took an unusual Twitter poll asking whether he should dispose of 10% of his Tesla stake. Part of Monday’s sales were to help pay taxes on the exercise of 2.1 million options.I was puzzled by this last week. Last Monday, Musk exercised 2.15 million options and sold 934,091 shares to pay taxes under a prearranged Rule 10b5-1 plan that he had set up in September. Then last Tuesday through Saturday he dumped 5.4 million more shares, not under the 10b5-1 plan, not as a result of options exercises. “How does that 10b5-1 plan work, anyway,”  I asked; it seemed weird that it would exercise 2.15 million options and sell 934,000 shares on Monday and then stop. “Maybe the plan says ‘exercise 2.15 million shares per week and sell the stock,’” I wrote, but I wondered. Maybe he had canceled the 10b5-1 plan to spend more time on his spontaneous, poll-related, trolling-driven voluntary stock sales? But, no, I guess the plan does say “exercise 2 million-ish shares per week each Monday and sell the stock”? Or close enough. Yesterday he exercised 2,107,672 options and sold 934,091 shares for about $930 million, an average price of about $996.37 per share, all under his September Rule 10b5-1 plan. (Here are the Form 4s.) Tomorrow I assume he’ll be back to dumping stock voluntarily, and then next Monday he’ll exercise 2 million more options, and so on. 


      This is how the stock market works now, you think I am joking but I never joke, everything is much stupider than my attempts to parody it


The other day  I wrote that “The basic issue is that right now everything is dumb. You can complain about that, or you can embrace it.” I said:If you are the CEO of a public company, I want you to consider very seriously going to an investment conference with no pants on. Your stock will go up, your shareholders will be happy and your cost of financing will go down. “Why would my stock go up because I don’t wear pants,” you ask me, and I say, shh, shh, it just will, don’t ask why. “I have my dignity, I am not going to go to an important business conference with no pants on just to amuse some apes on Reddit,” you say, and I say: You are not as committed to maximizing shareholder value as I thought you were.Was I joking? Well, the suggestion was based on, let’s say, alleged fact. But, sure, I suppose I hoped I was exaggerating a bit? Here’s a MarketWatch story from Thornton McEnery:At roughly 1 a.m. EST on Monday, [Ryan Cohen,] the 30-something Chewy co-founder, turned activist investor, turned GameStop chairman, tweeted “eew eew llams a evah I,” which spelled backward reads “I have a small wee wee.”As we’ve talked about in the past, fundamentals can be fun, but nothing moves GameStop shares like an inscrutable tweet from the company’s perceived savior turned actual chairman. ...Many of Cohen’s twitter followers took the backwardness of everything as a signal that Cohen was trying to communicate the opposite meaning, for example, engaging in some public self-care by spending the twilight of Monday morning doing a public affirmation that he indeed has a large “wee wee.”By midday, GameStop shares had climbed up as high as 4.2%, before trimming that advance.McEnery advances a Straussian reading of the tweet, arguing — I swear — that Cohen might have meant to reference the “South Park” catchphrase “Oh my God, they killed Kenny,” because Reddit meme-stock investors “have made Citadel founder Ken Griffin into their prime enemy, re-christening him as ‘Kenny G’ or simply ‘Kenny.’” Anyway if you are the chief executive officer of a public company and you can add half a billion dollars of market cap by tweeting inscrutably about your anatomy, should you do it? I dunno, you are kind of on your own here.


      NFT Stuff (1)


Technically this is a fungible token but:The Green Bay Packers will hold a stock sale Tuesday, offering shares of “ownership” in the NFL franchise for the first time in nearly 10 years. Funds raised will be used for stadium improvements. An individual can buy a share of the Packers for $300, the sixth time the team has offered shares to fans in its history. The shares have no financial value and can’t be resold. Shareholders of the Green Bay franchise don’t get paid dividends. The stock doesn’t appreciate in value and isn’t transferable, except to family members by gift or in the event of death. Essentially, fans can get bragging rights for owning a piece of the team and a stock certificate commemorating the purchase. Yeah, tell you what, make it transferable, put it on the blockchain, bam, you’ve got a $40 billion market cap. Give the shares voting rights to change the team name and mascot. The Green Bay Bored Apes. This is all going to happen isn’t it.


      NFT Stuff (2)


Sure, pretending to buy the Packers is nice, but now you can pretend to buy the U.S. Constitution:Sotheby’s is auctioning off an extremely rare and historic first-edition printing of the U.S. Constitution, and crypto investors are pooling millions of dollars worth of ether to buy it.An organization known as ConstitutionDAO is raising the money using a digital crypto wallet with the aim of crowdsourcing enough funds to make the winning bid when the document hits the auction block on Thursday night.The foundational text is valued at $15 million to $20 million. Since launching five days ago, the group has thus far raised 967 ether, or $4.3 million.The exercise offers some of the first practical insight into how crypto infrastructure can be used to facilitate fractional ownership of a physical artifact.ConstitutionDAO is a decentralized autonomous organization, or DAO, formed for the sole purpose of putting an original copy of the Constitution back in the hands of the people.Ben Thompson points out that this is all pretty approximate; ConstitutionDAO will not give its token holders fractionalized ownership of the Constitution:The most obvious reason for this limitation is regulatory: issuing ownership tokens with the expectation of a return would make ConstitutionDAO a security; moreover, a DAO is digital, and the Constitution copy is physical, and it is not well established in most jurisdictions how or if a DAO can own physical property. Then there is the fact that Sotheby’s has to follow Know Your Customer (KYC) laws: if the DAO is simply a bunch of anonymous Ethereum addresses how can the auction house satisfy its legal requirements around limiting money laundering?Instead, according to the project’s Purchase Process Details, it appears that the actual bidder for the Constitution will be a just-formed LLC with two members/beneficiaries who may sign a letter of intent to be bound by DAO decisions, but still TBD. It’s also not clear whether or not the founders of the project will take money off of the table …Also, not to be like this, but there is an original copy of the Constitution on permanent display at the National Archives; it is already “in the hands of the people,” in the sense that (1) it is owned by the U.S. government and (2) the U.S. government is, when you think about it, sort of a decentralized autonomous organization made up of the citizens of the U.S.? The citizens can kind of tell the government what to do? By voting? When you think about it? I don’t know. I’m sure that in five years ConstitutionDAO token holders will vote to change the Second Amendment to say “putting laser implants in your eyes is now mandatory” and somehow that will have the force of law.


      NFT Stuff (3)


Here’s a paragraph about  celebrities doing non-fungible tokens:“There are some that are done tastefully i.e. Paris Hilton’s drop with Nifty Gateway, and there are some with poor design, poor launch partners and poor execution,” said WhaleShark, one of the world’s biggest NFT collectors, who bought an NFT from Paris Hilton but is staying away from other celeb NFTs. “The latter tend to come across as money grabs, rather than a true leveraging of one’s fan base to drive NFT mainstream adoption.” A Hilton NFT of a hummingbird that sold for $10,000 in April last sold for $12,000.That sure was a paragraph.


      Things happen


Corporate  Snitching to SEC Surges as Telework Emboldens Tipsters (earlier). Pfizer Moves to Allow Cheap Versions of  Promising Covid Pill. Retirement Fund Giant Calpers Votes to Use Leverage, More Alternative Assets. Third U.S.  Bitcoin Futures ETF Launches After Weeks-Long Delay. The CEO of a $1.45 billion fintech bought an 11-employee small-town bank with a pig mascot. If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] The numbers were actually $1.2 billion and $800 million of 2021 and 2019 convertibles, respectively, plus 15% greenshoe options that were exercised.[2] The bonds were net share settled, a technicality meaning that each $1,000 bond would be paid off on conversion with $1,000 in cash and *the rest* in shares; if the conversion value was $10,000, you’d get $1,000 in cash and $9,000 in stock. Page 20 of Tesla’s 10Q for the first quarter discusses the settlement of these bonds (the “2021 Notes”).[3] For tax reasons, people care a lot about keeping the bond hedge and warrant separate; one way to do this is that the warrant usually has a somewhat longer maturity — by a few months — than the convertible bonds or the bond hedge. Here the bonds matured in March 2021; the warrant matured in 40 equal tranches in June and July 2021. Here is an Internal Revenue Service memo discussing the call options overlay structure and how to optimize its tax treatment; one rough way to put it is that, if you do it right, the amount that the company pays for the bond hedge is tax-deductible but the amount that it gets paid for the warrant is not taxable.[4] It is a little unclear if the warrants covered the same 3.8 million shares as the convertible bond and bond hedge, as is common (see page 79 of the 2014 Form 10K), or twice as many shares, as sometimes happens to increase the value of the warrant (see the 8-Ks announcing the deal and greenshoe).[5] In the real world, the main way the banks in this transaction hedge the warrant is *by being short an offsetting bond hedge*. But here, with convertible bonds that may have converted early due to the huge stock-price run-up, the warrant may have dominated. In any case JPMorgan’s lawsuit, sensibly, talks only about the warrant and ignores the bond hedge.[6] Again, you can read the form confirmation for the warrant transactions here, though it doesn’t say much; the relevant provisions are on page 9 (“Consequences of Announcement Events” and “Announcement Event”). The actual governing provisions, including what I quoted, are in the International Swaps and Derivatives Association Equity Derivatives Definitions, which are incorporated into the confirm for the deal. I have quoted from page 7 of JPMorgan’s lawsuit, which quotes the Equity Definitions; the modifications are mine.[7] Meanwhile, for complicated tax reasons (see note 3), the bond hedge generally will not adjust in the same way as the warrant, so the bank will demand lots of extra value from the client on the warrant but not give it any offsetting value on the bond hedge. “Tax reasons, what can we do,” the bank will shrug.[8] It has done acquisitions — e.g.  of SolarCity Corp. in 2016 — but that would not trigger this adjustment.[9] One crude measure is to take the timeline of the convertible, from roughly March 1, 2014, through March 1, 2021, divide that into pre- and post-tweet periods (i.e. at Aug. 7, 2018), and take the average volatility over the pre- and post-tweet periods. In the post-tweet period, Tesla’s average implied volatility (per Bloomberg page HVT, 30-day at-the-money implied volatility) has been about 66%; pre-tweet it was about 44%. The average 260-day historical volatility numbers are similar. Tesla was about 50% more volatile after Musk pretended to take it private than it was before.[10] These warrants are net share settled; effectively, JPMorgan can pay the exercise price of the warrants with some of the shares it would otherwise get. So the lower the strike price, the more shares JPMorgan gets. 










            Follow Us













              Get the newsletter



























Like Money Stuff? | 
Get unlimited access to Bloomberg.com, where you'll find trusted, data-based journalism in 120 countries around the world and expert analysis from exclusive daily newsletters.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022


















<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cfbcgf.5sud/c2636cc4.gif" alt="" border="0" /></a>
