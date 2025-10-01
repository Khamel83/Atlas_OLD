# Money Stuff: Take the Swaps Off the Balance Sheet

**Source**: inputs/saved_emails/Money Stuff Take the Swaps Off the Balance Sheet_Tue,_24_May_2022_13-51-52_-0400_(EDT)_180f73333fcb96b7.eml
**Type**: email
**Created**: 2025-08-25T02:54:04.747518

---

CapitolisHere is a trade that you could do: Sell a one-year total return swap on $100 million of Stock X to a hedge fund. The idea of the sw
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Capitolis
    
  
Here is a trade that you could do:	Sell a one-year total return swap on $100 million of Stock X to a hedge fund. The idea of the swap is that you give the hedge fund economic exposure to $100 million of Stock X. Simplifying slightly, (1) if Stock X goes up Y% over the year, you pay the hedge fund $Y million at the end of the year; (2) if Stock X goes down Z% over the year, the hedge fund pays you $Z million at the end of the year; and (3) the hedge fund pays you interest — say $4 million, 4% of the $100 million notional amount — during the year.	Go out into the money market and borrow $100 million at, say, 3% interest.	Use the money you borrowed in Step 2 to buy $100 million worth of Stock X to perfectly hedge the swap in Step 1. If Stock X goes up Y% over the year, you make $Y million from your stock position and pay the hedge fund $Y million on the swap, perfectly offsetting each other.This is a very popular and normal trade. You are getting paid an interest-rate margin: You pay 3% to borrow $100 million, you effectively lend it to the hedge fund at 4%, and you collect the $1 million difference as profit. The stock is almost irrelevant to you.  The hedge fund wants it to go up, but you don’t care. This is a fixed-income trade; you are getting paid the difference between two interest rates.What are you getting paid for? Well, for one thing, you are taking credit risk to the hedge fund: If the stock goes down and the hedge fund doesn’t pay, you lose money. (The stock isn’t entirely irrelevant to you, since this credit risk only matters if the stock goes down.) For another thing, you are getting paid for providing funding: You went out to the money market to borrow that $100 million on the hedge fund’s behalf, and the fund is rewarding you for that effort.[1] Ordinarily the person doing this trade — the “you” in this description — is a big investment bank. There are many reasons for that. Banks have lots of money, and easy access to money markets to borrow more. They can buy stock easily. They talk to all the hedge funds and have trading agreements with them and hold themselves out as market makers, so when a hedge fund wants to do a swap like this it will naturally call one of its banks and not, say, some other hedge fund.This is a trade that was made infamous recently by the blowup at Archegos Capital Management, which did a bunch of giant swaps with a bunch of banks on about a dozen stocks. When some of the stocks went down, it turned out Archegos wasn’t good for the money; the banks sold the stocks to limit their losses and a couple of them lost a lot of money. This is the credit risk that I mentioned above, everyone is aware of it, banks try to manage it carefully — most of Archegos’s banks were fine! — and charge an appropriate spread for it, and bank regulators also try to keep an eye on it.There is another problem for the bank, though. The problem for the bank is that, if you do this trade, you will add $100 million of assets (the stock you buy in Step 3) and $100 million of liabilities (the money you borrow in Step 2) to your balance sheet. If you are a bank, growing your balance sheet costs you money. Classically a bank has to have capital in proportion to its assets; if a bank has $100 million of assets, regulators might require it to have at least $8 million of equity capital — stockholders’ money — to cushion it against losses. (The actual number is way more complicated than that but 8% is sort of a crude generic capital ratio.) In my hypothetical trade, the bank just borrowed $100 million to fund its $100 million of stock, but in reality the bank would need to fund some of it with equity. Bankers tend to think that equity is expensive. If your shareholders expect a 15% return on equity, and this trade increases your capital requirements by $8 million, then the capital “cost” of this trade is about $1.2 million a year — more than you are actually getting paid.Incidentally you also have the swap on your balance sheet, as an asset or a liability, but a small one. Derivatives go on your balance sheet at their fair value, and the fair value of this swap, initially, is roughly zero: It is roughly a fair bet between you and the hedge fund, so its expected value is close to zero.[2] As the stock moves the swap will become a bigger asset (if the stock goes down) or liability (if it goes up), but initially it does not have that much balance-sheet impact.What you might want, if you are a clever banker, is to move that $100 million of stock off your balance sheet. Your thought process might be:	Look, in Step 2 of this trade, you were borrowing $100 million from the money market for 3%.	So there are people in the world — money-market funds, pensions, whoever — who have $100 million and are willing to lend it to you for 3% interest so you can buy the stock to do this trade.	What if, instead of lending you the money, those people bought the stock for you. 	They would spend their $100 million on Stock X, and put it in a box, and write you a total return swap on it, one that exactly offsets the swap you write to the hedge fund in Step 1.[3]	And you would pay them a financing rate of, say, 3.1% on the swap, which is more than they were getting in the money market.Now, instead of borrowing money to buy stock, you — the bank — just sit in between two swaps. Instead of growing your balance sheet by $100 million, you don’t do that. Instead of making 1% on this trade (4% financing rate from the hedge fund minus 3% cost of money), you are making 0.9% (4% on one swap minus 3.1% on the other), but you are freeing up $100 million of balance sheet so it’s worth it. You’re better off because you save on capital. The lenders are better off because you’re paying them an extra 0.1%. The hedge fund is indifferent; it’s still getting the same swap from you. Everyone is better off!Arguably the financial system is worse off because you have lower capital requirements against essentially identical risks, but, you know, that's how capital regulation works. If regulation requires $10 of capital for a trade, and $7 of capital for an economically identical trade that uses different paperwork, then money will naturally flow to the trade with lower capital requirements. If that leads to levels of bank capital that are too low overall, or if it encourages banks to pile into very risky trades, then that’s bad. Anyway here is a Wall Street Journal story about Capitolis Inc.:In the same way Airbnb turned vacant homes into vacation rentals, Capitolis is turning the unused capital of investing giants like BlackRock Inc. into assets that banks can use to facilitate all kinds of transactions. ...Enter Capitolis: It matches investments from asset managers, pension funds and money-market funds with the transactions banks facilitate and underwrite. The firm has raised some $60 billion from investors for the banks to use in the past two years and reduced trillions of dollars in trading positions, said Gil Mandelzis, its founder and chief executive.JPMorgan Chase & Co. and Citigroup Inc., two of the biggest players in global markets, use Capitolis to free up their traders to work with more clients. The two banks are also Capitolis investors, alongside venture-capital firms Sequoia Capital and Andreessen Horowitz. A March funding round valued the startup at $1.6 billion. Mr. Mandelzis’s new idea resembles an old one: Banks have long sliced up and sold their big corporate loans to other banks and investors. Capitolis figured out how to use this syndication concept to turn all kinds of banking products—foreign-exchange swaps and lines of credit, to name a few—into a kind of fixed-income security or loan they can sell to investors. For example, Citigroup owns a basket of equities tied to its clients’ trades. Capitolis, using investor money, essentially mirrors Citigroup’s trades—entering into a derivative contract to take the risk off the bank’s balance sheet. Citigroup is freed up to do more trading, and the investors get a fixed payout. That’s what I described above. Instead of Citi buying stocks to offset its clients’ total return swaps (the first trade I described above), an off-balance-sheet Capitolis vehicle buys the stocks and writes total return swaps to Citi, lowering Citi’s capital requirements. Here is an S&P Global Ratings report about one of these vehicles, called Ionic Capital II Trust, which can raise up to $15.5 billion to buy stocks to hedge Citigroup total return swaps. The vehicle issues commercial paper with an A-1 rating. Basically if you are BlackRock or whoever, and you are looking to park some money somewhere safe for a short period, you can lend your money to Citi directly (which grows Citi’s balance sheet), or you can lend your money to this thing, which will buy stocks for Citi without growing its balance sheet. Your credit risk is pretty much the same (you are relying on Citi paying you), but this thing is better for Citi’s capital treatment.The Journal story goes on[4]:Capitolis’s plan to outsource banks’ capital needs, while still in its infancy, has the potential to reshape their role in the market and the broader economy. Divorcing the capital required for transactions from the process of executing them could allow banks to serve more customers—businesses and consumers alike—without taking on so much risk that they could blow up the financial system. The goal, the company’s founders say, is a market better able to absorb big spikes in trading volume and loan demand. “When it’s all over, we will have uncoupled capital from the underwriting equation,” said Mr. Mandelzis. “We’re going to look back and wonder how they used to do it when it was bundled.”That is: In the ordinary course, banks do trades that require them to buy stuff, and then they have the stuff on their balance sheets. In a perfect world (for the banks!), banks would do trades that require them to buy stuff, but the stuff would all be in separately funded special-purpose vehicles for capital efficiency.I am telling you about this because I think it is smart and neat and, as a former structurer of financial boxes and arrows, I appreciate some good boxes and arrows. I also think that, as stories like “banks are doing derivatives trades and then putting them into off-balance-sheet vehicles to reduce capital requirements” go, this one is quite benign. I think the next financial crisis is unlikely to be caused by off-balance-sheet funding of equity total return swaps. But certainly I realize that not everyone will take it that way! I realize that Archegos is pretty recent! Some people simply do not like stories like “banks are doing derivatives trades and then putting them into off-balance-sheet vehicles to reduce capital requirements,” no matter how good they are.
  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      SEC v. ESG
    
  
