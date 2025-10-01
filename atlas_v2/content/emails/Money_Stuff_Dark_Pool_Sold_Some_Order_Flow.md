# Money Stuff: Dark Pool Sold Some Order Flow

**Source**: inputs/saved_emails/Money Stuff Dark Pool Sold Some Order Flow_Thu,_23_Sep_2021_12-38-54_-0400_(EDT)_17c138914aee6fd0.eml
**Type**: email
**Created**: 2025-08-25T02:53:57.457327

---

Programming note: Money Stuff will be off tomorrow, back on Monday.
  
    
      Bad PFOF
    
  
A rough, inaccurate but useful way to think about U.S. equity market structure is that the prices on the stock exchange are bad. You can go to a public stock exchange and see a “lit,” public bid and offer for every stock; the exchange will tell you at all times, like, “you can buy this stock for $10.05 or sell it for $9.95.” (The best buying and selling price available on all the lit exchanges is called the “national best bid and offer” or NBBO.) But if you ever find yourself paying the lit price to buy a stock, or accepting the lit price to sell it, you have done poorly. That is just the sticker price, the advertised price, the price for rubes. Somewhere, in the dark, there are hidden orders at better prices, and if you and your broker are any good you will find them. I want to stress that this is rough and inaccurate; if you work for a stock exchange, or for an electronic market maker that quotes on the exchanges, you don’t have to email me to be like “actually our quotes are great.” I just mean that, to understand what people get mad about in market structure, it is often helpful to start from the premise “they think the NBBO is bad.”If you start from that premise you can build a model in which there are basically four different “market” prices for a stock. In ascending order:	The national best bid is the price you’d get if you tried to sell the stock on a lit stock exchange. This price is too low. Say it’s $9.95.	The “real” best bid is the best price you could find to sell the stock if you knew where to look. Say there’s some dark pool somewhere where someone has a hidden order to buy the stock at $9.99; if you find that order you can sell at $9.99.	The “real” best offer is the best price you could find to buy the stock if you knew where to look. Say it’s $10.01.	The national best offer is the best price you could find to buy the stock on a lit stock exchange. This price is too high. Say it’s $10.05.Prices 1 and 4, the NBBO, are transparent; anyone can see what they are. Prices 2 and 3, the “real” best prices available in dark pools and hidden liquidity and internalizers’ books and so forth, are not; certain sorts of experts know what they are but most people have to guess at them.Your goal, as a person looking to buy or sell stock, is to find the real best price, by scouring dark pools and knowing a lot about markets and routing orders cleverly, or by having a trusted intermediary do that for you. The goal of the expert intermediary selling you the stock is … well, their goal is complicated. Their goal is to (1) make money for themselves and (2) keep you coming back.If they sell you stock at worse prices than the NBBO they will get in trouble. If they sell you stock at the NBBO, they will do well — on this model, they can buy stock at the real best price and resell it to you at the NBBO, keeping the difference for themselves — but if you are sophisticated you won’t keep coming back. This model is so widely understood that executing trades at the NBBO is often considered bad. What you want is to get “price improvement,” to execute at some price better than the NBBO, so that you think you might be getting the real price. And so the game for the expert intermediaries selling you the stock is to sell it to you at some price between the lit best price and the real best price. You try to buy stock, the national best offer is $10.05, your broker says “good news, we got you price improvement, you’re filled at $10.03.” You are happy because you got a better price than the NBBO; you got the great-customer discount; you might even have gotten the real price, what do you know. The market maker who sold you the stock is happy because it can buy at $10.01 (the real best price) and sell at $10.03 (the price-improved, better-than-NBBO-but-still-worse-than-real best price). If you knew that the real price was $10.01 you’d be mad, but you don’t; for all you know the real price was $10.03, you got it, and you’re doing great.This model is too cynical, but I think it accurately captures why people are mad about payment for order flow for retail stock trading. We have  discussed payment for order flow several times before, in more sensible and less cynical ways, but on the cynical model all PFOF is is:	You send an order to your broker.	Your broker sends it to a wholesaler, an electronic market maker for retail customers.	The wholesaler buys it at the real price, say $10.01.	The wholesaler sells it to you at some price-improved price, say $10.03.	The wholesaler makes $0.02.	The wholesaler gives some of that money to your broker as payment for getting to do this free-money trade.Again, again, too cynical. The wrongest part of this model is probably point 3; the wholesaler does not, as a general matter, go out and “front-run” your order by buying it at the real price and turning around to sell it to you at a higher price. (The wholesaler runs a book, trades with you out of inventory, has its own model of the correct price, tries to trade at some spread around that, etc.) But people do get really mad about payment for order flow, even though it gives retail customers better prices than they would get on the public stock exchange, and it is worth understanding that position. If you start from “well, of course, but the prices on the public stock exchange are for rubes, nobody pays those,” it becomes pretty understandable. I don’t really want to endorse the model I laid out above except, oh man, look at this Securities and Exchange Commission enforcement action from Monday:The Securities and Exchange Commission instituted settled charges against Illinois-based Coda Markets, Inc. for making material omissions and misleading statements to the broker-dealer subscribers of its alternative trading system (ATS) about how it handled and routed orders for execution. …The SEC's order finds that from December 2016 to July 2019, Coda failed to disclose its use of a circular routing arrangement when handling subscriber orders. According to the SEC's order, Coda disclosed that it created individually customized routing tables for the subscribers to its ATS, with venues ranked in the routing tables depending on the subscriber's trading priorities. The order finds that when Coda had discretion over the routing table, Coda inserted one of two broker-dealers as the first external destination because, among other reasons, Coda had agreements with these broker-dealers to share the net trading profits on executions of orders routed from Coda. Coda is a broker-dealer, and it runs a dark pool called Coda ATS. Some of its customers were subscribers to its dark pool; they would send orders to Coda, and Coda would either execute the orders in the dark pool or, for “the vast majority of Coda’s order flow,” route them somewhere else: It would send an order to other dark pools and stock exchanges until it executed, with the dark pools and exchanges ranked on some criteria along the lines of “where will we get the best price.” Customers would send their orders to Coda because they hoped to buy stock at the real price, rather than the lit price. Maybe the stock is for sale at the real price in Coda’s dark pool, and they’ll buy it there, or maybe it’s for sale at the real price in some other dark pool, and Coda, which is smart, will route their orders to that pool so they can buy it there. And then here’s what Coda did:During the relevant period, Coda had agreements with two other broker-dealers to execute orders received from Coda by trading on a net basis (the “Net Trading Firms”), wherein Coda prescribed how the Net Trading Firms would handle the majority of the orders they received from Coda. When Coda routed a subscriber order to one of the Net Trading Firms, the Net Trading Firm would hold the subscriber order in reserve and then, in most cases, send a principal order back to Coda. Coda would then route the Net Trading Firm’s principal order to one or more external markets to seek non-displayed liquidity. If the Net Trading Firm’s principal order executed, Coda would communicate the execution(s) back to the Net Trading Firm, which would then effect an offsetting trade with the subscriber at a net price which was different than the price of the trade obtained by Coda on the external market for the principal order.The Net Trading Firms and Coda agreed that they would price the offsetting leg (between the Net Trading Firm and the subscriber) such that the Net Trading Firm would provide 5% of the price improvement to Coda’s subscriber order, and retain the remaining 95% of the price improvement.During the relevant period, Coda had a profit sharing agreement with the Net Trading Firms. When a Net Trading Firm executed an order routed from Coda, the Net Trading Firm paid Coda approximately 70% of the net trading profit derived from the net trade. That is:	Coda would get a customer order to buy stock.	Coda would send that order to one of its partner firms (the “Net Trading Firms”) to execute.	They would say “hang on a minute.”	They would send their order to buy the same stock back to the Coda dark pool.	Coda would send that order to some other dark pools to try to buy stock at the real price (“to one or more external markets to seek non-displayed liquidity”).	Coda would come back to the partner firm and say “good news, you bought the stock at $10.01.”	The partner firm would say “great, also, we sold the stock to your customer at $10.048.”[1]	Coda would go back to the customer and say “good news, your order got filled in our dark pool at $10.048, which is $0.002 better than the national best offer of $10.05 on the lit stock exchange.”	The partner firm would say to Coda “pleasure doing business with you, here’s $0.027.”[2]The customers think they have no cause for complaint, because they did better than the NBBO. The whole thing is an institutional equivalent of retail payment for order flow: The partner firms fill the customers at a better price than the NBBO, make some profit for themselves, and kick back some of it to the broker (Coda).[3]It seems … quite … bad? Like the customers went to Coda expecting it to just route their order where it would get the best price. (Because Coda sort of said that that’s what it would do.) Instead it gave the order to its partner net trading firms, then sent their orders where they would get the best price, then let them fill the customers’ orders at a worse price, and then took a kickback. It is probably not technically “front-running,” but it is sort of front-running-adjacent. The customers got no value for it; the SEC says:Coda was not “seeking liquidity” from the Net Trading Firms because the Net Trading Firms usually took no steps to obtain liquidity for the subscriber order, and pursuant to the arrangement with Coda, usually would route a principal order directly back to Coda so that Coda could route it to an away market for execution.It could have just done that with the customer order, instead of going through the net trading firms. But then it wouldn’t get its money.Anyway Coda and its president settled with the SEC for about $1.2 million in fines, without admitting or denying the findings. Also this all ended long ago:By December 2019, Coda stopped the circular routing arrangement described above. Coda also ended its profit sharing agreements with the Net Trading Firms. Since December 2019, Coda has had an agreement with a market maker to pay Coda fixed payments for order flow as agreed by the parties. Ah, well, I’m sure that’s fine then.
  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      “Banks are technology companies”
    
  
