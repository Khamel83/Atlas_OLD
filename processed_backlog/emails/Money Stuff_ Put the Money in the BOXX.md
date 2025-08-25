# Money Stuff: Put the Money in the BOXX

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Thu, 22 Feb 2024 14:42:15 -0500 (EST)
**Source:** inputs/saved_emails/Money Stuff Put the Money in the BOXX_Thu,_22_Feb_2024_14-42-15_-0500_(EST)_18dd2571d1a7217f.eml
**Processed:** 2025-08-24T19:13:12.627213



  
  
    
      
        
      
    
  
  
    
      
        For a while now people have emailed me occasionally about BOXX, the Alpha Architect 1-3 Month Box ETF, which is, loosely speaking, a money-m
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      BOXX
    
  

For a while now people have emailed me occasionally about  BOXX, the Alpha Architect 1-3 Month Box ETF, which is, loosely speaking, a money-market exchange-traded fund whose holders get paid Treasury bill interest rates but don’t pay taxes. I mean, that’s what it looks like on the outside. On the inside it’s a pile of stock options. “Isn’t this cool,” is how these emails often go. Or, “what is going on here?”
Today Bloomberg’s Zachary Mider   has an article explaining BOXX’s magic, and it is very fun, and very much  up my alley, and if you are reading this column it’s probably very much up your alley as well:

A year-old investment fund offers returns that closely track short-term Treasuries, with starkly lower tax bills. The fund, Alpha Architect 1-3 Month Box ETF, uses a complex options strategy and a longstanding tax loophole that favors exchange-traded funds.
“We spent seven years figuring out how to do this,” said Wesley Gray, the ex-Marine and chief executive officer of Alpha Architect. “My job is just to deliver all the value I possibly can to my shareholders, within the law.”
The fund, known by its ticker BOXX, surpassed $1 billion in assets this month. It is one of a number of efforts to use the ETF loophole in creative new ways, said Jeffrey Colon, a tax professor at Fordham University’s School of Law in New York. He called BOXX “the poster child for tax arbitrage.”

I can’t not write about the poster child for tax arbitrage, can I? 
The goal is pretty simple. You want something close to a Treasury money-market fund: You want a place to park your money that pays roughly the current short-term Treasury interest rate, that is roughly as safe as short-term Treasury bills, and that will give you your money back whenever you need it. You want it to be in the form of an exchange-traded fund, so you can buy and sell shares on the stock exchange. And you want the tax treatment to be better than Treasury bills. Specifically, you want the tax treatment that you’d typically get from a stock ETF: You don’t want to pay taxes until you sell your shares, and when you do, you want to pay capital gains taxes.
So the first thing you want to do is turn interest income into capital gains. In the US, interest income — the interest you get paid on bonds or savings accounts or money market funds — is mostly taxed as ordinary income, at (federal) rates of  up to 37%. Long-term capital gains — your profits on selling assets that you’ve held for more than a year — are taxed at lower rates,  up to 20%. Turning interest income into capital gains is, therefore, good.
In some sense this should be easy. Interest is what you get paid for giving up the present use of your money. If you put your money in a savings account, the bank pays you interest every month for the use of your money. But if you buy, like, Nvidia Corp. stock, or Bitcoin, nobody pays you any interest. Instead, you expect the value of those things to go up over time, to compensate you for the use of your money. If you put $100 into Nvidia today and sell it for $150 in a year, part of that $50 is in some rough sense “interest,” compensation to you for giving up the use of your money for that year. Most of it, though, is “risk premium,” compensation to you for taking the risk that Nvidia might go down instead. But there’s no actual division; it’s just $50 of capital gains.
But of course Nvidia really might go down instead. (Thus the risk premium.) So the job is to buy some asset that will appreciate, but only by the risk-free amount, and without risk: Instead of buying a stock that might go up 100% or down 50%, you want to buy an asset that will definitely go up exactly 5%. (I assume here that the short-term risk-free interest rate in the US is about 5%.)
Here is the simplest way you might imagine turning interest into capital gains. You give me $100 today, I promise to pay you back $105 in a year and a day, and I don’t pay you any interest along the way. “No interest income,” you say to the Internal Revenue Service. And then in a year I give you back $105 and you say, well, I bought a bond for $100 and sold it for $105 after a year and a day, so I have $5 of long-term capital gains. 
This doesn’t work, though. It’s too obvious, and the US tax code specifically says that this sort of substitute for interest — called “original issue discount” — gets counted as interest income, not capital gains.
  [1]

