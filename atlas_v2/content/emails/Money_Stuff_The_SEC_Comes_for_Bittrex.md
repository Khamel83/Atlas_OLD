# Money Stuff: The SEC Comes for Bittrex

**Source**: inputs/saved_emails/Money Stuff The SEC Comes for Bittrex_Mon,_17_Apr_2023_14-56-53_-0400_(EDT)_1879094a48ef8222.eml
**Type**: email
**Created**: 2025-08-25T02:53:58.307661

---

The basic rule in the US is that, if you operate a stock exchange, you need to register with the US Securities and Exchange Commission as a 
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Bittrex
    
  

The basic rule in the US is that, if you operate a stock exchange, you need to register with the US Securities and Exchange Commission as a national stock exchange. This comes with a lot of oversight; in particular, the rules of your exchange have to be published and transparent and approved by the SEC.
I suppose you could debate what qualifies as a stock exchange. Roughly, an exchange is a venue for bringing together buyers and sellers of stock so they can trade with each other, but in modern finance there are gray areas. There are some things that look sort of like stock exchanges — dark pools, alternative trading systems — that are not actually registered as stock exchanges. But they are registered with the SEC too, and the SEC also supervises their operations. For that matter there are stockbrokers: A broker’s website and mobile app can look and feel a bit like a stock exchange, to a retail customer; you can log onto Robinhood and see prices and buy and sell stock. But  there are rules distinguishing brokers from exchanges (a broker mostly does not provide a platform for people to trade with each other, but routes orders to other market venues), and anyway broker-dealers are also registered with the SEC. Also stock clearinghouses (which settle trades, moving stock from the seller to the buyer) have to register. Basically any stock-exchange-like thing has to register with the SEC.
Now, these are not really rules about stock exchanges; technically the rules are about securities, not stocks. If you run an exchange-like thing for trading securities — stocks, bonds, options, etc. — you have to register with the SEC.
There are crypto exchanges in the US. They operate as exchanges (venues for bringing together buyers and sellers), and also often as clearinghouses (they move tokens from sellers to buyers
  [1]
). They are not generally registered with the SEC as securities exchanges (or ATSs, or clearinghouses). They offer trading in crypto tokens. Some of those tokens — Bitcoin, Ether — are not securities.
  [2]
 But the SEC takes the view — in speeches, in various enforcement actions — that almost all of them are securities. 
This means that most crypto exchanges that operate in the US are probably, in the SEC’s view, breaking the law. I assert this pretty confidently based on my reading of the SEC’s whole vibe, but the SEC has not really come out and said it directly, by, you know, bringing enforcement cases against crypto exchanges. It has come close. Last year it brought an insider trading case against a former Coinbase Global Inc. employee, accusing him of insider trading some tokens that Coinbase listed; the SEC claimed that these tokens were securities, and  I tweeted “This is a weird way for the SEC to say that Coinbase is running an illegal securities exchange?” Last month the SEC   sent a Wells notice to Coinbase, basically telling Coinbase that it is going to bring charges against it for operating an illegal securities exchange. But not yet.
Today  the SEC brought charges against Bittrex Inc. for allegedly operating an illegal securities exchange:

The Securities and Exchange Commission today charged crypto asset trading platform Bittrex, Inc. and its co-founder and former CEO William Shihara for operating an unregistered national securities exchange, broker, and clearing agency. ...
Since at least 2014, Bittrex has held itself out as a platform that facilitated buying and selling of crypto assets that the SEC’s complaint alleges were offered and sold as securities. From 2017 through 2022, Bittrex earned at least $1.3 billion in revenues from, among other things, transaction fees from investors, including U.S. investors, while servicing them as a broker, exchange, and clearing agency without registering any of these activities with the Commission.

