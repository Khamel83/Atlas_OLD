# =?utf-8?B?TW9uZXkgU3R1ZmY6IERvbuKAmXQgQnV5IHRoZSBCYWQgRGF0YQ==?=

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Wed, 15 Sep 2021 12:51:11 -0400 (EDT)
**Source:** inputs/saved_emails/=utf-8BTW9uZXkgU3R1ZmY6IERvbuKAmXQgQnV5IHRoZSBCYWQgRGF0YQ===_Wed,_15_Sep_2021_12-51-11_-0400_(EDT)_17bea616f0b9e003.eml
**Processed:** 2025-08-24T19:13:04.077186








































          Programming note: Money Stuff will be off tomorrow, back on Friday.


      App Annie


Here is a thing that, I suspect, keeps a lot of hedge fund lawyers up at night. Your hedge fund is in the business of getting “edge.” It wants to know things that other people do not know, in order to buy the stocks that will go up. One way to get edge is to bribe the assistant treasurer of a public company to give you the company’s earnings release in advance, but this is strongly disfavored and your hedge fund has effective policies against it. Another way to get edge, quite popular these days, is to buy “alternative data.” Somebody has a satellite and they fly it over mall parking lots and count up the cars in front of each store, and you pay them and they give you those numbers, and then you buy the stocks of the stores with lots of cars in front of them, and then a month later those stores announce good earnings and you make a profit.The car-counting is a classic story of alternative data, but the way alternative data mostly works in practice is that a lot of people use apps on their mobile phones, and everyone involved in the mobile app business is harvesting data and frantically selling it to each other and to hedge funds. So basically the “alternative data” that your hedge fund buys is of the form “this many people used this company’s app,” or “people spent this much on this company’s products through apps,” or “phone location data shows that this many people walked into this store,” or whatever. Someone in the app business collects that data and then sells it to hedge funds, including yours. And you use this mobile-app data to get a sense of how many people are interacting with some company, so you can buy or sell that company’s stock.Now, if you bribe the company’s assistant treasurer to get an early peek at an earnings release, that is clearly “insider trading.” It is illegal, the bad kind of edge. As I  like to say, insider trading is not about fairness; it’s about theft. Someone (the company) owns the information (the earnings release); somebody else (the assistant treasurer) takes it, in breach of a duty to the owners of the information, and gives it to you illegitimately. So you are trading on illegally obtained information and get in trouble.What about that mobile-app data that you’re buying from an alternative data provider? Well, it is nonpublic information: Not everyone has it, which is why you want it; it gives you an edge.[1] But the question is whether you got it illegitimately, which means, whether the data broker owned the data and had the right to sell it to you. I think that is a complicated question? Roughly speaking:	If the people using the apps give the apps permission to track them, and the companies that make the apps give permission to the aggregators to aggregate them, and the aggregators give permission to the data vendors to sell their data, and the vendors sell the data to you, fine, great. Everybody has consented to the use of their information, so you can use it freely.	If at any point in that chain — which can have more or fewer links than I wrote in the previous paragraph — someone doesn’t give permission, then the data is misappropriated. If you use that data in your trading, you are insider trading, trading based on misappropriated material nonpublic information. Also the person doing the misappropriating — the person passing along data without permission — is also engaged in insider trading, if they know that you’re going to be using it to trade.So if an app says “we don’t sell your data,” and then it sells that data to hedge funds, that data is arguably misappropriated? Arguably it is material nonpublic information that belongs to the users of the app, and is sold to hedge funds without their permission? Or if people click a box in an app saying “sure go nuts sell my data to anyone,” and the app sells the data to some third-party service, but the app’s contract with the third-party service says “don’t sell any of this data, in an identifiable form, to hedge funds,” and the service does that, then, again, that’s misappropriation and possible insider trading.And so as the general counsel of a hedge fund you do due diligence, and you ask the alternative data provider questions like “did everyone give informed consent to you collecting this data and selling it to me, a hedge fund?” And they say yes, and you hope they’re telling the truth, and you examine their contracts and the apps’ terms of service and so forth to make sure that the chain of data is reasonably clean. But you probably always worry a bit because, I don’t know, the whole business of apps selling data to each other does seem like it is not founded on best practices of fully informed consent?Yesterday the U.S. Securities and Exchange Commission brought a pretty important enforcement action against a company called App Annie Inc. and its former chief executive officer, Bertrand Schmitt; Schmitt and App Annie settled for about $10 million. App Annie got data from apps and sold it to hedge funds without using best practices of fully informed consent:According to the SEC's order, App Annie is one of the largest sellers of market data on mobile app performance, including estimates on the number of times a particular company's app is downloaded, how often it's used, and the amount of revenue the app generates for the company. Trading firms commonly refer to this type of information as "alternative data" because it is not contained within companies' financial statements or other traditional data sources. The order finds that App Annie and Schmitt understood that companies would only share their confidential app performance data with App Annie if it promised not to disclose their data to third parties, and as a result App Annie and Schmitt assured companies that their data would be aggregated and anonymized before being used by a statistical model to generate estimates of app performance. Contrary to these representations, the order finds that from late 2014 through mid-2018, App Annie used non-aggregated and non-anonymized data to alter its model-generated estimates to make them more valuable to sell to trading firms.The order further finds that App Annie and Schmitt misrepresented to their trading firm customers that App Annie generated the estimates in a way that was consistent with the consents it obtained from companies that shared their confidential data, and that App Annie had effective internal controls to prevent the misuse of confidential data and to ensure that it was in compliance with the federal securities laws. According to the SEC's order, App Annie and Schmitt were aware that trading firm customers were making investment decisions based on App Annie's estimates, and App Annie also shared ideas for how the trading firms could use the estimates to trade ahead of upcoming earnings announcements.It is a little hard to tell what people thought was going on. Basically if you are a company with an app, you can use an App Annie product for free to, like, see how good your app is:App Annie provides a free analytics product called “Connect” to companies that offer apps, including public companies, which enables those companies to track how their apps are performing. As a condition of their use of Connect, those companies provide App Annie with their app store credentials to allow App Annie to collect their confidential app performance metrics (“Connect Data”). App Annie tells Connect users that it will generate estimates of app performance using their Connect Data, but that it will only use Connect Data in aggregated and anonymized form to generate those estimates.And if you are a hedge fund you can buy App Annie’s “estimates” of app performance, which you can then use as part of your own modeling of the company’s financial performance:App Annie’s business model relied on selling estimates of how apps belonging to certain companies were performing. App Annie sold these estimates through a paid subscription product called “Intelligence,” which included “Store Intelligence” (for estimates of app revenue and app downloads) and “Usage Intelligence” (for estimates of app usage). Paying subscribers were companies that offered apps and trading firms, such as hedge funds. During the relevant period, substantially all of App Annie’s revenue was derived from selling Intelligence estimates to these subscribers. …App Annie’s marketing materials encouraged “investors” and “finance professionals” to use Intelligence estimates to “inform their investment strategy.” App Annie’s website claimed that investors could “make more informed decisions about existing positions” by “benchmark[ing] the performance of public app companies against key metrics including user engagement, revenue and growth.” Schmitt occasionally participated in meetings with existing and prospective trading firm subscribers, and some of the materials used in these meetings pitched that Intelligence estimates could help with “financial modeling,” “sharpen earnings forecasts with estimated downloads and revenue inputs,” and “identify investment opportunities.”As far as I can tell these “estimates” worked like this:	App Annie used aggregated anonymous data from the apps it tracks to build a statistical model of how apps with certain characteristics perform.	It used that model to generate an estimate of how each particular company’s app performed.	Then it checked that estimate against how the app actually performed, which it knew, from collecting that app’s data, and corrected the estimate to reflect the actual performance.Arguably steps (1) and (2) were unnecessary, from a performance-estimation standpoint? Like, you just have the answer; why build a statistical model to estimate it? But they were important from a selling-data-to-hedge-funds standpoint: App Annie “represented to Intelligence subscribers that Intelligence estimates were generated through a statistical model that used aggregated and anonymized Connect Data, and that Connect users had consented to App Annie using their confidential data in this way.” And in fact the Connect users — the companies — had consented to App Annie using their data in that way.[2] But that’s not how App Annie used it, or at least, not the only way:Beginning at least in 2014, in an effort to make the Intelligence estimates closer to the actual app performance metrics, App Annie created a manual process whereby a “Delivery Team,” which consisted of a subset of App Annie engineers based in Beijing, China, made manual alterations to estimates generated by the statistical model before they were delivered to Intelligence subscribers. Schmitt was aware of and approved the creation and use of this manual alteration process.The Delivery Team manually altered the estimates for apps that were of greatest interest to App Annie’s highest-paying subscribers. When App Annie received complaints from subscribers about the inaccuracy of a particular company’s app performance estimates, the Delivery Team was tasked with improving the estimates through this manual process. To make these manual alterations, the Delivery Team looked at confidential Connect Data, including public company app performance data. The Delivery Team was not trained or supervised by anyone in the Company’s Data Science group and did not document which estimates were adjusted or what changes were made. There was no statistical basis for these post-model alterations. The only purpose of these alterations was to make the estimates closer to the actual metrics.Schmitt approved the creation and use of this manual alteration process because he believed it was cheaper and more effective at making the estimates closer to the actual results than a process that would have complied with the Connect Terms of Service, such as having data scientists research and implement improvements to the statistical model itself. I … honestly I sort of sympathize? If you know how much revenue a company got through its app, it seems a bit baroque to have a team of data scientists build a statistical model based on data from hundreds of apps, and refine that model in order to make it more accurately estimate how much revenue the company got through its app, when you can just look at the answer. Like, yes, telling people the actual data is cheaper and more effective at making the estimates closer to the actual results than some more complicated process that does not involve looking at the actual results. This is a very simple business, really, that was rendered a lot more complicated by the desire to wave vaguely in the direction of securities-law compliance.Anyway it’s all fine now:In June 2018, after the Company had learned of the SEC’s investigation, App Annie discontinued all post-model estimate alteration practices based on non-aggregated and non-anonymized Connect Data. The Company also began excluding all public company data from its statistical model, consistent with its representations to Intelligence subscribers and Connect users. Around the same time, Schmitt resigned and the Board replaced him as CEO.App Annie eventually implemented a new version of the statistical model underlying the Store Intelligence product that had been proposed by the Chief Data Scientist in or around mid-2016.I actually feel like if you are a hedge fund lawyer this case probably comes as a relief to you? Like, yes, you were buying illegal alternative data, but (1) the data was good and (2) you didn’t get in trouble. App Annie got in trouble, for lying to you, rather than you getting in trouble, for believing them.Which seems fair and good, don’t get me wrong, but you were the one doing the trading. It is not necessarily intuitive that an app-performance-analytics-and-data-aggregation company would get in trouble for securities fraud for using non-aggregated data in its estimates of app performance. App Annie wasn’t buying or selling securities. SEC Commissioner Hester Peirce tweeted in dissent: “This settlement stretches the ‘in connection with the purchase and sale of securities’ requirement under 10b/10b-5 beyond where I think it should go.”[3] I disagree: I think that this is a subtle insider trading case, and the SEC was clever to pursue it and to correctly identify the bad guy (App Annie, which lied to hedge funds to sell illegal data, not the hedge funds, which were deceived and bought the data). But it is not obvious. And I suppose that if you are a hedge fund lawyer, now you are on notice that you should be asking your alternative data providers some tougher questions.






















































      GreenSky