So you have to get away from debt. You can do this with stock, but stock doesn’t have a guaranteed return. What you want is to (1) buy a stock today, (2) hedge the risk of the stock price and (3) sell it in a year for 5% more than you paid for it.
This can be done! Classically it is called a “forward contract.” You buy a share of stock today for $100. You agree to sell it to me, for a fixed price (the “strike price” or “forward price”), in a year. In a year, I give you the cash and you give me the stock.
How much should I pay you in a year? Well, I should pay you enough to compensate you for locking up your money for a year.
  [2]
 If the risk-free interest rate is 5% and the stock doesn’t pay a dividend, I should pay you $105. You put $100 into the stock today, I give you $105 in a year, you give me the stock. You have hedged out the stock-price risk — even if the stock goes up to $200 or down to $20, you’re selling it for $105 in a year — so you don’t need any compensation for risk. You just get paid a risk-free interest rate. But the transaction here is not “you put in $100 today and get back your money with $5 interest in a year”; it’s “you buy stock today and sell it for a profit in a year.” So, plausibly, capital gains. (Not tax or legal advice!) 
Stock forwards are not particularly usual contracts. But you can build them. The way to build a stock forward is by buying a put option and selling a call option. So:
	Today, you buy a share of stock for $100.	Today, you sell me a call option giving me the right (but not the obligation) to buy the stock from you for $105 in a year.	Today, you buy from me a put option giving you the right (but not the obligation) to sell me the stock for $105 in a year.	It is a convenient feature of financial markets — called “put-call parity” — that the price of the call option you sell equals the price of the put option you buy, making your net outlay in Steps 2 and 3 zero, or close to it. (The reason for this is that the combination of the put and the call is equivalent to a forward contract, struck at the fair forward price, so the price of that forward — or the options that make it up — should be zero.)	In a year, if the stock is above $105, I exercise the call option and buy the stock from you for $105. If it’s below $105, you exercise the put option and sell me the stock for $105.
  [3]

	In any case, you put in $100 today ($100 for the stock, plus the price of the put, minus the offsetting price of the call) and get back $105 in a year. 	In other words, you got 5% interest on your $100.

Buying the stock makes you long the stock. Buying the put and selling the call make you “synthetically short” the stock: Owning a put and selling a call is economically equivalent to selling the stock forward. If you are long the stock and short the forward, then you have no stock price risk. You’re just locking up your money in a risk-free trade for a year, and you get paid the risk-free interest rate.
Here’s a variation that is more complicated visually but a bit simpler operationally:
	You don’t buy any stock.	You buy a put option and sell a call option, each with a strike price of $105. The net cost of these options is zero, just as it was above.	You sell a put option and buy a call option, each with a strike price of, say, $55. This gives you the right to buy the stock for $55 in a year, and it gives me the right to sell you the stock for $55 in a year.	The net cost of those options (the ones in Step 3) is, let’s say, $47.60.	In a year, if the stock is above $105, then I exercise my $105 call option (and buy the stock from you at $105), and you exercise your call option (and buy the stock from me at $55), and the net result is that you get $50 (and no stock).	If the stock is below $55, then I exercise my put option (and sell you the stock at $55), and you exercise your put option (and sell me the stock at $105), and the net result is that you get $50 (and no stock).	If the stock is between $55 and $105, then you exercise your put option (and sell me the stock at $105) and your call option (and buy the stock from me at $55), and the net result is that you get $50 (and no stock).	In any case, you paid $47.60 today (for the options in Step 3) and got back $50 in a year.	In other words, you got 5% interest on your $47.60.

