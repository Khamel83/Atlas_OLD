# =?utf-8?B?TW9uZXkgU3R1ZmY6IFNvbWUgRmxvYQ==?=
 =?utf-8?B?dGluZyBSYXRlcyBXb27igJl0IEZsb2F0?=

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Mon, 11 Sep 2023 14:37:52 -0400 (EDT)
**Source:** inputs/saved_emails/=utf-8BTW9uZXkgU3R1ZmY6IFNvbWUgRmxvYQ===
 =utf-8BdGluZyBSYXRlcyBXb27igJl0IEZsb2F0=_Mon,_11_Sep_2023_14-37-52_-0400_(EDT)_18a85893f86fb162.eml
**Processed:** 2025-08-24T19:13:09.450378



  
  
    
      
        
      
    
  
  
    
      
        Banks often raise money by issuing fixed-to-floating-rate preferred stock: They sell shares for $25, and for some fixed period (often five, 
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Libor
    
  

Banks often raise money by issuing fixed-to-floating-rate  preferred stock: They sell shares for $25, and for some fixed period (often five, seven or 10 years) those shares pay an annual dividend of, say, 6% ($1.50 per year, or $0.375 per quarter). And then after that they start paying a dividend that changes each quarter based on some benchmark interest rate. Usually the preferred stock is perpetual — the bank never has to pay it back — but it is callable: After it switches from a fixed to a floating rate, the bank can decide to pay it back at par ($25 per share). The rough idea is:
	For the bank, this looks like perpetual preferred stock, which counts as good loss-absorbing regulatory capital.	For investors, this looks a bit like a medium-term bond: The preferred is perpetual, but it only has five to 10 years of fixed-rate interest-rate risk; after that the bank will either call it, or it will pay a market-based interest rate and so should trade fairly close to par.

For many years, the standard benchmark interest rate was Libor, the London interbank offered rate, and fixed-to-floating preferreds normally reset to Libor plus some fixed spread. “Libor plus 4.0%,” the contract might say, and then if three-month Libor was 3.0% on some quarterly reset date, the dividend rate for that quarter would be 7.0% per year ($0.4375 for the quarter). (Technically this is a “dividend rate,” but it is natural and common to call it an “interest rate” instead, since the preferred is a fixed-income instrument.)
A puzzle in issuing a stock like this is how to define Libor. 
Libor was a rate determined by calling around a bunch of banks each day and asking them how much they’d charge to lend money, unsecured, for various terms and various currencies, to other big banks. The administrator — for a long time it was the British Bankers’ Association — would do the poll and then publish a trimmed average of the answers as Libor. 
Traditionally in these contracts Libor would be defined something like this
  [1]
:
	There is some Bloomberg or Reuters page that shows the BBA’s published Libor rates, and “three-month Libor” is defined as the interest rate (for US dollars and three-month maturity) displayed on that page, “or such other page as may replace” that page.	If Bloomberg or Reuters no longer displays a Libor page, then Libor is generally defined as the result that you get by calling “four nationally-recognized banks in the London interbank market” and asking them for “their offered quotation for deposits in U.S. dollars for a period of three months … to prime banks in the London interbank market at approximately 11:00 a.m. (London time),” and then averaging their quotes. That is, basically, if the Libor poll is no longer reported on a financial information service, the bank will re-create a small version of the poll itself.	If you can’t get any banks to quote a Libor-like rate, then “the dividend shall be calculated at the dividend rate in effect for the immediately preceding dividend period”: If there’s no Libor this quarter, you just use last quarter’s Libor.

Well, there’s no Libor anymore. There was a big scandal a decade ago — it turns out that when you ask banks what interest rate they pay, sometimes they lie — and regulators slowly got rid of it. Now there are other floating benchmark interest rates that are based more on market data; in the US the main one is SOFR, the Secured Overnight Financing Rate, based on Treasury repo transactions. SOFR is a bit different from Libor — it’s overnight, whereas Libor was for longer terms, and it’s secured (by Treasuries), whereas Libor was unsecured — but it is like Libor in being the successor standard US dollar floating interest rate.
And there are all these contracts — floating-rate loans, bonds, preferred stocks, all sorts of things — that reference Libor. Some of these contracts were renegotiated as Libor went away: I owed you money at Libor plus 4%, Libor was going away, so we sat down to negotiate a new floating rate. But many contracts were hard to renegotiate: A preferred stock, for instance, is owned by lots of anonymous investors who can’t easily be contacted to agree to a new rate.
So, in the US, Congress and the Federal Reserve got involved. The very very simple fix would be to just declare, by law, “all references to Libor now mean SOFR,” but that would be economically wrong: Libor, being longer-term and riskier than SOFR, is higher than SOFR, so just replacing Libor with SOFR would lower everyone’s interest rates. The more reasonable but almost as simple fix would be to just declare, by law, “all references to Libor now mean SOFR plus an adjustment” to reflect the fact that three-month Libor was a three-month unsecured rate and SOFR is an overnight secured rate.
And Congress kind of did that? Last year it passed  the Libor Act, which says roughly that:
	If there is a contract that uses Libor, then Libor, in that contract, will be replaced by a “benchmark replacement” chosen by the Federal Reserve; except
	If the contract has a “fallback provision” — if it says something like “if there’s no Libor, we’ll use this other interest-rate benchmark” — then the contract will just use that fallback provision instead of the Fed’s benchmark.

And then the Fed  published regulations implementing that. And now “three-month Libor” means “three-month CME Term SOFR plus 0.26161%.”
Now here is a question. I laid out how typical bank fixed-to-floating preferred stock works:
	The floating rate is a published Libor rate.	If Libor isn’t published, it’s a rate based on polling banks.	If there’s no Libor at all, the floating rate is the previous quarter’s rate.

Does that have a “fallback provision”? Obviously Option 1 is just Libor, and that went away. Option 2 — re-create Libor yourself by polling banks — does not count as a fallback provision; the Libor Act says that “a requirement that a person (other than a benchmark administrator) conduct a poll, survey, or inquiries for quotes or information concerning interbank lending or deposit rates shall be disregarded as if not included in the fallback provisions of such LIBOR contract and shall be deemed null and void and without any force or effect.”
But Option 3? I mean, in a fixed-to-floating preferred, (1) there is a fixed rate for five to 10 years and then (2) it’s Libor. If Libor goes away while the preferred is still fixed-rate, then, by pure mechanical reading of the contract, that means that the preferred is fixed-rate forever: After it becomes floating-rate, each quarter, you look at Libor, you can’t find a Libor, so the contract says that the interest rate for that quarter is the same as the previous quarter. Which is the fixed rate.
And so if you are a bank that issued a fixed-to-floating preferred in the last decade, when interest rates were low, and it will soon start floating, and interest rates are high now, you might say, well, we have fallback language, and the rate is fixed (and low) forever.
Here is  a fun story from Barron’s:

Welcome to the Twilight Zone of two preferred stocks from PennyMac Mortgage Investment Trust (ticker: PMT), a real estate investment trust that invests in mortgages (and no relation to government sponsored enterprise Freddie Mac). These two preferreds, series A (PMT.PRA) and series B (PMT.PRB), were of the fixed-to-floating-rate variety. That means they paid a fixed dividend until a specified time, after which their payouts would be adjusted based on the London interbank offered rate, or Libor, plus a spread.
Based on that, PennyMac preferred-share investors likely anticipated a big rise in payouts next year. The series A preferred dividend was slated to adjust from 8.125% annually on March 15, 2024, to Libor plus 5.831%. The series B dividend was set to change from 8% to Libor plus 5.99%. Those changes would likely have put the preferreds' payouts over 11%. ...
But in a press release published late in the afternoon on the last Friday of August, PennyMac announced that, per the contractual provisions for its preferred shares, the dividends would be fixed at the rate of the preceding period -- for series A and series B shares, 8.125% and 8%, respectively. Had PennyMac used a base rate of 5.56% (SOFR's 5.3% plus 0.26161%), that would produce a dividend rate of 11.39161% for series A and 11.55% for series B. … 
Adding insult to injury, the shares sank in the wake of the Aug. 25 dividend announcement: Series A fell 6.5% to $21.83 this past Thursday, and series B dropped 5% to $21.67. ...
Market pros have been critical of PennyMac's actions, which differed from the vast majority of payers of floating-rate instruments that transitioned to SOFR from Libor. "PMT's behavior was particularly nasty, even exploitative, to investors," wrote Charles Lieberman, chief investment officer of Advisors Capital Management, in an email. He's also an investor in other mortgage REITs' fixed-to-float preferred shares.
Lieberman noted the PennyMac preferreds were $25 par issues traded on exchanges and aimed at individual investors. "I don't think they would have had the sheer chutzpah to treat institutional investors that badly, " he wrote. "I'm glad we had no exposure here, since I would have been royally upset."

I don’t know! The thing is, PennyMac
  [2]
 can’t just change the terms of its preferred stocks by itself. Either the Libor Act changed those terms (in which case PennyMac’s shares pay SOFR, plus 0.26161%, plus 5.831% or 5.99%), or it didn’t (in which case they pay 8.125% or 8% flat). Apparently PennyMac takes the view that the third option in its preferred stock — the rate stays fixed forever — is a fallback provision, and so the Libor Act didn’t override it, so that’s what the preferred stock now pays. (Here is  the press release, and here is the original 2017 prospectus for the 8.125% preferred.) That strikes me as … probably correct? The contract says that, if Libor goes away, the rate stays fixed forever. Libor went away, so the rate stays fixed forever.
Casual examination of other fixed-to-floating preferreds suggests that PennyMac is not alone. A lot of banks did replace all their Libors with SOFRs along the lines of the Libor Act; here are announcements from  Morgan Stanley,  Citizens Financial Group Inc. and Regions Financial Corp. But here is a more complicated  announcement from State Street Corp. from June. State Street has some fixed-to-floating preferred stock (and bonds) that were indexed to Libor, and that will now, under the Libor Act, be indexed to SOFR. But it also has some that won’t be:
Each series of State Street’s Preferred Stock listed in Annex 3 to this press release is governed by the terms of a certificate of designation (each, a “Certificate”) and will not transition to Three-month CME Term SOFR by operation of law or otherwise. The Certificate for each such series specifies a fixed dividend rate (the “Dividend Rate”) for a dividend period beginning on a specified date (the “Commencement Date”), in each case as shown for each series in Annex 3 to this press release, if Three-Month USD LIBOR cannot otherwise be determined as provided in the applicable Certificate. Given that the Commencement Date for each such series follows the LIBOR Replacement Date, the Dividend Rate for each series after the applicable Commencement Date will be the applicable fixed rate specified in Annex 3 to this press release.
That is, some of State Street’s preferreds are in the same boat as PennyMac’s: They currently have a fixed rate (“the Commencement Date for each such series follows the LIBOR Replacement Date”), so their current interest rate doesn’t change due to the Libor Act. And when they move to a floating rate in the future, there is fallback language saying that, if there’s no Libor, they just use the previous quarter’s rate. Which will be the fixed rate, forever.
Obviously PennyMac could call the preferred stocks at their first call date in 2024. This would mean paying investors $25 for shares that currently trade below $22. And then PennyMac could replace them with new preferred stock that pays a higher dividend rate, say SOFR plus 6%. That would be nice, for investors; it would give the investors roughly the experience (seven years of fixed payments, then perpetual floating-rate payments) that they signed up for. But, you know, why? PennyMac has lucked into cheap(ish) perpetual financing, and it would be a bit silly to give it up.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Bitcoin futures ETFs
    
  

The basic story is:
	There is obviously demand for a Bitcoin exchange-traded fund, a thing that you can trade on the stock exchange and hold in your brokerage account that gives you exposure to the price of Bitcoin. If you could make that, people would buy it.	The easy way to make that would be to create an ETF that holds a pot of Bitcoins, issues shares of the pot, and allows arbitrageurs to exchange Bitcoins for shares and vice versa. That is roughly the way, you know, stock and bond ETFs work, and it is good and straightforward.	However, in the US, the Securities and Exchange Commission has adamantly opposed this method — the spot Bitcoin ETF — due to some combination of weird concerns about manipulation on crypto exchanges plus, I think, a general philosophical desire not to make it too easy for retail investors or traditional institutions to buy crypto.	You need SEC approval to list a new ETF, the SEC has not approved any spot Bitcoin ETFs, so there aren’t any in the US.	So some people came up with a clever workaround,   the Bitcoin futures ETF, where they raise a pot of money and use it to trade Bitcoin futures on regulated commodity exchanges. The ETF shares represent a claim on those futures rather than on a pot of Bitcoin.	That’s pretty good — the futures prices track Bitcoin prices pretty well — though there’s some tracking error and it’s more expensive than just sitting on a pot of Bitcoins.	Crucially, the SEC has approved Bitcoin futures ETFs: They trade only regulated futures listed on US commodity exchanges, so the SEC can’t really complain that their markets are manipulated.
  [3]

	So there are, in the US, Bitcoin futures ETFs but not spot Bitcoin ETFs.	Grayscale Bitcoin Trust, a pot of Bitcoins that is not an ETF, has sued the SEC, demanding that the SEC let it turn its pot of Bitcoins into a spot Bitcoin ETF.	Last month, Grayscale   won its case in court. It is not an ETF yet — the SEC still has some cards to play — but it will 	probably become one.	This is good for Grayscale (which gets to convert into an ETF), though it   has some downsides (fees for ETFs are generally a lot lower than the 2% Grayscale charges).	It is very good for other big ETF firms that can now get into the spot Bitcoin ETF game. BlackRock Inc., for instance,   has one in the works.	It is very bad for the people who made Bitcoin futures ETFs. What a good idea they had! A clever workaround to a regulatory impediment, something that let investors get, like, 90% of the benefits of a Bitcoin ETF while threading the needle of SEC approval. In a world without spot Bitcoin ETFs, the Bitcoin futures ETF was a desirable product, though also something of a niche product; you were never going to get everyone comfortable with its complexities. Still, good workaround. But more or less pointless now, if everyone can buy a simple cheap spot Bitcoin ETF instead.

Bloomberg’s   Vildana Hajric reports:

Spot Bitcoin ETFs haven’t even been approved in the US, and yet already some see them as an existential threat to the futures-based funds that came before them. …
“The BTC-futures ETFs will probably experience significant outflows if spot-based ETFs are approved,” said K33’s Vetle Lunde. “They are far less straightforward in addition to incurring higher costs due to rolling, thus leading to underperformance over time.”
With spot ETFs more likely than futures-based ones to be a reflection of real-time supply and demand, their introduction may cause “migration of trading activity and liquidity” away from Bitcoin futures markets in the US, “to the extent spot Bitcoin ETFs replace futures-based Bitcoin ETFs,” wrote JPMorgan strategist Nikolaos Panigirtzoglou in a July note.

I hesitate to say this, but when I think about derivatives-based ETFs outside of crypto, I tend to think of three main use cases:
	Commodity ETFs are often futures-based, because it’s hard for an ETF to actually hold a big stash of gold or wheat or whatever,
  [4]
 so a commodities ETF will trade futures instead. Probably this is part of the reason that there is no US spot Bitcoin ETF — probably the SEC worries a little about Bitcoin custody — but it seems like a solvable problem for Bitcoins in a way that it isn’t for wheat.	If you want to do a short ETF — one that bets that the price of some asset will go down — you probably have to do that with derivatives.	If you want to do a levered ETF — one that goes up $2 or $3 for every $1 the underlying asset goes up — you probably have to do that with derivatives too.

If you run a Bitcoin futures ETF, and you see the spot Bitcoin ETFs coming for you, are you at least considering opening a 2x levered Bitcoin ETF? I’m sure the SEC would love that.

  
    
      Credit
    
  

For … I want to say my entire career as an investment banker and then financial writer, there was a standard story about corporate loan and bond terms, and it went like this:
	There were a lot of investors with a lot of money looking for yield, and not that much yield available.	Therefore, when companies wanted to borrow money, they had a lot of leeway to write documents (loan agreements, bond indentures) that were favorable to them. Loans were often “covenant-lite,” and the documents often allowed companies to do various tricky maneuvers that would   disadvantage some creditors.	Every so often lenders would notice, and complain, and push back, and sometimes even win — some of the most egregious terms proposed by borrowers were   rejected by the market — but broadly things were pretty borrower-friendly. Lenders would complain, but then they would lend anyway.

There are nuances to this story, and it is not a pure story about the macro environment. Borrower-friendly terms were also a matter of who was borrowing and who was lending: In recent years, in particular, a lot of borrowing has been done by companies owned by sophisticated private equity firms who care a lot about maximizing their flexibility, and a lot of lending has been done by collateralized loan obligation managers who kind of don’t care. But the basic story of “money is plentiful, lenders don’t want to miss out on deals, so they agree to weak terms” had a good run.
But then rates went up and it ended? The Financial Times reports that “credit hedge funds that focus on distressed debt are making bumper profits this year as the rise in borrowing costs hits weaker companies,” and it adds:

The tougher fundraising environment has given hedge funds much more negotiating power to ask for interest rates of 14 per cent or higher, while building in tougher covenants to ensure they are repaid. 
“I think this is a golden age for fresh credit because legacy credit has a lot of flaws in it, not least a lack of covenants,” said Stuart Fiertz, president of London-based Cheyne Capital.
“We can come in with very good covenants and shape the transaction any way we like.”

The broad story in credit markets for a long time has been that the borrowers shape the transaction, not the lenders. Not anymore. The broad story has been that lenders make loans, but complain a lot about the terms. Now the lenders are positively bragging about the terms!

  
    
      Private banking
    
  

If you are a private banker whose job is lending money to wealthy people, one part of the job is being ingratiating and charming and polite to the wealthy people so they will want to borrow money from you, and another part of the job is, when they ask to borrow money, actually getting them the money quickly and with a minimum of inconvenience. The first part of the job is probably easier to select and train for, but the second part is probably more useful for the clients.
Here is a fun Wall Street Journal profile of Jane Heller, a private banker to “titans of industry like Carl Icahn and A-list celebrities like [Martha] Stewart” at Bank of America Corp., whose approach seems to involve (1) being somewhat rude to clients, though in a charming way:

Heller is notoriously blunt. A few years ago, she landed a new client after she confronted him for sitting too close to her while she was eating lunch at the Cipriani near her Manhattan office. 
For years, Heller’s gruff voice mail told callers: “Hello, this is Jane, leave your name and number and I’ll call you back. If you don’t leave your name and number, I won’t call you back.” 

and (2) actually getting them the money efficiently:

Clients say they stick with Heller because she has been there for them in times of need and spares them from the bureaucracy they can run into at other big banks. 
When Martha Stewart went on a trip to Maine and decided on a whim to buy a remote estate built by Henry Ford’s son, Heller first chided her, saying “People go to Maine and buy L.L. Bean boots,” not houses. Then she delivered a mortgage for it right away.

There are probably lessons here. (If you are a private banker, would you rather have the sorts of clients who are looking for ingratiating charm in their private banker, or the sorts of clients who are looking for the efficient delivery of large sums of money? My gut instinct is that the purely economic clients are nicer to deal with, but on the other hand the margins might be lower.) Also here is a very good line from Carl Icahn:
In recent months, Heller has been deeply involved in renegotiating Icahn’s loans after the activist investor came under attack from a well-known short seller. “She gives you the feeling that she does have your interests at least right up with her own,” Icahn says. 
At least right up there! Imagine if Carl Icahn got the feeling, from his banker, that she put his interests ahead of her own. Surely he wouldn’t trust her! If you go to Carl Icahn and say “hey Carl I am just looking out for you, I don’t care about myself,” he knows you are lying. If you go to him and say “I’m looking out for myself but you’ll do okay too,” you are speaking his language.

  
    
      Oh Elon
    
  

Walter Isaacson’s biography of Elon Musk is coming out this week, there are various  previews of it, and it seems like it will be quite something. If you like reading about Elon Musk — and if you are reading Money Stuff there is a decent chance that you like reading about Elon Musk, though it is also possible that, like me, you have had enough Elon Musk content for a while — then there is a lot to read about Elon Musk.
I particularly enjoyed  Shawn McCreesh’s profile of Isaacson in New York magazine, which includes the sentence “Isaacson writes that Grimes was furious when she found out later and wasn’t at all sure whether she would ever allow her Musk babies (a boy named X and a girl named Y and a new baby boy named Techno Mechanicus) to hang out with Zilis’s Musk babies (a boy named Strider Sekhar Sirius and a girl named Azure Astra Alice).”
Also McCreesh asked if Isaacson “never saw [Musk] doing ketamine in a hot tub or anything,” to which Isaacson replies “I have never had him and a hot tub in the same field of vision,” which, fair, but it’s sort of an odd gap.
  [5]
 Isaacson apparently began shadowing Musk  in 2021, which means that there is some chance that, when Musk was   turned away at the door at Berghain in April 2022, his biographer was there for it? I mean, apparently not — “Isaacson tells [McCreesh] he didn’t party with the playboy mogul” — but isn’t it fun to imagine that? I feel like if I wanted to get a complete sense of Elon Musk I would want to shadow him as he (1) made clutch engineering decisions at SpaceX and Tesla, (2) tweeted intemperately late at night and (3) went to the club? Plenty of people sublimate social disappointment into technological and financial ambition, but maybe nobody in history has ever done it as successfully or as transparently as Musk. Getting turned away at Berghain is his biography.
Or there is Jennifer Szalai’s  review of the book in the New York Times, which ends like this:
Reading this book, one begins to wonder if the old bird-site [Twitter] will be Musk’s Waterloo. “He thought of it as a technology company,” Isaacson writes, “when in fact it was an advertising medium based on human emotions and relationships.” Isaacson believes that Musk wanted to buy Twitter because he had been so bullied as a kid and “now he could own the playground.” It’s an awkward metaphor, but that’s also what makes it perfect. Owning a playground won’t stop you from getting bullied. If you think about it, owning a playground won’t get you much of anything at all.
Well, right. But getting bullied can cause you to buy the playground.

  
    
      Things happen
    
  


Arm Considers Raising IPO Price Range. VinFast’s 504% Rally Burns Traders Playing  Greater Fool Theory. UBS to Cut Hundreds of   Wealth Jobs in Asia as Activity Slows. Former Bank of Ireland chief  leaves Credit Suisse. Mizuho seeks to break curse over  foreign forays on Wall Street. A Primer on  Multi-Strategy Hedge Funds. China Eases Rules for   Insurers Buying Stocks in Support Measure. PwC to curtail  consulting work for US audit clients to reduce conflict risk. Ex-US prison counselor admits  accepting bribe from Galleon's Rajaratnam. Boss of Failed Crypto Exchange Gets   11,000-Year Sentence. Influx of  Russian fraudsters gives Turkish cyber crime hub new lease of life. “We find that  better-looking individuals are more likely to own stocks and invest a larger share of wealth in stocks.” “Have  the money date in your sexy clothes.” “I used to think something like this could only happen in Europe,  or St. Louis.”
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] Here I am quoting from the  PennyMac prospectus, but others are similar. Here’s a  State Street Corp. one.


  [2] PennyMac is not a bank, but it is a mortgage real estate investment trust, which is kind of like a bank, and it issues preferred stock.


  [3] This doesn’t make a ton of sense, and if you think that the market for spot Bitcoin is highly vulnerable to manipulation you shouldn’t like Bitcoin derivatives that much better, but here we are.


  [4] Or, for slightly different reasons, a big stash of 
VIX.


  [5] Also a careful answer only about hot tubs and  not ketamine!


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cjg9tm.5jeg/84d40b12.gif" alt="" border="0" /></a>