I just want to predict right now that at some point in the future someone is going to borrow money from Goldman Sachs Group Inc. to pay an unexpected medical expense, and they’re going to have a hard time paying Goldman Sachs back, and Goldman Sachs is going to be very understanding and helpful in working with them but it will try to get its money back, and despite all of Goldman Sachs’s efforts to accommodate them the borrower will be unable to pay, and Goldman Sachs is going to, gently and politely and regretfully, take them to court for the money, and there are going to be one million headlines like “WALL STREET TRADING TITAN GOLDMAN SACHS SUES CANCER-STRICKEN SINGLE MOTHER FOR HER LAST PENNY.” I don’t know man,  I don’t know:Goldman Sachs Group Inc. agreed to buy GreenSky Inc. for about $2.24 billion, adding to its Marcus consumer-banking platform a company that offers payment plans to customers with home-improvement projects or health-care needs.Aren’t you tempted to go borrow a bunch of money from Goldman GreenSky to redo your kitchen, and then not pay them back? What are they gonna do?GreenSky: Hi we were calling about your loan?You: Sure.GreenSky: Were you planning to pay it back?You: Oh no, no no no no no. No. No indeed, not at all.GreenSky: Hmm. Well of course we respect your viewpoint and want to work with you here, but I must warn you that if you do not pay back your loan we may have to report you to credit agencies and perhaps even sue you.You: Don’t you work for Goldman Sachs?GreenSky: Technically, yes, as of Tuesday.You: I am just a regular Main Street borrower trying to get by in this economy and install nice quartz counters, and GREAT VAMPIRE SQUID GOLDMAN SACHS IS RELENTLESSLY JAMMING ITS BLOOD FUNNEL INTO ME?GreenSky: You did borrow the money. Like a month ago.You: If I ever hear from you again I am going to go to the press.The press: Hi, sorry, I could not help overhearing. Did you say that Goldman Sachs was threatening you? This is obviously not legal or financial or interior-decorating or media-relations advice but, man, I do feel like Goldman’s consumer buy-now-pay-later kitchen-remodeling-and-medical-expenses business is gonna be real gentle in its collection efforts for a while.[4]I could be wrong, though; my associations with Goldman come largely from working there (disclosure![5]) before, during and after the global financial crisis of 2008. For a while after the crisis Goldman was by far the most publicly hated bank (the vampire squid thing, etc.), for reasons that were pretty mysterious to me but that might have had something to do with the fact that it didn’t have much of a Main Street presence. Nobody had a checking account at Goldman, nobody bought their house with a Goldman mortgage, so nobody had a face to put to the Goldman name and everyone just assumed they were evil.Getting deeper into the consumer business, besides being a business move, is an interesting public-relations choice for Goldman, a gamble that people will feel fonder about Goldman if they actually interact with it. I don’t know that that’s generally true of banks! But that’s an opportunity too: You don’t have to be the nicest bank; you just have to be nicer, in the public mind, than, you know,  Wells Fargo & Co. If you don’t do any consumer lending maybe that is hard; if you do some, maybe the bar is low.











      YOLO