We talked yesterday about a US Securities and Exchange Commission enforcement case against BNY Mellon Investment Adviser Inc. The issue is that BNY Mellon ran some mutual funds and advertised that they considered environmental, social and governance factors in all of their investment decisions, but in fact they only considered those factors in like 75% of their investment decisions, so BNY Mellon had to pay the SEC a $1.5 million fine. That is a simple and objectively measurable problem: BNY Mellon’s marketing materials said things like “ahead of investing, each security being considered for investment by our global industry analysts must have an ESG quality review,” and BNY Mellon in fact did ESG quality reviews that produced ESG scores before making most of its investments, but sometimes it did not. Sometimes it bought stocks with no ESG scores at all. What I suggested yesterday is that this might be all that the SEC can do with its enforcement powers to fight “greenwashing,” the worry that asset managers talk about their focus on ESG investing but are in some way not “really” doing ESG. This was true of BNY Mellon in a trivial way: It claimed to do ESG reviews and sometimes did not. But presumably in most cases, the people concerned about greenwashing are not concerned about that. They are concerned about investment managers who say “we do ESG reviews of every investment,” and do in fact do ESG reviews of every investment, but the reviews are bad. For whatever reason: They are too lazy, or they focus on the wrong sorts of ESG, or they give companies credit for stuff that you think is bad and penalize them for stuff that you think is good. What is “real” ESG is to some degree subjective, and there will always be critics of how any fund approaches it. And that, I argued, is harder for the SEC to police: There are no rules for what is “real” ESG, so investment managers get to decide for themselves, and as long as those decisions are not in obvious bad faith the SEC can’t and probably shouldn’t go after them.Well but the other alternative is for the SEC to write some rules on what “real” ESG is:Rules being prepared by the Securities and Exchange Commission would specify disclosures to be made by investment funds that have terms such as “ESG”, “sustainable”, or “low-carbon” in their names. The rules are expected to require information about how ESG funds are marketed, how ESG is incorporated into investing and how these funds vote at companies’ annual meetings, according to people familiar with the SEC’s thinking. …“There is currently a wide range of what asset managers might mean by certain terms and what criteria they might use,” Gary Gensler, SEC chair, said in March. “It is easy to tell if milk is fat free. It might be time to make it easier to tell whether a fund is really what they say they are.”The four-member SEC, which includes Gensler and two other Democratic appointees, is scheduled to vote on Wednesday to release the draft rules for public comment.You could imagine a rule that says “you can’t call yourself an ESG fund unless you vote in favor of all shareholder proposals asking companies to write reports about their carbon impact.” The actual rule wouldn’t say that; it would say, like, “if you vote against a shareholder proposal about carbon reports, you need to disclose that, possibly in a parenthesis in your fund name,” like “The BlackRock Large-Cap ESG Fund (But We Voted Against 17 Climate Resolutions Last Year)”[5] or whatever. The SEC is primarily a disclosure regulator, but it knows how to make disclosure of things it dislikes unpleasant, so that everyone chooses not to do those things to avoid disclosing them.[6]I think there are obvious potential problems with the SEC deciding what is and is not ESG. “It is easy to tell if milk is fat free” because you measure to see how much fat is in it. It is harder to tell if a fund is ESG because different people have different environmental, social and governance priorities. A rule that helps investors understand whether an “ESG” fund shares their ESG priorities is probably helpful. A rule that mandates that ESG funds pursue the SEC’s ESG priorities — that says what sorts of things are and aren’t ESG — is trickier. I expect the SEC’s rules will do a bit of both. 
  
    
      
        
      
    
  


  
    
      NFT Stuff
    
  
