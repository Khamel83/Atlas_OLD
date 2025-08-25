# Money Stuff: Banking Gets a Bit Narrower

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Thu, 20 Apr 2023 14:23:56 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Banking Gets a Bit Narrower_Thu,_20_Apr_2023_14-23-56_-0400_(EDT)_1879fe8db3220baf.eml
**Processed:** 2025-08-24T19:13:08.456144



  
  
    
      
        
      
    
  
  
    
      
        Programming note: Money Stuff will be off tomorrow, back on Monday.We have talked a few times recently about, like, the theory of banking. T
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          Programming note: Money Stuff will be off tomorrow, back on Monday.

  
    
      Emergent narrow banking
    
  

We have   talked a few   times   recently about, like,   the theory of banking. That theory goes roughly like this. Banks fund themselves with deposits, which are basically short term and safe: If you have $100 in a bank account, you expect that it will always be worth $100, and you expect to be able to withdraw five $20 bills any time you want. Meanwhile banks invest their money in assets (loans, bonds) which are basically long term and risky: Banks make loans to risky businesses that don’t have to be repaid for years. 
This business has well-known problems. The main problems are:
	The deposits are short-term but the assets are long-term: If all the depositors want their money back at once, it isn’t there, because it has been loaned out. This can lead to bank runs, panics, fire sales of assets, It’s a Wonderful Life, etc.	The deposits are safe but the assets are risky: If the bank makes bad loans and loses money, there won’t be enough money to pay back depositors, and bank deposits are meant to be money, so depositors really count on their bank deposits being safe.

This business — “fractional reserve banking,” it is often called
  [1]
 — is inherently risky and fragile. Everyone knows this, and there are standard methods to mitigate the risks. Banks have capital requirements (they are partly funded with equity, not deposits, so if the assets lose value the depositors still get their money back). They have liquidity requirements (some of their assets are short term and safe, so if depositors want money back there’s some money to give them). There is safety-and-soundness regulation and supervision (the government tries to prevent banks from making loans that will lose money). There is the lender of last resort (the central bank lends money to solvent banks that need cash, so if depositors want their money back the banks can get it). There is deposit insurance (the government promises that depositors will get their money back, making bank accounts safer and runs less likely). Still there is some unavoidable residue of fragility: The mismatch between the banks’ safe short term liabilities and their risky long term assets creates risk, and somebody — if not depositors then the government — has to bear that risk.
You might draw one of two conclusions from this:
	Oh well! Banking is good; there is social value in this fragility; it allows society to pool its safe capital to be able to take on risks. “Banking is a way for people collectively to make long-term, risky bets without noticing them, a way to pool risks so that everyone is safer and better-off,”   I wrote last month. “Financial systems help us overcome a collective action problem,” Steve Randy Waldman  wrote in 2011: “In a world of investment projects whose costs and risks are perfectly transparent, most individuals would be frightened. … A banking system is a superposition of fraud and genius that interposes itself between investors and entrepreneurs” to encourage investment and make everyone better off.	No, this is bad, it’s antiquated, we should fix it. Let’s get rid of fractional reserve banking and do something else.

Conceptually the main way to do that goes something like this:
	Banks should take short-term safe deposits and invest them in short-term safe assets. 	Long-term risky assets should be funded with long-term risky liabilities. 

This is loosely speaking called the “Chicago plan,” or “narrow banking.” Banks would just hold cash for their depositors, so the cash would always be there and banks would not have any risk of runs or credit losses. In modern banking, the banks would not hold “cash” in the sense of $20 bills in a vault; rather, they’d take deposits and turn around and deposit the money as reserves at the Federal Reserve.
  [2]
 The Fed pays interest on reserves, so the banks could earn enough money to pay for salaries and branches and still pay some interest to their customers. (Though it’s not clear why a narrow bank would need branches
  [3]
; it would be a lot cheaper to operate a narrow bank than a full bank, so presumably it would need less of an interest margin.)
Meanwhile, risky loans would come from people who intend to make risky loans: You could have, say, a loan fund that raises money from investors, locks up their money for 10 years, uses the money to make 10-year loans, and then pays back the investors whatever the fund gets back on the loans.
  [4]
 If the fund makes bad loans, the investors lose money; they bear the risk knowingly and directly, unlike bank depositors who sort of don’t know where their money is going.
