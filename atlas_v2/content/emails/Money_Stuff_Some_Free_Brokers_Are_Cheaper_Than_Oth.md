# Money Stuff: Some Free Brokers Are Cheaper Than Others

**Source**: inputs/saved_emails/Money Stuff Some Free Brokers Are Cheaper Than Others_Thu,_25_Aug_2022_14-03-15_-0400_(EDT)_182d62d8f311d732.eml
**Type**: email
**Created**: 2025-08-25T02:53:57.108570

---

Programming note: Money Stuff will be off tomorrow, back on Monday.In general, in the US, if you buy or sell stock through a big retail brok
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          Programming note: Money Stuff will be off tomorrow, back on Monday.

  
    
      PFOF
    
  

In general, in the US, if you buy or sell stock through a big retail brokerage, your broker sends your order to a “wholesaler” — a big electronic market-making firm like Citadel Securities, Virtu Financial Inc. or Jane Street Capital — which takes the other side of the trade, selling you the stock you’re buying or buying the stock you’re selling. The wholesalers want to trade with retail orders, because in general retail orders are less risky than orders on the public stock exchanges; they have less “adverse selection.” If a market maker is trading on the stock exchange, and it buys 100 shares of stock, then there is a decent chance that the seller knows something it doesn’t. Perhaps the seller is a clever hedge fund that has done lots of clever research and knows that the stock is about to go down; if so, the market maker will lose money on the stock it bought. Or perhaps the seller is a gigantic pension fund and is going to go on to dump a million shares and drive down the price; if so, the market maker will also lose money on the stock it bought. Or perhaps the seller is an even faster and smarter electronic trader than the market maker, and it knows that the stock will go down in the next microsecond, etc.
But if the market maker buys 100 shares directly from a Robinhood Markets Inc. customer, then it knows that it is not trading with a big pension fund or hedge fund or high-frequency trader. It’s certainly possible that a Robinhood trader is particularly well informed, or has a ton of stock to sell (or buy) and has broken up that trade into smaller orders, but it is less likely than it is on the stock exchange. So this is a more attractive trade for the market maker.
And so market makers strike deals with retail brokerages to trade with their order flow. In exchange for this sweet sweet retail order flow, the market makers give the brokerages two things:
	
Price improvement: If the lowest offer price for a stock on the stock exchange is $10.02, the market maker might sell it to the retail customers for a bit less, say $10.017. If the highest bid price is $10.01, the market maker might buy it from retail customers for a bit more, say $10.013. Effectively the wholesaler charges a lower bid/ask spread for less risky order flow. The retail broker’s customers get the savings.	
Payment for order flow, or PFOF: The market maker just writes the brokerage a check for sending it the order flow. The retail brokerage keeps this money for itself, though in practice in a competitive market the brokerage might use the money to, for instance, subsidize zero-commission trading.

This is all terrifically controversial and we talk about it a lot, for instance  here.
Intuitively, there is a simple one-for-one tradeoff between price improvement and payment for order flow. If a retail order is worth $1 to a wholesaler, it might be willing to pay $1 to trade with that order, but it should be indifferent between paying $1 of price improvement to the retail customer, or paying $1 of PFOF to the retail brokerage, or paying $0.60 of price improvement and $0.40 of PFOF, or whatever other split. (In fact there seems to be a  quasi-SEC-endorsed best-practices split of at least 80% price improvement and at most 20% payment for order flow, though that’s not a rule or anything.) 
Some retail brokerages seem to make a lot of their money from payment for order flow. Others make less. Some big retail brokerages do not accept any payment for order flow at all: They still use this system (routing their orders to market makers), but they take 100% of the value in the form of price improvement for their customers instead of payments for themselves. Intuitively, you might think that the brokerages that get a lot of PFOF would get worse price improvement.
But, nope! Here is Bill Alpert in Barron’s:

Critics of retail brokers like Robinhood Markets condemn those companies for routing customers’ orders to market makers like Citadel Securities in exchange for payments. ...
The suspicion is that greater payments to brokers must be offset by less favorable execution prices. But that isn’t what a new study finds.
In an Aug. 13 working paper, five finance professors analyzed 85,000 stock trades they made through five leading retail brokers. They did get significantly different pricing through different brokers for identical orders to buy or sell at the current market price.
But their best pricing came from a broker that takes payment for order flow, namely TD Ameritrade, now a unit of Charles Schwab. Fidelity, which takes no order payments, got worse prices on the professors’ trades than did TD Ameritrade. And its prices were no better than those from the E*Trade unit of Morgan Stanley, which does take payments. Robinhood, which used revenue from order-flow payments to subsidize the industry’s first commission-free trading, delivered middle-of-the-pack pricing. Interactive Brokers ranked last in the execution pricing of the professors’ orders.

And here is the paper, “The ‘Actual Retail Price’ of Equity Trades,” by Christopher Schwarz, Brad Barber, Xing Huang, Philippe Jorion and Terrance Odean. They opened accounts at five brokerages and placed 85,000 trades in 128 stocks, using the brokerages’ application programming interface when possible to trade automatically. They mostly did trades of $100 (rounded to the nearest number of full shares), with a few $1,000 trades. And they found that:
	They got better execution than the national best bid or offer available on the stock exchange. “Across our six brokerage accounts, we calculated that the average round trip cost ranged from –0.07% to –0.45%; the average price improvement varied from $0.03 to $0.08 per share.” That is, on average, when they bought a stock and then sold it later in the day, they lost about 0.07% to 0.45% of their money.
  [1]
 If they had traded at the national best bid or offer — the publicly available benchmark price on the stock exchange — they would have lost 0.62% of their money.
  [2]
 But their retail brokerages routed their orders to wholesalers, who saved them $0.03 to $0.08 per share, or 0.17% to 0.55% of their money.	But they got systematically different execution quality from different brokerages. Their trades cost on average 0.07% at TD Ameritrade, 0.20% at E*Trade, 0.23% at Fidelity, 0.31% at Robinhood, 0.44% in their Interactive Brokers Pro account (which charges commissions and does not take PFOF), and 0.46% in their Interactive Brokers Lite account (which has no commissions and takes PFOF). There was also “some variation in the best and worst venues,” i.e. wholesalers; “Citadel on average provides the best execution while Two Sigma and UBS have the worst execution, with a maximum range around 3 cents.”	And these differences were not correlated to how much payment for order flow those brokerages get. The no-PFOF accounts did not systematically get better execution than the ones that took PFOF.

“There is no evidence that PFOF harms price execution,” they say, but I am not sure that is what is interesting here? What is interesting is that some brokerages get better execution than others, and that “the dispersion is due to off-exchange wholesalers systematically giving different execution prices for the same trades to different brokers,” but that it has nothing to do with how much those brokerages pay wholesalers. The same wholesalers execute the same order for the same number of shares of the same stock at different prices for different retail brokerages:

To investigate whether brokers are systematically given different price execution regardless of venue or stock routing decisions, we obtain specific routing data for every trade for four of our brokers. … We find that our observed execution differences are largely explained by “broker execution.” We come to this conclusion by calculating the difference in price executions for matched trades, i.e., the exact same trades executed by the same venue for different brokers at the same time. All the execution differences we observe are explained by this driver. In addition, broker execution differences are not due to one venue only but are systematic across all the venues. …
In the end, we find that our price differences are due to different brokers getting different execution prices for the exact same trade at the same venue. 

That is, they find that every wholesaler gives (say) Interactive Brokers orders less price improvement than TD Ameritrade orders. Why? They don’t say! Weird.
Here are two possible explanations, which are a little bit related to each other. One is that retail brokerages are seeking “best execution” for their customers in a sort of aggregate way.
  [3]
 They route their orders to wholesalers not by running an individual auction for each trade, but by examining the wholesalers’ overall performance over days or months and sending more orders to wholesalers who provide better total price improvement. But the brokers vary in what they are looking for. For instance, one broker might prefer a wholesaler who provides a lot of price improvement on small orders and less price improvement on large orders (because its customers mostly do small trades); another might prefer one who does better on large orders (because its customers mostly do big trades). 