Here is  the SEC’s complaint, which is straightforward. Bittrex is an exchange (and a broker, and a clearinghouse). It lists a bunch of tokens. Some of them, in the SEC’s view, are securities. “For purposes of prevailing on the Exchange Act claims set forth herein, the SEC needonly establish that Bittrex transacted in a single crypto asset security,” says the complaint, but then it goes on to list six crypto tokens that the SEC is pretty sure are securities.
Here again the argument is straightforward and familiar. The US Supreme Court  has said that a “security” includes “the investment of money in a common enterprise with a reasonable expectation of profits to be derived from the efforts of others.” Lots and lots of crypto projects raised money from investors by promising to build some sort of profitable product or ecosystem on the blockchain. The SEC cites some of them.

Algorand is a blockchain protocol founded by Silvio Micali. The Algorand blockchain uses a consensus algorithm it calls “pure proof-of-stake,” in which each user’s ability to influence the choice of a new block is proportional to its stake (number of tokens) in the system.
“ALGO” is the native token of the Algorand blockchain, and has a maximum supply of 10 billion ALGO minted at the launch of the Algorand network. Because ALGO is the native token of the Algorand blockchain, those utilizing the Algorand blockchain need to hold (and potentially stake) certain amounts of ALGO.
The Algorand Foundation Ltd. (the “Algorand Foundation”) conducted an initial ALGO token sale on or about June 19, 2019, selling 25 million tokens at $2.40 per ALGO, raising approximately $60 million. … 
The publicly available information disseminated by Algorand, Inc. and the Algorand Foundation led ALGO investors to reasonably expect to profit from Algorand, Inc.’s and the Algorand Foundation’s efforts to grow the Algorand protocol, which would in turn potentially increase demand for, and therefore the value of, the ALGO token itself. …
The Algorand Foundation described “Governance” as a way for investors to make investment returns on their ALGO purchases—stating it is “a decentralized program which allows Algo holders to vote on the future of Algorand” and “the best way to earn rewards for holding Algo, with APY% of 10.02% - 14.05% seen in previous periods.” …
The Algorand, Inc. and Algorand Foundation websites tout their teams’ technical experience and expertise in the areas of cryptography and business development. For example, Algorand, Inc.’s website states: “Blending technical mastery and professional stability, the Algorand team consists of internationally recognized researchers, mathematicians, cryptographers, and economists along with proven business leaders from global technology companies.”

None of this stuff even sounds particularly bad. But the bones of it are:
	Algorand (and lots of other crypto projects) raised money from investors to build its project.	The investors expected to make money from their investment in this enterprise.	They expected to make this money because of “the efforts of others”: The team promoting the project (and raising the money) was also going to build it, and the investors were hoping for a return because they thought the team would do a good job.

That’s just stock. There’s a blockchain, sure, and the mechanics of how ALGO tokens participate in the upside of the Algorand blockchain are somewhat different from the mechanics of how META shares participate in the upside of Meta Platforms Inc. But basically, the SEC says, this is stock: You invest money in a team that is building a tech project, and if the project works out you get rich. Bittrex was offering this stock on its exchange. So it should have registered as a stock exchange.
The complaint also details that Bittrex kind of knew this:
When deciding whether to include an asset on the Bittrex Platform, Bittrex assessed whether the financial benefits of doing so outweighed the risk that the asset in question would be subject to scrutiny by regulators, including specifically the SEC. For example, in or around March 2017, Shihara told the other Bittrex co-founders with regards to a particular crypto asset: “the problem is that its going to be seen by the SEC as a security. im meeting with these guys face to face to get specifics on how much they want to raise, who they are raising it from, and what they expect the after market to be. its a big enough opportunity that we might want to roll the dice on the sec investigation. we have a couple of paths forward but one idea was to have them take a position in bittrex and own the risk of an SEC investigation with us.”
And:

To further its dual goals of making more crypto assets available on the Bittrex Platform and avoiding regulatory scrutiny, starting in at least May 2017, Bittrex routinely directed that crypto asset issuers “scrub” their offering and marketing materials of “investment-related terms,” including language that would “get unwanted attention from the SEC.” Bittrex regularly asked issuers to remove “problematic statements” from their marketing materials—statements indicating that the asset was marketed as a security—as a prerequisite for making the issuers’ crypto assets available for trading on the Bittrex Platform. Bittrex unofficially dubbed this practice the “problematic statement cleanup.” 
The “problematic statement cleanup” was nearly always done after the initial offering of the crypto asset—i.e., after the crypto asset had already been offered and sold to investors. In other words, the issuers of the crypto assets had already marketed, offered, and sold the crypto assets to the investing public by using the very “problematic statements” that Bittrex recognized were “investment-related terms” that indicated the assets could be securities. In requiring issuers to “scrub” their documents, Bittrex did not actually change the economic reality of those offers and sales, but rather simply attempted to remove or “scrub” any evidence of these public statements without changing the actual characteristics of the offering or asset even assuming the deletions were successful.

The SEC quotes a “cheat sheet” that Bittrex gave its employees to flag bad features of crypto tokens. One “common problematic feature” is “Tokens providing passive income (e.g. dividends, buy back and burning of tokens),”
  [3]
 and one “common problematic statement” is “[proof of work] and [proof of stake] rewards described as token holders receiving ‘interest.’” That is, the common economic features of crypto tokens — the ways that a token participates in the upside of its project, either through token buybacks or through issuance of new tokens to holders — run the risk of turning them into securities, according to Bittrex.
The complaint also explains why the SEC cares about this, why it thinks that the system of securities exchange registration matters. One aspect of it is that, in traditional finance, brokers and exchanges and clearinghouses tend to be different entities; there is a lot of intermediation in traditional finance, where regular customers access the market through their broker’s website, brokers trade on a separate stock exchange, and settlement happens through a separate clearinghouse.
Crypto has enthusiastically disintermediated this: Retail traders open accounts directly on the crypto exchange, and the exchange matches trades, holds everyone’s crypto for them and settles trades. A year ago a lot of people in crypto would have told you that this was good and efficient, that they had cut out the layers of wasteful middlemen in traditional finance. Then FTX failed and took billions of dollars of customer money with it and, you know, that position is more controversial.
The SEC endorses the traditional system:

Separation of these core functions aims to minimize conflicts between the interests of securities intermediaries and investors. Registration provides the means for the SEC to understand the business of the securities intermediaries and their relationship with investors in order to protect those investors and the securities markets, and to prevent fraud or other abuses. 
Investors in traditional national securities markets do not generally trade directly with national securities exchanges or clearing agencies but instead are customers of broker-dealers.

The SEC also makes the point that traditional stock exchanges have to have published transparent rules, including about how they list and delist stocks. Crypto exchanges don’t:

By contrast, a crypto asset platform that fails to register in any capacity declares itself free from any obligation to follow those provisions in the Exchange Act, including the types of rules described above, that are designed to protect investors, promote the public interest, and provide truthful and material information to investors. As a result, investors are at the whim of the crypto asset platform to give them information about their standards and procedures for listing (and de-listing) investments, about the investments themselves, including whether any particular listed crypto asset may potentially be delisted, and the platform’s operations.
A private conversation in or around June 2017 between a Bittrex employee and one of Bittrex’s three founders illustrates the type of investor harm that can result from a crypto asset platform failing to follow or even recognize these obligations. The employee complained to the founder: “I hate people bitching that we don’t email them about market removals…I LOST SO MUCH CAUSE I DIDn’T KNOW.” The founder responded that his preferred response to those investors was “go f*** yourself” or at a minimum to tell them to “track your own damn investment or get a broker to do it for you.”