I used to work in an equity capital markets group at an investment bank so this brought back happy memories:The syndicate desk—a longtime fixture at banks across Wall Street where IPOs and other large stock sales are priced and allocated to investors—has long clung to traditional ways of doing business like phone orders and scribbled pieces of paper, even as other businesses go digital. ...Ben Batory, head of Franklin Equity Group Trading at Franklin Templeton, said for decades he and his team have kept track of how many shares they asked for in IPOs—as well as how many they received and at what price—on loose sheets of paper. He and his counterparts at other firms talk of calling multiple bankers on a deal to make sure their orders are recorded correctly. And then they wait. The morning after an IPO prices, a banker calls them, tells them how many shares they got, at what price, and what percentage of fees they owe to each of the dozen or so underwriters. It is up to Mr. Batory, or someone in his shoes, to keep track of it all.“All these things are ripe for error,” he said. “There can be five deals a day, and you need to get the amount right, get the commission right, and it’s all chicken scratch on a piece of paper on my desk. It’s incredibly challenging.”Would you believe that the solution is to have some sort of website where customers can type in how many shares they want, and then the banks could look at the order book and decide how many shares to allocate to each investor, and then the investors could just see on the website how many shares they got and how much they had to pay? Seems too easy, doesn't it? Like if it were as simple as that someone would have just done it, right? Ha well anyway:Capital Markets Gateway LLC has set out to change that. Backed by Franklin Templeton, Fidelity Investments, Goldman Sachs Group Inc., JPMorgan Chase & Co. and Morgan Stanley, among others, CMG was launched in 2017 by former bankers at Robert W. Baird & Co. …When the system is up and running, buy-side firms—of which nearly 100 are signed up—will be able to see what deals are pricing when, what the terms are and digitally enter their orders with lead bankers, so long as they have an existing relationship with them.Once IPOs and other offerings are priced, instead of waiting until the following morning to learn via a phone call if they received any allocation, fund managers can find out electronically that same evening. Isn’t technology amazing. My basic theory is that there are a lot of areas of finance where much of the lucrative value-add that a highly paid expert provides is, like, “remembering who wants to buy a stock” or “remembering the terms of the last 10 deals” or whatever. Much of the work that investment banks do requires nuanced judgment and creativity and boldness and deep personal connections; some of it … does not.If people call you up and say “I want to buy the stock” and you write down their names on a piece of paper and put it in your pocket, you can go to the client and say “I have a $10 billion book of demand for your stock,” and the client will be like “wow you are amazing, our hero, here’s a $20 million fee to pay for your expertise and hard work and market knowledge and investor relationships.” Whereas if people type their orders on a website and the client looks at the website and sees $10 billion of demand for the stock and you are standing next to the website looking important the client will say “could you move please, you’re blocking our view of the website.”Just putting all this stuff on a computer demystifies it a bit, which is probably not great for margins. Or maybe it’s great for margins insofar as it allows the bank to replace highly paid high-touch professionals with scalable apps; it’s just not great for banker compensation. And my other basic theory is that the goal of an investment bank is to maximize banker compensation. 
  
    
      
        
      
    
  


  
    
      Meme stocks
    
  
