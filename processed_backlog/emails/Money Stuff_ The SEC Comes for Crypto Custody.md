# Money Stuff: The SEC Comes for Crypto Custody

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Thu, 16 Feb 2023 14:53:57 -0500 (EST)
**Source:** inputs/saved_emails/Money Stuff The SEC Comes for Crypto Custody_Thu,_16_Feb_2023_14-53-57_-0500_(EST)_1865bcb8de1fcbc4.eml
**Processed:** 2025-08-24T19:13:10.890127



  
  
    
      
        
      
    
  
  
    
      
        Programming note: Money Stuff will be off tomorrow, back on Monday.Roughly speaking the way the US stock market works is that all of the sto
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          Programming note: Money Stuff will be off tomorrow, back on Monday.

  
    
      Crypto custody
    
  

Roughly speaking the way the US stock market works is that all of the stocks are in one place. The place is called DTC, the Depository Trust Company, which in some sense owns almost all of the stocks. If you own a stock, what you own is an entry on a list at your brokerage, saying that you are entitled to some of the stocks that it is holding onto for clients, and what your brokerage has is an entry on a list at DTC, saying that it is entitled to some of the stocks that DTC is holding onto. (And what DTC mostly owns is entries on lists at all the companies, or their transfer agents, saying that it owns the stocks that those companies issue.) 
One thing this means is that when I buy some stock from you, the way we settle that transaction — the way you actually deliver the stock to me — is by updating DTC’s list. We tell DTC about the transaction, it increments the stock in my account (really my broker’s, who increments my account) and decrements the stock in yours. This is far more efficient than if, for instance, you owned your stock in the form of paper stock certificates, and to settle trades you had to courier those certificates over to me, which is pretty much how things worked in the olden days.
Another thing this means is that DTC is an extremely important weird market utility, highly trusted and so heavily regulated. “DTC is a member of the U.S. Federal Reserve System, a limited-purpose trust company under New York State banking law and a registered clearing agency with the U.S. Securities and Exchange Commission,”  says its website, on the same page that also mentions that it holds $87 trillion worth of securities. 
The way the crypto market works is a bit different. One way for crypto to work is that there is a blockchain, a decentralized ledger maintained by thousands of independent nodes, and you can own some Bitcoin on the blockchain, and you and I can agree on a trade in which I send you some dollars (by wire transfer or Venmo or whatever) and you send me some Bitcoin on the Bitcoin blockchain. How do we meet each other and agree to that trade? You could imagine some sort of exchange — like US stock exchanges — that allows us to post orders to buy and sell crypto, and if our orders cross — if I want to buy and you want to sell — then we are matched with each other and then settle up using Venmo and the blockchain. This can work in some sort of informal way (like, a message board for us to meet and negotiate trades), or in modern crypto you can have decentralized exchanges built on smart contracts where trades and settlements all occur on the blockchain.
  [1]

But practically speaking the way that a lot of crypto works is more like the stock market: There is some central intermediary, much like DTC, that holds onto a lot of crypto for a lot of investors; we can call it the “depository.” The investors agree on a trade — you agree to sell me some Bitcoin — on an exchange, and then we settle that trade by updating our accounts with the depository. There are some differences, though:
	The depository is normally also the exchange: If you and I are trading on Coinbase, Coinbase is holding onto our crypto for us and updating its ledger when we agree to a trade on its exchange. This is different from the stock market, where the exchanges — NYSE and Nasdaq and so forth — are separate from DTC.	There is normally one depository per exchange: If you have some Bitcoin on Binance, and you and I agree on a trade on Coinbase, you can’t just instantly send me your Binance Bitcoins to settle that trade. Each exchange has its own depository, unlike in the US stock market, where you and I can agree a trade on NYSE or Nasdaq or wherever and then settle up using DTC.	The exchange is … I mean … less trusted by US regulatory authorities than DTC is? To be clear, DTC is very trusted by US regulatory authorities; it is a centerpiece of modern securities markets. Crypto exchanges range from, you know, “not quite as trusted as DTC” to, uh, well, much worse than that.

