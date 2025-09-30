# Money Stuff: Look Out for Cops in the Pump and Dump

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Mon, 11 Oct 2021 12:17:58 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Look Out for Cops in the Pump and Dump_Mon,_11_Oct_2021_12-17-58_-0400_(EDT)_17c7025ebcde5d54.eml
**Processed:** 2025-08-24T19:13:09.238968















































      Pump and Dump Organization


This is not legal advice or anything, but one good rule of thumb is that if you are on an internet message board looking to hire a hit man, and you end up chatting with an enthusiastic poster who seems like he might do a good job of murdering the person you want murdered, the odds that he is in fact an undercover police officer are nearly 100%. Same with lots of online crimes, though with different probabilities. Are you buying illegal drugs on a message board? You might get the drugs, or you might get arrested, hard to say. Are you buying a missile launcher on a message board? You are definitely getting arrested, nobody is selling a missile launcher on a message board, that is cops.The percentage of people on stock pump-and-dump message boards who are cops is, I suspect, not that high, but it is rising. Here’s a good story from Australia, where the police and regulators seem to have a much stronger sense of fair play than they do in the U.S.:The [Australian Securities and Investments Commission] has taken the unprecedented step of posting a message in a Telegram chat room to warn traders they may be breaking the law.In a post on Monday at 9.32am on a newly formed chat group called “Pump and Dump Organization,” an account named ASIC posted that “coordinated pumping of shares can be illegal”.“We can see all trades and have access to trader identities. We’re monitoring this platform and we may be investigating you. You run the risk of a criminal record, including fines of more than $1M and prison time by being involved.”The post was not taken seriously. One user said the post was sent by someone “from another telegram group trying to spook people here. ASIC don’t send messages like this.” Another said it was “fake ASIC.”But an ASIC spokesman confirmed the post was genuine, marking new ground for the corporate watchdog. …Undeterred, the group pressed on. At 9.54am, members were told the stock the group was going to pump was YPB Group, which has a market capitalisation of $14 million.“USE THE MARKET ORDER AND SEND IT TO THE SKY!!” the moderator’s post said just before markets opened for trade.In early trade, the stock leapt 0.2¢, or 50 per cent to 0.6¢, before closing at 0.5¢. YPB was previously the subject of booster activity in the ASX Stock Tips Facebook group in July 2020 when the moderator of the group told members: “This STOCK is about to FLY. Don’t CRY when it does.” Unclear if they got arrested or what. Meanwhile if this had happened in the U.S., the Federal Bureau of Investigation would have posted under an account name like “yolo_crime420,” and instead of saying “this is the FBI, you may be committing a crime, stay safe out there,” they would have said “hey everyone good pumping but let’s also do some wash sales back and forth to each other, also by the way I am a drug dealer so I am hoping to use this pump to launder my money, also are any of you looking for a hit man?”






















































      Overcollateralized stablecoins