Perhaps this system would make borrowing more expensive, as the current system of “fraud and genius” disguises risks in the financial system and so makes it more willing to take risks cheaply. But perhaps it would be less fragile; it would cost society a little more most years but a lot less some years.
People sometimes talk about imposing this sort of system by legislation or regulation; this had a wave of popularity after 2008, though that has waned in recent years. I have   written before that the Fed seems to have no interest in narrow banking — it kind of hates it and has declined to approve a bank that tried to do exactly this model — and I don’t really expect fractional reserve banking to end anytime soon.
But I do want to point out that there are indications that the markets are moving toward narrow banking all on their own. We   talked last month about money market funds and the Fed’s reverse repo program. You can put your money in a money market fund that will just park it directly at the Fed, though when a money market fund parks cash at the Fed that is called “reverse repo” rather than “reserves.” A money market fund that just parks its money at the Fed has essentially no risk: All of its assets are short-term (they are parked overnight) and safe (its debtor is the Fed), so your money is safer there than it is at a bank. It has few expenses: It doesn’t need a branch network or a lot of lending officers to take in money online and park it at the Fed, so it can pass on most of the interest that the Fed pays it directly to its customers. And the Fed does pay it a lot of interest — reverse repos pay something like 4.8% — so it can end up paying depositors more interest for taking less risk than a bank can.
In 2021, when interest rates were zero-ish everywhere and when there hadn’t been a big bank failure in a while, nobody had all that much incentive to move their money from a bank account paying 0% interest to a money market fund paying barely more. But in 2023, when people were worried about their banks’ safety anyway, moving from a bank account paying 0% interest to a safer narrow money market fund paying 4.8% seems pretty attractive. And so people do.  The Wall Street Journal reports:

Main Street banks such as Citizens Financial Group Inc. and First Horizon Corp. said in recent first-quarter earnings reports they are having a tougher time hanging onto customer money in a world where the Federal Reserve has aggressively raised interest rates. To keep those depositors around, some lenders are paying more on savings accounts and turning to products like certificates of deposit.
Though profits rose at many banks in the first quarter, the deposit declines signal a fundamental change in their business. Deposits were plentiful in the era of superlow rates because customers had little incentive to move their money elsewhere. Banks grew to rely on them as a cheap source of funding that they could use to make loans or buy bonds and other securities.  …
In recent months, with the Fed continuing to raise rates, consumers and businesses at banks across the industry started moving their money from bank deposits to higher-yield offerings such as money-market funds and Treasurys. Customers who used to be satisfied keeping their money in accounts that paid no interest decided they no longer were. 
The collapse last month of Silicon Valley Bank and Signature Bank accelerated the shift at some firms. Both banks were felled by panicky customers pulling out their money after concerns started spreading about the banks’ health. Customers at those banks and some other smaller firms across the U.S. started moving their money to the largest banks, betting they were safer even in crisis. …
Even the biggest banks, which enjoyed a windfall of deposits from smaller-bank customers, had to pay more for deposits.
JPMorgan Chase & Co. said last week it picked up about $50 billion in new deposits following March’s bank failures, but overall deposits were up only $37 billion from the end of 2022, indicating they would have dropped if not for the industry turmoil. JPMorgan executives cautioned that the new deposits might not stick.

Then there is the other side of the Chicago plan: If banks don’t do lending, lending needs to come from funds whose investors lock up their money and consciously take on the risk of making loans. Those funds might have to charge more for loans than banks do, because their investors, unlike bank depositors, are knowingly locking up their money and taking risks and so want to be compensated.
And of course there is a lot of that in modern finance, loans that come from funds rather than from banks. Leveraged buyouts, for instance, used to be financed with a combination of junk bonds (bought by funds, insurers, etc.) and bank loans (bought by banks). In recent years, the “bank loans” have increasingly been owned by hedge funds, collateralized loan obligations, etc.; banks syndicate them but increasingly they end up on someone else’s balance sheet. And more recently a lot of   leveraged buyouts have increasingly been financed   by private credit, deals with loan funds (often sponsored by private equity firms) that cut out banks entirely.
It is not just leveraged buyouts, though. Apollo Global Management Inc.   bought a lot of Credit Suisse Group AG’s structured finance and weird lending businesses, before Credit Suisse disappeared, forming a new lending business funded by investors and its insurance company. Last month it gave PacWest Bancorp a $1.4 billion lending facility, and   I wrote: “It used to be that banks funded themselves with deposits and used the money to make loans to private equity firms. Now banks fund themselves with loans from private equity firms.” 
Or here is   a Bloomberg News story today about Blackstone Inc.’s earnings:

[Blackstone President Jon] Gray said that the tumult following the collapse of three US regional lenders last month has created investment opportunities — even after Blackstone backed a firm’s losing bid for Silicon Valley Bank. Blackstone has been talking to small banks about stepping in to lend alongside them as more look to slim down their balance sheets.
“Because of the focus on liquidity they may want to find partners,” Gray said.

Small banks don’t want to make loans “because of the focus on liquidity”: Their deposits are more risky, so their banking needs to be narrower. So they turn to funds run by Blackstone, which raises long-term money from investors who want to take credit risk, to make their loans.
Basically in 2023 the market has created a lot of money-market funds that look like the deposit-taking side of narrow banking, and a lot of credit funds that look like the lending side of narrow banking. I don’t want to overstate this, and there are still a lot of big universal banks that are attracting deposits and making lots of loans. But they have some competition from narrower banking.
One very speculative thing that I might say here is that the magic — the opacity, the “superposition of fraud and genius” — of traditional fractional reserve banking is maybe a bit harder to do in a world that pays attention to it. It is relatively easy to find a bank’s balance sheet online, and if one person reads that balance sheet and notices that the bank is insolvent, it is relatively easy for her to tweet that and have it go viral and cause a bank run.
  [5]
 “Game’s the same, just got more fierce,” the vice chairman of the Federal Deposit Insurance Corp.   said last week, about bank runs in the age of social media. If banking relies on a certain opacity, modern communications technology and social media might just make that opacity harder to achieve.
  [6]
 If it’s too easy to see what the magician is doing, the magic doesn’t work anymore.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Bloodbath
    
  

The situation seems to be that it is mathematically impossible for Bed Bath & Beyond Inc. to raise enough money by selling stock to avert bankruptcy. It’s not quite as simple as that — you can write down some scenarios where it can raise enough money — but they are pretty far-fetched. The Wall Street Journal reports:

Bed Bath & Beyond Inc. is preparing a bankruptcy filing for as early as this weekend as its falling stock price makes it near impossible to raise enough capital to avert default, according to people familiar with the matter.
The embattled retailer recently said it needed to raise $300 million from share sales by April 26 to stay out of chapter 11. …
As of April 10, Bed Bath & Beyond had raised $48.5 million from its latest stock-sale effort. At the time, it had 178 million shares available to sell, which would only net the company about $70 million or $80 million given the stock’s recent trading prices. 
The retailer has warned that if it isn’t able to raise capital through its equity offering, it would have to file for bankruptcy and likely liquidate its assets. Bloomberg reported earlier Wednesday that Bed Bath & Beyond had resumed preparing for bankruptcy.

We  talked about this yesterday; as far as I can tell that Bloomberg report led to a rally in the stock price, because I guess retail meme-stock investors enjoy bankruptcy. Not enough of a rally, though, and  the stock is back down today.
If you are Bed Bath & Beyond, what do you do? Are you still selling stock? Presumably you have been selling stock for two reasons:
	Some desperate hope of raising enough to stay out of bankruptcy, and	If you fail, at least you raise some money to hand over to creditors, and at this point you’re basically working for the creditors anyway.

As your hopes of avoiding bankruptcy fade, it becomes crueler and crueler to your retail investors to keep selling them stock: They are just throwing away their money, and you know it. (And you have told them that — the prospectus for this stock offering is full of warnings that Bed Bath is probably going bankrupt — though they don’t seem to believe you.) On the other hand, as your hopes of avoiding bankruptcy fade, your fiduciary responsibilities are increasingly to your creditors rather than your shareholders, and presumably those creditors want you to raise as much money as you can from shareholders to hand over to them. I can’t tell you how much I am looking forward to the lawsuits here.

  
    
      Bond sales
    
  

