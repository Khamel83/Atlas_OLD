# Money Stuff: Goldman Has a Derivatives Robot

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Wed, 25 Oct 2023 14:30:56 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Goldman Has a Derivatives Robot_Wed,_25_Oct_2023_14-30-56_-0400_(EDT)_18b681ab70126fed.eml
**Processed:** 2025-08-24T19:13:11.715439














        Disclosure! I used to sell customized derivatives at Goldman Sachs Group Inc. There are roughly four steps in pricing a complex derivative t





































      Derivatives structuring



Disclosure! I used to sell customized derivatives at Goldman Sachs Group Inc. There are roughly four steps in pricing a complex derivative to show to a client:
	You need a pricing model for that type of derivative. This will be built by quants and will live in the bank’s systems (or on Bloomberg), ready to be applied to particular cases; you pick the model and then fill in the terms of the trade.	You need to get market data (prices, volatilities, interest rates, etc.) to input into the model. This data will be ingested and will also live on the bank’s systems (or on Bloomberg), ready to be used by the model. 	You might need to adjust the market data, somewhat subjectively, to account for the size and risk and liquidity and terms of your particular trade. If your market data feed says that the implied volatility of a six-month 100-share call option is 35%, but you are selling a five-year option on 10 million shares, you might not want to use 35%.	Then the model will give you a price, and you will look at it and ask yourself “how much more can I charge the client for this trade?” If the trade is fairly standard and the client is an aggressive hedge fund with its own model who is bidding out the trade to six banks and will call your boss to scream at her if your price is wide, you will quote pretty much what the model says is fair value. If the trade is unique and the client is an   assistant treasurer at a sleepy corporate client who is grateful to you for taking him out to an occasional steak dinner, you will add like 2% edge to the model price. This is the most important part of the job.


Oh, I kid, probably programming the model (Step 1) is the most important part; if you get that wrong then you have huge systemic problems. But the quants do that. At the level of derivatives sales, nudging the price up to what the client is willing to pay is what earns you your bonus.
  [1]

Anyway Steps 1 and 2 are fairly deterministic; there are broadly accepted ways to price derivatives and to obtain and clean market data.
  [2]
 Step 3 requires a certain intuitive feel for markets, and for risk, and for the firm’s positions and risk appetite. That feel typically comes from thoughtful experience in the markets, but could it also come from, like, a regression? Sure? This pattern recognition seems like the sort of thing an artificial intelligence could get good at.
Step 4 requires a certain intuitive feel for the client. Again, typically from experience with clients, but could a robot figure out “show tight prices to big hedge funds and wide prices to sleepy corporate treasurers”? Sure? Could the robot take the assistant treasurers out to the steak dinners? You probably still need salespeople for something.
Bloomberg’s William Shaw   reports on Goldman’s current plans for selling customized derivatives:

Goldman Sachs Group Inc. is expanding its use of a technology that leverages artificial intelligence in the hopes that it will make it easier for clients to plan complex derivatives trades.
After already using the software to shake up the worlds of equities and foreign exchange options, the firm in recent weeks began allowing clients to use its visual structuring product for credit derivatives. It’s aiming to offer the service for rates trading in the first half of next year, Chris Churchman, who runs Goldman’s digital trading platform Marquee, said in an interview.
The product, which Goldman began offering last year, helps institutional clients with price discovery and trading ideas. It also assesses the risks of a given trade and can gauge the chances that the trade will pay off.
To do so, the offering uses neural networks, which learn through trial and error like a human brain, as well as natural language processing, which deciphers vast troves of speech and text, to price some complex trades. …
For instance, if a client is interested in trading a particular asset, the system can quickly analyze how that asset’s current premium compares to past periods. The system can also instantaneously price different variations of a trade, predict when it might pay off and show how that investment might behave as the prices of other assets move.

Okay. I guess my question is, do the neural nets know how much to charge? Like if you log on to this thing and do a ton of sophisticated modeling and price up a bunch of slightly different variations to minimize premium, does the neural net think “huh this person is gonna fight for every basis point” and start showing you tighter prices? If you log on to this thing and, in the natural-language input box, you type “what is derivative,” does the neural net gleefully rub its little electronic hands together and say “ooh this is gonna make my year”?
  [3]






























      SBF Stuff: Testimony



 Obviously:

