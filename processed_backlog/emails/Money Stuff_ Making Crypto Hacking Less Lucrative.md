# Money Stuff: Making Crypto Hacking Less Lucrative

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Thu, 20 Oct 2022 13:51:56 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Making Crypto Hacking Less Lucrative_Thu,_20_Oct_2022_13-51-56_-0400_(EDT)_183f686ff9870346.eml
**Processed:** 2025-08-24T19:13:07.395916














        Programming note: Money Stuff will be off tomorrow, back on Monday.Finance rewards cleverness. Sometimes this is true in a pleasingly positi











































          Programming note: Money Stuff will be off tomorrow, back on Monday.



      A certain amount of crime



Finance rewards cleverness. Sometimes this is true in a pleasingly positive-sum way; if you can cleverly think up a new way to slice cash flows or allocate risk then you can get rich by increasing economic activity. Often, though, it is true in some straightforwardly zero-sum way: If you have a contract with a counterparty, and you cleverly ferret out a hidden provision in the contract that says that your counterparty has to give you $10 million, then you get $10 million and they lose $10 million. 
We talk quite a lot around here about those stories. Lots of market structure, for instance, falls into this category: If you find a way to buy stock a bit before someone else does, you win and they lose, but not necessarily in a way that makes the world better. It’s just a game that you’re playing with each other. Or: People finding clever readings of credit-default swaps
was a
big theme of this
column for a few
years. Someone buys CDS to bet against (or hedge) the credit risk of a company, and someone else sells them that CDS to bet on the credit of that company, and then the buyer and the seller separately go to the company and say “hey if you press this button right here our counterparty will have to give us $50 million and we’ll give you $20 million of it,” and the company is like “who are you? Sure, I guess,” and it is weird. There are intersections between this stuff and the real economic world — I think that sometimes it is net good for the world, and other times it is net bad — but it mostly feels pretty abstract. Some hedge funds are trying to trick each other using finance and that’s just their business.
There are, in the traditional financial system, constraints on this sort of cleverness. Obviously one set of constraints is, like, it is hard to find arbitrages in markets or flaws in contracts, and the people on the other side are also smart and have good computers and good lawyers and are trying to trick you too. Still, sometimes you will find a winning trade.
Even so, though,   there are a lot of external constraints, constraints of laws and norms. If you find a flaw in a contract that says your counterparty has to pay you $50 million, she might say no. And you might go to court over it, and point to the language that says she has to pay you $50 million, and the judge might say “what, no, this is stupid, it can’t have meant that, get out of here.” The judge will refer to vague ideas — equity, the intent of the parties, the covenant of good faith and fair dealing — to reject your clever reading of the contract. And then you won’t get your $50 million. There is some amount of cleverness that is too clever.
Or if you find some really clever market-structure trick, some button that you can push to reliably make money on every trade, a regulator might show up and accuse you of “market manipulation.” That is a somewhat ill-defined concept, but if you are reliably making money on every trade by being cleverer than your counterparties, there’s a decent chance that you are guilty of it. (And in fact the US Securities and Exchange Commission   seems to think that causing a “manufactured default” in CDS — asking a company to push a button to make your CDS counterparty pay you — is illegal market manipulation.)
Or: About a decade ago, some electricity traders at JPMorgan Chase & Co. read the rule book of the electricity market really closely and  noticed that the rules would reward them for insanely uneconomic activity. They did this insanely uneconomic activity, and were richly rewarded. And then they were even more richly fined by regulators. I once   wrote about this case:
JPMorgan read the rules carefully and greedily, and exploited the rules. It did this openly and honestly, in ways that were ridiculous but explicitly allowed by the rules. The Federal Energy Regulatory Commission fined it $410 million for doing this, and JPMorgan meekly paid up. What JPMorgan did was explicitly allowed by the rules, but that doesn't mean that it was allowed. Just because rules are dumb and you are smart, that doesn't always mean that you get to take advantage of them.
At some very high level of generality, there are the explicit rules — the words of the contract, the mechanisms of the stock exchange, etc. — and then there is a background set of fairness norms. And if you find a way to make a ton of money with a too-clever reading of the explicit rules, the background fairness norms will kick into gear and you will get in trouble. Following the rules is good, but following the rules to absurd places is bad, perhaps a crime.
In crypto … yeesh. In crypto, explicit rules are very popular, and are often coded into computer programs. The rules of a decentralized finance market will be embedded in open-source smart contracts, and you can read them, and if you find a clever way to exploit them — to “hack” the smart contract, or to “manipulate” the market, to use loaded, traditional terms — then you can do that, quickly and efficiently and at scale.
But crypto is also very young, as an industry, which means two things:
	All these smart contracts were written 20 minutes ago, they do not have many years of testing, and some of them will have big flaws that someone can exploit.	There is not long-standing agreement on some set of background norms about what to do when that happens.