Speaking of things that are not investing or legal or media-relations advice:Robinhood Markets Inc., the go-to trading app for young investors, wants its user base to get even younger.The digital brokerage is kicking off a nationwide marketing campaign Wednesday that is designed to turn more college students into Robinhood customers. Robinhood will give students who sign up for brokerage accounts using their school email address $15 to trade, and enter them into a $20,000 giveaway. Robinhood executives will tour campuses of community colleges and historically black colleges and universities this fall. ...Aparna Chennapragada, Robinhood’s product chief, said that the marketing push is a continuation of Robinhood’s long-term mission to make investing accessible to people who hadn’t historically participated in the markets. The campaign, she said, is about “meeting the next generation where they are” and communicating that by starting young, college students can enjoy the benefits of compound returns over decades.Courting students is tricky for Robinhood. Critics say the app has turned trading into a game-like experience that encourages unsophisticated investors to take risks they don’t understand.Yes, if you are 18 and you buy weekly-expiry out-of-the-money call options on GameStop Corp. every week from now until you retire you will definitely compound at a rate of … no honestly I can see the appeal here? For many Americans, college is pretty much going to be the lifetime low point of their net worth: They have no money, aren’t earning anything, and have just taken out tens of thousands of dollars of debt. So they can’t get all that much worse off by day-trading Dogecoin and YOLOing weekly GameStop options.[6] It is an inexpensive and appropriately timed form of investor education: Better to do your wild day-trading with a tiny account in college, get burned, get it out of your system, and then have 40 sadder and wiser years to save for retirement. The way to become a sophisticated investor taking risks that you do understand is mostly to start as an unsophisticated investor, take risks you don’t understand, lose money and learn. Might as well get started on that cheap and early.


      Coinbase Borrow


