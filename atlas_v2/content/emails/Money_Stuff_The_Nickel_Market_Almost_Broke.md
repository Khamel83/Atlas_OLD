# Money Stuff: The Nickel Market Almost Broke

**Source**: inputs/saved_emails/Money Stuff The Nickel Market Almost Broke_Wed,_30_Nov_2022_13-53-52_-0500_(EST)_184c9e3bb9df6f5c.eml
**Type**: email
**Created**: 2025-08-25T02:54:06.297087

---

A fact about financial markets that occasionally produces strange results is that the total market value of a thing is, conventionally, (1) 
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      LME
    
  

A fact about financial markets that occasionally produces strange results is that the total market value of a thing is, conventionally, (1) the amount of that thing that exists times (2) the price of the last trade. So Bloomberg tells me that there are about 304.5 million shares of GameStop Corp. stock outstanding, and they closed at $25.60 yesterday, so GameStop’s market capitalization — the total value of its stock — is 304.5 million times $25.60, or about $8 billion. Nobody recently bought or sold all of GameStop for $8 billion, and if somebody did, the price would probably not be $8 billion.
  [1]
 But if you wanted to buy or sell one share of GameStop, the price you’d pay or get would be about $25.60, and you can multiply.
One type of strange result you can get from this is that if you have some weird small stock or cryptocurrency that doesn’t trade very much, you can give it a very large market capitalization by selling one share or token to your buddy at an inflated price, and then you can go around telling people “ooh look at the huge market cap of this thing, it is so valuable, it must have discovered a cure for cancer,” and maybe you can do bad stuff with that. We have talked about the infamous New Jersey deli that was  worth $2 billion. It wasn’t, of course, but its stock didn’t trade much, and it traded at a high price, and you could multiply. Allegedly  this supported a fraud. Or we have talked a lot about this in the context of cryptocurrencies, which are easy to produce in huge quantities and then sell to your buddies; the downfall of FTX and Alameda  seems to have  involved inflated market values of tokens that FTX had invented and mostly held itself.
But there are other possible strange results. Here is a stylized one:
	There is some commodity futures contract. There are a million contracts outstanding at a price of $20,000.	Holders of the contract have to post margin — collateral — to the commodity exchange each day. Whenever the price of the contract goes up by a dollar, people who are short the contract have to post $1 more of margin, and people who are long can take out $1 of margin. And vice versa.	Late at night, when trading is light, someone wants to buy a lot of contracts, and there aren’t many people around to sell them to her. So she ends up buying 10,000 contracts at $30,000 each. 	Everyone else wakes up in the morning to find that the price is now $30,000.	The people who were short 1 million contracts at $20,000 now have to post an extra $10,000 per contract — $10 billion total — of margin.	This is very unpleasant for them, and they might not have the money.	They could instead close out their short positions by buying back their contracts, but that (1) requires them to come up with the money anyway and (2) makes the price of the contracts go up more.