And so sometimes there will be a “hack” or “exploit” in crypto and people will say “hey that’s great, the contract worked as written, you’re not allowed to complain.” (Thus the scare quotes around “hack” and “exploit”: Some people will deny that those loaded terms apply.) Other times, people will say “this is unacceptable,” and everyone will get together to  reverse the transactions and act like they never happened. Other times, people will say “hey let’s call the police,” and perhaps the police will come and arrest the “hacker” for hacking or market manipulation or whatever. There are other possible outcomes. I   wrote yesterday, somewhat fancifully, about decentralized autonomous vigilantism as a possible solution to crypto hacks.
Still there does seem to be a developing norm that says “if you hack a decentralized finance protocol and run off with a bunch of money, you can keep some of it as a reward for your cleverness, but you have to return most of it because keeping it all would be mean and perhaps a crime.” The model is a “bug bounty,” though sort of after the fact: If you find a flaw in a protocol’s security, they should pay you a reward for pointing it out, but you should not get to take all their money.
And so we   talked last week about a guy who did a market manipulation on a DeFi protocol called Mango, taking something like $116 million. The guy’s name is Avraham Eisenberg. Here is a post by Chris Brunet rounding up Eisenberg’s alleged Discord posts as he planned this exploit, which include:
	Eisenberg asks: “I’m investigating a platform that could maybe lead to a 9 figure payday. Should I do it”	Someone in the Discord replies “probably … unles it is highly illegal,” and Eisenberg replies “Are there rules these days”	Someone asks “is this just one of those oracle manipulatooor things to drain LPs,” and he replies “Sorta. You take a long position. And then you make numba go up.”

And then Eisenberg himself went on Twitter to issue a “statement on recent events” that might be up there with Satoshi Nakamoto’s Bitcoin white paper as one of the great foundational documents of crypto:

I was involved with a team that operated a highly profitable trading strategy last week.
I believe all of our actions were legal open market actions, using the protocol as designed, even if the development team did not fully anticipate all the consequences of setting parameters the way they are.
Unfortunately, the exchange this took place on, Mango Markets, became insolvent as a result, with the insurance fund being insufficient to cover all liquidations. This led to other users being unable to access their funds.
To remedy the situation, I helped negotiate a settlement agreement with the insurance fund with the goal of making all users whole as soon as possible as well as recapitalizing the exchange. 

Mango built a game, and Eisenberg played that game in a highly profitable way, and as a result he got $116 million and the game ended. But now he will give back some of the money so the game can continue for everyone else.
You can imagine a lot of different background norms working here. “Code is law, anything that happens is fine, and adversarial hardening will over time make hacks less likely” is definitely  a popular take in crypto, and maybe it’s fine. But my sense is that if you want crypto to be a big industry, if you want it to be appealing to retail investors and large institutions and governments, you will want some other norm. Some norm like “if there’s a hack, someone will fix it.”
Sam Bankman-Fried runs the crypto exchange FTX, and his net worth is pretty directly tied to broad retail, institutional and governmental adoption of crypto. Bloomberg’s   Joanna Ossinger reports:

