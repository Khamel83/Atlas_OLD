# Money Stuff: Citi Missed a Fat Finger

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Wed, 22 May 2024 12:55:03 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Citi Missed a Fat Finger_Wed,_22_May_2024_12-55-03_-0400_(EDT)_18fa13a6a0d4d098.eml
**Processed:** 2025-08-24T19:13:12.885880



  
  
    
      
        
      
    
  
  
    
      
        Sometimes banks get in trouble with regulators for misconduct, and the regulators fine the banks and issue an order describing the misconduc
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Oops
    
  
Sometimes banks get in trouble with regulators for misconduct, and the regulators fine the banks and issue an order describing the misconduct, and I read a description of the misconduct and am like “ah yes that sounds like misconduct.” Other times, I read the description and am like “hmm I guess but that’s kind of a gray area and I can understand why they thought it was allowed.” (Perhaps this is just me.) But sometimes, I read the description of the misconduct and am like “well that’s just using a computer, that’s just how computers work, anyone would mess that up, you can’t blame them for that.” Of course there the misconduct is in designing the computer system in such a way that people will inevitably mess it up.For some reason, that sort of misconduct seems to happen a lot at Citigroup Inc. In 2021, Citi accidentally sent $900 million to some angry hedge funds because of what I called “a gothic horror story about software design.” Today the UK’s Financial Conduct Authority and Prudential Regulatory Authority fined Citi £61.6 million ($79 million) for a 2022 fat-finger stock trade that happened like this:On the morning of 2 May 2022 (a UK Bank Holiday), a trader on the Delta 1 Desk made an inputting error whilst loading a basket of equities into an Order Management System (OMS) used by the Delta 1 Desk, called PTE. The trader had intended to sell a basket of equities to the value US$58m. However, the trader erroneously loaded a basket with a notional size of US$444bn comprising 349 stocks, across multiple European markets. …The trader had entered the value of the basket of equities in the wrong field, the unit quantity field rather than the notional value field, whilst entering the instructions which created the erroneous basket.That is from the FCA’s order; here are the announcement and the PRA order, which actually goes through a number of previous Citigroup computer errors. But this May 2022 incident is the big one.Here, the story is that the trader worked on the delta-one desk, trading equity index futures. Citi got a client order to sell a block of MSCI World Index futures, and the trader “set about booking a basket of equities to hedge a proportion of CGML’s European exposure to the MSCI World Index.” This meant selling a lot of individual stocks: Citi’s computer had “a pre-loaded index” reflecting 349 stocks “across 13 European countries” that the trader wanted to sell to hedge.So there’s a computer screen with a box for “how many shares do you want to sell” (or, rather, units of the basket) and another box for “how many dollars worth do you want to sell,” and you can input your trade either way. If the units of the basket have a notional value of $7,684 each, you can type “7,548” in the “units” field, or you can type “58,000,000” in the “dollars” field, and either way you will sell about 7,548 units for about $58 million.
  [1]