On Thursday I  talked at some length about a way to manufacture a stablecoin — a cryptocurrency that is always worth a dollar — out of no ingredients other than Bitcoin (or some other volatile cryptocurrency). The recipe is fairly simple:	You get a Bitcoin.	A Bitcoin is worth $55,000.	Maybe tomorrow it will be worth, like, $52,000, or even $45,000.	But it won’t be worth less than, say, $25,000.	So you issue (say) 25,000 stablecoins, each worth $1, collateralized by the Bitcoin.	Someone has to put up the other $30,000 to buy the Bitcoin (along with the $25,000 from selling the stablecoins). This person is left with the residual claim on the Bitcoin, i.e., once the 25,000 stablecoins are paid back at a dollar, the residual claimant gets whatever the Bitcoin is worth above that. If Bitcoin goes to $100,000, the residual claimant ends up owning $75,000 worth of Bitcoin after paying off $25,000 worth of stablecoins (and makes a $45,000 profit). If Bitcoin goes to $30,000, the residual claimant ends up owning $5,000 worth (and losing $25,000). If Bitcoin goes to $20,000 the residual claimant is wiped out and the stablecoins are no longer stable but what are the odds of that.My point here was, one, to explain that this basic approach — tranching of a risky asset into junior and senior claims — is the main move in traditional finance, and that combinations and variations on this move are most of what the financial system does. Two, I wanted to explain some of the advantages and disadvantages of this approach compared to the other main method of making a stablecoin, which is to sell 25,000 dollar stablecoins for cash and put the $25,000 you raise into a traditional dollar bank account (or, more realistically, use it to buy safe dollar-denominated assets like commercial paper or Treasury bills). The main advantage of the Bitcoin-based approach (call it an “overcollateralized stablecoin”) is that it manufactures stablecoins out of pure crypto, without too much of an interface with the traditional banking system; if you don’t trust banks to hold your dollars, this seems preferable. The main disadvantage is that it manufactures stablecoins out of pure crypto, without any actual dollars; if you don’t trust Bitcoin to hold its value, this seems worse.[1]My third point was that Tether, the biggest and weirdest and most controversial stablecoin, mostly seems to be the other kind of stablecoin, call it a “backed stablecoin,” the kind with money in the bank. It advertises that all of its coins are backed at least 1-for-1 with safe dollar assets. But in fact a (small but interesting) fraction of those “safe dollar assets” are in fact secured loans to crypto companies, secured specifically by cryptocurrency. Tether is mostly (it says) in the business of getting dollars, issuing stablecoins, and putting the dollars in the bank (or Chinese commercial paper), but it is also a little bit in the business of getting dollars, issuing stablecoins, and using the dollars to fund levered Bitcoin positions.But I neglected to mention that there are a number of stablecoins that are explicitly, entirely in that business, stablecoins that just are overcollateralized stablecoins. The most famous is probably Dai, the stablecoin of MakerDAO. “The Maker Protocol, also known as the Multi-Collateral Dai (MCD) system, allows users to generate Dai by leveraging collateral assets,” says its white paper. And:Dai is generated, backed, and kept stable through collateral assets that are deposited into Maker Vaults on the Maker Protocol. A collateral asset is a digital asset that MKR holders have voted to accept into the Protocol.To generate Dai, the Maker Protocol accepts as collateral any Ethereum-based asset that has been approved by MKR holders. MKR holders must also approve specific, corresponding Risk Parameters for each accepted collateral (e.g., more stable assets might get more lenient Risk Parameters, while more risky assets could get stricter Risk Parameters). Detailed information on Risk Parameters is below. These and other decisions of MKR holders are made through the Maker decentralized governance process.And:When a user deposits ETH or any supported ERC20 token into the Maker platform as collateral, Dai is created and loaned to the user at a collateral-to-loan ratio of 66%,[2] which increases the supply of Dai.One thing I will say about this is that it is way more transparent and straightforward than the picture I tried to paint of Tether as sort of doing some amount of complicated transformation of Bitcoins into dollars at some unspecified level of overcollateralization. This is just a decentralized platform automatically transforming Ether into dollars at a specified level of overcollateralization with clearly defined procedures for making sure the collateral is sufficient and for liquidating if it isn’t.The other thing I will say is that, as a person whose background is in traditional finance, I like the opaque mysterious version more? One thing I said on Thursday is: A bank makes a bunch of loans in exchange for senior claims on businesses, houses, etc. Then it pools those loans together on its balance sheet and issues a bunch of different claims on that balance sheet. The most senior claims, classically, are “bank deposits”; the most junior claims are “equity” or “capital.” Some people want to own a bank; they think that First Bank of X is good at running its business and will grow its assets and improve its margins and its stock will be worth more in the future, so they buy equity (shares of stock) of the bank. Other people, though, just want to keep their money somewhere safe; they put their deposits in the First Bank of X because they are confident that a dollar deposited in an account there will always be worth a dollar.The fundamental reason for this confidence is that bank deposits are senior claims (deposits) on a pool of senior claims (loans) on a diversified set of good assets (businesses, houses). (In modern banking there are other reasons — deposit insurance, etc. — but this is the fundamental reason.) But notice that this is magic: At one end of the process you have risky businesses, at the other end of the process you have perfectly safe dollars. Again, this is due in part to deposit insurance and regulation and lenders of last resort, but it is due mainly to the magic of composing senior claims on senior claims. You use seniority to turn risky things into safe things.When I say “this is magic,” I don’t just mean “this is pretty cool.” I mean that it feels like magic, that it is a sleight of hand, that to work effectively it demands willing suspension of disbelief from its observers, that it requires a mystery.[3] When you open a bank account, the bank doesn’t tell you “well we have a 9% capital ratio, so if our loans lose 9% of their value or less your account will be money-good, and our loans are made at an average loan-to-value ratio of 68%, so if the underlying assets lose 32% of their value or less our loans will be good, and if you multiply that it means that your cash won’t be touched unless the underlying assets lose more than 38% of their value in a correlated way, which we have calculated has a less than 1-in-1,000,000 chance of happening.” If your bank told you that you would never give them your money. What your bank tells you is “if you put a dollar in this account it’s a dollar.” There are enough layers of opacity between your deposit and the underlying risky assets that you don’t think of them as being at all connected.Similarly in crypto. “Here’s a thing that is worth a dollar as long as the price of Ether doesn’t fall by more than a third” is quite straightforward and useful but it does focus the mind on the bad outcome; it gives you the recipe for how to break it. “Here’s a thing that is worth a dollar and never you mind how” is possibly more useful. Obviously if the mechanism is “we steal the money and lie to you that it’s worth a dollar” then that’s bad. But a mechanism like “we use your dollars to buy some commercial paper but also to make overcollateralized loans against crypto with several layers of buffer against losses and with a certain amount of transparency but not all that much,” could be good, better than a simple transparent mechanism.Obviously a lot of crypto people feel the opposite: Decentralization, trustlessness, transparency are all important values in the crypto world, and being able to understand the immutable code of how your cryptocurrency gets turned into a stablecoin feels good. But there are lessons to be learned from the traditional finance system too, and a big one might be something like “opacity has its purposes.” Tether has certainly learned that lesson!











      The kids have SPACs now