Crypto billionaire Sam Bankman-Fried has outlined a framework for limiting the impact of the hacks and exploits plaguing the industry, including capping the maximum bounty for attackers at $5 million. …
Bankman-Fried, co-founder of digital-asset exchange FTX, proposed in a blog post what he called a “5-5 standard” where hackers keep either 5% of the amount they’ve taken from a protocol or $5 million, whichever is smaller.
Other key provisos are that customers must be made whole and that the hacker is acting in “good faith” and fully intended to cooperate and return most of the assets. In crypto, attackers are sometimes viewed as white-hat hackers who seek to expose vulnerabilities in return for a reward rather than to make malicious gains.

Here is the rest of  that post, which consists of Bankman-Fried’s draft proposals for “a set of standards that we as an industry could enact to create clarity and protect customers while waiting for full federal regulatory regimes,” covering things like sanctions, disclosure, securities regulation, decentralized finance, etc. But I suppose the proposed standardization of hacking rewards is the most interesting part. The idea is to have rewards for cleverness that are generous, but not absurd, to reward cleverness without making clever hacking the entire point of the game.
Of course this doesn’t solve everything. For one thing, how do you make hackers follow the industry standards? If a hacker/exploiter/manipulator comes up with a really good trade and steals $500 million, and decides not to give back $495 million of it, what do you do? I suppose the answer is “call the police,” and then you are back to relying on the background norms of the traditional legal system.
Also: What if you find a “highly profitable trading strategy” and you “believe all of [your] actions were legal open market actions, using the protocol as designed,” but others disagree and think you did a hack? “The maximum reward for market manipulation is $5 million” is a fine standard, but you still have to have some way to decide what is “market manipulation” and what is just clever trading.























































      Oh Elon



I guess he’s closing?

Elon Musk said he and other investors are “obviously overpaying” for Twitter Inc.
Tesla Inc.’s chief executive officer said he is “excited about the Twitter situation,” describing the social media company as an asset that has “sort of languished for a long time” but has “incredible potential.”
The company’s long-term potential is an “order of magnitude greater than its current value,” Musk’s said on Tesla’s quarterly earnings call Wednesday.

Of course if he is planning to change his mind at the last minute — if he is going to show up at
4:59 p.m. next Friday and say “nope, can’t close, turns out there are bots on Twitter” — then talking up the value of Twitter this week would make it even funnier. So you never know. But, probably, closing.
Is he overpaying? Leaving aside all of the legal wrangling, Musk’s deal for Twitter is a strange bit of merger economics. You could tell a story that goes something like: 
	Twitter is worth about $20 billion.
  [1]

	When Musk buys it and spruces it up, it will be worth $200 billion, an order of magnitude more, in the same ballpark as Meta Platforms Inc.	There is absolutely no way that Twitter can make itself worth more than $20 billion without Musk. Whatever Musk will do to make Twitter worth $200 billion is something that only he could do; Twitter cannot implement his plan, or some other plan, or hire better executives, or restructure itself, or do anything else on its own that will create anything like the value he can.

There are merger stories like that, where the buyer has some plausible way to extract significant synergies from the target. You combine the target’s widget business with the buyer’s sprocket business and you can cross-sell widget/sprocket combinations at a huge premium, etc. The target is worth $20 billion on its own, but $30 billion combined with the buyer, and only the buyer can create that combination.
But Musk is not a big corporation doing a strategic deal — he’s a guy — and there are no obvious synergies between Twitter and his other businesses (cars, rockets, tunnels, brain implants). On the   Tesla earnings call, Musk was asked “With your pending acquisition of Twitter and your stakes in SpaceX and Neuralink and Tesla, how much would the combined companies benefit from operating under a single super structure, if at all, like a Google Alphabet?” And he replied “It’s not clear to me what the overlap is. It’s not 0, but it’s — I think we’re reaching.”
Also Musk has given  some indication of his plans for Twitter, and there is no obvious roadmap to $200 billion. It’s all stuff — charge for some features, try to get more users — that Twitter’s existing management could have thought of, and probably did.
But Musk, in this story, has some magic power: He can create tens of billions of dollars of market value by waving a magic wand, in a way that no ordinary mortal can replicate or even understand. I, uh, I guess I almost believe that? “The way finance works now is that things are valuable not based on their cash flows but on their proximity to Elon Musk,” I have   often written. I call this the Elon Markets Hypothesis. It seems to be   what motivated his co-investors to join him in the Twitter deal. Musk creates value out of thin air. Twitter is bad now, but it has incredible potential, and only Musk can unlock it.
In a typical strategic merger there will be some negotiation over the allocation of synergies. The target is worth $20 billion on its own, it will be worth $30 billion if the buyer buys it, and the target will want to get some of that $10 billion for its own shareholders. That $10 billion is created by the combination; neither the buyer nor the target can get it on their own. If the buyer pays $25 billion for the target, it isn’t “overpaying”; it’s sharing the synergies. In a rough sense I suppose that happened here. Twitter is worth $20 billion on its own, and $200 billion with Musk’s magic. Most of the value comes from his magic, but he does need Twitter to do the magic on. He’s paying more than it’s worth now, but less than it’s worth to him.












      The SEC is busy