Sam Bankman-Fried will take the stand to defend his actions in the lead-up to the collapse of his digital-asset empire, after taking a beating from former colleagues who painted him as the mastermind of a years-long scheme to defraud customers and investors.
Bankman-Fried’s lawyers told the judge on Wednesday that their client will testify in his own trial when they start their defense case later this week.

There are kind of two theories of criminal trials in the US:
	The prosecution has the burden of proving that you did a crime. They put on a case, and your lawyers pick holes in it, trying to create “reasonable doubt” in the minds of jurors. The jury then goes back and decides whether the prosecution has proven its case beyond a reasonable doubt. If yes, you are convicted. If they are not sure, you are acquitted.	The prosecution tells a story (in which you did a crime), and your lawyers tell a different story (in which you are innocent). The jury then goes back and decides which story is more compelling. If it’s the prosecution story, you are convicted. If it’s your story, you are acquitted.

Theory 1 is correct, as a matter of law; that is how the law is supposed to work, and what the judge’s instructions to the jury will say, and what happens in Twelve Angry Men, and how a lot of criminal defense lawyers think about things.
In particular, criminal defense lawyers will be very cautious about telling their own competing story, because they will not want the jury to compare stories. As a matter of legal theory, if jurors look at two competing stories and say “we think the prosecution is 70% likely to be right and the defense is 30% likely to be right,” then they should acquit, because that is reasonable doubt. But faced directly with the two stories, they might be inclined to pick the more compelling one; they might convict because the prosecution’s story is somewhat better than the defense’s. And so defense lawyers will resist giving the jurors a head-to-head comparison; they will focus on holes in the prosecution’s case, so they can emphasize “the prosecution’s story is not true beyond doubt” rather than the harder “our story is better than theirs.”
I have always been partial to Theory 2 anyway. People like stories! Jurors will be tempted to pick a flawed story from the prosecution over no story from the defense. They are sitting in the courtroom, you are sitting at the defendant’s table, they are going to assume you did something wrong. You have to give them an innocent explanation of how you came to be there. You have to give them something to feel good about if they are going to acquit.
This is just idle musing, and I am probably wrong in the general case. But this case is easy! The prosecutors have basically all of Sam Bankman-Fried’s colleagues testifying “we did tons of crimes because Sam told us to.” They have the computer code for FTX, which is   strikingly crime-y for computer code. Even if they didn’t have any of that, they have the brute facts of:
	Customers put billions of dollars into FTX.	Sam Bankman-Fried spent billions of dollars on luxury real estate and political campaigns and celebrity endorsements and personal investments.	The customer money is gone.

You really don’t need anything else for a jury to be like “ooh yeah that story is bad”! If the defense’s closing argument is, like, spending six hours poking holes in the witnesses’ testimony, that doesn’t help! There’s too much of it! The jury can be like “sure yes the defense raised some doubts about 200 of the 1,000 pieces of evidence against him but, still, man, not good.”
Meanwhile Sam Bankman-Fried   has a competing story in which the money vanished through a combination of unexpected crypto market moves and innocent accounting mistakes. Is this as good a story as the prosecution’s story? No! Is it his only chance of winning? Obviously!



      SBF Stuff: Toward a general theory of scammers



“I don’t think SBF knowingly stole customer money,”  said Michael Lewis on 60 Minutes, and “he believes he is innocent.” If Lewis is correct then that will probably help him testify: If you’re going to be subjected to withering cross-examination about the crimes you did, it helps if you believe that you are innocent.
Is Lewis right? I think so! But that is, I think, the normal state for a scammer.
  [4]
 Financial scams are in their essence about self-deception; you can’t be a great scammer without being at least somewhat deluded yourself.
  [5]
 Classically financial scams work along these lines:
	There is a financial business that takes money from investors, customers, creditors, etc., and promises to give it back, usually with some return.	The person running the business has at least some discretion over what he does with the investors’ money. (Practical discretion — he has the password to the bank account — if not actual legal discretion.)	He makes bets with that money, with the intention of (1) getting back at least enough money to pay back his investors (and any promised return) and (2) keeping any extra winnings for himself.
He convinces himself this is fine. He can’t lose! He’s so good at making bets, and these bets are so safe, and anyway the clients would want him to do them, and also really aren’t they disclosed in the fine print of the clients’ account agreements? 