The margin calls are based on the total market value of the contract, so a smallish amount of trading can in theory produce a huge margin call.
We have  talked a  few  times  about the wild breakdown in the London Metals Exchange nickel market this March. Basically the price of LME nickel futures contracts spiked from about $29,000 per ton on Friday, March 4, to about $48,000 per ton at the end of Monday, March 7, due to a combination of fundamental (Russia’s invasion of Ukraine) and technical (short-squeeze-ish) factors. On Tuesday, March 8, LME nickel trading re-opened at 1 a.m.; by 6:08 a.m. the price had risen to $101,365. Later that morning, LME shut down nickel trading for more than a week; it also unwound all of the Tuesday morning trades, reverting the price to Monday’s final price of $48,078. When nickel finally reopened on March 16, it traded down on small volume for a while until reaching a more normalized price of $28,000 or so the following week.
In the past, I have mostly told this story as the story of one big nickel trader, Xiang Guangda, and his metals company, Tsingshan Holdings Group Co. Xiang got short a lot of nickel futures (partly but not entirely as a hedge to Tsingshan’s own nickel output), and when the price moved against him his brokers called him for billions of dollars of margin, and he basically said no. And the exchange called the brokers for billions of dollars of margin, but they didn’t have it (because Xiang didn’t post it to them), and so rather than bankrupt them and Xiang and everyone else, the exchange just said, okay, never mind, let’s undo those trades and pause nickel trading for a while. 
This is kind of an infuriating story;  I wrote earlier this month:
For one thing it seems unfair to cancel trades to bail out one big trader; it is arbitrary, and the opposite of how markets are supposed to work, and particularly harsh for the people on the other side of the trades. Also Xiang was a well-connected Chinese metals tycoon, and the LME is Hong Kong-owned, and there were some theories about the LME bending its rules for favored clients.
And in fact some of the traders on the other side — mainly Elliott Associates LP and Jane Street Global Trading LLC — were annoyed enough to sue the LME, arguing that it didn’t have the right to cancel trades like that. This week the LME filed its response, telling   its version of the story, and that version barely mentions Xiang.
  [2]
 Instead, it says:
	Trading early Tuesday morning was super-weird and not at normal prices.	Those trades led to a huge increase in the nickel price, which would have caused almost $20 billion of margin calls to a bunch of LME member brokers.	If the LME had called for that much margin, it would have bankrupted several traders and blown up the whole market.

This is not exactly a different story, but it is a more impersonal one. And yet also a riveting and alarming one. The LME sets the scene:
At around 22:30 every business day, LME Clear calculates overnight margin requirements, which are released at 03:00 the following business day, with any increases payable by Clearing Members by 09:00. In addition, where appropriate, LME Clear may release an additional intra-day margin call. When it does so, Clearing Members have one hour to pay.
And then describes how the wheels were already starting to come off on Monday:

Initial Margin calls due for payment by 09:00 were missed by three Members. One of these, amounting to $[redacted], remained unpaid, putting the Member in question in default, with potentially serious consequences.
By 13.15 pm, Members had faced an unprecedented 9 intra-day margin calls: the cumulative increase in margin requirement was approximately $7bn; this was nearly three times larger than the record set just the previous trading day, 4 March, which had itself been 40% higher than the previous record. LME Clear was concerned that it would not be feasible for Members to meet further intra-day margin calls. On a call at 13:45, the Market Risk Team was so concerned about Member liquidity that it recommended that no further intra-day margin calls be made for the rest of the day. This was extremely unusual and a departure from internal policy; nevertheless, [LME Clear Chief Executive Officer Adrian] Farnham considered it appropriate in response to the extreme market conditions, since it mitigated the liquidity pressure by giving Members time to meet their margin calls. Mr Farnham is clear, however, that this was no more than a temporary stop-gap and was not sustainable beyond the end of the day: LME Clear could not continue to be under-collateralised against Member default, particularly in such a volatile market, given the risk this posed to the market as a whole.

The price of nickel had moved so much that traders couldn’t meet margin calls, and so LME decided to stop calling them for margin. That’s a big risk! The purpose of margin is to make sure that traders on the losing side of a trade will pay what they owe. If they don’t post margin, then maybe the trade will move back into their favor, they won’t owe any money, and everything will be fine. Or maybe the trade will move against them even more, they will owe more money, and they won’t have it. Then you have a disaster: The clearinghouse owes money to the people on the winning side of the trade, but the money isn’t there, because the clearinghouse didn’t call for margin in time. 
Anyway the LME let this ride for a while on Monday afternoon, hoping things would get back to normal. And then on Tuesday morning everything broke:

When [LME CEO Matthew] Chamberlain saw these extreme price movements, he recognised that the market had become disorderly. That view was based on his expertise and long familiarity with the nickel market, the absolute price levels, the extraordinary speed of the increase and the absence of rational market forces capable of explaining these developments.
Mr. Farnham was informed at 05:53 that six Members had not paid their overnight margin payments, totalling $2bn (approximately one third of the total due). The massive price increases on 8 March would have necessitated further and still more unprecedented intraday margin increases. Based on his estimation of the likely increase in intra-day margin calls (which turned out to be an under-estimate), it was clear to Mr. Chamberlain that there was a very real risk of multiple Member defaults; that many Members would struggle or be unable to meet these margin calls; and that some might face insolvency.
This expectation was borne out in the early morning as between 05:33 and 08:18 the senior leadership of LME and LME Clear were approached by no fewer than seven Members who signalled that they were in difficulty in posting margin. ...
At 07:24 Mr. Kirkwood, Head of Market Risk at LME Clear, circulated a spreadsheet showing margin call calculations based on prices at 07:00, Members' current open positions and LME Clear's assessment of Members' credit worthiness (the "First Default Risk Spreadsheet"). It demonstrated that a minimum of $19.75bn of further intra-day margin calls would need to be made that day, to be paid within one hour of being called. Mr. Farnham describes this sum as "staggering and not like anything LME Clear had seen before" .

If they couldn’t post margin, (1) they’d be in default and (2) the price of nickel would go up even more:
Member defaults had the potential to raise the price even further in what is known as the "pro-cyclical feedback loop". Mr. Farnham describes this a "death spiral, in which the actions LME Clear would be required to take to try to address the defaults would exacerbate the underlying causes, leading to further defaults and so on". Mr. Chamberlain also took this into account (in the period between the suspension decision and Decision to wind back the clock). This would, in Mr. Chamberlain's view, have been likely to "make a bad situation much worse, by creating a self-perpetuating spiral of price increases" leading to further defaults and market disorder.
So the LME got together and considered a neatly numbered list of options:
	Option 1A: Let the Tuesday morning trades stand, call for $20 billion of margin, and blow everyone up. They didn’t like that.	Option 1B: Let the Tuesday morning trades stand, but ignore them for margin purposes, instead “calculating margin by reference to the Monday Closing Price.” That is less disruptive to trading, and doesn’t blow anyone up, since no one has to post more margin. But it’s incredibly risky, and would leave “LME Clear significantly under collateralised in breach of its regulatory obligations.” If you think that the Tuesday prices are real, then letting everyone slide on margin is a terrible idea. If you think the Tuesday prices are wrong, better to cancel them.	Option 2: Adjust the prices of the Tuesday trades, which seemed pretty arbitrary and was rejected.	Option 3A: Cancel all trades after midnight. That’s what they did.	Option 3B: Cancel some trades after midnight, and “seek to identify a point in time during the morning of 8 March as a cut-off for upholding trades.” They just went with the simpler Option 3A: The price on Monday was normal enough; the price on Tuesday was not.

Bloomberg  calculated at the time that the LME ended up canceling $3.9 billion worth of trades over about seven hours on Tuesday morning. This is not my stylized story of a sleepy illiquid overnight market moving the price dramatically: The Tuesday morning session was busy, even if the price swung wildly, and, in Chamberlain’s view, did not “make sense.” But it is still a story in which canceling $3.9 billion of trades avoided $20 billion of margin calls. To LME, at the time, that seemed like a good trade.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      FTX
    
  

The     story that is emerging about the collapse of Sam Bankman-Fried’s crypto exchange, FTX, and its affiliated trading firm, Alameda Research, is that FTX took customer money for crypto trades, and Alameda used its own money for crypto trades, and nobody kept track of the money, so Alameda kept using FTX customer money for trades, and FTX didn’t notice, and Alameda kept losing that money, and it also didn’t notice? And then one day someone noticed and the whole thing vanished in a puff of smoke? I don’t know! That story makes no sense to me at all! And I don’t think that it is a good story or anything; in many ways an orderly fraud would be better than a vast money-sucking whirlwind of chaos. But “nobody kept track of the money” does seem to be the story that everyone is going with.
Here is a Wall Street Journal story about  the early days of Alameda:

Mr. Bankman-Fried placed huge bets on crypto assets but paid little heed to the risk of those bets, brushing off the staffers’ concerns, according to people familiar with the matter. The firm commingled trading capital with operating cash and had poor record-keeping that left its profits and losses unclear, they said.
“He didn’t want to feel constrained,” said Naia Bouscal, a former software engineer at Alameda who left with [Alameda co-founder Tara] Mac Aulay and the others. “But as a result we ended up not really knowing how much money we even had.”