A somewhat exaggerated model you could have for the US Securities and Exchange Commission under its current chair, Gary Gensler, is that Gensler wants to remake all of securities regulation all at once. He wants to create a new   environmental disclosure regime for public companies that is roughly parallel to the SEC’s existing financial disclosure regime, more or less doubling the amount of corporate disclosure regulation that the SEC does. He wants to   scrap the existing system of US equity market structure — where brokers route retail orders to wholesalers — and replace it with something different and uncertain (auctions for every trade?). He wants to extend some version of the rules that apply to public companies and funds to   private companies and funds. Those are probably the biggest ones, but there are like a dozen other pretty big ones. Changing   CDS regulation and   10b5-1 plans and   activist disclosure and lots of other things. Also   there is crypto.
You could imagine the SEC’s staff loving this. “Finally, after years of not remaking securities regulation, we’ve got something exciting to do!” But it is easier, for me, to imagine most of the staff finding this very annoying. For one thing, they have worked there for a while, and they presumably have a certain fondness for existing securities regulation, a certain investment in it. When the new boss comes in and says “sorry, all of securities regulation is wrong, we’ve got to scrap it and start over,” it is hard for the staff not to hear that as an insult. That securities regulation is, in some sense, their securities regulation; they interpreted and enforced and defended those rules for years, and they wrote some of them. They took some pride in the system of securities regulation that they worked on every day. And now their boss says they were wasting their time.
For another thing, it’s a lot of work, rewriting all of securities regulation from scratch! Gensler wants to do it, but he’s not the one writing all the rules and doing the cost-benefit analyses. The staff was going along, working at their full-time jobs, and now Gensler wants them to keep doing those jobs while also rewriting all of regulation. Why wouldn’t that be annoying?
The  Wall Street Journal reports:

The Securities and Exchange Commission’s fast-paced rule-making agenda under Chairman Gary Gensler has stretched staff resources, and some officials worry it could increase the risk of lawsuits, the agency’s internal watchdog said in a recent report.
In meetings with the SEC’s inspector general, managers at the agency expressed concerns about short deadlines for staff to draft proposed rules and for public stakeholders to submit comments on them, according to the Oct. 13 report. Mr. Gensler’s rule-making teams have borrowed staff from across the agency, making it difficult to complete other parts of the SEC’s mission, managers reported.
While no one identified concrete errors in rule proposals, some managers told the inspector general that “the more aggressive agenda…potentially limits the time available for staff research and analysis, and increases litigation risk.”

The staff’s complaints are not proof that Gensler is wrong, but you can see why they’d be annoyed.



      YOLO



In my experience nobody has a more colorful prose style than equity volatility strategists. There’s something about writing about volatility that makes your writing volatile? Here’s   Bloomberg’s Tracy Alloway on institutional investors trading short-dated options, quoting Charlie McElligott, a strategist at Nomura Securities International Inc.:

“YOLOing into 0 and 1 Days-Til-Expiration (DTE) options has now been ‘institutionalized’ by vol traders at many of the largest funds on the Street,” McElligott wrote in a note to clients. “It’s not about retail-alone playing this game anymore.”
“We have seen witnessed some absolutely biblical usage of 0DTE and 1DTE options, and it’s acting like jet fuel being dumped on the already out of control ‘macro’ fire occurring into persistent ‘negative gamma’ momentum overshoot flows,” he added. “Using the certainty of dealer hedging flows that their orders create to then amplify and ‘juice’ the intended directional market move … before closing-out positions mere hours later by end of day.” 

Biblical jet fuel is juicing the flows of fire! Love it. More, please:
“Most critically as it relates to the outrageous ranges and swings this past week in US equities and into the upcoming expiration, it is the staggering amount of (negative) front-delta into Friday’s [options expiry] that has then needed to be traded on the approach, which is then acting as further shadow-convexity in the market,” he says. 
Ahh so good.
Look. Retail investors on Reddit have been saying for years that there is a viable trading strategy that goes like this:
	You buy short-dated out-of-the-money call options on a stock.	This forces options dealers to buy that stock to hedge the options.	This pushes the stock up.	As the stock goes up, the dealers need to buy even more of the stock to remain properly hedged.	This pushes the stock up more.	As the stock goes up, your call options are more valuable.	Congratulations, you have created a self-fulfilling trade. You can’t lose.

When I first heard this theory,   I was skeptical. Yes, right, at some level this is a correct description of how dealers hedge call options: They buy some stock to hedge options that they sell, and then buy more stock as the price goes up. But there is a lot of other stuff going on in the market, and it seems implausible that retail investors buying stock options would be able to push around the price of a big liquid stock like Tesla Inc. And the effect of dealer hedging goes both ways: If the stock goes down, dealers will sell some of their stock to remain properly hedged, which will push it down more. You are not getting a free lunch. The idea that this would just work, as a self-fulfilling automatic money maker, seemed absurd.
I mean, it is absurd, but after January 2021 I am more open to the possibility that it happens. Did retail investors buy a ton of short-dated out-of-the-money call options on GameStop Corp.,   causing dealers to hedge by buying a lot of the stock and pushing its price up to insane heights? Uh …   maybe? That’s what they said they did, and the stock sure did go up, though the SEC’s report on the GameStop phenomenon   mostly discounts this “gamma squeeze” story.   Others disagree, and all in all I think it is more plausible than it used to be that retail investors can push stock prices around with a lot of options buying. Boy is that not investing advice.
So if you tell me now that professional investors are YOLOing 1-DTE options to push the stock up and automatically make money, “using the certainty of dealer hedging flows that their orders create to then amplify and ‘juice’ the intended directional market move,” my reaction is sure, whatever, I guess that’s a thing now. 



      Things happen



This  Powerful BlackRock Team Has the Ear of Governments and Megabanks. A Fed President Spoke at an Invite-Only, Off-the-Record Bank Client Event. Retail investors take  shelter in cash after stock market rout. LNG  Freight Rates Hit $450,000 a Day as Russia Disrupts Fuel Supplies. Elon Musk’s Starlink Is at the Forefront of a   Corporatized Space War in Ukraine. How the  warehouse boom devoured America's workforce. Latest   Times Square Attraction Could be a Caesars Palace Casino. Weed Is Coming to   Circle K Gas Stations in US Next Year.  Bees unleashed in attack on deputies during eviction enforcement, Hampden County sheriff says. Congratulations  lettuce.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!

  [1] All the numbers here are fake. It was worth significantly more than $20 billion before Musk signed a deal to buy it, some of
Musk’s co-investors now think it is worth much less, and its current market value of about $40 billion is based on Musk’s deal price rather than its standalone value. Twenty billion is a decent wild guess at its current standalone market value, but if you said $10 billion or $40 billion that would be fine too.











            Follow Us













              Get the newsletter



























Like getting this newsletter?
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022


















<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23chizwe.685j/a7502939.gif" alt="" border="0" /></a>