I … don’t mind this?It involves converting room nights for sale into nonfungible tokens, or NFTs, that can be bought or sold by hotel guests, similar to the StubHub market for concert and sporting event tickets. ...Casa de Campo has signed with the startup Pinktada, which recently launched a booking system that includes hotels in the Caribbean, Mexico, San Francisco and Hawaii.Hotel guests can reserve rooms at those properties by buying NFTs through Pinktada. By using this system, guests can book a room at a discount to what the hotel would charge for a refundable reservation.The sale is final from the point of view of hotel owners, so their revenue is guaranteed whether or not the room is used. If travelers change plans, they can use the tokens for other Pinktada hotels or sell them to another traveler in the Pinktada network.Pinktada (the name is a reference to a type of pearl oyster) promises to be the buyer-of-last resort if another traveler doesn’t buy it.“You give hotel owners certainty of income, but give travelers the flexibility if their plans change to sell or swap tokens,” said Mark Gordon, Pinktada’s co-founder and chief hospitality officer.I’m sorry? I probably should mind it. But I feel like I make fun of nonfungible token projects around here all the time so it’s worth acknowledging the ones that are, you know, fine. A while back I did a Q&A with Morning Brew, and they asked me: “Would you ever buy an NFT? If so, what would it be?” And I said:See, I feel like the sophisticated answer here is something like, “Sure, it would be a house.” Like I think that what is interesting about the idea of a “non-fungible token” is the possibility of linking some non-fungible thing in the real world, or some non-fungible slice of some real-world thing, to some transferable digital representation. And there is a strand of crypto thinking that is like “we are going to build a new financial system that will take over the entire job of financing and paying for the real world,” and in this vein you need to think about ways to represent real economic activity. You want ways to digitize ownership of houses and factories and the contents of particular shipping containers and stuff like that.And a lot of people who come to crypto with this way of thinking are like, well, we’ll start by building out the digital primitives first, and then we’ll figure out ways to associate them with real-world objects. So we’ll figure out a way to build and trade non-fungible tokens, starting with tokens that are just empty nonsense, but then once we have that technology, we can work on trading tokens that are not empty nonsense. So one day instead of getting the title to your house through some archaic title registry where you have to go down to the basement of a courthouse and leaf through ancient paper documents and figure out if there are liens on the house, it will all be on the blockchain and home sales will be easy and you can own a fraction of a home and get a mortgage instantly, etc., etc., etc. And I am not saying that I expect all that stuff to happen in the near term, but it is at least an interesting vision for something, and the concept of “non-fungible token” is part of it.And that is more or less this. You have some class of not-quite-fungible things in the real world, reservations for particular dates in particular rooms of particular hotels. People want reservations mostly for normal consumption reasons, not for unhinged speculation, but (1) their plans might change, etc., so they might want to be able to resell them and (2) sure I guess you could speculate on the future price of hotel reservations, why not. So it is good to create a liquid secondary market for reservations: It is better for buyers than an alternative of nonrefundable reservations (because they can resell if their plans change), it is better for hotels than an alternative of freely refundable reservations (because they get certainty of income), and, who knows, it might attract a new class of buyers (hotel-room speculators, high-frequency hotel-room market makers, whatever).Of course the hotels could just offer nonrefundable-but-transferable reservations; if I reserved a room and then sold it to you, we could call up the hotel and tell them that you’re coming in my place. But this could be an administrative hassle for the hotel; better for the hotel if some third party keeps track of the reservation, runs the marketplace, and just tells the hotel who is going to show up. Also having a third-party platform do it makes it easier for people to trade reservations across different hotels. You can cancel at one hotel and book at another, or maybe you are doing a complex arbitrage trade where you get long an ocean-view suite and hedge your risk by shorting three parking-lot singles, I don’t know. Of course you could build a trading platform for hotel reservations, sign up hotels and customers to use it, and skip the entire concept of an “NFT.” (Like StubHub, which is a platform for trading tickets, not NFTs “of” tickets.) The platform could keep a centralized database of reservations (by arrangement with the hotels), you could trade by going through the platform, you don’t need a blockchain. But there are some commonly asserted advantages to a blockchain that might be relevant here. If the hotel reservations are NFTs on a blockchain instead of just entries in Pinktada’s database, then in theory other people could build competing trading platforms for the same reservations, or you could sell your reservation-NFT off the platform. Or competitors could act as market makers on Pinktada’s platform and be able to compete on equal terms. An open permissionless decentralized blockchain might be good for hotel-room liquidity, which I suppose is the goal here.I am not sure that’s what’s actually happening! Certainly in the early stages “Pinktada has a database” is not really different from “Pinktada has a blockchain.” Still at a conceptual level I don’t think this is a bad use of NFTs. Certainly not compared to all the other uses of NFTs.The other advantage of this is that, at least as of a few months ago, crypto people had a lot of money and wanted to blow it on NFTs, so selling them an NFT of a hotel stay might be more lucrative than just selling them the hotel stay:Owners say this ensures they get paid for the rooms because guests would sell their reservation in the market if they decide not to go, and appeal to the crypto-enthusiastic traveler.“We can reach another consumer that maybe isn’t booking through traditional means,” said Jason Kycek, senior vice president with Casa de Campo Resort & Villas, a Dominican Republic resort, who is planning to soon begin booking rooms with NFTs.Just don’t let them pay for room service with TerraUSD.
  
    
      Dot Collector
    
  