The basic idea of a special purpose acquisition company is that some famous investor or seasoned operator raises a blind pool of money from public investors who are willing to bet on her no questions asked, and then she goes out and takes a company public with the money, selling the company on her own ties to big investors and her operational skill. Public investors want to be able to co-invest with successful investors, private companies want to go public by pairing up with successful operators who can mentor them, everyone wins, etc.But at some point SPAC sponsors realized that it would help them raise money from retail investors if they went around  pretending to be upstarts who were disrupting traditional Wall Street’s stranglehold on going public. “Invest with us because we are deeply tied in to the world of capital and big institutions love us” is a good pitch, but “invest with us because we are totally outside of the world of capital and big institutions hate us” is … also a pitch ... that … empirically … kind of works? If you are a successful investor with deep ties to traditional Wall Street, you can go ahead and do that pitch, it’s a free country, but if that is the pitch that works then why shouldn’t random young people launch their own SPACs? Here are Bloomberg’s  Ben Scent and Crystal Kim:Now the kids are joining the party. More than a dozen people age 30 and younger have been named as executives or board members at blank-check companies that have filed listing plans since June, according to data provider SPAC Research. These include a 27-year-old who got a master’s in project management from Georgetown University in 2020, a 29-year-old Atlantan who’s involved in four of them, and a pair of 23-year-old fraternity brothers from Cornell who list a $9 million, seven-bedroom mansion as their headquarters.For instance:Started by teammates on the Cornell tennis squad, Rose Hill aims to raise $125 million to hunt for an acquisition in Latin America, with a listing likely in October. Founders Albert G. Hill IV and Juan Jose Rosas, both members of the Delta Upsilon fraternity, spent time at Chardan Capital Markets LLC, an adviser that’s carved out a niche arranging blank-check deals. Hill, a great-great-grandson of the legendary gambler-turned-oil baron H.L. Hunt, also had a stint as an entry-level investment banking analyst at Guggenheim Partners and runs an online mattress company on the side. Rosas, an information science major from Lima, was a member of Cornell’s hedge fund club and interned at Point72 Asset Management.Sure, why not. I am actually surprised that I have not read a dozen stories about SPACs started by people who have built big followings on Reddit? Like being a Hunt heir and interning at Point72 are both relevant experiences for raising and deploying capital, but they feel a little traditional. If you want to pitch people on investing in a disruptive SPAC, “I go by yolo_crime420 on WallStreetBets” feels like an intriguing but so far underutilized pitch.


      4


