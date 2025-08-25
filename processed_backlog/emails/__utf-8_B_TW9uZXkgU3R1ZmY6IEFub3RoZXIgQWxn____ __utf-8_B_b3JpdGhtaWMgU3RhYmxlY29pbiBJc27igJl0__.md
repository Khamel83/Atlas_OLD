# =?utf-8?B?TW9uZXkgU3R1ZmY6IEFub3RoZXIgQWxn?=
 =?utf-8?B?b3JpdGhtaWMgU3RhYmxlY29pbiBJc27igJl0?=

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Tue, 10 May 2022 13:45:54 -0400 (EDT)
**Source:** inputs/saved_emails/=utf-8BTW9uZXkgU3R1ZmY6IEFub3RoZXIgQWxn=
 =utf-8Bb3JpdGhtaWMgU3RhYmxlY29pbiBJc27igJl0=_Tue,_10_May_2022_13-45-54_-0400_(EDT)_180af14e8c649ccc.eml
**Processed:** 2025-08-24T19:13:09.903199



  
  
    
      
        
      
    
  
  
    
      
        AlgostablesI guess it is time to talk about algorithmic stablecoins again. Terra, or UST,[1] is an algorithmic stablecoin whose price is mai
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Algostables
    
  
I guess it is time to talk about algorithmic stablecoins again. Terra, or UST,[1] is an algorithmic stablecoin whose price is maintained by an arbitrage relationship with another cryptocurrency, Luna. One UST is supposed to be worth one US dollar, and one UST can always be exchanged for a floating quantity of Luna with a market value of $1. If a UST is trading at $0.99, you can buy it for $0.99 and then exchange it for $1 worth of Luna, making an instant profit. If it is trading at $1.01, you can buy $1 worth of Luna (for $1) and use it to buy a UST worth $1.01, making an instant profit. Because of this arbitrage relationship, while the price of Luna can fluctuate, the price of Terra should always be $1: If it trades above or below $1, people will exchange Terra for Luna or Luna for Terra until the price of Terra gets back to $1.When we  talked about Terra last month, I wrote:On first principles this is insane. It relies on [Luna] always being worth something. If [Luna] trades at $0.01, you can print 10 million of them and buy 100,000 [Terra] and push the price up. But if [Luna] trades at $0.00, you can print infinity quadrillion of them and you’re still not gonna be able to push up the price of [Terra]. If [Luna] is worthless, it cannot be used to support the price of [Terra]. And because you just made it up, there is no particular reason for [Luna] to be worth anything, so there is no particular reason for [Terra] to be worth a dollar. If I made up [Luna] and [Terra] on my computer and said to you “I will give you the number 10 billion in this Excel spreadsheet if you give me 1 million U.S. dollars,” you would say no, and if I raised my offer to 400 quadrillion you would not change your mind.Nonetheless! It works? The rough intuition here is that there is a lot of demand for stablecoins; there is particularly a lot of demand for Terra because Terraform Labs, the entity that created Luna and Terra, essentially pays 19.5% promotional interest on UST deposits. People want a stablecoin that is worth a dollar, so they are inclined to treat Terra as though it’s worth a dollar, which makes it worth a dollar. They buy lots of Luna to turn into Terra, which means that the price of Luna goes up, which means that there is plenty of valuable Luna to support the price of Terra, which means that Terra is robustly worth a dollar.Ha, well, oops:Rather than trading at $1, as designed, the TerraUSD coin, or UST, slipped over the weekend to around 99 cents. By Monday evening in New York, it had plunged to 60 cents, obliterating its previous low of 92 cents in May 2021. It clawed back losses on Tuesday and is fluctuating between around 90 cents and $1 --  a sign of trouble. …There are around 18.5 billion of UST in circulation, according to CoinMarketCap, a big enough presence that its swings could have systemic implications for other coins and protocols. And Do Kwon, the crypto upstart behind UST, has previously committed to buying as much as $10 billion worth of Bitcoin as part of his support of the coin, further entwining the project with the core of the digital-asset market. ...That led to a series of crypto market interventions from Kwon and the so-called council of the Luna Foundation Guard (LFG), a consortium of crypto players that includes Kanav Kariya of Jump Crypto. Jump Crypto declined to comment. Near midnight New York time on Monday, UST remained under pressure. Luna was trading around $29, down 52% from a day earlier, according to CoinMarketCap. And:The declines spurred backers led by Do Kwon, the founder of Terraform Labs -- which powers the Terra blockchain -- to issue $1.5 billion in loans denominated in both UST and Bitcoin to help support the digital currency. The basic thing that makes Terra valuable is confidence in it. The essential source of this confidence is ... just sort of recursive social belief? If you think that everyone else will treat Terra as worth a dollar, then you will treat it as worth a dollar, and you won’t sell it for $0.90 in a panic, which means that it won’t go down to $0.90, etc. But if you think that everyone else will treat Terra as worth zero, then you will dump it as fast as you can at whatever price you can get, which means that it will go down below $0.90, etc.Also there is an algorithm, but it is a complicated cloak thrown over these basic social facts. If one Terra goes down to $0.90, the arbitrage mechanism — you exchange one Terra for $1 worth of Luna, and then sell your Luna into the market for $1 — just doesn’t work. You exchange one Terra for $1 of Luna, but confidence in Luna is also falling, and the market is being flooded with Luna as people try to do this arbitrage. So the $1 worth of Luna you received is no longer worth $1, and then the next person who redeems Terra gets even more Luna and has to sell even more of them, which drives the price down more, which increases the amount of Luna being issued, etc., in a “death spiral.” There is no particular floor on this process, and it can go until everything is worth zero. However! As we discussed last month, Kwon and the Luna Foundation Guard did a smart thing. During the virtuous cycle of Terra’s existence, as its market capitalization grew and as Luna became more valuable, they used their valuable Luna to buy a bunch of Bitcoins. Luna is a creature of Terraform: If you lose confidence in Terra you will simultaneously lose confidence in Luna, and being able to exchange one Terra for infinity bazillion Luna will not do anything to prop up the price of Terra. But Bitcoin is an entirely separate thing. Terraform made up Terra and Luna, but somebody else made up Bitcoin. If people lose confidence in Luna and Terra, Bitcoin will still be valuable.And so the LFG bought a bunch of Bitcoin and promised to use it to defend Terra’s peg to the dollar. If one Terra goes down to $0.90, instead of turning Terra into Luna and selling them in a death spiral, the LFG can buy Terra for $0.90 and pay for it in Bitcoin. If the LFG has enough Bitcoin, and if Bitcoin’s price holds up, then it can defend the peg and keep the price of Terra close to $1.The point is that you print a lot of Luna when Luna prices are high and exchange them for Bitcoin. And then if Luna prices fall, you can use the Bitcoin to buy Terra and keep it at $1, avoiding a death spiral. As I wrote last month: “The basic structure of the trade is (1) Ponzi, (2) acceptance, (3) diversification, (4) permanence.”I suppose Kwon would have liked a few more months of widespread acceptance of Terra, so he could build up the Bitcoin reserves. (“We will keep growing reserves until it becomes mathematically impossible for idiots to claim depeg risk for $UST,” Kwon tweeted in March; the target was $10 billion of Bitcoin.) But he bought a lot of Bitcoin, anyway, which gave him a lot of ammunition to use to defend Terra’s peg when it broke over the last few days.So far it is … working … okay? As of noon today, CoinMarketCap tells me that Terra is at about $0.91, which is simultaneously (1) quite a lot lower than $1 but also (2) quite a lot higher than $0. Those are the two stable equilibria of an algorithmic stablecoin: In the long run, either it’s worth a dollar or it’s worthless. Terra is still fighting it out: It broke the buck (bad), but it does not seem to be in a death spiral (good). Either Kwon, LFG and other Terra bulls will defend the peg and wrestle it back to $1, or, uh, well, or they won’t and it will go to the other place.As of right now I don’t know what the answer is and wouldn’t want to hazard a guess, though I will say that $0.91 is much closer to $1 than it is to $0. “Deploying more capital - steady lads,” Kwon tweeted yesterday. I bet he’s having fun. “Close to announcing a recovery plan for $UST. Hang tight,” he tweeted this morning.People often talk about “bank runs” on stablecoins. Here, for instance, is the Federal Reserve’s annual Financial Stability Report, released yesterday, which contains some worrying about run risk on stablecoins:Stablecoins typically aim to be convertible, at par, to dollars, but they are backed by assets that may lose value or become illiquid during stress; hence, they face redemption risks similar to those of prime and tax-exempt [money market funds]. These vulnerabilities may be exacerbated by a lack of transparency regarding the riskiness and liquidity of assets backing stablecoins. Additionally, the increasing use of stablecoins to meet margin requirements for levered trading in other cryptocurrencies may amplify volatility in demand for stablecoins and heighten redemption risks.The idea of a bank run is that you have a backed stablecoin, like Tether, in which each $1 stablecoin is in theory backed by at least $1 worth of dollar-denominated assets. The worry in a bank run is that people all decide to withdraw their money from the stablecoin at once, perhaps because they worry about its solvency (i.e., they worry that it is only backed by $0.99 of assets) or for some other reason. To meet withdrawals, the stablecoin has to sell assets, which drives down their price, which leaves the coin backed only by, say, $0.95 worth of assets. Panicky holders withdraw even more money, pushing the assets down more. And since holders get paid out at $1, they drain value out of the pool; people who don’t withdraw are left with claims on the bad illiquid assets, which are worth even less.That’s not great, but what I want to emphasize is that this is much worse. A bank run is a fairly mild event compared to a death spiral. In a bank run, your $1 stablecoin is backed by some pool of assets that are worth something; a rush to withdraw money leads to fire sales that depress their value, but their value derives from something other than confidence in the stablecoin. In a death spiral, the whole system is built on confidence in the stablecoin; if that confidence evaporates then there is no floor at all on the value.To put it another way: In the 2008 financial crisis, a money market fund called the Reserve Primary Fund “broke the buck”; it had exposure to Lehman Brothers debt, which defaulted, leading to a run on the fund and ultimately its liquidation. This was huge news at the time, a seminal event of the global financial crisis. Also Reserve Primary Fund investors got back about 99 cents on the dollar. The potential outcomes for a money market fund, or a fully backed stablecoin, are like (1) $1 or (2) slightly less than $1. That is not how algorithmic stablecoins work.Meanwhile, the mechanism that LFG is using to defend the peg is interesting. It has loaned Bitcoin to market makers to use to protect the UST peg to the dollar. For one thing, this means that LFG (or, rather, the market makers) is effectively selling Bitcoin to buy UST, putting pressure on the price of Bitcoin: If you are dumping Bitcoin to prop up the price of Terra, the price of Bitcoin will go down.If you are a market maker, presumably your bet here is that you can buy Terra at $0.91, it will stabilize, and you will end up being able to sell it in a few days for $1, making a quick 10% profit. Then I guess you buy back the Bitcoins you used and deliver them back to LFG? You have some Bitcoin/dollar price risk; I suppose you can hedge that. The trade here is that $1 is a stable equilibrium for Terra, and if you can push it back to that equilibrium you’ll make a nice return on your efforts. You just need to make sure that you have enough capital to push it back to $1.Because the bad outcome is that this does not work, there is a death spiral, and Terra ends up worthless. Then you wasted like a billion dollars of Bitcoin buying something that was going to zero. That would be bad! Arguably LFG’s decision to deploy a lot of Bitcoin is a sign of confidence that it will work. Otherwise they’d keep the Bitcoins.
  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Meme finance
    
  