“Seattle-based Bittrex was already prepared to wind down its U.S. operations,”  reports the Wall Street Journal, “citing the difficulty of working with U.S. regulators that have taken enforcement action against over 100 crypto defendants in six years.” 
Which: yes. If you run a crypto exchange and you come into the SEC and say “we want to register as a securities exchange so we can let our customers trade securities tokens on our website,” the SEC will stop you right there and say “Wait: customers? Website? No no no no no, if you are an exchange, you can’t have customers, or a website; that’s for brokers. You can’t come in here and register a securities exchange with customers.” And then you go away, confused and sad and probably sued. There is a traditional financial system, and crypto has built a different system, and the SEC has pretty much everywhere said “nah, you gotta follow the traditional system.” And crypto people have said “well we can’t really do that because ...” and the SEC has said “shh, shh, we don’t care.”
And so last week the SEC  issued an update on a proposed rule updating the definition of “exchange” to, among other things, cover decentralized-finance crypto exchanges. Republican SEC Commissioner Hester Peirce  dissented, complaining that “rather than embracing the promise of new technology as we have done in the past, here we propose to embrace stagnation, force centralization, urge expatriation, and welcome extinction of new technology.” Her point is that crypto exchanges have built innovative new ways to trade securities, and rather than adapting the rules to those innovations, the SEC is demanding that those exchanges abandon the innovations and conform to the traditional rules.
I have said this before, but that’s the sort of argument that people took seriously a year ago, and now do not. I   wrote in February:
I submit to you that the main fact of crypto regulation in early 2023 is that regulators feel really burned by the events of 2022, and particularly by the collapse of FTX. “We want to work with these nice smart young people who are building the financial system of the future, and I am sure that with their advice we can write smart regulations that protect consumers while still fostering innovation” was a totally normal thing for regulators (except the SEC) to think and say in 2021. But now it is not! Now too many of those smart young people are under indictment or giving interviews from undisclosed locations; too much customer money is gone.
Nobody wants to hear it! Ooh, if we enforce traditional securities laws without adapting them to crypto, there will be no crypto trading in the US: fine! The SEC’s majority view is just crystal clear here:
	Virtually all crypto tokens are securities.	Securities cannot legally be traded, in the US, except on a registered securities exchange.
  [4]

	Hahaha good luck registering your crypto exchange!

Peirce says:

During my time as a Commissioner, this agency repeatedly has urged firms seeking to sell crypto tokens or build crypto businesses to come in and register. Many firms have responded to this call; they have engaged with staff and Commissioners intensively to determine whether they need to register and, if so, how they might do so. With the exception of a few token registrations and a very small number of ATSs employing a clunky (to satisfy regulatory demands) method of facilitating trades, no firm has been able to do so.
A Commission serious about regulating—and not destroying—this market would reflect on this near unblemished record of regulatory failure and do something about it. We would consider the possibility that our rules, which in the past have evolved to address the needs of, and the risks presented by, investors and firms in the traditional securities markets, might require some tweaking to permit firms to offer innovative ways of doing finance using novel technologies. 

“A Commission serious about regulating—and not destroying—this market” would be a different SEC! You don’t have to like it, but it is easy to know what the SEC wants.
Also, I should note that two of the crypto tokens mentioned as securities here — DASH and  Algorand — appear to be listed on Coinbase. If it’s illegal for Bittrex to trade them then presumably it is also illegal for Coinbase to trade them. I’m sure we’ll find out the SEC’s views on that soon enough.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      IO mortgages
    
  

For most people, the biggest interest-rate bet they will make in their lives is taking out a mortgage.
  [5]
 If you were a pretty sophisticated Wall Street professional — say, the president of Goldman Sachs Group Inc.? — and it was 2020, what sort of interest-rate bet would you want to make? Well, at least with the hindsight of 2023, “interest rates in 2020 are very low and they will probably go up from here” would have been a good bet, so you might have wanted to get short duration. So you’d borrow as much money as you could at a low long-term fixed interest rate. Most banks would give you a 30-year mortgage at a fixed rate, which is a good start. But most mortgages amortize — you pay back some of the principal each month — which reduces their duration. If you wanted to be short a lot of duration, you might look for a bank to give you a non-amortizing mortgage where you only pay interest, not principal, for many years. (Ideally you’d pay a very low interest rate because of your good credit and fancy job.) And then you could use the money to pay for a house that you could have bought with cash, and invest the cash in very short-term investments — like bank deposits? — so that it is available to deploy when rates go up. You have borrowed long to lend short; you have effectively gotten yourself an interest-rate swap where you pay a fixed rate and receive a floating rate. 