We   talked yesterday about a self-limiting feature of the recent US banking crisis: Interest rates went up, which caused banks to lose money on their bond portfolios, which caused some bank failures, which caused interest rates — at least, the rates on the long-term bonds those banks held — to go down. That doesn’t do much good for the banks that failed — they are already gone — but any bank that muddled through now looks a bit less bad, because its bonds recovered a bit. “If rising interest rates cause banks to fail,” I wrote, “that will lead to a recession, which will cause interest rates to drop, which will rescue those banks. The trick is the timing.”
For the banks that did fail, the beneficiary is whoever gets their bonds, which basically means the Federal Deposit Insurance Corp. For a while after the FDIC took over Silicon Valley Bank, there was some speculation that the FDIC would make a profit on the deal: It acquired SVB due to the hole in its balance sheet caused by unrealized losses on its bond holdings, but then those bonds rallied after SVB failed, which in theory could have repaired the hole in the balance sheet and left the FDIC with a profit. In practice, probably not. The  Wall Street Journal reports:

The Federal Deposit Insurance Corp. has begun selling bonds it inherited from Silicon Valley Bank and Signature Bank to recoup the cost of rescuing the failed banks’ depositors.
The FDIC put up for auction about $700 million of high-quality mortgage-backed bonds Tuesday in what could prove to be a test of how much the U.S. government recovers on the $114 billion in face value of the bonds it assumed.
“Per the median price guidance from the six dealers who have published price talk so far, the government should expect to get back around 86 cents on the dollar for the entire portfolio,” said Adam Murphy, founder of Empirasign, a bond-data service.
The FDIC estimates that its deposit-insurance fund will lose about $22.5 billion from depositor payouts. Most of that will be reimbursed through an assessment on other banks, resulting in a $3.3 billion net loss, the agency said. 

Long-term interest rates have come down a bit since SVB failed, as the bank failures and general banking fragility has increased the risk of recession. On the other hand, the FDIC takeover does not totally avoid the basic dynamics of a bank run, which are that if you have to pay out billions of dollars of deposits by selling all your bonds at once, that will drive down the prices of those bonds:

The market for mortgage-backed bonds weakened slightly this week, possibly in anticipation of future sales by the government. The risk premium investors demand to buy frequently traded 30-year mortgage bonds has roughly doubled since mid-February to about 0.65 percentage point over U.S. Treasury bonds, according to FactSet.
“It’s going to be a challenge to absorb $90 billion of market value,” said Walt Schmidt, a senior vice president at FHN Financial, a mortgage-bond brokerage.


  
    
      Chainsmokers
    
  

I guess the main difference between Wall Street and Silicon Valley is that if you are a senior executive at Goldman Sachs Group Inc. and also an electronic dance music DJ, your colleagues and mentors on Wall Street  will say things like “please stop being a DJ” or “wow this is some textbook midlife-crisis stuff,” whereas if you are a dance-pop duo and also want to become venture capitalists, other venture capitalists will say things like “great idea,” or “you know, you guys are founders, too, and you built an amazing company,” or “can I be in your music video?” Here is  a Bloomberg Businessweek feature on the founders of Mantis VC, a venture capital firm, who are also the Chainsmokers, a dance-pop firm: 

The Chainsmokers have given their haters something else to hold against them: They’ve become venture capitalists, starting Mantis VC, a firm that raised a total of $110 million in the boom years of 2020 and 2021 from investors like TPG Inc. co-founder Jim Coulter and billionaire Mark Cuban. Cuban, in fact, can be seen in one of the duo’s TikTok videos, in which Pall rips the T-shirt off Taggart’s back during a performance and hands it to their benefactor to use as a napkin. “I’ve known them for a while,” Cuban said in an email. “Like them.” …
The Chainsmokers befriended the likes of Drew Houston, Dropbox Inc.’s chief executive officer, and Michael Seibel, a Y Combinator Inc. managing director, who urged them to chase their venture capitalist dreams. “Guys like this kind of encouraged us,” Pall said in an interview at the pair’s Hollywood Hills headquarters on a Tuesday afternoon in late July. …
Pall recalled the early conversations with some of their friends in the highest echelons of the tech industry. “They were like, ‘You know, you guys are founders, too, and you built an amazing company,’ ” he said. “‘There’s a lot of value in that that you can provide.’”

I am somewhat forcing the comparison between the Chainsmokers and Goldman CEO David Solomon, who is also a DJ. For one thing, Solomon was a successful investment banker long before he became a prominent (?) DJ. Nobody came up to him after a DJ gig to be like “you have built a successful playlist, you could probably add a lot of value as an investment banker.” Whereas with the Chainsmokers it was like “you have some hit songs, good enough, welcome to venture capital.” 

  
    
      Things happen
    
  