My  main corporate finance advice for much of 2021 was, like, “be a meme stock.” There were a lot of retail investors on Reddit looking to pour money into the stocks of companies whose executives catered to meme investors. If you were a corporate chief executive officer and you were willing to talk a lot about Bitcoin and Dogecoin and non-fungible tokens, mix it up on Twitter, and occasionally do Zoom interviews with no pants on, then retail investors would love you and your stock would go up. That would be good in part because then you could do an  at-the-market stock offering and raise money to  make your business better, but also because your stock going up is good in itself: The purpose of a public-company executive is to make the stock go up. Traditionally one does that with cash flows, but in 2021 the way to do it was with memes, and good executives adapted.Now it is 2022 and the whole meme-stock thing  seems to be dead? But “Do Meme Stuff” is still a chapter in the corporate finance textbooks, so you can still give it a try. In particular, if you run a publicly traded chain of strip clubs, it does make a certain sense to try to meme it up. All the elements are there:	You run a chain of strip clubs, which has an obvious titillating appeal to a certain class of very online investors.	Not wearing pants is pretty much the whole premise of your business.	You can promise to accept Bitcoin.	You can do non-fungible tokens.	I don’t know, those are the main elements I guess, this is not particularly scientific. The main counterargument is “no, it is 2022, this is over.” Still, I appreciate that RCI Hospitality Holdings Inc., which runs adult entertainment clubs including “Rick’s Cabaret, Jaguars Club, Tootsie’s Cabaret, XTC Cabaret, Club Onyx, Hoops Cabaret and Sports Bar, Scarlett’s Cabaret, Temptations Adult Cabaret, Foxy’s Cabaret, Vivid Cabaret, Downtown Cabaret, Cabaret East, The Seville, Silver City Cabaret, and Kappa Men’s Club,”  went full meme this week:RCI Hospitality Holdings Inc., which owns strip clubs and bars across the U.S., is bringing its earnings call to Twitter Monday as it tries to generate buzz among retail traders and boost its slumping stock price.The novel approach to the quarterly call, typically a chance to present results and take questions from analysts, comes as the turbulent market is crushing retail traders, who proved their power to move equity prices during the pandemic meme-stock boom. Still, RCI sees social media as an inexpensive way to potentially broaden its shareholder base, according to Chief Executive Officer Eric Langan.“We need more reach and we can’t get it through traditional banks,” said Langan, 54, who joined Twitter in February. “We spend so much time and money going after institutional investors, this is a much easier and much less expensive route.” …To drum up buzz, it hired financial influencer account Litquidity,  an online brand well-known among young Wall Streeters that boasts almost 900,000 followers on Instagram and Twitter, to run its social-media earnings call.The  Bloomberg transcript of the call is … mostly pretty normal? It seems like they mostly got the usual stock analysts dialing in to ask normal stock-analyst questions in a slightly less convenient forum. But there are some retail questions like, uh, can you sell the stock in the strip clubs:Awesome. Hey, thanks, thanks for doing this, I'm new investor and really excited about the direction of the company. Eric, as you touched on obviously the the point of this Twitter spaces to get the individual investors excited and one of the things for me, it was a little disconcerting as such low trading volume.And just one small thing that came to mind, is there any way without kind of crossing boundaries to get club billers potentially interested in becoming investors and some sort of, I don't know maybe like some loyalty program or something like that, any thoughts?Eric Langan, President and Chief Executive Officer:We are doing our NFT which is will be our benefits program, but we also had a program back in the early '90s called own a piece of the action and we amortize that we NASDAQ traded company and all the clubs and we've been talking recently about bringing that promotion back as well. And putting that back out into the clubs since so many individual investors are also the customers and are guests of our locations. Or investors proposing people they’d like to see in the clubs:Yeah, great quarter guys. And again, Eric, thank you for being so proactive within the community. I really appreciate it. As the younger guy experience in these type of clubs. I wonder if the team has looked into acquiring talent through venues like Twitch and YouTube, I'm not sure if you've heard of the names of up-and comers like Aiden Ross and -- but any detail on that to kind of get the best talent through the door?Sure. The stock was down about 3.7% as of noon today. Just doing a Twitter Spaces about NFTs doesn’t really work magic anymore.
  
    
      
        
      
    
  


  
    
      SPAC SPAC SPAC
    
  