But if instead you type “58,000,000” in the units field, you will sell 58 million units for $444 billion. And that will be extremely bad, because you did not mean to do that, and selling $444 billion of stock all at once is going to crash the market. So you will try very hard not to type your order in the wrong box. Most days, you will succeed. In fact, the chances are good that you will go your whole career as a trader at Citigroup without ever typing a big order in the wrong box. But will one Citi trader once type a big order in the wrong box? With a large enough sample, yes, of course. This one did.But it is not entirely the trader’s fault. Amazingly, Citi also programmed its computer system to confuse units and dollars. The trader typed the order in the wrong box, but then the system calculated the notional value and showed it to the trader. If you multiply 58 million units by the $7,684 price of the basket, you get a $444 billion notional amount, which is what the system should have shown, and which might have alerted the trader that there was a problem. But the system instead displayed a notional amount of $58 million — the same as the number of units — which is exactly what the trader was expecting. Here is an insane paragraph from the FCA order (emphasis added):Ordinarily, the Value at Benchmark field (ValAtBM) on the PTE screen displays the value of the relevant basket at a specified benchmark and is used where traders need to track the value against a reference price. In this case, PTE defaulted to the option "Strike". The default "Strike" option was programmed to determine the price of the Index at the prior day's close, by reference to an external data feed. However, as data from that external feed was unavailable, the price of the value of the Index instead defaulted to -1 rather than the benchmark price which was US$7684.40. The quantity of units was therefore multiplied by -1. There were number of other fields on the PTE screen in which the total notional value of the basket was correctly displayed. However, the trader only checked the the ValAtBM on PTE to confirm the size of the basket. When the trader checked the value of the inputted basket, they were presented with a figure of negative 58 million for the value of the basket (58 million multiplied by -1). The trader saw a ValAtBM of -58,000,000, which was the number they expected to see, and thus they clicked Execute to continue to the next check. The quantity box, next to the ValAtBM also presented 58,000,000. Had the data feed been available, ValAtBM would have shown a basket of approximately US$444bn i.e., the true notional value of the basket.The most human possible mistake, in an order-entry system, is typing a dollar amount in the shares field.
  [2]
 In designing an order-entry system, you should try to make it impossible to make that mistake. But instead Citi’s system defaulted to displaying a value of $1 per share (technically -$1, but that’s a hard distinction to notice
  [3]
) when its data feeds were turned off.
  [4]
 So the trader typed 58,000,000 in the shares field, meaning to type it in the dollars field, and the software was like “okay right 58 million dollars.” Insane!Still, let’s call it human error. (“There were number of other fields on the PTE screen in which the total notional value of the basket was correctly displayed.”) The next question is “well what does the computer system do to safeguard against it?” But you already know the answer. The answer is “the computer system pops up a series of warnings, but it does that on every trade, so traders have learned from experience to ignore the warnings.” I mean, that is how I interpret this passage from the FCA order:At 08:56 a ‘Trade Limit Warning’ pop-up alert appeared within PTE. This presented the trader with 711 warning messages, consisting of hard block and soft block messages, listed in a single alert where only the first 18 lines of alerts were immediately visible unless the person who received the alert scrolled down. The trader did not appreciate their inputting error and overrode all of the soft warnings in the pop-up.You get 711 alerts, you only see 18 of them, you are like “ehh 18 alerts is pretty much the normal number,” you override them all without reading.Two hard blocks generated by the PTE system, which could not be overridden, collectively stopped US$248bn of the basket of equities progressing for execution. The trader was then presented with a further pop-up alert entitled “Final Trade Confirmation”. It contained a wave notional value of all the individual equities in the basket as a total (which was approximately US$196bn). The trader clicked the “OK” option which routed the remaining basket of equities with a notional value of $196bn into CitiSmart for execution using a VWAP trading algorithm, where individual parent and child orders were generated.Okay here my sympathy starts to wane a little. Getting 711 warnings is apparently exactly as good as getting 18 warnings, and roughly as good as getting zero; nobody’s going to read 18 warnings. But getting one “are you sure you want to sell $196 billion of stock???” pop-up is pretty informative? You probably should look at that one? And click yes if you want to sell $196 billion of stock? Which you don’t? Typing the number in the wrong box is understandable; confirming a trade at 3,000 times the intended notional is worse. I suppose that if you have been doing this long enough you start to have a reflex like “I typed my order on the screen already, I don’t need to read the confirmation pop-up before I click it,” but here the software design probably does know better than you do. You should read the confirmation pop-up before you click it!Now, it does seem to be important that this was a delta-one trader selling, not one stock, but rather a basket of 349 stocks. Citi did have various safeguards — what the FCA calls “hard blocks” — of the form “if someone tries to send an order that is too big, don’t let them, even if they click ‘yes.’” The problem is that these blocks applied on a stock-by-stock basis, and this trader was selling all the stocks at once. Citi’s system had a hard block for “order notional,” which was “set at US$2bn (for each individual item in an order),” so if you tried to sell more than $2 billion of a stock the system would block it. It had a similar hard block for selling more than 200 million shares of any stock. Selling $444 billion of a market-cap-weighted basket of 349 stocks will require selling more than $2 billion of a lot of those stocks, and more than 200 million shares of others, and those trades were blocked: “These hard blocks prevented 58 orders totalling US$248bn of the original US$444bn notional value of the basket progressing for execution.”But that leaves orders to sell less than $2 billion each of 291 stocks, for a total of $196 billion, which is still a lot. And there was no overall order-size hard block, what the FCA calls “a Wave Notional hard block that would cancel basket trades that exceeded a total value limit and prevent the entire order progressing for execution.” The FCA notes that Citi’s New York delta-one desk “did have a wave notional hard block of this type,” set at $4 billion. But “the wave notional hard block was not rolled out to the EMEA instance of” Citi’s software.
  [5]
 Citi knew that if traders were trying to sell more than $4 billion of an index at once that was probably a mistake, but they only prevented it in New York, not in London.Other protections also kicked in — including when the initial orders caused the underlying stocks to drop — and the trader was eventually able to cancel the rest of the order, but “a total US$1.4bn sell orders were executed across various European exchanges,” causing a roughly 4% flash crash in European indexes and losing $48 million for Citi.Meanwhile, what were all the risk managers doing? Some combination of “being on vacation,” “also ignoring annoying duplicative alerts,” and “sending emails to which they got no responses”:At 08:48 on 2 May 2022 as a result of scheduled staff leave, the Algorithmic Service Desk, a team responsible for real-time monitoring of internal executions, passed its responsibilities to the Electronic Execution desk (EE Desk). The EE Desk is primarily responsible for real time monitoring of algorithmic order flow originated from external clients. The EE Desk did not escalate either the 284 information alerts generated from the erroneous basket trade, or the suspension alerts. Furthermore, additional post-trade monitoring performed by the E-Trading Risk and Controls Team (ETRC) failed to escalate the incident appropriately because their monitoring system filtered out all but eight of the information alerts relating to the erroneous basket trade. The ETRC team escalated the incident to the EE Desk covering the Algorithmic Service Desk, via email, at 09:31, 20 minutes after the trader had cancelled the order. Having received no response to their email, the ETRC team followed up with them four hours later.Note the FCA’s timestamps. The Algorithmic Service Desk handed off its responsibilities at 8:48; the trader was ignoring pop-up warnings by 8:56. I really do not know what to make of the fact that the “team responsible for real-time monitoring of internal executions” went on vacation eight minutes before an internal execution got fat-fingered. Is some Citi trader fat-fingering trades like this all the time, and only the heroic concentration of the Algorithmic Service Desk keeps it from hourly disaster?I like to imagine that the Algorithmic Service Desk person wrapped up work, sent an email formally handing off her responsibilities, left her desk, and was still in the office waiting for the elevator when this all went down.
  [6]
 Her phone buzzed frantically and she took it out, looked, sighed, turned it off, said “nope, I’m on vacation, this is someone else’s problem,” and got on the elevator.
  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Certificate of dumb transfer
    
  