A key explanation of, like, modern life is that politics are so vicious and polarized because (1) everyone uses Facebook, (2) Facebook has an algorithm to decide what stuff to show people, (3) that algorithm is built to maximize engagement, (4) the algorithm is very effective, and (5) it turns out that what maximizes engagement is vicious polarizing stuff, oops. That probably exaggerates the role of Facebook’s algorithm and understates the agency of its users — “Everything you hate about the Internet is actually everything you hate about people,” says Balk’s First Law — but there’s something to it. Social media reflects and also shapes human behavior, in an emergent way. It targets a behavior it likes — spending more time on Facebook, basically — and tries to maximize it. To do that, it maximizes behaviors that correlate with the target behavior, like posting and reading vicious political content. It gives people what they want, as revealed by their actions, which is not what they actually want. (Or is it?) And so at some level you have behaviors in the real world that seem to be designed by an algorithm to maximize engagement on social media; politics are vicious and volatile because that’s what Facebook, deep down, wants.Okay now let’s do stocks! At Margins, Ranjan Roy has a great post on “Memestocks and Reddit redesigns” arguing that some of the 2021 meme-stock craze is due to changes in Reddit’s algorithms to maximize engagement: The stock market is volatile and bizarre because that’s what Reddit, deep down, wants. You read about a stock, Reddit sends you “you might also like ...” notifications about that stock and other stocks, those notifications are designed to draw you in, they work, you spend more time looking at stocks on Reddit, your identity starts to become “person who cares about this stock,” you buy the stock, you start posting about it, you start buying weekly-expiry out-of-the-money call options on the stock and posting your daily profits and losses, the stock goes to $1,000, it becomes the biggest story in the national news, everyone in the country is obsessed with it, and they are all coming to Reddit because the story is not “stock goes up” but “stock goes up because people are having fun and getting rich on Reddit.” From the dumb perspective of the Reddit algorithm that sends you those notifications, this is what success looks like: It sent you those notifications, and now everyone is on Reddit. It is a paperclip maximizer: Its goal is to get more people to spend more time on Reddit, and the way it does that is to cause global financial markets to be wildly volatile and disconnected from fundamental value because it turns out — who knew? — that that drives more engagement with Reddit. Nobody at Reddit sat down and said “hey we should pump up some weird stocks, that will maximize traffic”; its engagement algorithms just figured that out on their own. And now here we are. Roy:When the history of the memestock craze is written, there are a lot of known factors (or at least, they’re clear to me). ZIRP. Robinhood and the gamification of trading. Stimulus checks and people sitting at home. But especially, in light of this week’s amazing Wall Street Journal series the Facebook Files ... unanticipated consequences of engagement-driven algorithms are top of mind.When Reddit raised a ton of money and hired a media growth legend, I’m sure sending AMC to the moon was never on anyone’s mind. But as we slowly try to make sense of what’s happened in the financial markets over the past year, it’s worth remembering how a redirection in a business model and UX tweaks can create massive outsized behavioral changes that make the world a lot weirder and harder to understand.
  
    
      Evergrande
    
  