If a company has quarterly earnings per share of $0.494 it reports earnings per share of $0.49 since people traditionally use whole pennies. If it has quarterly earnings per share of $0.495 it reports earnings per share of $0.50, which is more pleasant. A $0.001 change in actual unrounded earnings per share produces a $0.01 change in reported earnings per share. There’s a lot of leverage on that tenth of a cent. If you are doing the numbers and at the end of a quarter you come up with EPS of $0.492, oh well, you report $0.49. But if you come up with $0.494 maybe you go back and do the numbers again? Maybe you triple-check to make sure you’re not missing anything that might make it $0.495? Maybe you even nudge some contract into this quarter, or some expense into next quarter, to make it come out that way? Because that extra $0.001 is worth a lot?Or maybe you don’t, maybe you are horrified by the suggestion, maybe you just report the numbers whatever they may be. Maybe you think “this is a slippery slope to perdition; anyone who would look for an extra $0.001 in earnings to be able to round up will end up doing massive accounting frauds and Ponzis.”The Securities and Exchange Commission agrees with you; here is the Wall Street Journal:The Securities and Exchange Commission’s review of companies’ earnings per share has brought cases against three firms over the past year or so, and could come into greater focus under the regulator’s new leadership.The initiative, launched a few years ago, reviews earnings per share for the majority of U.S. public companies at least once a year, looking to spot questionable reported figures. The team working on the effort, part of the SEC’s enforcement division, uses analytics and has built a database to try to pinpoint potential manipulators of EPS, the commonly used measure of a company’s financial performance. ...SEC officials use risk-based data analytics to find companies that may have engaged in manipulations, and sometimes rounding issues can lead to an investigation.The initiative’s database was built on the basis of academic research dating back to 2009 that examined the unusually high absence of the numeral “4” in companies’ quarterly financial numbers, posing questions whether firms were improperly rounding up their earnings.Companies continue to use the numeral “4” in their unrounded quarterly EPS in less than 10% of cases, highlighting the potential for earnings manipulation through strategic rounding, said Nadya Malenko, an associate finance professor at University of Michigan. She conducted the research with former SEC commissioner Joseph Grundfest and Yao Shen, an assistant finance professor at Baruch College.The researchers assumed that every number should appear in the tenths place of unrounded EPS 10% of the time. Some companies could have an unusually low usage of “4” by statistical chance, but there is a strong correlation between this low usage and firms’ future restatements in their overall financials, Ms. Malenko said.Companies that often scooch 4s into 5s end up doing restatements more often; the tiny dishonesty begets bigger dishonesty. You could sort of imagine the story going the other way. Some companies scooch 4s up to 5s because they’re so close to being able to round up, but if you’re really dishonest, why do you care about being close? If your actual EPS turns out to be $0.492, why not report $0.50 anyway? Why not report $2.75? (Why not fudge the math so that your unrounded EPS comes out to $2.754 and you don’t appear in any SEC databases of suspicious rounders?) Rounding up by an extra tenth of a cent seems like a pretty modest red flag compared to some of the alternatives.


      Good metaphor


Here’s a 20-year-old crypto trader  interviewed by Bloomberg:The nice thing about crypto is that you’re exposed to all the loose wiring that exists in this industry. And you can electrocute yourself on that wiring, but you can also get an intimate understanding of how the internals work. I think, given the fact that you can pretty much do anything you want unencumbered and without anyone’s permission, ideally you need to be this curious, hands-on person to learn it best.


      Things happen


KKR Co-CEOs Henry Kravis and George Roberts Step Down. Beyond Evergrande, China’s Property Market Faces a $5 Trillion Reckoning. How Evergrande's Rags-to-Riches Founder Is Trying to  Save His Empire. Ex-Evergrande Economist Says Firm Ignored His Warnings Over Debt. US-listed Chinese group Renren settles investor complaint for $300m. Risky Volatility Funds Set to Make a Comeback. Credit Suisse report into Greensill failings hit by delays. The next fashion trend is clothes that don't exist. Bill de Blasio is first NYC mayor with no championship teams in 100 years. “I’ve had the soft, leathery caress of a bat’s wing against my buttocks while having a poo.” The Saudi royal family gave Donald Trump a fake tiger fur.If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] There is a related set of advantages and disadvantages having to do with financial stability. Simply: A Bitcoin-backed overcollateralized stablecoin doesn’t touch the traditional financial system and poses no real threat to financial stability, while a commercial-paper-backed stablecoin could suffer a run and lead to a fire sale of dollar commercial paper. But conversely, a Bitcoin-backed overcollateralized stablecoin could suffer a run and lead to a fire sale of Bitcoins, posing a threat to the stability of the *crypto* ecosystem.[2] Presumably this means “loan-to value ratio of 66%,” i.e. if you put $150 of Ether into the vault you get back $100 of Dai.[3] My thinking on this point is influenced by this old post by Steve Randy Waldman about the purposes of complexity in finance.










            Follow Us













              Get the newsletter



























Like Money Stuff? | 
Get unlimited access to Bloomberg.com, where you'll find trusted, data-based journalism in 120 countries around the world and expert analysis from exclusive daily newsletters.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.








           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.


          Unsubscribe | Bloomberg.com | Contact Us











                  |











          Bloomberg L.P. 731 Lexington, New York, NY, 10022


















<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cf2bwk.6300/8f12c9ca.gif" alt="" border="0" /></a>