My one good regulatory idea is the Certificate of Dumb Investment, which would replace the US Securities and Exchange Commission’s current regime of “accredited investors” with a simpler one. You sign a form saying:I want to buy a dumb investment. I understand that the person selling it will almost certainly steal all my money, and that I would almost certainly be better off just buying index funds, but I want to do this dumb thing anyway. I agree that I will never, under any circumstances, complain to anyone when this investment inevitably goes wrong. I understand that violating this agreement is a felony.And then you take it to an SEC employee, “who slaps you hard across the face and says ‘really???’” And if you say “yes, really,” then you get the certificate, and you can invest in whatever you want to, but if you then lose all of your money you are not allowed to complain.The form, to be clear, is the least important part of this. Virtually any dumb investment will require you to sign a form saying “I understand that this investment is risky and I could lose all my money, but I’m oh so smart and daring and I am not bothered by that.” Anyone would sign that! That’s marketing. Who doesn’t want to be sophisticated? No, the important parts are:	Slapping you beforehand, and	Not allowing you to complain afterwards.Anyway here’s a Telegraph story about Revolut:The banking app, which is not a licensed bank, is asking suspected fraud victims to take selfies while holding up a piece of paper that says they understand they are “unlikely” to get their money back.The app requires customers to go through the security checks when it suspects they could be the victim of a scam.It uses this intervention, Revolut said, to “break the spell” of a potential scammer.But the selfies were described as “horrible” and “like hostage photos” by solicitors who represented scam victims.I gather that if you tell Revolut to send your money to a scammer, and Revolut notices, it says “you are being scammed, are you sure?,” and if you say “yes” then they make you send the selfie before they will send the money. I’m kind of with Revolut here, but on the other hand, if they’re so sure it’s a scam maybe they should just not allow the transfer? Even if the customer sends the selfie? Perhaps you want a hard block here.
  
    
      NFT backdating
    
  