They left in 2018. “Mr. Bankman-Fried told The Wall Street Journal … that Alameda addressed the accounting, risk and other issues they raised,” which makes it sound like Alameda did know how much money it had for the last four years, but in fact Bankman-Fried has been saying  on Twitter and  in interviews that Alameda and FTX did not keep particularly careful track of their money, so who knows. The Journal goes on:

Mr. Bankman-Fried had worked at quantitative trading giant Jane Street Capital LLC, a firm that has extensive risk controls. But when colleagues at Alameda proposed setting up rigorous structures and systems for risk, compliance and accounting, Mr. Bankman-Fried was dismissive of the idea, according to the people.
He said such extensive controls could crimp Alameda’s activity and limit how fast the firm could move to place trades, the people said, reducing potential profit.
Alameda built a trading algorithm to make a large number of automated, rapid-fire trades, but some at the firm feared it couldn’t keep track of all the activity, the people said. The staffers said Alameda needed to do a better job tracking its trading to properly account for its gains and losses, but Mr. Bankman-Fried rejected the idea, according to the people.

One thing about   working at Jane Street is that, when you show up for work at Jane Street as a trader, your job is not, like, “rebuild Jane Street using only materials found in nature.” Your job at Jane Street is more like “we have built a good technology stack and risk-management and accounting and performance attribution systems, now go find some profitable trades.” You find some trades that you think are profitable, you do them, and if you’re right then Jane Street’s existing systems will notice and reward you. If you’re wrong, the risk systems will stop you. You are just in charge of finding the good trades.
If, later, you leave to start your own firm, you will take with you your skill at finding good trades. (Which seems like a perishable thing.) But it’s not obvious that you will take with you Jane Street’s risk-management culture, and you certainly won’t take its risk-management systems. And then when your colleagues say to you “hey, let’s set up some risk systems and hire an accountant, like we had at Jane Street,” you can reply “nah, I’d prefer to ignore that stuff, like I did at Jane Street.” You’re both right! Someone else at Jane Street set up those systems so you didn’t have to worry about them. But now you’re in charge, and if you don’t worry about them no one will, and then you end up not knowing how much money you have, or how much you’re making or losing, or how much you owe your customers.
Meanwhile here is a Financial Times story about  the lavish later days of FTX:

A lack of internal controls that are typical of large financial companies meant FTX’s spending went largely unchecked, according to former employees and filings in the group’s Delaware bankruptcy case.
“[It was] kids leading kids,” said one former employee. “The entire operation was idiotically inefficient, but equally mesmerising,” they added. “I had never witnessed so much money in my life. I don’t think anybody had, including SBF.” …
The perks enjoyed by employees of the now-collapsed exchange included round-the-clock catering in the Bahamas office, “in addition to the free groceries, barbershop pop-up, and bi-weekly massages”, according to one employee.
FTX also provided Bahamas staff with a “full suite of cars and gas covered for all employees [and] unlimited, full expense covered trips to any office globally”, the employee added. Staff at FTX US, its separate arm for the American market, were allowed $200 a day in DoorDash food delivery credits.
Alameda Research, a crypto hedge fund founded by Bankman-Fried, also owes $55,319 to the Margaritaville Beach Resort in Nassau, which was founded by US musician Jimmy Buffett, according to bankruptcy filings this week. A “Who’s To Blame” margarita at one of the resort’s bars costs $13.

I think that this is best understood as an accounting problem. A month ago,  a common perception of FTX was that it had “one of the highest revenue/profit/valuation per employee as any company in the world.” As far as I can tell, FTX believed this. If in fact your employees are incredibly good at making money, then lavishing them with perks is simply optimal. Allowing $200 a day in DoorDash to prevent your insanely profitable employees from ever having to think about their meal budget is a good business move. Your employees’ time and attention is so valuable that it is foolish to make them waste time filling out expense reports.
But a big part of the reason that FTX believed it was so profitable is that nobody made any effort to keep track of the money. If you lose $4 billion trading and borrow $8 billion of customer money to cover the gap and don’t keep track of that borrowing, then it looks like you made $4 billion trading, and you will say things like “we are incredibly profitable per employee, $200 DoorDash for everyone!” FTX spent like the company it thought it was, but it didn’t bother to find out what kind of company it actually was.

  
    
      
        
      
    
  


  
    
      Hung deals
    
  