I guess that if you are a financial regulator there is something to be said for taking an inscrutable tough-love approach with companies that run into trouble:Company: We are almost out of money and have so many creditors. Should we prioritize delivering product to customers, or paying suppliers, or making payments on debt to local retail investors, or making payments on debt to offshore bond investors?Regulator: Yes.Company: ...Regulator: ...Company: Okay, good one, ha ha ha, but seriously we can’t pay everyone.Regulator: Try.What is the benefit, to the regulator, of saying “if I were you I’d pay the retail investors and stiff the offshore ones”? Why would you want to sound like you approve of stiffing anyone? You want the company to feel bad about all of this, to be nervous; you don’t want to be too quick to bless a plan to wriggle out of any debts. I’m not sure that that’s exactly what  this is, though it kind of sounds like it:Financial regulators in Beijing issued a broad set of instructions to China Evergrande Group, telling the embattled developer to focus on completing unfinished properties and repaying individual investors while avoiding a near-term default on dollar bonds.In a recent meeting with Evergrande representatives, regulators said the company should communicate proactively with bondholders to avoid a default but didn’t give more specific guidance, a person familiar with the matter said. The developer has an $83.5 million coupon due Thursday, with a 30-day grace period to make the payment.There’s no indication that regulators offered financial support to Evergrande for the bond payment, and it’s unclear whether officials believe the company should eventually impose losses on offshore creditors. Policy makers are trying to learn more about who holds Evergrande’s bonds, the person said, asking not to be identified discussing sensitive information.Focus on delivering properties to customers and paying individual investors, but don’t default on your offshore bonds either. Just try not to be in trouble anymore? I guess “avoiding near-term default on dollar bonds” is the softest ask there. “Get dollar bondholders not to complain for a couple of weeks, then default on them” is one possible interpretation of that one. If you are a dollar bondholder and Evergrande calls you after this meeting to say “hey just give us two weeks and we’ll have your money,” do you believe them?
  
    
      Employer front-running
    
  