What is the right way to think about the diffusion of the famously weird culture of Bridgewater Associates, the world’s largest hedge fund? Bridgewater founder Ray Dalio has spent a lot of time in recent years marketing that culture, with a book and a YouTube video with Diddy and a lot of publicity about how his principles for business management can work beyond Bridgewater.Is that, like, just the usual thing where a guy gets rich managing a hedge fund and then wants to turn his wealth into respect, in this case by becoming a business/life guru?Are there commercial advantages to Bridgewater from the guru thing? If you are a big pension fund and you allocate a lot of money to Bridgewater and you constantly read articles about how weird its culture is, maybe you withdraw your money. If you constantly read articles about how good its culture is, and watch videos of Ray Dalio mentoring Diddy, maybe you give Bridgewater more money.Are there commercial disadvantages? What if Bridgewater’s edge comes from (1) having a truth-centered meritocratic culture, (2) attracting truth-centered people with lots of merit, and (3) being the only place those people fit in? What if Dalio is so successful at promoting his management philosophy that dozens of big companies convert to a Bridgewater-like culture, and smart ambitious people who love truth have lots of good options and stop going to Bridgewater? What if other investment firms convert to Bridgewater’s culture, get better at finding the truth, and compete away Bridgewater’s returns?Anyway any time I read about the Dot Collector I am going to laugh, cringe, and mention it in Money Stuff:Coinbase, a cryptocurrency trading firm that garnered attention for banning salary negotiations and political speech among employees in recent years, is testing another practice that has raised eyebrows internally: asking employees to frequently rate each other. Some employees at the company have been using a real-time evaluation app invented by Bridgewater Associates, the well-known hedge fund founded by Ray Dalio, which helped enforce a culture of “radical transparency” that encourages blunt honesty, according to two people with direct knowledge.The app, Dot Collector, is sold by Principles, a company Dalio founded. Coinbase’s version lets employees evaluate co-workers, including their managers, on how well they exemplify the crypto firm’s 10 cultural tenets—which include clear communication, efficient execution and positive energy—during meetings and other interactions, these people said. After an interaction, an employee can give their colleague a thumbs-up, thumbs-down, or neutral rating. …While rapid-feedback technology is becoming more common in the tech industry, it’s rare for tech companies to use the Dot Collector software itself, said Paul Rubenstein, chief people officer of the employee analytics provider Visier.“I have never actually talked to some other head of HR who uses it,” he said.After you read this column I guess let me know on Twitter how well it exemplifies Money Stuff’s 10 cultural tenets. Honestly I should probably write a list of Money Stuff’s 10 cultural tenets. Making fun of crypto, saying that everything is securities fraud, addressing convoluted insider-trading hypotheticals … I am going to stop because I find this embarrassing; clear-eyed critical self-knowledge is not for me. But it’s nice that Coinbase is into it.
  
    
      Things happen
    
  