Of course most people do not take out mortgages primarily to make interest-rate bets; most people take out mortgages because that’s how they can afford to buy a house. The president of Goldman Sachs though ... probably more thoughtful about his interest-rate bets? Less likely to need the money, more likely to be doing a trade? More likely to have a view on the path of rates, and a desire to get short duration? More likely to shop around for the bank that will buy as much duration from him as possible? 
Bloomberg’s Noah Buhayar, Jennifer Surane, Max Reyes and Ann Choi have a story about how First Republic Bank sought out sophisticated rich customers,   which was a mistake:

Wealthy homebuyers and property investors with high incomes and sterling credit scores could get a mortgage from First Republic Bank with a rock-bottom rate for several years. Better yet, they didn’t have to start repaying the principal for a decade. 
Across Manhattan, the San Francisco Bay area and Southern California, those terms attracted legions of wealthy clients — including executives from other banks — as interest rates sank during the pandemic. The loans left borrowers with more cash to invest and spend than if they financed their properties with more conventional mortgages. Demand was so strong that it helped First Republic double its assets in four years, while deposits surged. …
The mortgages are performing well, but their low rates and delayed repayments hurt their value. … By the start of this year, First Republic estimated its $137 billion stockpile of mortgages would be worth about $19 billion less than their carrying value if sold off, its annual report shows. …
New York City property records from the past few years show customers came from all over the financial sector and included industry leaders such as Goldman Sachs Group Inc. President John Waldron, who took out an $11.2 million mortgage in June 2020, and R. Lawrence Roth, a board member at Oppenheimer Holdings Inc. … All of their loans had 10-year interest-only periods and rates starting below 3%.

Yes look if you are a regional bank and the president of Goldman Sachs comes in and says “hi I’d like to make an $11 million interest-rate bet with you,” you are getting adversely selected. 
One way to think about the 2023 banking mini-crisis in the US is that the problem was with banks whose customers were too sophisticated.
  [6]
 Silicon Valley Bank borrowed short to lend long and ended up with a mark-to-market hole in its balance sheet when interest rates went up, but that’s   a pretty common story for any bank; the problem at SVB was that   all of its depositors were venture-backed tech firms who noticed that hole in the balance sheet, shared that information with their networks, and acted quickly to protect themselves. They were too smart for   their bank’s own good.
Similarly First Republic courted wealthy and sophisticated clients with favorable mortgage rates. But wealthy and sophisticated clients are kind of a mixed bag! Sure they have the money to pay you back; their credit is good. But the risk is that you will sell them products that are advantageous for them, and not so much for you.

  
    
      Schwab
    
  

A good price for a stock trade is $0. If you run a retail brokerage and you charge customers $0 for stock trades, they will tend to keep their money with you and do a lot of stock trades; if you charge them $4.99 they’ll say “meh, stock trading, not great.” Making stock trading frictionless is good for attracting stock trading, and you are in the business of attracting stock trading.
But it costs you money to do the trades — you need computers and customer service and so forth — and so you need to pay for them somehow. And so a big question in modern US retail stock brokerage is how brokers can make money to subsidize commission-free stock trading. One approach that gets a lot of attention is payment for order flow: The broker can charge its customer $0 for a trade, and then instead of paying to execute the trade on a stock exchange, it can get paid by a market maker that really wants to execute the trade. This is hotly controversial for reasons we have   discussed too many times, and the US Securities and Exchange Commission has been   working on rules to restrict it, rules that might make it harder for brokers to offer commission-free trading.
But there is another, simpler, more popular approach, which is that most brokerage customers tend to have cash in their brokerage accounts, cash that they have not yet invested in stocks. The brokerage can take that cash, invest it in safe bonds, earn some interest, pay a little of the interest to customers, keep the rest of it for itself, and subsidize free trading that way. That is, the brokerage can also be a bank, and make a net interest margin on the difference between what it pays customers on their deposits and what it earns from investing them. In 2019,  Patrick McKenzie pointed out that “57% of Schwab’s revenues are from net interest. The firm could literally give away every other service; discount the mutual fund fees to zero, do away with commissions, etc etc, and they would still be profitable.” 
It is possible that that was a low-rates phenomenon, or at least that it breaks down a bit when rates rise rapidly. Bloomberg’s Annie Massa and Edward Harrison   reported last week:

Charles Schwab Corp. stunned Wall Street in 2019 by slashing trading commissions to zero, forcing its competitors to adapt. The move amounted to a big bet that its bank — rather than its well-known discount brokerage — would keep driving profits.
For a while, it worked to perfection. The pandemic hit, interest rates were pinned near historic lows, and Schwab raked in billions as the fees it had forsaken were offset by what the company earned from its banking operation.
But last month’s collapse of three US banks, the industry’s worst crisis since 2008, has turned that wager on its head.
Now Schwab, the biggest publicly traded US brokerage, faces one of the most painful moments in its 50-year history. After a rapid surge in interest rates, deposits sank while unrealized losses swelled. 

Schwab got customer cash and invested it in bonds that lost money:

Because Schwab generates most of its money from customer funds idling in low-yielding accounts — which it “sweeps” into its bank arm — the firm needed somewhere to invest incoming cash as trading surged. 
Like Silicon Valley Bank, the largest of the three lenders that imploded last month, Schwab plowed into debt that will take five years or more to mature. … The investments are now underwater, though Schwab won’t have to book a loss unless it’s forced to sell them. 

And meanwhile the customer cash is drying up because there are better rates elsewhere:

Whether the remaining deposits stay put will depend to a degree on the big independent advisers that buttress Schwab’s business. They’re increasingly focused on getting the best returns for clients’ cash.
Charles Sachs, chief investment officer at Kaufman Rossin Wealth, is among them. He moves customer money from Schwab sweep accounts into its higher-yielding money-market funds, on almost a daily basis.

When rates are very low and your brokerage customers are YOLO’ing GameStop Corp. options, it is not really worth their time to move money from a cash sweep account earning 0% to a money-market fund earning 0.5%. When rates go up, though, the money-market funds start looking more attractive, and leaving cash idle to be ready to buy meme stocks is less attractive. 
Anyway Schwab   reported earnings today and they were fine:

Shares of Schwab rose 2.8% to $52.18 at 11:46 a.m. in New York, paring their decline this year to 37%. … Schwab’s customer deposits slid 11% since year-end to $325.7 billion as of March 31. They’re down 30% from a year earlier, a drop that roughly matched Wall Street estimates.  
In a sign of strength, customers continued to add money to Schwab’s investment offerings. Core net new assets totaled $132 billion, including more than $53 billion in March alone, the second-most ever for that month. 
The Federal Reserve’s rapid interest rate hikes buffeted Schwab’s business in recent quarters. Deposits, which underpin revenue, declined as customers moved away from lower-interest accounts and looked for investments that provide better returns for their excess cash. That trend is beginning to moderate, executives said Monday.


  
    
      Everything is securities fraud
    
  

If a publicly traded company owns a television network and uses it to make false claims about rigged US elections, is that securities fraud? Uh, I mean, technically   this is a shareholder derivative lawsuit, but I’m going to count it:
A Fox Corp. investor sued Rupert Murdoch and his son Lachlan on Tuesday, blaming them for allowing Fox News to spread lies about the election and prompting the [Dominion] defamation case. Delaware’s Chancery Court suit accuses the Murdochs and three other Fox directors of “knowingly” hosts and guests to spread Trump’s false stolen-election claims.
Here is  the complaint, which “asserts claims for breaches of fiduciary duty” against the directors. A sample:

The Board’s decision to chase viewers by promoting the false stolen election claims has exposed the Company to public ridicule and negatively impacted the credibility of Fox News as a media organization that is supposed to accurately report newsworthy events. The Company is now the subject of two defamation cases, with combined damages claimed to exceed $4 billion. …
The Board’s failures caused and/or allowed the Company to sell a fictitious story of election fraud for the sole purpose of serving its own business purposes, in disregard for the truth, the Board’s fiduciary obligations and the Company’s best interests.