In the US, the Securities and Exchange Commission regulates “investment advisers,” which means not only people who advise clients about their investments, but also people and firms who manage funds; big hedge funds and mutual funds are generally managed by registered investment advisers. There  are rules about an investment adviser’s custody of client assets: You can’t just keep your client’s stock certificates in a pile under your desk; those assets need to be held by a “qualified custodian” in your client’s name. And there are standard ways to implement this; there are trust companies and brokerages that are in the business of being custodians for investment advisers, and that effectively own the advisers’ clients’ stocks through DTC.
Historically those rules have applied to “client funds or securities”: The SEC regulates securities trades, and so it focuses mostly on securities and money. But in the Dodd-Frank Act of 2010, Congress gave the SEC power to regulate advisers’ custody of client “assets,” which seems to include not just securities and money but also real estate, derivatives, etc.
  [2]
 
And — though probably nobody thought much about it at the time — crypto. And so yesterday the SEC  proposed new rules for custody of client assets:
The proposed rules would exercise Commission authority under section 411 of the Dodd-Frank Act by broadening the application of the current investment adviser custody rule beyond client funds and securities to include any client assets in an investment adviser’s possession or when an investment adviser has authority to obtain possession of client assets. Like the current rule, the proposed rule would entrust safekeeping of client assets to qualified custodians, including, for example, certain banks or broker-dealers.The proposed changes are intended to help ensure that qualified custodians provide certain standard custodial protections when maintaining an advisory client’s assets. These protections are designed, among other things, to ensure client assets are properly segregated and held in accounts to protect the assets in the event of a qualified custodian bankruptcy or other insolvency.
I suppose that this is about lots of things, including the mechanics of the adviser/custodian relationship, surprise examinations of client assets, etc., but it is especially about crypto. SEC Chair Gary Gensler  said in a statement:

Make no mistake: Today’s rule, the 2009 rule, covers a significant amount of crypto assets. As the release states, “most crypto assets are likely to be funds or crypto asset securities covered by the current rule.” Further, though some crypto trading and lending platforms may claim to custody investors’ crypto, that does not mean they are qualified custodians. Rather than properly segregating investors’ crypto, these platforms have commingled those assets with their own crypto or other investors’ crypto. When these platforms go bankrupt—something we’ve seen time and again recently—investors’ assets often have become property of the failed company, leaving investors in line at the bankruptcy court.
Make no mistake: Based upon how crypto platforms generally operate, investment advisers cannot rely on them as qualified custodians.
Further, today’s proposal, in covering all asset classes, would cover all crypto assets—including those that currently are covered as funds and securities and those that are not funds or securities. Thus, through this expanded custody rule, investors working with advisers would receive the time-tested protections that they deserve for all of their assets, including crypto assets, consistent with what Congress envisioned.

A couple of points here. First, the effect of this rule is to ban registered advisers from trading crypto on most exchanges: To trade crypto on most centralized exchanges, you need to deposit the crypto on the exchange first, which destroys custody. From the proposed rule:
Importantly, however, to comply with the proposed rule, an adviser with custody of client crypto assets would generally need to ensure those assets are maintained with a qualified custodian that has possession or control of the assets at all times in which the adviser has custody. While this is true for most client assets over which an adviser has custody, it is particularly relevant with respect to crypto assets because, as we understand, much of the crypto asset trading volume occurs on crypto asset trading platforms that often directly settle the trades placed on their platforms. As a result, many crypto trading platforms require investors to pre-fund trades, a process in which investors transfer their crypto assets, including crypto asset securities, or fiat currency to such an exchange prior to the execution of any trade. Because we understand that most crypto assets, including crypto asset securities, trade on platforms that are not qualified custodians, this practice would generally result in an adviser with custody of a crypto asset security being in violation of the current custody rule because custody of the crypto asset security would not be maintained by a qualified custodian from the time the crypto asset security was moved to the trading platform through the settlement of the trade. 
You can trade stocks on the stock exchange because the stocks live at DTC and you own them through a qualified custodian, but if you trade crypto on Binance then the crypto lives at Binance and the SEC might have concerns. Some crypto exchanges have custody services that probably qualify — “Paul Grewal,  Coinbase’s chief legal officer, said the firm is confident that its New York-chartered trust entity ‘will remain a qualified custodian’” — but your choices are more limited. SEC Commissioner Mark Uyeda  said in his statement that “the proposing release takes great pains to paint a ‘no-win’ scenario for crypto assets,” and:

The proposing release also explicitly states that – because crypto assets trade on platforms that are not qualified custodians – an adviser that trades crypto assets on a platform would violate the proposed rule. Hence, the preamble in the proposing release indicates that it is unlikely that crypto assets can be maintained at qualified custodians or traded on crypto trading platforms in compliance with the proposed rule. How could an adviser seeking to comply with this rule possibly invest client funds in crypto assets after reading this release?
This approach to custody appears to mask a policy decision to block access to crypto as an asset class.