Basically the market for leveraged loans was very good at the beginning of 2022, and pretty bad as we near the end of 2022, so a lot of banks signed up to do a lot of buyout loans in 2022 that they ended up being unable to sell on decent terms. If you are a bank, you have to decide whether to sell your loans now, at a loss, or hold on to them and hope the price goes back up. This is an economic decision — like any other trading decision — though it also has an accounting component; if you don’t try to sell the loans then you don’t know how much money you’ve lost. Also there are some year-end issues to consider.   Anyway:

Banks in the US and Europe with around $42 billion of buyout debt stuck on their balance sheets are making the most of their last chance to get rid of it this year.
Stabilization in the leveraged loan and high yield bond markets has led to an opening for deals -- including for bonds and loans tied to the buyout of TV ratings business Nielsen Holdings Plc -- as banks try to reduce debt on their balance sheets before the holidays. Offloading the so-called hung debt, even at steep discounts, confines losses to this financial year while also appeasing risk departments and regulators. …
“If the window is open for these hung deals, you will see the banks jump through it because the window is not open for every deal,” said Bill Zox, portfolio manager at Brandywine Global Investment Management. “And it could shut again at any time.”
Hung debt has been a big problem for Wall Street this year. Banks have taken huge mark-to-market losses on deals they underwrote before a rapid rise in interest rates crushed funding markets and the threat of recession quashed investor demand for riskier assets. With that backdrop, stabilization of leveraged loan prices -- which recently recovered to an average of close to 93 cents on the dollar in the US, according to index data -- has created a fertile ground for deals.
Still, while some debt is being offloaded, more recent buyouts are adding to the pile, including about $13 billion of financing related to Elon Musk’s acquisition of Twitter and, more recently, a private equity buyout of a majority stake in Roper Technologies Inc.’s industrial operations business.

Around here, I have eyes only for that Twitter Inc. debt. I have   joked a  lot about writing the offering memorandum for that debt, but I suppose realistically it’s going to be a one-page agreement saying “you agree to buy this debt on an as-is basis, we make no promises about anything, and you acknowledge that you’ve seen Elon Musk’s Twitter feed and want to buy the debt nonetheless.” And then the price will be, you know, 60 cents on the dollar or whatever. 
I have seen a lot of people speculate about that debt ending up in the hands of tough distressed-debt vulture funds who will keep a close eye on Twitter’s cash flows and fight Elon Musk for control of Twitter, and my reaction is: What? No. If you are a tough distressed-debt vulture investor you have plenty to keep you busy fighting against ordinary companies and private equity sponsors; you don’t need Elon Musk as an enemy. Also you probably don’t want to end up owning Twitter, particularly not if you had to fight Elon Musk for it. What will be left?
No, if I were Musk’s bankers I’d be trying to sell that debt to … venture capitalists?   Jason Calacanis’s “randos”? Start a retail vehicle, like, the Support Elon’s Twitter Free Speech Thing Credit Fund, to buy the debt at 80? Find some buyers who trust Musk completely and don’t want a fight with him. Or, I’d try selling it to Apple Inc., or Jeff Bezos. Selling that debt to someone who wants a fight with Musk and can afford it, and who might want to own Twitter, makes sense. I just don’t think that’s a distressed fund.

  
    
      Blockchain blockchain blockchain
    
  

There was a huge vogue, in about 2017 and 2018, for blockchain projects. “We will put the stock exchange on the blockchain,” or loan trading, or supermarket produce, or real estate, or cargo manifests, or whatever. If you ran a stock exchange or a bank or a shipping company, you needed to have a blockchain project. An industry of blockchain consultants sprang up to sell blockchain projects. The projects were announced. The announcements got written up in the press. We talked about them a lot, around here, back in 2017 and 2018. Not so much since then.
The last few months have been pretty bad for the reputation of, like, centralized cryptocurrency shadow banks. This has almost nothing to do with the question of whether a blockchain is a good database architecture for stock exchanges or property registers or shipping. But if you announced a blockchain project in 2018, and by 2020 you realized it wasn’t going anywhere, 2022 is a good year to formally kill it. We   talked last week about the Australian Securities Exchange killing its blockchain project (which started way back in 2015), and  now here’s this:

Maersk and IBM will wind down their shipping blockchain TradeLens by early 2023, ending the pair’s five year project to improve global trade by connecting supply chains on a permissioned blockchain.
TradeLens emerged during the “enterprise blockchain” era of 2018 as a high-flying effort to make inter-corporate trade more efficient. Open to shipping and freight operators, its members could validate the transaction of goods as recorded on a transparent digital ledger. ...
“TradeLens has not reached the level of commercial viability necessary to continue work and meet the financial expectations as an independent business,” Maersk Head of Business Platforms Rotem Hershko said in a statement.

I assume that Maersk will still have some way to keep lists of what’s on its ships? Like that seems like an important function for a shipping company? But they’ll no longer put out excited press releases about how they keep the lists.

  
    
      Things happen
    
  

Activist House Flippers Take On Wall Street to Keep Homes From Investors. UBS Backtracks on CEO’s Plan to Reach Wider Swath of Wealthy US Clients. A year of pain: investors struggle in a  new era of higher rates. Yield Curve  Inversion Reaches New Extremes. EU wants to use frozen Russian assets to  fund Ukraine reconstruction.   AMC Networks to Cut 20% of US Staff as CEO Abruptly Departs.   DoorDash to Slash About 1,250 Jobs to Pare Back Rising Costs. Singapore’s Temasek  opens review into ill-fated FTX investment. Saudi Wealth Funds Follows   Green Bond with $17 billion Loan. Elon Musk’s Twitter Politics Add to Pressure on  Tesla’s Brand Image. “These were not  the lies of a calculating con artist, but of a mentally ill person who could not help himself.” Ramaphosa Says $580,000 Was   Innocently Hidden in Game Farm Sofa.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] Ordinarily the way that this happens is that someone wants to *buy* all of a company, and to do that they normally need to pay significantly *more* than its market capitalization: The per-share price you pay to buy all of the shares is higher than the per-share price you pay to buy one share, in part because you are paying a “control premium” but also because of how supply curves slope. The way demand curves slope, you might also think that a company that was desperate to *sell* all of itself would get a *lower* price than its market cap. (The per-share price you get for a market order to sell one million shares is generally lower than the per-share price you get for selling 100 shares, so why shouldn’t that extend indefinitely?) In practice this doesn’t come up much: Why would a company want to sell all of its shares at below their market price? Still it is a possibility. I don’t pretend to understand 
the situation at Redbox Entertainment Inc., but one possible description is that the board of directors realized it desperately needed to sell itself, and so took a price that was way way lower than its market price.


  [2] Xiang was not an LME member; instead, he seems to have had over-the-counter trades with his brokers, which they hedged on the LME. The LME’s response suggests that they didn’t even know about this. Paragraph 66: “Subsequent to the Decision, it has emerged that underlying the unprecedented price convulsions on 8 March 2022 there very substantial short positions in the over-the-counter (‘OTC’) market contributing to market disorder. OTC trading is carried out directly between the trading counterparties, without the supervision of an exchange. Entities within the Tsingshan Holding Group Co Ltd (‘Tsingshan’) group appear to have been some (but not all) of those holding large OTC short positions. On 8 March, the LME was not aware of the large short positions in the OTC market: the LME does not monitor OTC positions and, indeed, there are only limited circumstances in which the LME requests disclosure of information about Members' (or their Clients') OTC positions. As explained below, the Claimants are simply wrong to suggest that the LME was motivated to protect Tsingshan or others in its position. Mr. Chamberlain reasonably considered that he did not need to isolate the cause of the disorder in order to determine that the market was disorderly or to determine the appropriate response.”


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23chrrck.5jhx/3a0c6420.gif" alt="" border="0" /></a>