The Financial Times has the story of a Frankfurt fund manager who “admitted in court on Wednesday to ‘front-running’ investment decisions he made on behalf of his employer on 55 occasions between April and September last year, making €8.1m in net profit”:On an ordinary trading day, he would buy and sell shares worth €500m on behalf of his employer and was aware that large orders placed by Union moved share prices, on average by 0.6 per cent to 0.8 per cent.In one example of his front-running, he spent €913,000 on call options for shares in Deutsche Post just seconds before placing a large order of the stock on behalf of Union that moved the share price by 2.7 per cent. He sold the options within an hour, making a profit of €227,000.The defendant told the judges that he started insider trading as he was deeply frustrated by his pay of €440,000 in 2019. After receiving only half the pay rise he had hoped for in early April 2020, he felt “offended” and decided to recoup the rest himself.I guess? If you work for a big financial institution, you are in proximity to a lot of money. They will pay you some of the money, but if they don’t pay you enough for your tastes, I suppose you can just take some of the money for yourself. Particularly if no one is looking:The fund manager started executing private trades at his desk at Union’s headquarters. “As everyone else was working from home, it was only me and one junior colleague in the office,” he told five judges at Frankfurt district court.Meanwhile in the U.S., here are uncannily similar allegations from the Securities and Exchange Commission today:The Securities and Exchange Commission today announced charges against Sergei Polevikov, who worked as a quantitative analyst at two prominent asset management firms, for perpetrating a years-long front-running scheme that generated illicit profits of at least $8.5 million.According to the SEC's complaint, filed in the United States District Court for the Southern District of New York, from at least January 2014 through October 2019, Polevikov had access to real-time, non-public information about the size and timing of his employers' securities orders and trades, and used that information to secretly trade on, and ahead of, his employers' trades. As alleged, Polevikov, on nearly 3,000 occasions, bought or sold a stock on the same side of the market as his employers before his employers executed trades in the same stock for their fund clients. Polevikov typically would close his positions the same day as he opened them, capitalizing on the price movement caused by his employers' large trades. The SEC alleges that Polevikov concealed his fraudulent scheme by executing the trades in the account of his wife, Maryna Arystava, who uses a different last name.He was also charged criminally. Apparently he was spotted because he, uh, made three thousand successful day trades?The investigation originated from the SEC's Market Abuse Unit's Analysis and Detection Center, which uses data analysis tools to detect suspicious patterns, such as improbably successful trading across different securities over time. These capabilities enabled the SEC to spot Polevikov’s trading activities which consistently generated small profits that added up to a total of at least $8.5 million over the course of the scheme.One of my main rules of insider trading is that if you are going to insider trade you shouldn’t do it by buying short-dated out-of-the-money call options on merger targets, particularly if you have never traded options before: That looks real real suspicious and the SEC will notice. But I sympathize a little with the people who do that, because it is a way to use your inside information to make a lot of money quickly, and the alternative is, what? Making smallish normal-seeming stock trades without much obvious news but with some statistical edge from knowing your employer’s orders, making a modest profit each time, and doing it thousands of times? They’re gonna notice that too.
  
    
      Things happen
    
  