Back in March, the US Securities and Exchange Commission proposed new rules for special purpose acquisition companies. A SPAC is a blank-check company that goes public, raises a pot of money, and then uses it to merge with some private company, thus taking it public in a “de-SPAC transaction.” There is a view that the target company can be more casual with its disclosure in the de-SPAC transaction than in a regular initial public offering. In a regular IPO, the company that is going public has to describe its business accurately, with a focus on actual historical performance; in a SPAC, the theory goes, the company can market itself based on wildly optimistic projections of future profits, and if it gets those projections wrong no one gets in trouble.The SEC’s proposed rules crack down on that in various ways; we  discussed them in March. One small odd element of the rules has to do with “underwriter liability.” Basically if a bank underwrites an IPO, and the disclosure in the IPO is wrong, the bank can be sued. Similarly if a bank underwrites the initial offering of a SPAC, and the disclosure is wrong, the bank can be sued — but SPACs are just empty boxes raising cash, so there is not a lot of disclosure there to be wrong. Eventually the SPAC merges with a target company, and it puts out a disclosure document for that de-SPAC merger, describing the actual business of the target company (and its optimistic financial projections, etc.). But there is no “underwriter” for the de-SPAC merger — the banks are not technically selling stock — and so there is no underwriter liability. So if the disclosure about the target company is wrong, it is hard to sue the banks.The SEC proposed to change this. Specifically, the proposal says that if a bank both underwrites the initial public offering of the SPAC, and advises on the de-SPAC merger with the target company, then the bank will be liable for any misstatements in the target company’s disclosure.[2] “In this way,” says the SEC, the proposed rule “underscores and reinforces that the liability protections in de-SPAC transactions involving registered offerings have the same effect as those in underwritten initial public offerings.”What does this rule mean? The SEC suggests that it will make underwriters more careful gatekeepers of de-SPAC transactions:The due diligence efforts performed by underwriters are central to the integrity of our disclosure system. The investing public relies on underwriters to “screen the multitude of issuers seeking access to the capital markets” and expects them to verify the accuracy of the information in the registration statement. … The Commission has stated that “an underwriter [in a securities offering] impliedly represents that he has made such an investigation [of the accuracy of the information in the registration statement] in accordance with professional standards” and “[i]nvestors properly rely on this added protection which has a direct bearing on their appraisal of the reliability of the representations in the prospectus.”But there is an alternative interpretation of what the rule means, which is: If you are a SPAC, you need to hire one bank to do the SPAC’s initial public offering, and a different bank to do the de-SPAC merger. As long as one bank doesn’t do both things, then neither has any underwriter liability. It’s a bit more complicated than that — typical SPAC underwriting fees are paid partly up front and partly on the de-SPAC merger, and getting those back-end fees can trigger underwriter liability, so you have to fiddle with the economics a bit — but that is the basic idea. The SEC has created a nice new program to make companies hire an extra bank for their SPAC deals.Anyway here is a story titled “Global Banks Flee the Monster SPAC Market They Helped Create”:Just a few years after banks helped create a gargantuan market for blank-check companies, they’re pulling away from the deals, afraid of the risks. Goldman Sachs Group Inc. is ending its involvement with most of the special purpose acquisition companies it took public and pausing new U.S. SPAC issuance, Bloomberg reported on Monday. Bank of America Corp. scaled back work with some SPACs and could retreat further as it evaluates its policies surrounding the deals, people familiar with the matter said. …The banks’ recent concerns center around liability risks stemming from the new rules, which are aimed at tightening oversight on a market after it set back-to-back yearly records. The proposals would require SPACs to disclose more information about potential conflicts of interest and make it easier for investors to sue over false projections.  They also would require underwriters of a blank-check offering to also be underwriters of the SPAC’s subsequent purchase of a target firm, known as the de-SPAC. That expansion of underwriter liability poses a greater risk for investment banks, prominent law firms have cautioned.Well. They are fleeing the SPACs they created. But in theory Goldman could go do the mergers for Bank of America’s SPACs, and BofA could do the mergers for Goldman’s SPACs, and everyone could get paid and no one would have underwriter liability. The SPAC market is not exactly booming right now, but if it comes back I suspect that the result of the SEC rules will be a division of labor among SPAC-issuance banks and SPAC-merger banks. I am not sure how that helps anyone, except maybe the banks.
  
    
      Anti-ESG
    
  