Another point is, you know, the SEC is not wrong. Crypto exchanges do have a long history of losing customer assets, and of landing in bankruptcy with customers who are very confused specifically about custody questions. Crypto exchanges mostly create the impression that they segregate customer assets, and then mostly end up with customers who are unsecured creditors in bankruptcy. Even Coinbase, which does seem to   keep its customers’ crypto segregated,  can’t definitively promise them that they won’t be unsecured creditors in bankruptcy: The legal regimes for crypto custody are just less settled than the regimes for securities custody. 
One more point I’d like to make is about the SEC’s creativity. The SEC does not “regulate crypto.” In US law, at least some cryptocurrencies — the big ones, like Bitcoin and Ether — are classified as commodities not subject to SEC jurisdiction. But the SEC has launched a pretty comprehensive offensive to take over crypto regulation:
	The SEC   argues that when a crypto project issues tokens to fund its development, those tokens are almost always securities: Other than a few grandfathered tokens like Bitcoin and Ether, most tokens are going to be securities subject to SEC jurisdiction.	The SEC argues that interest-bearing crypto accounts — lending and   staking products — are always securities; if a crypto exchange holds your Bitcoin for you and pays you interest, that’s a security subject to SEC jurisdiction.	The SEC here is using its authority to regulate investment advisers to indirectly regulate crypto: Investment funds are subject to SEC regulation, so the SEC will tell them what to do with their crypto, even if that crypto is not a security.

A general theme of financial regulation is that regulators write rules, and then creative financial-industry lawyers find ways around them. The industry lawyers tend to have advantages over the regulators: They are better paid, for one thing, but also the regulators have to write general public rules that account for all cases and then the industry lawyers get to poke holes in them at their leisure. I once   wrote specifically about crypto:
If you are the SEC, and crypto people say “please write clear transparent rules so we know what is and isn’t allowed,” you might hear that as “please write clear transparent rules so that we can game them.” This would be a reasonable lesson for the SEC to take from (1) the history of crypto’s “code is law” philosophy ending in hacks, (2) the history of crypto firms ignoring the US securities laws, and for that matter (3) the history of traditional finance firms trying to game the SEC’s rules. Crypto is a wholly new area for US securities regulation, and if you try to write all the rules from scratch in one go you will get things wrong. And then people will ruthlessly exploit whatever you get wrong.
And that is the stereotype: The industry is ruthless and creative about exploiting the rules, and the regulators are constantly playing catch-up.
I just want to say that in crypto right now the SEC is being ruthless and creative about exploiting legal provisions to expand its powers, and the industry seems to be playing catch-up. Just an unusual situation!

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Soligenix
    
  

We have talked before about the problems of meme-stock corporate governance, and particularly the problem of meme-stock shareholder voting. The problem is:
	If you’re a weird public company with a very retail investor base, you will have a hard time getting your shareholders to vote on anything, since retail shareholders stereotypically do not vote.	If you’re a weird public company with a very retail investor base, you will probably end up needing your shareholders to vote for something or other, because you’re weird.

So Digital World Acquisition Corp. wanted to get shareholder approval to extend the time on its deal to buy Donald Trump’s social media company, but   it couldn’t get it, because the retail shareholders who were extremely enthusiastic about buying its stock, and about the deal, were not enthusiastic enough to vote. Or AMC Entertainment Holdings Inc. has a lot of enthusiastic retail shareholders, and it got very good at selling them stock, but it eventually ran out of authorized shares to sell, and it needed holders of a majority of its outstanding shares to vote to authorize more, and it couldn’t get enough votes.
AMC   (probably) solved this problem with some clever engineering. It created a new class of preferred stock, gave each preferred share 100 votes, and distributed 1/100th of a preferred share for each common share, basically a stock split where if you had one common share with one vote now you had one common share and 1/100th of a preferred share with a total of two votes. (The 1/100th of a preferred share is called an APE, an AMC Preferred Equity Unit.) It’s not obvious that this would change much — you still have to get a majority of the combined APE and common holders to vote to authorize more shares — but AMC added a clever twist. It issued the preferred shares to a depositary, Computershare Trust Co., and had Computershare issue the APE units to AMC’s shareholders. So now 100% of the preferred shares are owned, not by a bunch of retail shareholders, but by Computershare. The retail APE holders still get to vote, and Computershare still has to vote its shares however the APE holders vote, but Computershare has to vote all of the shares: If 20% of the APE holders vote yes, 5% vote no, and 75% don’t vote at all, then Computershare will vote 80% of the preferred shares for yes and 20% for no. AMC still needs to win the vote, but it has solved the problem of retail shareholders not voting at all.
  [3]