Didi Says It Will Proceed With Delisting From NYSE. How Janus Henderson Lost Two CEOs and Billions of Client Assets. $40bn crypto collapse turns South Korea against the ‘Lunatic’ leader. Why Shale Drillers Are Pumping Out Dividends Instead of More Oil and Gas. Bankers Nervous About Funding Boots Bids Amid Market Volatility. Broadcom in Talks to Pay About $60 Billion for VMware. Banks and funds stash record $2tn overnight at Fed facility. Wall Street Bank Lobby Lines Up Against a US Digital Dollar. Crypto Shows All the Signs of Financial Stability Risk, ECB Says. China Faces Growing Pressure to Iron Out Audit Deal With the U.S. Signs of change at ExxonMobil a year after hedge fund proxy fight. Adam Neumann-backed blockchain startup Flowcarbon raises $70 million. BNP Sued After Vetoing Boss's Proposal to Work Remotely From French Riviera.If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] It is less relevant to our purposes but you are also getting paid for stock execution: You also went out and bought that $100 million of Stock X on the hedge fund’s behalf, and the hedge fund is probably paying you for that in the form of explicit commissions or a bit of extra interest-rate margin.[2] This is basically true for your accounting balance sheet: Derivatives are measured at fair value, and the fair value of an at-the-money swap like this on Day One ought to be close to zero. (Or, really, close to the edge that you are charging on the trade.) It is less true for *regulatory capital*; modern capital regimes will make you have capital against derivatives positions not based purely on their current balance-sheet fair value, to account for things like counterparty credit risk. (And those regimes will to some extent offset swaps with their hedges, etc.) In the text I am giving a broad intuition about balance sheet, not describing the capital rules in detail. But the broad intuition is just that you need less capital for the swap than for the underlying stock, because the stock is on your balance sheet and the swap isn’t. [3] That is, it offsets the market risk. You keep the credit risk. If the hedge fund disappears, you still have to pay the lenders, just as you would in the initial trade.[4] I am eliding other parts of Capitolis’s business that are less interesting to me, like compressions and novations in FX trades, etc. Here is more from Alex Rampell at Andreessen Horowitz, a Capitolis investor.[5] This is made up, I have no idea how many resolutions BlackRock voted against or what the names of its ESG funds are. But there are always stories about how BlackRock votes on shareholder climate resolutions, etc.[6] We talked about this when we discussed the SEC’s proposed regulations for *companies’* climate disclosure. For instance, the SEC wants to require public companies to either (1) have a board committee that regularly discusses climate-related risks or (2) disclose why it doesn’t have that committee. Choosing option (2) seems unpleasant, and like an invitation to get sued, so companies will probably set up those committees.
        
      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cgkcpx.5oy5/5a847761.gif" alt="" border="0" /></a>