The actual prices don’t matter much; the point is that you have put in some money today in exchange for a fixed amount of money in the future, using options. You get synthetically short (in Step 2), just like in the previous example. But instead of getting long by buying the stock, you get synthetically long by buying the call and selling the put (in Step 3). You are long and short the stock using options. This is neater because rather than buying stock and options, you do everything in one place, in the options market. This is called a “box spread.”
Does it turn interest income into capital gains? Sure,  more or less. Not legal advice!  Alpha Architect says:
The taxation of box spreads is complex; the tax rates (e.g., 25% or 40%) and tax character (e.g., income vs. capital gain) of options can differ from the taxation of treasury bills. The situation can get even more complex for index options, such as SPX, which are considered 1256 contracts, meaning 60% of their gains are taxed at long-term capital gains rates, and 40% are taxed at short-term capital gains rates. 
But let’s just loosely say that, yes, this transmutes a thing called “interest” into capital gains on some equity derivatives. And in fact  derivatives traders think of box spreads as a way to lend money in the options market and get paid roughly the risk-free interest rate. And that’s what BOXX does: It mostly buys box spreads on the S&P 500 index, earning Treasury-like interest through equity index derivatives. 
There is one other nice feature of box spreads using US listed options. I talked above about you trading options with me. But of course if you buy a put option from me today, and then in a year you exercise the option and demand that I pay you for the stock, there is some risk that I won’t have the money. Trading US listed options solves this problem, because in listed options your counterparty is not me — some guy whose credit is risky — but rather the Options Clearing Corp., which backs all US listed options trades. The OCC is not actually an agency of the US government, and its credit is not exactly identical to that of US Treasury bills. But you might nonetheless feel pretty confident in its credit: It is a too-big-to-fail financial-markets utility with a strong credit rating and a lot of regulatory interest. “The OCC is a SIFMU, or systematically important financial market utility, which means the federal reserve will (most likely) get involved if something is amiss at the OCC,”  Gray writes on Alpha Architect’s blog. Lending money in the box spread market pays roughly Treasury-like interest, and has roughly Treasury-like credit risk. Which is what you wanted.
So far, so good, you have turned interest income into capital gains. But that only does so much. If you know that you want to lock up your money for 18 months and get paid the risk-free interest rate on it, then, yes, you can buy an 18-month box spread and (perhaps) turn your interest income into long-term capital gains. But that’s not a great product. What you want in a product is something more flexible:
	The product lasts forever and is constantly earning the short-term risk-free interest rate on whatever money it holds.	Anyone can put money in or take money out at any time.	They pay taxes only when they take their money out, and only on their gains (the difference between what they take out and what they put in).

For that you need some ETF technology. Mider writes:

ETFs’ tax advantage stems from their ability to avoid capital gains. That’s the kind of taxable event that happens when you sell something for more than you paid. A 1969 law allows a certain type of investment fund to avoid those events if it hands appreciated securities, rather than cash, to an investor withdrawing from the fund — a transaction known as in-kind redemption. The tax break was rarely used until ETFs were invented two decades later.
Thanks to the tax treatment of in-kind redemptions, ETFs typically record no gains at all. That means the tax hit from winning stock bets is postponed until the investor sells the ETF, a perk holders of mutual funds, hedge funds and individual brokerage accounts don’t typically enjoy.