“The reality is that if you created a business in China that’s worth billions, you’ve done so with the blessing of the government, so it’s definitely the wrong time to be cashing in.” Fed Tees Up Taper and Signals Rate Rises Possible Next Year. Biden to Tap Crypto,  Big-Bank Critic to Run Wall Street Watchdog. Elizabeth Warren and Democrats Are Going After  SPAC Kingpins. Private Equity Party Is Ending and  We’re Exhausted, Carlyle Says. “Citigroup Inc. workers in London were greeted by  therapy puppies upon their return this month.” Elon Musk Says  Dogecoin Fees Need to Drop to be Viable for Purchases. Cathie Wood Would Sell Tesla Next Year  If It Reached $3,000. Pro-rata vs. user-centric accounting. “In the mid-1980s, Mr. Van Peebles was one of the few Black options traders on the American Stock Exchange — ‘making deals, like always,’ he said.”If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] I continue to assume that the national best offer is $10.05. So the partner firm, buying at $10.01, got $0.04 of price improvement. It kept 95% ($0.038) for itself and gave 5% ($0.002) to the customer.[2] That is, “the Net Trading Firm paid Coda approximately 70% of the net trading profit derived from the net trade,” or 70% of $0.038 in my example numbers.[3] The economics here do seem worse, for the customer, than they are in retail payment for order flow. We talked about Larry Tabb’s and Jackson Gutenplan’s report at Bloomberg last month, finding that “Market makers captured 48.5% of the spread in executing self-directed retail orders in 2Q. Of the balance, 13.3% was paid to the broker and 38.2% went to the client.” That’s not exactly apples-to-apples with the SEC’s numbers here. But roughly speaking here Coda gets 66.5% of the economics (70% of 95%), the partner net trading firms get 28.5%, and the customers get 5%. 
        
      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like Money Stuff? | 
Get unlimited access to Bloomberg.com, where you'll find trusted, data-based journalism in 120 countries around the world and expert analysis from exclusive daily newsletters.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23ceyhqx.5uot/a32f830f.gif" alt="" border="0" /></a>