This paper looks at $100 trades, which are pretty small. You could imagine a story that goes like: “TD Ameritrade is the best brokerage for executing small trades, while other brokerages might be better for large trades. But this paper only ranks brokerages on execution of small trades, so it finds that TD Ameritrade is the best.”
The other explanation has to do with what I said at the beginning, about adverse selection and retail orders being more attractive than institutional ones. That is not always and uniformly true. Some retail brokerages have customers who are more institutional-like: They are better informed or trade larger sizes. A wholesaler who trades with those customers will do worse than a wholesaler who trades with smaller and less-informed retail customers. So it will offer them less price improvement. If a brokerage’s orders are riskier and less profitable for wholesalers, those orders will get less price improvement. The fact that the professors’ Interactive Brokers Pro account performed relatively poorly might have something to do with who Interactive Brokers Pro is designed for: pros. If you are a market maker trading with pros, you will charge a higher spread than if you are trading with amateurs.
  [4]

The basic thing that happens in retail stock trading is that wholesalers are able to segregate the market into institutional orders (on the stock exchange, risky) and retail orders (direct from brokers, less risky), and charge the retail orders less because they are less risky. The implication of this paper might be that they can discriminate more finely: Some retail brokerages have riskier orders than others, so they get charged more.
This sort of thing can make people angry. Segregating retail and institutional orders means that institutional orders get charged more and retail orders get charged less, which means that effectively your boring conservative mutual fund’s trades subsidize some Robinhood gambler’s trading. And I suppose you have the same problem with discrimination among brokerages. Here is a  Bloomberg News story about this paper:
Extrapolating from the results, they estimate it costs small-time US investors as much as $34 billion a year, said Christopher Schwarz, the finance professor at the University of California, Irvine who wrote the study along with four colleagues. … The overall cost figure is an estimate of what investors would save if their orders were executed by the best performing of the five brokers in the study instead of the fourth best.
But I’m not sure that is the right conclusion? The best-performing broker is cheaper because wholesalers can discriminate; they think that some brokerages’ orders are less risky than others’, so they charge some brokerages less and others more. If the wholesalers couldn’t discriminate — if they gave every brokerage the same price improvement, or if every retail investor in America read this paper and moved their accounts to TD Ameritrade — then they would have to charge the less-risky investors more to make up for charging the more-risky investors less.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Whistle-blowers
    
  

One way to run the US Securities and Exchange Commission would be that you have a bunch of enforcement lawyers, and they look for fraud, and if they find fraud the SEC collects a big fine, and then the SEC lawyer who brought the case collects 30% of the fine, personally, as a bonus.
This approach would have some advantages. The SEC routinely extracts nine-digit fines — last month Morgan Stanley   paid $200 million because some of its bankers sent each other text messages — and if SEC enforcement lawyers routinely got paid $60 million bonuses, then the SEC would attract some very talented and motivated enforcement lawyers, who would be very good at extracting fines. This would bring in a lot of money to the US government, and might also do a lot to deter securities fraud.
But on balance I think this approach would be bad? If the SEC’s lawyers got a cut of the fines they extracted, they would have incentives mainly to extract really big fines, which is part of the SEC’s job, but not all or even most of it. The SEC also has to, like, write good rules to encourage capital formation, and shut down scammers who are doing a lot of harm but who don’t have the money to pay nine-digit fines. Occasionally it even has to investigate some behavior and decide “you know what, this is actually okay, we don’t need to extract a fine for this.”
A prize-money-driven SEC would underweight all of those things and focus mainly on extracting big fines from big banks. It would be more interested in clear-cut but low-impact misbehavior (texting on personal phones!) by deep-pocketed repeat-player institutions than in harmful but complicated and novel misbehavior by new entrants (Ponzi schemes in decentralized finance!). It would de-prioritize rule-writing and emphasize   regulation by enforcement, which is like rule-writing except that you get to extract a big fine for making new rules. 
Now, this is not the way that the SEC is actually run. SEC lawyers are paid government salaries and don’t get a cut of the fines they bring in.  On the other hand:

Over the past several years, the Securities and Exchange Commission’s whistleblower awards program has been championed by lawyers and politicians for offering powerful incentives to tipsters to come to the regulator with evidence of wrongdoing.
A new study, however, finds that almost a quarter of the SEC’s whistleblower awards have gone to law firms with attorneys who have close connections to the regulator, potentially deterring other whistleblowers from coming forward. …
Using SEC data from awards issued between 2012 and 2020 that was obtained through the Freedom of Information Act, the study shows that about 23% of awards in the database—or 30—went to law firms with at least one attorney who was a former SEC official, highlighting the potential benefits that this group’s connections might have. ...
Jordan Thomas, an attorney who helped establish the SEC whistleblower program and now at law firm SEC Whistleblower Advocates PLLC, is “a single dominant ‘revolver,’” according to the study. Mr. Thomas, during his time working for law firm Labaton Sucharow LLP, was responsible for 10 awards in the study’s database, accounting for about 20% of all the dollars awarded in the study, at about $152.6 million, the study said.

Here is the paper, by Alexander Platt, titled “ The Whistleblower Industrial Complex.” From the abstract:
The upshot is that the SEC and CFTC have effectively privatized the tip-sifting function that is at the core of the [whistle-blower programs]. Private lawyers have likely extracted hundreds of millions of dollars in fees and expenses from these programs, with a disproportionate share going to a concentrated group of well-connected, repeat players. 
We have talked about Jordan Thomas — the lawyer who designed the whistleblower program at the SEC and then left to be one of its main beneficiaries — before;   I wrote: “This is a good trade — build a spigot of government money and plant yourself in front of it.” If you currently work at the SEC, I suppose you have incentives to increase the flow out of the spigot so that one day you too can plant yourself in front of it.

  
    
      
        
      
    
  


  
    
      Anti-ESG
    
  

Here  you go:

Texas is taking steps that could cost BlackRock Inc., UBS Group AG and eight other finance firms business with the state after finding them to be hostile to the energy industry.
Glenn Hegar, the Republican state comptroller, on Wednesday named the firms he considers to “boycott” the fossil fuel sector. The move ends roughly six months of suspense that led Texas municipal-bond issuers to avoid banks whose status was unclear amid the office’s probe into companies’ energy policies. Governmental entities should use the list as a “filtration system” when entering contracts, Hegar said in an interview. 

Those firms disagree:

BlackRock, the world’s largest asset manager, said in an emailed statement that the company disagrees with the comptroller’s assessment. 
“This is not a fact-based judgment,” the statement said. “BlackRock does not boycott fossil fuels -- investing over $100 billion in Texas energy companies on behalf of our clients proves that. Elected and appointed public officials have a duty to act in the best interests of the people they serve. Politicizing state pension funds, restricting access to investments, and impacting the financial returns of retirees is not consistent with that duty.”
A spokesperson for UBS said the company also disagrees with the decision. “We provided their office with extensive information on our policies and practices, demonstrating that UBS does not boycott energy companies even under a broad interpretation of Texas law,” the statement said. 

The basic issue here is that if you are an investment firm, and you decide not to invest in some particular oil company, Texas will send you a threatening letter saying “we won’t do business with people who boycott fossil fuels.” And you will say “no, no boycott, we didn’t invest in that company because we thought that the climate-related risks to its business were very high, so as a pure valuation matter we thought it was a bad investment.” And Texas will say “no we think it’s because you don’t like oil companies.” And you will send them a bunch of data and investing memos and policy statements and legal analyses about how really you are only considering climate change as a financial matter, and they won’t believe you. We talked about this sort of thing yesterday.  I wrote:
A certain amount of the ESG fight will take the form of broad public statements of principles. … But a lot of it will take the form (and has already taken the form) of fact-intensive debates about particular investment decisions. Some investment manager will say “we are underweight oil and gas companies because we are concerned about the financial impact of climate transition risk,” and some state regulator will say “we think it’s actually because you are environmentalists,” and the investment manager will say “no here is our investment model that considers environmental risk as a factor in assessing risk and returns,” and the regulator will say “we think that you are using inappropriately long investment horizons and imprudently weighting this risk in your calculation,” and the manager will provide support for its view, and they’ll go back and forth. Every financial decision can also become a political argument. It seems exhausting.
It still does.

  
    
      APE voting
    
  