In 2021, Damien Hirst offered art collectors a proposition that was very 2021 and very Damien Hirst:	Hirst had made 10,000 paintings of “colourful hand-painted dots on A4 paper,” as today’s story in the Guardian puts it, and he was offering them for sale, but with a twist.	The twist was that you could buy a nonfungible token (NFT), on the blockchain, corresponding to one of those dot paintings.	Then Hirst would light your painting on fire, and you’d get to keep the NFT.	Or, or, or, you could keep the painting, but then you would lose the NFT.“In total, buyers chose to retain the physical versions of 5,149 paintings”; almost 4,000 buyers chose the fire and the NFT. (“Hirst kept 1,000 of the works, although he opted to hold them as the NFT versions,” says the Guardian.) Anyway Hirst obviously did not bother putting all the dots on all 10,000 papers; there was a factory:According to sources familiar with the production of The Currency series, dozens of artists were hired to assist with the factory-style production of the paintings in 2018 and 2019. Some worked eight-hour days for several months, wearing cumbersome masks to protect from the paint fumes. ...Lawyers for Hirst and Science said they always adhered to relevant health and safety rules and practices.Sure. But the news today is:The initial sale brought in about $18m. At the time, Hirst said of the project: “It comprises of 10,000 NFTs, each corresponding to a unique physical artwork made in 2016.”The paintings were sold via a single authorised seller, Heni, run by Hirst’s business manager. It said at the time that the works were “created by hand in 2016”. However, five sources familiar with the creation of the works, including some of the painters who put the dots to paper, told the Guardian many of them were mass-produced in 2018 and 2019.I gather that early-career Damien Hirst works are worth more than later-career Damien Hirst factory products, though I am not sure why the difference between 2016 and 2019 would matter all that much. Surely no one was expecting that Hirst himself put all the dots on all the papers; surely, when you pay for a Damien Hirst painting, part of what you are paying for is, like, the joke that Hirst is making about the mass production and commercialization of art. But here specifically you were paying for the joke he was making about the blockchain! He was gonna burn the paintings! Imagine being angry that you paid Damien Hirst to burn a painting that his factory made in 2016, but then you found out that he actually burned a painting that his factory made in 2019.Honestly this makes me like Hirst more. I think this is the first good joke that I’ve ever seen in the “object-fire-token-money” NFT genre? In particular, it is a sophisticated blockchain joke. The blockchain, of course, is a tamper-proof record of provenance. Whatever bad things you can say about NFTs, one thing that is surely true of an NFT is that you can tell when it was created. The creation date of these NFTs — 2021, of course! — is permanently and immutably inscribed in the blockchain. The paintings’ creation date, man, who knows; he burned those. You can’t backdate the creation of a crypto artwork; immutable provable time sequencing is in some deep sense the point of crypto. But Hirst found a way to do it.
  
    
      Endless shrimp
    
  