What a weird sentence. Surely “serving [the Company’s] own business purposes” is the main fiduciary obligation of the board? More than credibility or avoiding ridicule? Like if the claim here was that Fox frittered away all of its money on things that the directors liked but that were bad for business, fine, but here the claim is that the directors thought the election lies were distasteful but good for business. I am not sure how that is a fiduciary breach.
The complaint cites various feel-good Fox public statements and says that “Defendants’ actions/inactions violated the Statement of Corporate Governance, the Standards of Business Conduct, the Corporate Social Responsibility policies, and the [Sustainability Accounting Standards Board] standard.” A   standard everything-is-securities-fraud   theory is that if a company says publicly that it has good ethics, and then it turns out that in fact it did unethical things, and the stock drops, then shareholders will sue for fraud; fine. (Fox’s stock is up since the 2020 election but never mind.) You can sue for securities fraud if the public statements are false. But suing for a breach of fiduciary duties seems odder: The essential claim here is that the directors prioritized the business interests of the company over truth, ethics, US democracy, etc. Which is bad, but not necessarily bad for shareholders.

  
    
      Things happen
    
  

JPMorgan, Citigroup and Wells Fargo  Reap Gains From Rates Roiling Small Banks. Banks Are Finally Facing Pressure to Pay Depositors More. In Morgan Stanley CEO Race,   Wealth Boss Emerges as One to Watch. Bank Failures Rattle Market for  Short-Term Lending.  Life Insurance Is Profitable Again, but Too Late for Many Insurers. Saudi Arabia Transfers Nearly $78 Billion of  Aramco Shares to Wealth Fund. Swiss-owned company’s  Russian gold trades expose gap in western sanctions. ChatGPT Can Decode Fed Speak,   Predict Stock Moves From Headlines. Elon Musk’s Twitter Payment Plan Puts   NYC Subway Alerts at Risk. ‘Overemployed’ Hustlers Exploit ChatGPT To Take On Even  More Full-Time Jobs. A $300,000 Salary   Feels Like $100,000 in The Priciest US Cities. Police search for group of suspects who stole  2 million dimes from truck in Northeast Philadelphia. Athletics Ireland sorry for mix-up that led to national 10km race being  too short.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] This is not a necessary function of a crypto exchange, really: The exchange could match buyers and sellers, and then the trades could settle “on chain,” with the tokens moving from the seller’s wallet to the buyer’s on the relevant crypto blockchain without ever passing through the exchange. Historically crypto exchanges have been more convenient when they’re centralized and keep custody of their customers’ tokens (and cash), but there are lots of decentralized exchanges that are not especially clearinghouse-like, and some big centralized exchanges let users self-custody these days. Still most centralized exchanges are also in the clearing business.


  [2] They are commodities. A feature of US law is that, broadly speaking, you can run a commodities exchange without much oversight, but if you run a commodities *futures* exchange you have to register with the US Commodity Futures Trading Commission. And so crypto exchanges tend not to offer derivatives trading to US customers, to avoid CFTC registration; sometimes they let US customers trade futures and then   get in trouble with the CFTC. A spot Bitcoin exchange — no futures, no securities — is the sweet spot for avoiding most US registration requirements.


  [3] Another is “tokens used/advertised for illegal activities and purposes (e.g. gambling, narcotics, darknet markets),” which doesn’t strike me as a big *securities-law* problem but is, you know, a problem.


  [4] This is loose — they can be traded on an ATS, or directly with a market maker, etc., as discussed above — but I suspect pretty close to what the SEC thinks.


  [5] Well. Arguably every financial decision is in some deep sense an interest-rate bet, so, like, going to work at a startup or getting a graduate degree or having children are in some sense decisions about discount rates. But the mortgage is an explicit rates bet.


  [6] Or   in crypto. That’s different. 


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Matt Levine's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23ciklbe.5kyr/00242d7b.gif" alt="" border="0" /></a>