We   talked yesterday about AMC Entertainment Holdings Inc.’s weird APE preferred-stock units, which are meant to be a close substitute for AMC’s common stock but which currently trade at about a 25% discount. (APE closed at $7.13 yesterday, AMC at $9.58.) Specifically we talked about an arbitrage trade — put on by Jim Chanos among others — of buying APE, shorting AMC, and hoping that that discount will close. The discount will close, for instance, if AMC gets shareholder approval to issue more common stock, at which point the APEs will automatically convert into common.  Here’s Chanos:
"Functionally, the two securities are the same. And I'd guess the apes [i.e., AMC’s enthusiastic retail shareholders] will be putting pressure on [AMC Chief Executive Officer Adam] Aron, if the discount continues, to make it freely convertable sooner rather than later," Chanos told CNBC.
I expressed some doubt about that, because the thing about apes is that they don’t vote. AMC has tried before to get shareholder approval to issue more common stock, but it couldn’t. It would need a majority of all its outstanding shares to vote to approve that, and that’s hard when 80% of its shares are held by retail investors. I wrote:
AMC stock is mostly held by retail investors, and it is widely assumed that retail shareholders mostly don’t vote their stock. And in fact if you look at the results of AMC’s shareholder voting this year — on routine matters like electing directors and approving executive pay — only about 145 million shares (out of 516 million) were actually voted. So it might just be impossible for AMC to get a majority of its shares to vote for anything.
A couple of people pointed out that the APEs help to solve that problem. The APE shares have the same voting rights as the common stock, meaning that AMC has effectively doubled its voting stock from 516 million to 1.03 billion shares. Day One, this doesn’t matter: Each AMC shareholder went from holding one common share to holding one common share and one APE, with the same voting rights; if those shareholders weren’t likely to vote their one share before then they are no more likely to vote their two shares now. But over time, you might expect that to change. Low-information low-involvement retail shareholders might be more likely to buy AMC common stock (it’s normal, it’s common stock, it has the ticker symbol “AMC”), while the APEs might migrate into the hands of specialized APE enthusiasts and arbitrageurs like Jim Chanos.
And then at some point AMC goes out to get a shareholder vote on converting the APE shares into common stock, and:
	A lot of the APE shares are held by professional arbitrageurs like Chanos who are really engaged with the idea of converting their shares into common — that’s their whole trade thesis — and so will definitely vote; and	Even with the APE shares that are held by low-engagement retail shareholders, it is an easier pitch for the company to say “look your APE shares are worth $7 and AMC stock is worth $9.50, so if you check a box on this form you’ll get a free $2.50”
  [5]
 than it was to say “please vote for us to be able to issue more shares to do unspecified corporate finance things.”

So the APEs are a way to give voting rights to people who will be naturally incentivized to vote for what AMC’s management wants, which is more common stock. This is by no means a certainty — if you only get 20% of AMC common shareholders to vote to authorize more shares, then you need to get 80% of APE holders to vote for it — but it helps.

  
    
      Securities fraud
    
  

A rough rule of US securities regulation is that if you do an unregistered securities offering you are giving your investors  a free put option. If you sell them stock at $100 without following the registration requirements, and the stock goes up, they get to keep the profits. If the stock goes down, though, they can sue you and get their $100 back. 
Is there some similar rule that you could use to give yourself a free call option? Like, you sell stock to investors at $100; if the stock goes down, the investors are stuck with it; if the stock goes up, though, you get to pay them back their $100 and keep the profits? It seems implausible. And yet:

 A group of cannabis companies and a law firm that allegedly defrauded investors are asking a Colorado federal judge for a win in the investors' suit, saying because cannabis is illegal under federal law, the investors can't recover any proceeds from their businesses, only their initial investments. … 