If you want to have exposure to oil companies, right now the market offers you two sorts of asset managers:	Regular asset managers will buy stock in oil companies. Some of them will be indexers (and buy stock in all the oil companies), while others will be active managers (and try to buy stock in the oil companies that will go up); some will be fairly unengaged shareholders, while others will call up the oil companies and say things like “you should try to make more money.”	ESG — environmental, social, and governance — asset managers will also buy stock in oil companies, but then they will call up the oil companies and say “hey you should try to pollute less.” Some of them will be indexers (and buy stock in all the oil companies), while others will do ESG screens and only buy stock in the oil companies that already pollute less than average. (In theory, some could be concentrated activist ESG investors, buying stock in the oil companies that pollute more than average and trying hard to get them to stop, though that seems rare.)The market, however, lacks a third category. What if you want an asset manager who will buy stock in oil companies and call them up and say “hey you should try to pollute more”? That’s hard to find! The major categories of asset manager are, as it were, “neutral” and “ESG”; “anti-ESG” is not yet a major category. More than that, even the big neutral asset managers — big indexers with no explicit ESG mandates — tend to be interested in the systemic risks of their portfolio; often they  view climate change as a systemic risk, and so they push the oil companies in their portfolio to pollute less. If you want your oil companies to pollute more, there is no natural home for you.Well, that’s not quite true; there are anti-ESG fund managers, and while they all seem to manage tiny amounts of capital they tend to get a lot of press. Here’s a new one:An upstart financial firm backed by Peter Thiel and Bill Ackman has a message for American corporations: Focus on making money, not taking stands.Vivek Ramaswamy, who made his fortune in pharmaceutical startups before writing a book last year called “Woke, Inc.,” says he has raised $20 million to start a fund manager that would urge companies not to wade into hot-button social or environmental issues. Mr. Thiel invested both personally and through his Founders Fund, joined by Palantir Technologies Inc. co-founder Joe Lonsdale and other venture investors. …The firm, called Strive, will be based far from Wall Street in Mr. Ramaswamy’s home state of Ohio. In an interview Monday, the 36-year-old dubbed his approach “excellence capitalism,” focused on letting companies do what they do best—and nothing else—and inveighed against what he sees as a creeping liberal bias inside BlackRock Inc. and its peers, Vanguard Group and State Street Corp. , which he called an “ideological cartel.” …Mr. Ramaswamy’s project began under cover months ago, code-named “Whitestone” to capture its aim of being the anti-Blackrock, people familiar with the matter said. It isn’t known what products it will offer, and it has a long way to go to rival the combined market power of the financial giants it seeks to challenge.Okay.
  
    
      Things happen
    
  