We  talked last week about how Coinbase Global Inc. tried to roll out a crypto lending program in which its customers would lend it money, it would pay them 4% interest, and it would use the money to, presumably, fund loans to other customers. This was shut down by the SEC, which told Coinbase that if it did this program it would need to register it as a security. Coinbase complained a lot. Anyway:Junk-bond investors gave cryptocurrencies their biggest endorsement yet as Coinbase Global Inc. sold $2 billion of debt.Demand was so high -- at least $7 billion of orders poured in -- that the crypto behemoth was able to boost the deal’s size from $1.5 billion, according to a person with knowledge of the matter.Equal amounts of seven- and 10-year bonds were sold at interest rates of 3.375% and 3.625%, respectively, lower than the initially discussed borrowing costs, other people familiar with the situation said.So that’s cheaper than the lending program, huh? And for a longer term? And, uh, those bonds are definitely securities? (Privately placed Rule 144A securities, but still.) The system works I guess.


      NFT insider trading


Oh sure sure sure:In a statement issued Wednesday morning, leading non-fungible token (NFT) marketplace OpenSea said it uncovered evidence of insider trading by one of its employees.“Yesterday we learned that one of our employees purchased items that they knew were set to display on our front page before they appeared there publicly,” the statement reads. …Allegations of insider trading at OpenSea appeared last night, courtesy of a Twitter account called @ZuwuTV, and it quickly went viral.Here is the statement. Here is the viral tweet, which alleges that an OpenSea employee “has a few secret wallets that appears to buy your front page drops before they are listed, then sells them shortly after the front-page-hype spike for profits, and then tumbles them back to his main wallet with his punk on it.”I just want to say how, like, drab this is. This isn’t “insider trading” in that he knows something about these tokens that no one else knows. There is nothing to know about these tokens! It’s insider trading in that he knows they’re going to be heavily advertised — on the front page of OpenSea — before anyone else does. If your model of NFTs is, like, “these things are good and people want them because they are a new form of art collecting and value accumulation, they have great aesthetic appeal, and they point a way to a technological future where physical goods are owned and traded on the blockchain,” who cares. If your model of NFTs is, like, “every day some new NFT gets hyped and everyone buys it and it goes up, and the next day a different NFT gets hyped and goes up, and it is all a game of hype and market manipulation” then, sure, this guy won the game.I  wrote yesterday that “a lot of actually existing NFTs have almost no consumption value outside of participating in a bubble.” Right? If I were an insider-trading OpenSea employee, I’d mint NFTs representing each of my insider trades on NFTs, and sell those.


      Things happen