Credit Suisse   AT1 Holders’ Wipeout Challenged in Swiss Court. Singapore bondholders prepare to  sue Switzerland over Credit Suisse. First EU-Wide   Crypto Regulations Clear Final Parliament Vote. House Republicans Face Resistance Reviving  Stablecoin Bill. Fidelity and State Street Push to  Make 401(k)s More Like Pensions. Britain’s ‘capitalism without capital’: the  pension funds that shun risk. EY Confronts Slowing Growth After  Breakup Deal Fails. US Banks Face   Shifting Hundreds of Billions in Assets to EU at ECB Request. SpaceX’s   Rocket Explodes Shortly After Liftoff. When  Apple Comes Calling, ‘It’s the Kiss of Death.’ Crypto Exchange Coinbase Receives License to  Operate in Bermuda. Sweden’s Biggest Pension Fund   Apologizes After $2 Billion Loss. Zurich Elite Caught in Racism Controversy on Blackface Video. BMW apologises for Shanghai auto show  ice cream meltdown. Clearlink CEO celebrates employee  selling dog so he could return to office. 
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] The name comes from the classic textbook description in which banks take $1 of deposits, have to keep $X of cash reserves, and so can lend out the other $(1 - X). X is some fraction that is considerably less than one (thus “fractional reserve banking”), and regulators set the reserve requirements; higher reserve requirements lead to safer banking and less lending, while lower reserve requirements lead to riskier banking and more lending. This does not really describe how modern banking works, and in fact the US  eliminated reserve requirements in 2020, though liquidity regulation has some related effects.


  [2] What would the Fed do with it? Currently  the Fed’s balance sheet consists mostly of Treasury bonds and agency mortgage-backed securities. In a world where everybody’s checking accounts were effectively parked at the Fed, that balance sheet would expand. You could imagine the Fed using that expanded balance sheet to buy more Treasuries and mortgages, in which case narrow banking would be a somewhat more indirect form of traditional mortgage banking, where banks borrow short-term from depositors to lend long-term to homeowners. (The Fed does not bear the *credit* risk of these mortgages, which are guaranteed by Fannie Mae and Freddie Mac, but then Fannie and Freddie are government entities as well; in practice the credit risk is owned either by the US Treasury or by investors who consciously buy risk-transfer securities from Fannie and Freddie.) I guess you could imagine some other approach, though. The Fed could use its expanded balance sheet to, like, buy corporate bonds, or to invest in the funds that make risky loans; you could have a system that is a lot like fractional reserve banking but intermediated by the Fed.


  [3] Or equity capital for that matter, or a return on equity, or highly paid executives, etc.


  [4] You don’t need exactly these features. “A loan fund that raises money from equity investors and offers them daily liquidity at net asset value, possibly with some gates to limit withdrawals, and then leverages that money by borrowing long-term from debt investors” is probably good enough; the point is for all of the investors to knowingly bear risk. “A loan fund that raises money from equity investors and then borrows overnight from big banks” is maybe *not* good enough: Overnight borrowing is too close to being bank deposits, too short-term and safe-seeming. (Morgan Ricks addresses the fragility of short-term borrowing in his book “ The Money Problem.”)


  [5] Or write a Substack post.  One version of the Silicon Valley Bank story is that Byrne Hobart read SVB’s balance sheet and  wrote a newsletter in February saying “on a mark-to-market basis, they were broke last quarter, albeit still liquid.” And then his venture capitalist readers texted all their portfolio companies telling them to get their money out of SVB, and they did, and SVB was no longer liquid.


  [6] On the other hand, that was kind of the promise of crypto: Bitcoin was created in part as a reaction to the financial crisis of 2008, and early crypto enthusiasts were very skeptical of fractional reserve banking. There was an idea that by making finance transparent and public on the blockchain, crypto would   create a new system that would be free from the risk and fragility of fractional reserve banking. And then crypto built an opaque leveraged fractional reserve system anyway, and it blew up just like 2008. “There is some … natural … human … longing … to borrow short and lend long with no equity,”   I once wrote, about the collapses of crypto shadow banks.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Matt Levine's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cildt8.5o1m/9303743a.gif" alt="" border="0" /></a>