Soligenix Inc. is a micro-cap biotech company listed on the Nasdaq. Nasdaq will delist companies whose stocks trade below $1 per share for an extended period. Soligenix’s stock traded below $1 for a long time, and Nasdaq threatened it with delisting starting in December 2021. By December 2022 it was still below $1 and  in real danger of delisting. The normal solution here is a reverse stock split: If your stock trades at $0.70, and you do a 1-for-10 reverse stock split, then every 10 shares (each worth $0.70) become one share, which should be worth $7.00. But you need shareholder approval for the split, and Soligenix was worried about its ability to get a majority of its retail, penny-stock shareholders to vote for anything.
  [4]

So Soligenix came up with an APE-like solution. Like AMC, it  issued new “blank-check preferred stock”; each share of its new Series D preferred stock came with one million votes.
  [5]
 And it distributed the preferred shares to its common shareholders, giving them each 1/1,000th of a preferred share (with 1,000 votes) for each common share that they own. So effectively all of the voting power of the company is in the Series D preferred, but the voting rights don’t really change, because every existing common shareholder owns the same proportional amount of Series D preferred.
But the Series D preferred stock is a temporary blip: Soligenix issued it in December, and it all disappeared last week.
  [6]
 It never traded, had no cash value, was issued to shareholders for $0 and then redeemed by the company for $0.
  [7]
 For a couple of months Soligenix had some extra shares with billions of votes, and now it doesn’t. 
Why? Well, here are the mechanics of how the Series D disappeared:
All shares of Series D Preferred Stock that are not present in person or by proxy at the meeting of stockholders held to vote on the reverse stock split as of immediately prior to the opening of the polls at such meeting will automatically be redeemed by the Company. Any outstanding shares of Series D Preferred Stock that have not been so redeemed will be redeemed if such redemption is ordered by the Company’s Board of Directors or automatically upon the approval by the Company’s stockholders of an amendment to the Company’s certificate of incorporation effecting the reverse stock split at such meeting.
Get it? Soligenix  held a shareholder meeting last Wednesday, Feb. 8. If you voted at the shareholder meeting — that is, if you filled out your proxy to vote your shares — then your preferred stock got canceled immediately after the vote. If you didn’t vote — if you forgot or were unreachable or whatever — then your preferred stock got canceled immediately before the vote. At the moment of the vote, the preferred stock represented roughly 99.9% of the voting power of the company, and only the preferred shares that actually voted were outstanding. They voted overwhelmingly for the reverse split, and it passed.
  [8]
 Soligenix  did a 1-for-15 reverse stock split, and the Series D disappeared back into the lawyer’s imagination from whence it came.
Is this legal? I mean, the answer is:
	nothing here is ever legal advice;	it is funny, anyway, and isn’t that the real purpose of securities lawyering; and	who would object?

The large majority of the shareholders who bothered to vote wanted this result; Soligenix just found a way to give it to them. 

  
    
      
        
      
    
  


  
    
      Designated counsel
    
  

Most of the time, if you are a person and you want to borrow money from a bank, the bank sends you a contract — a credit card agreement, say — and you sign it. If you send them back a markup of the agreement with some suggested changes to make it more friendly to you, they will not even understand what you are talking about. Nobody at the bank has the job of negotiating that agreement with you; that is not an agreement that gets negotiated. You just sign the form that they send you, or you don’t get the money.
At higher levels of finance, things are more equal and the leverage shifts. If you are a big corporation and you want to borrow money from a bank, they bank will send you a credit agreement, your lawyers will mark it up, your lawyers will negotiate with the bank’s lawyers and eventually you will agree on the terms. The bank wants your business and can be much more flexible with the contract than it would be with a retail customer.
There are, however, even higher levels. If you are a big private equity firm and you want to borrow money from some banks, you send them a credit agreement. And then you pick the lawyers that they hire to mark it up. Here’s a Bloomberg News story about “designated counsel”:

Originally heralded as a way to make the often-fractious buyout process more efficient, the widely-used designated counsel arrangement is now viewed by many, including some of Wall Street’s biggest names, as a potential conflict of interest. It allows private equity firms, guided by their lawyers, to appoint and pay for the law firms that represent the lenders funding their deals.
The International Organization of Securities Commissions (IOSCO) has begun looking into the designated counsel arrangement as part of a wider probe into leveraged debt markets, a spokesperson for the regulator said. Other regulators such as the Financial Conduct Authority are involved in IOSCO’s work. 
Since the early 2010s, market pressures — and access to plentiful cheap money — meant many lenders lacked the negotiating power to push for stronger protections. [Kirkland & Ellis partner Neel] Sachdev and his buyout clients have used this imbalance to convince lenders, like the credit units of private equity groups and Wall Street’s largest banks, to agree to lesser safeguards around debt levels and dividend payments on deals they help finance. …
Advocates of designated counsel argue that selecting a single law firm to represent all lenders in a deal means negotiations are less likely to get bogged down with multiple teams of lawyers arguing.
But the arrangement encouraged some lawyers to develop close relationships with their counterparts acting on behalf of private equity groups. For some law firms that translated into repeat work and a lucrative stream of business, according to people working at credit funds and law firms, who did not want to speak publicly to avoid damaging institutional relationships.
The extent to which some lawyers became dependent, at least partially, on this designated business has triggered concerns among a number of lenders about potential conflicts of interest.

There are sort of two points here:
	Big private equity firms push their lenders to hire designated counsel that they pick, and the lenders accept the designated counsel because they don’t have a lot of leverage in the negotiation. And then the designated counsel might not negotiate the covenants as aggressively as independent lawyers would.	Big private equity firms push their lenders to accept weak covenants, and the lenders accept the weak covenants because they don’t have a lot of leverage in the negotiation.

That is, the designated counsel are a result of the lenders not having much negotiating leverage, not (only) a cause. But rates are up, conditions are tighter, and now “direct lending units at firms such as Blackstone - which declined to comment for this story - are said to be drawing up lists of preferred law firms to act as designated counsel and actively pushing back when certain law firms are selected for the role.”

  
    
      People are worried about CEO narcissism
    
  

Here is a paper called “The beguiling behaviour of narcissistic CEOs: Evidence from repurchase announcements,” by Evans Ofosu Boamah and Shantanu Banerjee of Lancaster University, which on one level finds that companies with narcissistic chief executive officers are more likely to announce large share buybacks, but less likely to actually complete those buybacks:
Using signature characteristics as a measure of narcissism, we find that US firms with narcissist CEOs are more likely to make repurchase announcements and announce higher repurchase dollar amounts. However, these firms are less likely to follow through. They repurchase less and a small dollar amount when they make an actual repurchase in the announcement year. The higher rate and amount of repurchase announcements are more pronounced in poorly-governed firms with narcissistic CEOs. These results are robust to various specifications including a difference-in-difference specification using CEOs’ exogenous turnover, controlling for other CEO traits and using an alternative measure of narcissism based on pronoun usage in CEO communications. Collectively, the results presented in this study demonstrate that narcissist CEOs play a critical role in the intensity of share repurchase announcements and their executions, particularly for firms with weaker governance structure.
But at another level it demonstrates that financial academics can spend their time analyzing CEO signatures — like, literally, how they sign their names — and then trying to correlate those signatures to financial outcomes:
Psychology literature argues that handwriting styles reflect personality (Chaudhari and Thakkar, 2019). In line with this, we measure CEO narcissism using the area per character signature size narcissism measure. Using an unobtrusive measure such as signature size reduces the  reactivity, researcher expectation and demand characteristics that can weaken the measure’s validity (Chatterjee and Hambrick, 2007). We draw a rectangle that touches the CEO signature’s edges to measure the area per character signature size. We measure the area by multiplying the length and width of the rectangle. We measure CEO narcissism by dividing the area by the number of characters in the CEO’s signed name. According to our prediction, the greater a CEO’s narcissism score, as measured by the signature size, the more likely the announcement of repurchases and target a larger dollar amount.
I feel like that’s the sort of thing you can do in academia. If you work at a hedge fund and you go to your boss and say “I am going to predict how much stock our portfolio companies will buy back by taking a tape measure to the CEO’s signature in the proxy statement,” what would your boss say? I actually don’t know? I feel like I am going to get some emails that are like “I work at a hedge fund and we use handwriting analysis all the time to predict short-term stock price moves.” Really finance is the study of human behavior and I guess signing your name really big is a human behavior like anything else, apparently one that correlates with stock buyback announcements.

  
    
      Things happen
    
  