ETF Industry Risks  Losing Key Tax Edge as Democrat Whets Knife. Chevron to Triple Low-Carbon Investment. Fidelity Pushed for  Bitcoin ETF Approval in Private SEC Meeting. How  Billionaire Steve Cohen Learned to Love Cryptocurrencies. Crypto bosses say Coinbase is ‘fighting the good fight.’ CN Rail Walks Away From  K.C. Southern, Ending Takeover War. Dogecoin trademark fight. RIP Norm MacDonald.If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] It may or may not be “inside” information, in the colloquial sense of “nonpublic information that comes from the company.” Like the data might come from a public company selling data about its own app’s performance, or it might come from millions of individual users each letting some app harvest data about what they do on their phone. Either way it is nonpublic, which is what matters for insider-trading law.[2] Also, App Annie told hedge funds that it was not using public companies’ material nonpublic information, because that would be awkward from an insider-trading perspective. But it was: “App Annie and Schmitt also represented to subscribers that the Company had internal controls and processes to prevent the misuse of confidential Connect Data and to ensure that App Annie was in compliance with the federal securities laws. For example, they represented that public companies’ Connect Data was not used to generate Intelligence estimates. They understood that, without these representations, trading firm subscribers would not have purchased or used App Annie’s Intelligence estimates in making their trading decisions. During most of the relevant period, however, App Annie did not have effective internal controls and in fact used certain public companies’ Connect Data to generate Intelligence estimates.”[3] Traditionally when an SEC commissioner disagrees with an action taken by the majority of the commission, she will often publish some sort of dissenting statement on the SEC website, but in most cases a tweet is probably sufficient so here we are.[4] Meanwhile, uh: “GreenSky in July reached a settlement with the Consumer Financial Protection Bureau to resolve what the regulator called ‘careless business and customer service practices’ that allowed merchants and contractors to take out loans on behalf of thousands of customers who didn’t ask for them. GreenSky agreed to cancel up to $9 million in outstanding loans and pay a $2.5 million penalty.” Replace the word “GreenSky” there with the words “Goldman Sachs” and ask yourself what page of the newspaper that story appears on.[5] Also I have a Marcus savings account? I don’t know that using a standard banking product is the sort of thing that one discloses but perhaps it is relevant. I have not taken out a kitchen remodeling loan from Goldman, but if I ever do need a kitchen remodeling loan, I will probably go to Goldman GreenSky, send them a copy of this column, and let you all know how that goes. [6] There is a sad exception to this. From the same Wall Street Journal article: “Robinhood settled a wrongful-death lawsuit earlier this year brought by the family of a college student who took his own life after believing he racked up big trading losses on Robinhood.” Obviously Robinhood should (1) make it impossible to rack up big trading losses with a small account and (2) send people accurate account statements; this seems like a low bar but Robinhood has sometimes  failed to clear it.










            Follow Us













              Get the newsletter



























Like Money Stuff? | 
Get unlimited access to Bloomberg.com, where you'll find trusted, data-based journalism in 120 countries around the world and expert analysis from exclusive daily newsletters.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022


















<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cewx41.5l1k/9b81b676.gif" alt="" border="0" /></a>