We have   talked about this treatment in the past: US exchange-traded funds ordinarily do not buy or sell stocks. Instead, when you want to buy shares of (say) an S&P 500 index ETF, you buy the shares from an arbitrageur, who buys them from an “authorized participant,” a big bank or trading firm, who then creates them with the ETF: The authorized participant buys all the stocks in the underlying index and delivers them to the ETF in exchange for some new shares of the ETF. And when you want to sell, you sell to an arbitrageur, who sells to an authorized participant, who redeems the shares from the ETF: The authorized participant hands the shares back to the ETF and gets back the basket of underlying stocks, which it then sells.
  [4]

The key advantage of this is that those in-kind redemptions — when the ETF takes back shares and gives out its underlying holdings — are not taxable events under US law. So a well-run stock index ETF might never have any taxable gains, which means that its holders never have any taxable income from holding the ETF. (Unlike a regular mutual fund, which will have gains whenever it sells appreciated stocks, and which will pass those gains on to its holders.) When the holders sell their ETF shares, that is a taxable transaction for them; if the ETF shares have gone up, then they pay capital gains taxes on their gains. But just holding the ETF shouldn’t generate taxes.
I suppose in theory BOXX could work something like that: It could never buy or sell box spreads, but instead have an authorized participant buy the box spreads and exchange them for new ETF shares. In practice, that seems more challenging to pull off with index options than it is with stocks, and BOXX does something different. Mider:

Earning bond-like returns but recording them as capital gains from options bets, rather than interest, gives BOXX a chance to deploy the tax magic of ETFs. It does that by turning a single stock into a perpetual tax-loss-generating machine.
The stock that BOXX uses for this task is usually Booking Holdings Inc., the owner of reservation websites like Priceline, OpenTable and Booking.com. In addition to placing box spreads on the S&P 500, from time to time BOXX will also buy one on Booking shares. Booking’s unusually high price, which hasn’t dipped below $3,000 this year, makes it an attractive stock for these trades, Gray said.
Although Booking spreads typically represent less than 1% of BOXX’s holdings, they play a key role in its tax planning. A box spread is akin to making two bets, one that a stock or index will go up, and one that it will go down. Since the bets are symmetrical, the overall value of the spread is unaffected by market movements. But the individual components are: If Booking rises, the long bet will gain in value, and the short one will lose.
Whenever BOXX wants to cancel out some capital gains, it uses an in-kind redemption to hand off the winning leg of the Booking trade to a market maker, Gray said. It keeps the losing leg on its own books, generating a tax loss. ...
A relatively small investment in Booking, combined with the ETF loophole, can easily generate large tax losses. Last May, BOXX bought a box spread on Booking for about $1 million. Three months later, the long side of the trade had gained more than $30 million and the short side had lost almost the same amount.
Then BOXX shed the winning part of the trade through an in-kind redemption and kept the losing part on its books. The fund’s daily holding reports show that the maneuver positioned BOXX to book a tax loss of about $32 million, even though its overall bets on Booking made a few thousand dollars. That loss is more than all the actual returns the fund earned last year.

A box spread is a synthetic long position in a stock plus a synthetic short position in the stock. If the stock goes up, you make money on the long and lose money on the short; if it goes down, you lose money on the long and make money on the short. You sell the losing leg — generating a tax loss — and redeem the winning leg in-kind, avoiding a taxable gain. You do that with your weird little side trade in Booking, and you can generate enough tax losses to shield all of your actual (net) gains on your S&P 500 box spreads. And then you have a money-market fund whose interest is not taxable. Pretty good!

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Everything is seating charts
    
  

If you are a senior partner at Goldman Sachs Group Inc., you are not really in it for the money. Oh, I mean, you’re in it for the money — you get paid a lot, and you probably have an expensive lifestyle — but you have already made a lot of money, you have marketable skills, you can afford to quit, and the money is not top of mind.
No, if you are a senior partner at Goldman, you are in it for the committees. You have devoted much of your career to Goldman, and what you care about is your standing among the Goldman partnership, the respect that you get within the firm. And the surest indicator of that standing is what committees you are on. Ideally you’d be on the management committee; that’s the best committee, and being on that means that you are in the inner circle of senior partners. But if you can’t be on the management committee, there are some other good committees, and you’d like to at least be on them.
And there are very fine-grained forms of jealousy here. If you are the co-head of some important business, and you are not on a committee, and the other co-head of that business is on that committee, that is a mortal insult.  The Financial Times reports:

Two of Goldman Sachs’ top investment bankers have threatened to quit after being excluded from a new operating committee established under chief executive David Solomon, according to people familiar with the matter. 
Mark Sorrell, the London-based co-head of mergers and acquisitions and son of advertising executive Sir Martin Sorrell, and Gonzalo Garcia, co-head of European investment banking, have told Goldman they may leave after being excluded from the committee, the people said. 
Their respective co-heads — Stephan Feldgoise in mergers and acquisitions and Anthony Gutman in European investment banking — have been included in the committee, which has about a dozen members. ...
The source of the latest unrest is two new operating committees for investment banking and trading established by Solomon this year. They sit below Goldman’s top-tier management committee. Both Sorrell and Garcia were left out of the investment banking committee, the people said. ...
Conceived as a way to promote a new generation of leaders at Goldman and to streamline decision making, the new committees have ruffled feathers internally about who was in or out, the people said. Conspicuously absent from the committee in investment banking was anyone from Goldman’s equity capital markets and real estate businesses. 

Spectacular stuff, the most Goldman of all stories. Disclosure: I used to work at Goldman, and while I was very very far from being committee material, this story resonates with me. If you work at Goldman and you turn to your colleague and say “my rival was just put on committee and I was not, I think I have to quit,” your colleague will nod solemnly and say “yes of course, we’ll miss you, but you’ve got to have principles.”
Do you think they’ll quit? Do you think the threat will get them put on the committees? Also, if you are the CEO of Goldman you have all sorts of opportunities to use committees tactically. Are you worried that too many partners are leaving? Create some new committees and put lots of partners on them; that will make them feel good. Do you want more disfavored partners to leave? Create some new committees and leave those partners off; they’ll quit in five minutes. 

  
    
      War securitization
    
  

Hugo Dixon, Lee Buchheit and Daleep Singh propose some financial engineering on Russia’s invasion of Ukraine:
Ukraine has an indubitable claim under international law for the damages caused by Russia’s unprovoked of Ukraine. For its part, Russia has legal title to approximately $300 billion of assets (held in the name of the Russian Central Bank and the Russian Federation) that have been frozen by the G7 countries since 2022. The problem is that the country (Ukraine) to which reparations are owed does not have custody of the frozen assets and the countries (the G7) that do have custody of the frozen assets do not have a claim for reparations against Russia.
Ukraine has a good legal and moral claim on Russia’s money, but it can’t get the money. The G7 countries (the US, UK, Canada, France, Germany, Italy and Japan) are holding onto a lot of Russia’s money, but they have no legal or moral claim on the money. The trick is to transfer Ukraine’s claim to the G7 countries, so the G7 countries can transfer the money to Ukraine.
I suppose one way to do that would be to literally sell the claim — Ukraine has a valuable asset (the claim on Russia), and maybe someone who could better enforce it would pay for it — but a roughly equivalent way would be to put it in a box and lend some money against the box:

Ukraine could raise up to $300 billion through a syndicated loan provided by G7 governments. The loan would be collateralised by Kyiv’s claim for war damages against Moscow. In the most likely scenario that Vladimir Putin refuses to pay reparations, the G7 syndicate would “set off” the Kremlin’s $300 billion of frozen assets against the claim for reparations. …
A reparation-backed loan would create a mechanism by which legal title to the claim for reparations — an indubitable claim under international law — can be placed in the hands of parties with the legal and practical ability to satisfy that claim from Russian assets. …
The loan will be structured as a “limited recourse” obligation. This means the syndicate will agree to look solely to the collateral (the reparations claim against Russia) as the source for repayment of the loan.