The SEC approves  T+1 settlement. “‘It was like working for   Stalin or Hitler or something,’ says Jimmy Watson Jr., [John] McAfee’s former bodyguard and business partner.” Tech start-ups face dilemma over  expiring staff stock options. From   Math Camp to Handcuffs: FTX’s Downfall Was an Arc of Brotherhood and Betrayal. The Rainmakers: Meet the  20 powerhouse bankers who orchestrated the biggest deals of 2022 and defied a down market. Missed signals: behind Trafigura’s $577mn loss on  non-existent nickel. Credit Suisse’s Klein Says   First Boston Staff Will Own Firm. EU Sanctions Aim to Make Banks   Divulge Frozen Russian Assets. Adani  halts $847mn acquisition of coal-fired power plant in India. Turkey’s Latest   Lira Defense Is More-Costly Forward Contracts. JPMorgan’s Kolanovic Warns of ‘Volmageddon 2.0’ Risk in Options. Ex-JPMorgan Executive’s   Jeffrey Epstein Emails Revealed in Lawsuit Against Bank. Bing’s A.I. Chat Reveals Its Feelings: ‘I Want to Be Alive.’
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] These tend to be exchanges where you can trade, like, Ether or Solana for Ethereum- or Solana-based stablecoins, etc., not exchanges where you can trade *Bitcoins* for *actual dollars*, just because Venmo or whatever aren’t on the blockchain. 


  [2] See pages 11-12 of  the SEC’s proposed rule, which are maybe a touch argumentative about how much Congress really *intended* to cover non-security assets. “Earlier versions of this bill show that Congress considered retaining the current rule’s funds and securities formulation,” says a footnote; basically the argument is that “assets” must mean something more than “funds and securities,” because an early draft said “funds and securities” and then was changed to “assets.”


  [3] We   discussed this two weeks ago, and there is more to it: AMC also sold a bunch of APEs to a big investor who promised to vote them to authorize more shares, and the APEs have generally migrated into the hands of arbitrageurs with an incentive to approve the issuance. But the depositary voting stuff is the real innovation.


  [4] In fact, in September 2022, Soligenix asked its shareholders to authorize more shares, but the vote failed. Soligenix said in a securities filing: “Despite support for Proposal 2 exceeding 80% of the votes cast on the proposal, Proposal 2 did not receive the affirmative vote of holders of more than 50% of the Company’s issued and outstanding shares of Common Stock and, therefore, was not approved. A large proportion of the stockholders holding shares through banks, brokers or other nominees could not be identified or were unresponsive to the Company’s outreach in urging them to vote their shares.” The shareholders who voted wanted to authorize more shares, but most shareholders didn’t vote.


  [5] I learned of this because we 
talked yesterday about Purple Innovations Inc.’s PRPLS preferred shares, each of which had 10,000 votes, and reader Patrick Corn emailed to say that he could top that with a million votes per share.


  [6] I think? There is no filing reflecting that it disappeared, but the  initial announcement said that it would be redeemed “automatically upon the approval by the Company’s stockholders of an amendment to the Company’s certificate of incorporation effecting the reverse stock split,” which  happened last Wednesday.


  [7] Technically,  for $0.10 per 100 whole preferred shares (corresponding to 100,000 common shares) beneficially owned by a holder, but no cash payment for any fraction of 100 whole preferred shares. So if you owned 100,000 common shares you could get $0.10 out of this. The biggest shareholder, according to Bloomberg data, seems to be the Vanguard Group, with 1.6 million shares, so they stand to get $1.60 I guess, and a few executives disclosed in  the proxy seem to have more than 100,000 shares and so might get a few cents, but pretty much everyone else gets zero.


  [8] Specifically, there were about 43 million common shares and 43,335 preferred shares (with 43.3 billion *votes*) outstanding a month before the vote. There were about 18.6 billion votes for the reverse split, about 3 billion votes against, and about 591 million abstentions, meaning that roughly half of the shares voted one way or the other (or even filled out a proxy to abstain). But the other half were canceled, with the result that the proposal got 84% of the vote.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Matt Levine's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23ci7cdn.62ck/cd7eade6.gif" alt="" border="0" /></a>