"Any relief other than return of investment principal would necessarily be derived from the illegal profits of the parties' marijuana business and would represent an unlawful gain to Plaintiffs from their investment in an illegal marijuana business," Kaweske told the court.

Love it! “You can’t demand your share of our profits, because we got those profits from crime, so we should get to keep them.”

  
    
      Business cards
    
  

I  just:

Derek Peterson’s business card is, truly, always in his hand.
The technology chief at Boingo Wireless Inc. had a chip inserted, between his left thumb and index finger, that carries his contact information. New acquaintances can use their phones to download the details.
The rub: His attempts to transmit often draw looks of confusion, then disbelief, then gawking. He finds some phones need an app downloaded before his chip, which uses near-field communication technology, can be scanned. And some phones’ NFC readers aren’t mighty enough to detect the chip unless placed directly on top of his hand.

Why? Why not just tattoo a QR code on his forehead with his contact information? I guess there is some sort of early-adopter, network-effects thing going on here: If everyone kept their contact information in chips in their hands, then everyone would exchange contact information this way, so everyone’s phones would have appropriate hand-contact-chip readers and apps, and this whole thing would be more convenient than exchanging business cards or texting new acquaintances your contact info or whatever. As it is, it’s much less convenient, but you have to start somewhere. If you are the guy who is like “hi, I am from the future, my business card is on a chip in my hand, download the app now,” I guess some people will think that is cool and be more likely to do business with you. Others, less likely. But you are taking a calculated risk.
Anyway that’s from a very funny Wall Street Journal A-hed about nontraditional business cards:
Ayomide Joseph, a content marketer, tried to use a QR code to share his details with cybersecurity experts, but they refused. The FBI had issued a warning about cybercriminals who redirect codes to fraudulent websites. 
I am looking forward to reading a story about someone going to a Bored Ape Yacht Club meet-up, handing out QR-code business cards, and using the codes to hack everyone’s wallets and steal all their apes. 

  
    
      Things happen
    
  

Ethereum is really going to move to  proof-of-stake. Hedge Fund Founder Och   Sues Sculptor Over CEO’s ‘Ever-Escalating’ Pay. When Private Equity Takes Over a  Nursing Home. Citigroup Plans to Wind Down  Russian Consumer Operations. Twitter Whistleblower Peiter Zatko Has Warned of  Cyber Disasters for Decades. GameStop Boosts Compensation for Some Store Employees With Shares and Raises. The Future of Shipping Is ...   Sails? Gen Z Wants To Ditch Corporate Jobs For   Influencing, Social Media Dreams.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] Does this bother you? It shouldn’t. You pay a bid/ask spread to trade stock. If you buy stock and hold it for a long time, you should on average expect to make money, because stock represents a claim on corporate cash flows and in the long run the economy grows. But if you buy and sell stock in the same day, and if you trade purely at random — as they consciously did! — then on average you should expect to lose money. Your trade has zero expected profit, but you are paying something for liquidity.


  [2] See Table VI on page 44 of the paper.


  [3] Though this may change. SEC Chair Gary Gensler dislikes this, and has “asked staff to make recommendations for the Commission’s consideration around how to enhance order-by-order competition,” which “may be through open and transparent auctions or other means.” In that world, brokerages would have to seek the best price for each order, rather than choosing wholesalers based on how much aggregate price improvement they provide.


  [4] These two explanations are related in the sense that a brokerage whose customers mostly do small trades (1) will prioritize price improvement on small orders and (2) will probably not cause a lot of adverse selection. 


  [5] Obviously AMC will want a lawyer to look at that. The AMC stock can go down when the APEs convert, etc., it’s not guaranteed free money. But it's an easy pitch.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23ch6a0a.5s03/f095d997.gif" alt="" border="0" /></a>