The popular imagination of scammers, and of Bankman-Fried, is that they steeple their fingers and cackle and say “now to steal some customer money to buy mansions.” But why would that make sense? If you are Bankman-Fried and you are knowingly stealing customer money to buy Bahamas condos, and then everything collapses, why stay in the condos to get arrested? Also if you are knowingly stealing money then of course everything will collapse. Stealing money with a getaway plan? Sure, right, that happens. Stealing money and sticking around? Weird choice.
No, the way to end up in this situation is to steal money while thinking that it’s fine, that you’re not stealing it at all, that you’ll make it all back and then some, that what you are doing with the money (crypto altcoin arbitrage, buying politicians, buying publicity for crypto and your exchange) is necessary and profitable and not even a risk, that any losses are temporary blips. 
The normal way to become a big-time scammer is to combine an unusual appetite for (indeed, blindness to) risk with an unusual self-confidence. And to add an unusually act-utilitarian mindset, in which you are unconcerned with doing things the right way or following the proper procedures, because you care only about the end result.
Does that remind you of anyone? Sam Bankman-Fried’s whole personality was utilitarianism and risk-taking.
  [6]
 He   learned early on to take   every positive-expected-value bet, and from the start he seems to have deluded himself about what bets had positive expected value. The early history of his crypto trading firm, Alameda Research, involved him losing a bunch of investor money, saying “ehh there’s like an 80% chance we get it back,” concluding he could lie to customers about the lost money, and then in fact getting it back and feeling vindicated. He had the most perfect imaginable training for running a big financial scam. 



      SBF Stuff: FTX 2.0



The description above is not often consistent with:
	running a good legitimate business and	making bets, with the customer money, that pay off.

But it is not in principle inconsistent. It’s just that, ordinarily, if you take wild risks with other people’s money, lie to them about what you are doing, delude yourself into thinking that there’s no risk, and the bets pay out and you build a great business and everyone gets their money back, we don’t call you a scammer. We call you an unconventional visionary who moves fast and breaks things.
  [7]
 There is a ton of  moral luck involved in the popular and legal determination of who is a scammer and who is a maverick billionaire.
I do not pretend to understand the finances of the FTX bankruptcy estate at this point,
  [8]
 but it does seem at least possible that Sam Bankman-Fried was (1) running a good legitimate business and (2) making bets, with customer money, that will pay off? We   talked a few weeks ago about FTX’s stake in Anthropic, an artificial intelligence company, which has rapidly increased in value since Bankman-Fried invested, making FTX’s stake worth billions of dollars and going some way to filling the hole in customer funds.
Also though the FTX exchange seems to have been a good enough business that, even now, somebody might pay for it. Bloomberg’s   Steven Church reports:

FTX Trading Ltd. is considering proposals from three bidders to restart trading on what had been one of the world’s biggest crypto exchanges before the company sank into bankruptcy amid fraud allegations.
The company will make a decision about how to proceed by mid-December, the company’s investment banker, Kevin M. Cofsky of Perella Weinberg Partners, said Tuesday during a court hearing in Wilmington, Delaware. FTX is negotiating details of potentially binding offers with investors, Cofsky said.
Options include selling the entire exchange, including a valuable list of more than 9 million customers, or bringing in a partner to help restart the exchange, Cofsky told US Bankruptcy Judge John Dorsey. FTX is also mulling a reboot of the trading platform on its own, he said. …
FTX and its main creditor groups have tentatively settled some of the most difficult disputes in the case, which will allow the company to file a detailed payout plan in December, company attorney Andrew Dietderich said in court.
In bankruptcy, such plans typically give creditors an estimate — expressed as a percentage — of how much they can expect to recover. FTX, however, doesn’t currently know what customers will get back, Dietderich said. The recovery percentage will in part depend on how much value FTX can get from a potential sale, or reboot, of the exchange.

Of course, last November, this is exactly   what Bankman-Fried himself was pitching: He had a pot of weird assets (including Anthropic) and an exchange with some franchise value, and he was trying to sell them as a package for at least a penny more than the customer deposits. He almost got Binance to buy, but then Binance did some more due diligence,  noticed the missing customer money, was like “hmm we don’t want to touch that” and backed out. 
Just the timing of Bankman-Fried’s moral luck is fascinating. If he had managed to find a buyer then, look, this would all still be bad, and probably fraud, and he might even get in trouble. (His venture capitalist investors, for instance, would have complaints if Binance had actually bought FTX for $0.) But it would probably be, relatively speaking, pretty minor trouble. If you lose $8 billion of customer deposits you get in very bad trouble. Unless you find them again before you get arrested! After is no good.
It’s not all luck, though. It is plausible that, now that FTX’s bankruptcy estate is shopping the exchange to buyers, it has a positive value, but when Bankman-Fried was shopping it last year it had a large negative value, because Bankman-Fried was running it then and he’s not now. An exchange that operates pretty well but that is run by a guy who is stealing all the money really is worth less, as a going concern, than the shell of that exchange after he’s gone.



      SBF Stuff: Shadow trading?