Warehouse Owner Prologis Offers to  Buy Duke Realty for $24 Billion. Elon Musk Says Twitter Will  Comply With EU Content Rules After Takeover. Grindr Dating App to Go Public Through Tiga SPAC at $2.1 Billion Valuation. MicroStrategy’s  Bitcoin Bet on the Verge of Turning Negative. El Bagholder strikes again. Why Is It So Hard to Get a Restaurant Reservation Right Now? Michael Owen rinsed after baffling claim his NFTs won't lose 'initial value.' “At a costume party thrown after a day’s skiing, Wolff allegedly  struck a male colleague who was dressed as former U.S. President Donald Trump and then allegedly groped a female colleague, the people said.” Dolly Parton to star in a musical on TikTok about Taco Bell's Mexican pizza.If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] Technically “Terra” is the name for a whole class of stablecoins denominated in different fiat currencies, and “UST,” or “TerraUSD,” is the particular one denominated in US dollars. I am going to use them interchangeably. You can read the Terra documentation here.[2] From the release: “Proposed Rule 140a would clarify that a person who has acted as an underwriter in a SPAC initial public offering (‘SPAC IPO underwriter’) and participates in the distribution by taking steps to facilitate the de-SPAC transaction, or any related financing transaction, or otherwise participates (directly or indirectly) in the de-SPAC transaction will be deemed to be engaged in the distribution of the securities of the surviving public entity in a de-SPAC transaction within the meaning of Section 2(a)(11) of the Securities Act. Clarifying the underwriter status of SPAC IPO underwriters in connection with de-SPAC transactions should motivate them to exercise the care necessary to help ensure the accuracy of the disclosures in these transactions by affirming that they are subject to Section 11 liability for registered deSPAC transactions. In this way, proposed Rule 140a underscores and reinforces that the liability protections in de-SPAC transactions involving registered offerings have the same effect as those in underwritten initial public offerings.”
        
      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cggyut.5yz5/cf75d63c.gif" alt="" border="0" /></a>