I still think I’m mostly kidding about the endless shrimp thing? Red Lobster filed for bankruptcy over the weekend, complaining that its ultimate endless shrimp promotion cost it $11 million, but it does $2 billion of revenue and was “bogged down by increased labor costs and expensive leases on its restaurants.” It would be very funny if Red Lobster’s equity owner and shrimp supplier, Thai Union, stripped cash out of the company by stuffing it with impossible quantities of shrimp, causing its bankruptcy, but I think it’s probably not the main cause.Still, Red Lobster’s chief executive officer did sort of insinuate in the bankruptcy filings that that’s what happened, and it would be an incredible story of crustacean financial engineering if it were true. Anyway the first-day bankruptcy hearing happened yesterday and here’s the update from Thai Union:The Thai seafood supplier that owns Red Lobster Management LLC disputed allegations that it forced the now-bankrupt business to take its shrimp while former management promoted an “endless” shrimp deal at its restaurants.Thai Union Group Plc disputed the contents of a sworn statement filed in bankruptcy court from Red Lobster Chief Executive Officer Jonathan Tibus, which included allegations that the seafood supplier “exercised an outsized influence on the company’s shrimp purchasing.”A Red Lobster lawyer read a statement from Thai Union during the restaurant chain’s first bankruptcy court hearing in Orlando, Florida on Tuesday. Thai Union disputes all statements concerning the company and its relationship to Red Lobster, the lawyer said.Fine fine but I hope that lawyer brought a briefcase full of shrimp to the hearing just for comedy purposes.
  
    
      Things happen
    
  
Anglo Opens Talks With BHP After Rejecting $49 Billion Offer. Blackstone to Grant Equity to Most Employees in Future U.S. Buyouts. The Highest Paid CEOs of 2023. BuzzFeed Shares Soar as Ramaswamy Takes Stake, Seeks Talks. Foreign Purchase of U.S. Ammo Maker Sparks National-Security Battle. Oaktree seizes control of Inter Milan after Chinese owner fails to repay loan. RFK Jr. says he invested $24K in GameStop after meme stock rally: ‘Apes together strong.’ “Once you come to New York, you won’t go back to New Haven.”If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
      
    
  


  
    
      
        
          
            
              
            
          
        
      
    
  


  
    
      
        
          
        
  [1] The $7,684 comes from page 15 of the FCA order, the benchmark price of the basket. The 7,548 is just $58 million divided by $7,684.40. And 58 million times $7,684 gets you $444 billion.


  [2] That and orders of magnitude, like typing “58,000,000” in the “quantity in millions" field.


  [3] My experience of financial software is that quantities are often signed in unintuitive ways. And this one is intuitive! If I tried to sell $58 million of stock, and the software said “ORDER QUANTITY -$58,000,000,” I’d be like “sure, right, $58 million, and I’m selling, so it’s negative.” It is possible that some software designer somewhere thought “if we default to -1 for erroneous prices, everyone will immediately see that that’s impossible, you can’t have a negative price,” but traders see minus signs on quantities all the time and are unfazed by them. Also of course the minus sign is small and you might miss it.


  [4] I assume because of the bank holiday, though I don’t know, and it could be about trading hours or time differences or something.


  [5] Also, Citi had a hard block on certain orders that exceeded 95% of average daily volume for a stock. But this block applied to “DMA flow,” meaning “direct market access,” or orders sent directly to smart order routers, but not “DSA flow,” meaning orders generated within Citi’s CitiSmart algorithmic trading system. This trade was from CitiSmart and so not subject to a volume limit.


  [6] I understand that this is unlikely at 8:48 in the morning, and it’s probably more like “some other geography was in charge overnight and ordinarily hands off to London Algorithmic Service Desk in the London morning, but this day, because of a bank holiday, they handed off to a different desk.” 


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cl456u.5hsg/a139504b.gif" alt="" border="0" /></a>