There is no news hook here — this is a decades-old academic paper — but it’s news to me: Sam Bankman-Fried’s father, Joseph Bankman, wrote a paper on shadow trading in 2001. Here is “Substitutes for Insider Trading,” by Bankman and Ian Ayres:
When insider trading prohibitions limit the ability of insiders (or of a corporation itself) to use material non-public information to trade a particular firm’s stock, there may be incentive to use the information to trade instead on the stock of that firm’s rivals, suppliers, customers, or the manufacturers of complementary products. We refer to this form of trading as trading in stock substitutes. Stock substitute trading by a firm is legal. In many circumstance, substitute trading by employees is also legal. Trading in stock substitutes may be quite profitable, and there is anecdotal evidence that employees often engage in such trading. Our analysis suggests that substitute trading is less socially desirable than traditional insider trading. We recommend a set of disclosure rules designed to clarify existing law and provide information on the extent of stock substitute trading. We also discuss possible changes in the law that might limit inefficient trading in stock substitutes.
We have   talked before about   shadow trading, as this form of substitute trading is now often called. I have to say, “legal in many circumstances” and “quite profitable” is much better than what Bankman-Fried eventually did get up to.



      Twitter debt



Could  be worse:

The banks that financed Elon Musk's $44 billion purchase of Twitter are still struggling a year later to contain the damage to their balance sheets.
The banks currently expect to take a hit of at least 15%, or roughly $2 billion, when they sell the debt, people familiar with the matter said. That would mean hundreds of millions in losses for those holding the largest pieces, which include Morgan Stanley, Bank of America, Barclays and MUFG. BNP Paribas, Société Générale and Mizuho were also involved.
After holding the debt for a year -- an eternity in the corporate-finance world -- the banks, which had hoped they could sell it by Labor Day, have recently begun preparations to try to unload at least some of it, the people said.

Around the deal’s closing there was talk of banks getting bids at 50 cents on the dollar, so 85 would be pretty good? One purpose of installing Linda Yaccarino as the chief executive officer of Twitter (now called X) is that she can have basically normal conversations with investors as the banks try to sell the debt; investors will say things like “how’s business?” and she will say things like “oh good, good, advertisers coming back, really good.” As opposed to sending Elon Musk to those meetings and having him get bored and start trouble. “How’s business,” investors would ask, and he’d be like “you know what I’ve decided that debt isn’t real” and you’d never get 85 cents on the dollar.



      Crypto ontology



A classic crypto trade is:
	Acquire a ton of Bitcoins cheap in like 2011 and put them in a wallet.	Put the private keys to the wallet onto a password-protected hard drive.	Lose access to the hard drive. The funniest way to do this is by putting the hard drive at the bottom of a giant garbage dump, but the easiest way is just to forget the password.	Watch the price of Bitcoin go up a lot.	Moan a lot to the media about how you have hundreds of millions of dollars of Bitcoins, but you can’t get access to them.

I am not, like, recommending this trade or anything? I don’t know what you get out of it. Mainly attention? But I   wrote about the garbage dump guy in 2021, and I suggested that he could monetize his situation by either:
	Minting non-fungible tokens “of” his discarded hard drive, and selling them to crypto enthusiasts (sorry, it was 2021), or	Just selling heavily discounted shares in his contingent possibility of recovering the hard drive (to raise money to try to recover it, or not I suppose).

Realistically though you are in this trade for attention. You spend a few hundred millions of dollars’ worth of Bitcoins to be known as the guy who threw away a few hundreds of millions of dollars’ worth of Bitcoins? Why. I suppose another possible trade is, just pretend to have the inaccessible hard drive? Nobody else is going to dig up the dump to check.
Well, here’s a weird Wired story about a password-forgetter:
For years, Unciphered's hackers and many others in the crypto community have followed the story of a Swiss crypto entrepreneur living in San Francisco named Stefan Thomas, who owns this 2011-era IronKey [encrypted thumb drive], and who has lost the password to unlock it and access the nine-figure fortune it contains. Thomas has said in interviews that he's already tried eight incorrect guesses, leaving only two more tries before the IronKey erases the keys stored on it and he loses access to his bitcoins forever.
Unciphered is a startup that has figured out how to get his password without wasting any guesses, so they called him up and offered to do it, and he was like “nah I’d be happier not knowing”:

Earlier this month, not long after performing their USB-decrypting demonstration for me, Unciphered reached out to Thomas through a mutual associate who could vouch for the company’s new IronKey-unlocking abilities and offer assistance. The call didn't even get as far as discussing Unciphered's commission or fee before Thomas politely declined.
Thomas had already made a “handshake deal” with two other cracking teams a year earlier, he explained. In an effort to prevent the two teams from competing, he had offered each a portion of the proceeds if either one could unlock the drive. And he remains committed, even a year later, to giving those teams more time to work on the problem before he brings in anyone else—even though neither of the teams has shown any sign of pulling off the decryption trick that Unciphered has already accomplished.

Okay sure. “You might not [want the help] if the whole thing was a hoax to get attention with a too perfect to fact-check crypto-boom-era tale about a Mission: Impossible style self-destructing thumb drive,”  writes Rusty Foster. It would be funny if he had sold shares in the Bitcoins on the thumb drive, and unlocking the thumb drive would reveal that they’re not there and the shares were worthless. So many of the crypto-boom-era stories are turning out to be less than they seemed.



      Things happen



Weinstein   Ups Sculptor Bid Again in Bidding Fight With Rithm. Private Equity Wants a Piece of Your Retirement Savings.  Deutsche Bank pledges to raise investor returns on promising results. The Corporate  Retreat From Hong Kong Is Accelerating. China Developer   Country Garden Deemed in Default on Dollar Bond for First Time. UBS to Lay Off   Credit Suisse Investment Bankers in Spain.  Hipgnosis board under pressure as music pioneer faces crucial vote. Michael Cohen tells court he ‘reverse engineered’ Donald Trump’s financial statements. CFA Final Exam Pass Rate Slips to 47%, Below Historic Average. Restaurant Owners Are Fed Up With   Reservation-Hoarding Bots. “Around $6 million, I thought,  ought to do it.” “I pulled both emergency shut off handles because I thought I was dreaming and  I just wanna wake up.”
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!

  [1] I am oversimplifying, and some of the ways to build in edge are not in pricing but in structure:   Adding a one-day lookback to a trade is a far more elegant way to add edge than just increasing the price.


  [2] I’m going to get angry emails about this, aren’t I? I am not saying it’s easy, or even that every physics Ph.D. on Wall Street would agree on the right model to price a particular derivative. Just that every bank is going to pick a method.


  [3] If you type “what is derivative,” does the neural net decide what derivative to suggest? Does it serve you up a snowball?


  [4] I  went on Lewis’s podcast about the trial and discussed this, among other things.


  [5] I periodically recommend it around here, but Guy Lawson’s “Octopus: Sam Israel, the Secret Market, and Wall Street's Wildest Con” is, to my mind, the essential book about financial fraud, and particularly about this element of fraud psychology.


  [6] Zvi Mowshowitz writes: “Nor is this a type of person who we could consider might not be committing fraud if you put him in charge of a crypto exchange. There would not even have a distinction in their head between ‘fraud’ and ‘not fraud,’ between ‘I tell truth’ and ‘I tell lie’ or between ‘customer money’ and ‘money.’ To them, there are only actions and (some of their) consequences. If the customer asks for their money and you don’t have it, or people find out you don’t have the money, or that you said you had the money and you didn’t (or that you took the money), people might get mad. They might demand their money back. Don’t let that happen. That would be bad. But also don’t worry about it.”


  [7] Am I thinking of anyone in particular? Oh, you know.


  [8] There is a sort of folkloric number that $8 billion of customer money is missing, but a   September presentation shows $16 billion of filed customer claims (some disputed), $9.2 quintillion (lol) of “facially frivolous or errant” customer claims and $65 billion of non-customer claims (mostly for taxes). Obviously the estate is not going to find $81 billion, or $9.2 quintillion, of assets. But will it find enough to pay off all of the legitimate claims? I dunno.











            Follow Us













              Get the newsletter


















Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022







<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cjqco1.6502/378de44d.gif" alt="" border="0" /></a>