It’s not quite selling the claim, but it is more or less equivalent. One thing it would mean is that any peace negotiation between Ukraine and Russia wouldn’t be able to resolve the reparations question:
When Putin eventually sits at a negotiating table, he will surely demand his money back. The reparation loan structure has the advantage of giving the G7 countries a direct financial interest in NOT returning the money unless Russia pays reparations. Among other things, that entitles the G7 to a direct seat at the negotiating table. Without it, Ukraine could easily be bullied into surrendering its reparations claim as part of an armistice.
Once it sells the reparations claim, Ukraine can’t waive it.

  
    
      Epidemic of typos
    
  

We  talked last week about a typo in Lyft Inc.’s fourth-quarter earnings release. On the second page of the release, under “FY’24 Directional Commentary,” Lyft said that it expected its adjusted Ebitda margin to expand by “approximately 500 basis points year-over-year.” Later, Lyft put out a correction saying that was actually 50 basis points. The stock rallied hard on the wrong number, then fell a bit on the right one. “My bad,”  said Lyft’s chief executive officer, but also: “It was one zero in a press release.” I mean, honestly, fair.
Could be worse! Mister Car Wash Inc. put out its fourth-quarter earnings release at 4:12 p.m. yesterday. Its “Fiscal 2024 Outlook” includes comparable-store sales growth of -0.5% to 2.5%. Later in the evening, Mister Car Wash put out a revised earnings release to “correct a clerical error,” changing that guidance to +0.5% to 2.5%. “It was one minus sign in a press release,” I suppose, but if you work in finance you want to avoid extraneous minus signs? If you are going to sprinkle characters at random into your press releases, zeros are pretty good ones to sprinkle. Minus signs are bad!
Planet Fitness Inc. put out its fourth-quarter earnings release at 6:31 a.m. today. Its “2024 Outlook” includes “system-wide same store sales [growth] in the high single-digit percentage range.” Later this morning, it put out a revised earnings release to “correct a clerical error,” changing that guidance to 5% to 6%, which I suppose would be mid single-digits. I guess that one’s not really a typo. Six is in the top half of the single digits? I dunno.
Anyway Mister Car Wash’s and Planet Fitness’ typos didn’t cause huge volumes of volatile trading, as Lyft’s apparently did.
  [5]
 I don’t think there’s anything you really could have done with this information, but it is nice that Lyft is not alone I guess.

  
    
      Things happen
    
  

Stocks Around the World Are Swept Up in   AI Rally. Crypto Tycoon  Do Kwon Should Be Extradited to U.S., Montenegro Court Rules. Do Kwon’s Defense Vows Legal Battle to   Avoid Extradition to US. A $150 Billion Question: What Will Warren Buffett Do With  All That Cash? Alabama Embryo Ruling Casts Shadow Over   Future of IVF. Half of College Grads Are Working Jobs That  Don’t Use Their Degrees. Historic Mission Aims to   Break Curse, Return US to the Moon. Office  fragrances.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] And in fact US Treasury bills themselves are zero-coupon securities: They don’t pay interest, you just buy them for less than their value at maturity. But everyone understands that is interest.


  [2] Equivalently, *I* can lock up $100 for a year, in Treasury bills, and get back $105 in a year, which I will use to buy the stock from you. So I'm indifferent between paying you $100 for the stock now and paying you $105 for it in a year.


  [3] If the stock is at exactly $105 then I guess neither of us exercises our options and you just sell the stock in the market at $105.


  [4] To be clear, much of the time, if you want to buy or sell, someone else wants to sell or buy, and you just trade with them and there is no creation or redemption. But if more people want to buy (or sell), then ETF shares will be created (or redeemed).


  [5] Also it would have been extremely funny if Nvidia Corp. had had an earnings typo, but as far as I know it did not.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cki6ju.64z2/4a5b6d41.gif" alt="" border="0" /></a>
