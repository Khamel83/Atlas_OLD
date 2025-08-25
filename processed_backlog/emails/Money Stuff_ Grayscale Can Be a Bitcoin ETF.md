# Money Stuff: Grayscale Can Be a Bitcoin ETF

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Tue, 29 Aug 2023 13:44:50 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Grayscale Can Be a Bitcoin ETF_Tue,_29_Aug_2023_13-44-50_-0400_(EDT)_18a4266035923274.eml
**Processed:** 2025-08-24T19:13:08.440976



  
  
    
      
        
      
    
  
  
    
      
        There are two ways to run a Bitcoin exchange-traded fund: You could raise money from investors, park it in cash or Treasuries, and trade cas
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Grayscale
    
  

There are two ways to run a Bitcoin exchange-traded fund:
	You could raise money from investors, park it in cash or Treasuries, and trade cash-settled Bitcoin futures listed on a US commodities exchange.
  [1]
 The futures would periodically expire, paying off whatever Bitcoin is worth at the time, and you would roll the proceeds into new futures to keep your Bitcoin bet active. The ETF would roughly track the price of Bitcoin, because the futures pay off based on the price of Bitcoin, but there would be some frictional costs from rolling the futures and some tracking error.	You could raise money from investors, use it to buy Bitcoins, and keep the Bitcoins somewhere safe. Then you’d have Bitcoins, and the price of the ETF would track the price of Bitcoin. If it didn’t, arbitrageurs could deliver Bitcoins and get back ETF shares, or deliver ETF shares and get back Bitcoins, just like any normal stock index ETF.

It seems to me that Approach 1 is, you know, fine and interesting, but Approach 2 is strictly better: It’s simpler for the ETF manager to do, simpler for investors to understand, and has less friction and tracking error. My one quibble with Approach 2 is that you really do have to keep the Bitcoins somewhere safe, and there is a long, long, long history of people in crypto finding exciting new ways to lose their cryptocurrency, but I think that in 2023 “buy Bitcoins and don’t lose them” is the sort of thing that you can expect a regulated financial institution to manage.
But in fact the US Securities and Exchange Commission has approved Bitcoin futures ETFs (Approach 1) and repeatedly declined to approve spot Bitcoin ETFs (Approach 2), for reasons that have   never really made much sense to me. Essentially the SEC worries that the spot Bitcoin market is the Wild West, someone might manipulate it, and if they did then the price of the Bitcoin ETF would be manipulated. Whereas Bitcoin futures trade on the Chicago Mercantile Exchange,
  [2]
 a US commodities exchange regulated by the Commodity Futures Trading Commission; that market is presumably free of manipulation, so a Bitcoin futures ETF can rely on it.
This strikes me as a bit silly: The spot Bitcoin market is much bigger than the one for CME-listed Bitcoin futures,
  [3]
 and the futures are obviously a derivative of spot Bitcoin prices, so if you managed to manipulate the price of Bitcoin you would also succeed in manipulating the price of Bitcoin futures. As a matter of legal formalism, I can see why you might say “US-approved ETFs should only own things that trade on US-regulated exchanges,”
  [4]
 but as a matter of economic reality I don’t think it really works.
My assumption is that (1) the SEC really dislikes crypto, (2) a spot Bitcoin ETF is a straightforward, easy-to-understand, appealing product that would make it easier for a lot of US investors to own Bitcoin, and so (3) the SEC wants to block spot Bitcoin ETFs just to protect US investors from crypto generally. (Whereas a Bitcoin futures ETF is complicated and janky enough to turn off a lot of investors.) It can’t say that, but its stated reasons for blocking spot Bitcoin ETFs don’t make a ton of sense.
The biggest wannabe spot Bitcoin ETF is the  Grayscale Bitcoin Trust, a $16 billion pot of Bitcoins that is organized as a closed-end investment trust; it trades under the ticker GBTC, and it has been trying to convert into an ETF for years. In its current form, it can accept new investor money but can’t really redeem investors, which makes it not a great way to hold Bitcoin; it has over the years traded at large premiums or discounts to the actual price of Bitcoin, and as of yesterday it traded at about a 25% discount.
  [5]
 Converting to an ETF would make it easier for Grayscale to transform Bitcoins into GBTC shares and vice versa, which should more or less eliminate the discount and create billions of dollars of value for investors.
Grayscale kept asking the SEC to approve it as an ETF, the SEC kept saying no, so Grayscale sued in US federal courts.   Today it won:

A three-judge appeals panel in Washington on Tuesday overturned a decision by the US Securities and Exchange Commission to block the ETF, which would be tied to the spot Bitcoin price.
The ruling marks a major legal win for the crypto industry and sent the price of Bitcoin surging by as much as 6%. The SEC could still fight the decision.
Grayscale has said converting to an ETF would help it unlock about $5.7 billion in value from the $16.2 billion trust by making it easier to create and redeem shares. More broadly, the crypto industry has long viewed the launch of an ETF based on the cryptocurrency itself, rather than futures, as significant milestone.
In June 2022, the SEC rejected Grayscale’s conversion proposal arguing that an ETF based on Bitcoin lacked adequate oversight to detect fraud. Grayscale sued to overturn the decision accusing the SEC of discriminating against its product, while approving similar Bitcoin futures ETFs.
“The denial of Grayscale’s proposal was arbitrary and capricious because the Commission failed to explain its different treatment of similar products,” wrote Judge Neomi Rao.

Here is  the opinion. The court says:
Grayscale has demonstrated its proposed bitcoin ETP is materially similar, across relevant regulatory factors, to the approved bitcoin futures ETPs. First, the underlying assets—bitcoin and bitcoin futures—are closely correlated. And second, the surveillance sharing agreements with the CME are identical and should have the same likelihood of detecting fraudulent or manipulative conduct in the market for bitcoin and bitcoin futures. 
Basically Grayscale, like the Bitcoin futures ETFs, proposes to rely on the CME (which trades Bitcoin futures) to detect fraud and manipulation in the Bitcoin market.
  [6]
 The futures ETFs own futures traded on the CME, while Grayscale just owns actual Bitcoins, but any manipulation will probably affect both. From the opinion (citations omitted):

While the Commission asserted that owning assets not traded on the surveilled exchange was a “significant difference” and proclaimed that there was “reason to question whether a surveillance-sharing agreement with the CME would, in fact, assist in detecting and deterring fraudulent and manipulative misconduct affecting the price of the spot bitcoin held by that ETP,” it provided no support for these claims. Grayscale, however, provided evidence that CME bitcoin futures prices are 99.9 percent correlated with spot market prices. Based on that data, fraud in the spot market would present identical problems for a bitcoin ETP and a bitcoin futures ETP. Bitcoin futures are derivatives of bitcoin and, as long as the market is efficient, arbitrage will drive the prices together.
The Commission neither disputed Grayscale’s evidence that the spot and futures markets for bitcoin are 99.9 percent correlated, nor suggested that market inefficiencies or other factors would undermine the correlation. The Commission faults Grayscale for failing to provide other types of evidence. Without further explanation, however, the Commission’s assertion that “information in the record for this filing does not support [the] claim” that “any fraud or manipulation in the underlying [spot] market will affect both products in the same way” is unreasonable. The Commission’s unexplained discounting of the obvious financial and mathematical relationship between the spot and futures markets falls short of the standard for reasoned decisionmaking. 

And so the court reversed the SEC’s order for being “arbitrary and capricious.”
Substantively this seems correct and straightforward: It really is kind of arbitrary for the SEC to allow Bitcoin futures ETFs and not spot Bitcoin ETFs.
Still it is a potentially important decision. For most of my time watching financial markets, the courts and the financial industry have broadly deferred to the SEC as the expert financial regulator. If the SEC says “well Bitcoin futures ETFs are a safe product but spot Bitcoin ETFs are not,” who is a federal judge to second-guess that? The SEC’s decisions on a range of financial regulatory topics were, in effect, final; fighting the SEC often seemed to big repeat-player firms like a bad idea.
But that might be changing. The current SEC under Chair Gary Gensler has been aggressive about expanding its regulatory authority — in crypto, of course, but also in things like the regulation of  private funds or   environmental disclosure. Meanwhile the financial industry — the crypto industry, but also more traditional financial firms — has gotten more aggressive about pushing back on the SEC, fighting enforcement cases in court or suing the SEC for “arbitrary and capricious” rulemaking. And the post-Trump federal courts are far more willing to strike down regulatory decisions, and   more skeptical of regulation generally.
One possible interpretation of this case is that the SEC’s decision to block spot Bitcoin ETFs was unusually egregious, and a court fixed that, and there are no broader implications for anything. And that’s possible, because the spot Bitcoin ETF decision really was weird. But another possible interpretation is that the modern SEC has become more aggressive about regulating the crypto industry, and the broader financial industry, in a lot of different areas, while the crypto and financial industries have become more aggressive about fighting back and the modern US courts have become more aggressive about second-guessing the SEC. The SEC has gotten used to its decisions being, for all practical purposes, the law, and that might not be right anymore.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Sculptor
    
  

A classic tension in public company mergers and acquisitions is that, if you are running an auction to sell your company, you want to force bidders to put in their best bid in the auction. “Put in your very best bid,” you tell them, “because if you lose this auction you won’t get another chance to buy the company.” And then you open up the bids and pick the top one and sign a contract with the top bidder saying that you will sell them the company. And then you announce the deal, saying “we are selling our company to Bidder X for $10 per share.”
And then the next day Bidder Y, who bid $9.75 in the auction and lost, sends you a letter saying “okay fine we’ll pay $10.10.” And you say “no, it doesn’t work that way, we wanted your best bid in the auction, we told you you wouldn’t get another chance!” But, also, $10.10 is more than $10. And you still have a fiduciary obligation to your shareholders to get the best price. You can’t really tell Bidder Y no. You have to take their new bid seriously, because it is more money for your shareholders. You might have to get out of your merger agreement with Bidder X and sell to Bidder Y at the higher price.
The tension is that you can probably get a higher price in the auction by committing, ex ante, not to accept any bids after the auction: Bidders will put in higher bids if they know there are no second chances and if they win they get the company. But you can’t really commit to that because, ex post, if you get a higher bid you will feel compelled — by your fiduciary duty to your shareholders — to consider it.
There are standard best practices. When you start the auction process, you will ask every potential bidder to sign a nondisclosure agreement (promising to keep secret whatever they learn in due diligence). The NDA will often contain a bunch of standstill provisions in which the bidders promise not to, for instance:
	buy any more stock of the company;	make a tender offer for the company;	put in a public proposal to buy the company;	put in a private proposal to buy the company;	ask the company to waive the standstill.

The idea is that, if Bidder Y comes to the company after the auction and says “we’ll give you $10.10,” the company will have to consider that, undermining its deal with Bidder X. If Bidder Y even comes to the company after the auction and says “we know we are not allowed to put in another bid, but could you waive that provision so that we could put in another bid,” the company will have to consider that too, so as not to leave money on the table. And so the company’s advisers will do the best they can, ex ante, to prevent that, so that they can run a clean auction that gets the best price and then ends. 
The advantage of this is that it gives the winning bidder certainty that it will actually buy the company, rather than serving as a stalking horse for an endless public bidding war. (And so bidders in the auction should be willing to pay more.) The other advantage is that it makes life easier for the target company and its advisers: They can run an auction, pick the best bid, and move on with their lives, instead of being mired in weeks of fighting.
There are other best practices. The merger agreement that the company signs with the winning bidder will try to lock up that bidder’s deal: The company might promise not to look for more bidders, not to waive any provisions of the standstill, and not to negotiate with other buyers, etc. But in modern US M&A those provisions are rarely absolute; they will generally say “… unless the board determines that it has a fiduciary duty to do that.” If you do get a higher bid, you can’t just say “nope we have a contract sorry”; you have to consider it.
Also there is generally a breakup fee: If the company takes a higher offer and breaks its original deal, the winning bidder in the original auction gets some cash. One reason for this is to compensate the original winning bidder for being, in hindsight, a stalking horse for a bidding war. Another reason for it is to deter other bidders: If you lose the original auction and try to buy the company anyway, then not only do you have to top the winning bid, you also have to pay the breakup fee. (Again, though, this deterrent can’t be absolute, and courts generally limit breakup fees to a reasonable single-digit percentage of deal value.)
We have   talked a few   times about the contested M&A deal for Sculptor Capital Management Inc., a publicly traded hedge fund management company. Sculptor ran an auction to sell itself, talked to 70 potential bidders, signed lots of NDAs and standstills, got a few serious bids and ended up signing a merger agreement with Rithm Capital Corp., which agreed to pay $11.15 per share. 
Since then, another bidder — a group of hedge fund managers led by Boaz Weinstein and also including Bill Ackman, Marc Lasry and   Jeff Yass — has offered Sculptor $12.25 per share, and Sculptor has turned them down, arguing that they don’t really have financing and that their deal is too uncertain. The Weinstein group argues that they can’t make a fully committed offering if Sculptor won’t engage with them, and that Sculptor’s board has brushed them off — both during and after its official auction — because it wants to preserve Chief Executive Officer Jimmy Levin’s job. (Rithm will leave Levin in charge of Sculptor; Weinstein probably wouldn’t.)
And one tension is about how much Sculptor should let Weinstein do to firm up his bid. On the one hand, $12.25 is more than $11.15, and Sculptor’s board should want to maximize value for shareholders, so it should engage with Weinstein. On the other hand, it ran an auction and picked the best bidder: It has some contractual obligations to preserve its deal with Rithm, and the losing bidders have some contractual obligations not to try to break up that deal. So Weinstein has not put in a public proposal to buy Sculptor — that $12.25 proposal was delivered privately to the board, which then disclosed it itself — because he’s not allowed to; his NDA doesn’t let him make public proposals. (Sculptor’s  merger proxy discloses that it signed 25 NDAs in the auction process, of which 24 contained standstills and “twenty-two of the standstill provisions contained ‘don’t ask/don’t waive’ provisions” that prevent failed bidders from asking the board to make another bid; Sculptor’s board waived those provisions after hearing from Weinstein.)
Meanwhile Sculptor’s estranged founder, Daniel Och, has been asking Sculptor to do more to waive those provisions and let more people bid. He  sent the board another letter today:
On August 22, 2023, we requested that you waive certain restrictions in the non-disclosure agreements with Bidder J, Bidder H, and the Founders’ group (the “NDAs”), because we believed that preventing those bidders from publicly articulating their proposals and from speaking with us was contrary to the interests of shareholders. Specifically, we cannot understand how the Special Committee could possibly conclude that it is in the best interests of shareholders to deter us from communicating freely with such bidders to improve their bids, thereby reversing the prior massive diversion of value from shareholders to management in order to achieve maximum value for all shareholders.
Anyone buying Sculptor will have to deal with Och, who has a bunch of shares and some tax arrangements with Sculptor that are worth a lot of money; one bidder in the initial auction seems to have dropped out because it couldn’t come to terms with Och. Letting potential bidders negotiate with Och would probably allow them to make their bids, if not better, at least more certain. But when they signed up for the original auction they agreed not to talk to anyone else, because Sculptor’s board wanted to be in control of the sale process. But it is increasingly losing control.

  
    
      Citadel interns
    
  

The standard story about quantitative trading firms is that they prefer to recruit people who are very good at math and coding rather than people with any financial experience or training. The thinking is roughly that if you take someone who is good at math and coding, you can teach them the basics of trading pretty easily; if you take someone with an MBA and an active Robinhood account, you might have a hard time teaching them math. In fact, too much business background could be a negative: If you run a differentiated quantitative investing or market-making firm, you might think that you do things the Right Way, and big banks do things the Wrong Way, and traders who have worked at those banks have learned the wrong things and are now unfixable. Better to get a 20-year-old intern who is good at math and teach them from scratch.
Whether or not this theory is true on its own terms, it has some practical advantages. If you are recruiting 20-year-old math undergraduates to your hedge fund, you can impress them — and get them to come back as full-time employees, and get them to go recruit their best math classmates for you — by paying them amounts of money that are (1) way more than any other 20-year-olds make but (2) way less than you’d be paying to recruit financial industry veterans. If they are living on ramen at college, you can impress them with a couple of fancy lunches.
Also if the theory is true on its own terms, the interns will be useful right away! If you are mainly hiring people for math skills, you can get 20-year-olds with good math skills, and they can do math for you in a way that makes you money. If you are in a math business, and the 20-year-olds making $50,000 are half as good at math as your 30-year-old employees making $1 million, then they are a bargain right now.
Bloomberg’s Lulu Yilun Chen has a story about   Citadel’s internship program:

The highly sought-after interns were hand picked from 69,000 applicants by billionaire Ken Griffin’s lieutenants at Citadel and Citadel Securities LLC, as the finance giant looks to groom the next generation of math and computer whizzes that have helped it become one of the key components for market trading.
Over three days, the students will play the role of hedge fund traders, negotiating with counterparts, writing code, and devising automated strategies based on simulations with news feeds and macro data. It’s all part of a roughly 11-week program to prepare them for the often secretive world of trading and market-making, earning about $120 an hour along the way, or $19,200 a month.
“There’s only a finite pool of truly exceptional students,” said Kristina Martinez, Citadel’s managing director in charge of human resources in Asia-Pacific. “Because of the complexity of what we do and the fact that companies that intersect with us will be looking at the same people, we need to get in early.” …
Almost without exception, the interns come from the most prestigious universities in their regions, some boasting math Olympiad Gold prizes or math doctorates from Stanford University in California. MBAs rarely make the cut.

The interns are allegedly useful for Citadel’s actual business, though I suppose Citadel would say that even if it wasn’t true:
The tasks assigned to every intern are different — depending on whether they work on quantitative research, trading or operations — but they all involve actual problems facing the business. They’re expected to do a 15-minute presentation showcasing their work, and their solutions could be put to use.
Also Citadel is in the business of taking math people and teaching them, not just trading, but general business and personal skills:

Citadel brings in professional trainers to groom them, with exercises that include writing an email to a boss by condensing a rambling, 163-word note down to fewer than 60 words.
Another involves videotaping themselves for a self-introduction, where they are taught to project their voice, match their facial expression to their message, and avoid the pitfalls of filler words and up-speak intonation. They’re also given personality tests and taught how to seek feedback by summarizing what other people say.

Arguably MBAs arrive at their jobs knowing how to write emails to their boss and match their facial expressions to their messages, and math Ph.D.s arrive at their jobs knowing math, and Citadel is betting that the former is easier to teach than the latter.

  
    
      Business bribes
    
  

One of the hazier lines in law is the one between bribery and legitimate business entertainment. Taking a potential customer out to a nice dinner so you can pitch her on your product: Fine, probably? Having a $1,000 bottle of wine with that dinner: A bit iffier? Having five $1,000 bottles of wine: Iffier still? Sending her and her spouse out to dinner without you and picking up the tab: Does not seem like a legitimate business meeting? I don’t know, not legal advice, there are many gray areas.
Here is  an effort from the US Securities and Exchange Commission to draw some lines. For instance: If you schedule a conference in an exciting tourist destination, and you invite potential clients, and you pay their travel expenses, and the conference includes various useful appropriate activities designed to educate the clients about your products, but you also schedule (and pay for) lot of tourist activities for the clients alongside the official conference program, is that okay? I don’t know! But if you schedule the tourist activities at the same time as the official conference program, and they go to the tourist activities instead of the conference, then that feels a lot more like “bribes” than “client education”:

The Securities and Exchange Commission [Friday] announced that 3M Company agreed to pay more than $6.5 million to resolve charges that it violated the books and records and internal controls provisions of the Foreign Corrupt Practices Act (FCPA).
The SEC’s order finds that employees of a 3M wholly owned subsidiary based in China arranged for Chinese government officials employed by state-owned health care facilities to attend overseas conferences, educational events, and health care facility visits, ostensibly as part of the Chinese subsidiary’s marketing and outreach efforts. However, the arrangements to attend the events were often a pretext to provide the Chinese government officials with overseas travel, including tourism activities, to induce them to purchase 3M products.
Specifically, the order finds that, from at least 2014 to 2017, 3M’s Chinese subsidiary provided Chinese government officials overseas travel that included guided tours, shopping visits, day trips to nearby sights, and other leisure activities. According to the order, in a number of instances, the tourism activities were scheduled at the same time as the events the officials were supposedly attending, and at times the Chinese officials missed whole days of the events or simply never attended at all. Also, the events were in English and certain trips included Chinese government officials who neither understood English nor had adequate translation services. The order finds that 3M’s Chinese subsidiary paid nearly $1 million to fund at least 24 trips for Chinese government officials that included tourism activities.
According to the order, to obtain approval for the trips, the employees of 3M’s China-based subsidiary created a travel itinerary for the Chinese government officials to attend legitimate events, and the employees provided the itineraries to compliance personnel at the subsidiary for approval. However, the employees, in collusion with Chinese travel agencies, also created alternate itineraries consisting of tourism activities at or near the location of the overseas educational events, which the employees provided to the Chinese officials who went on the trips. The employees asked the trip participants to keep the alternate agenda hidden and falsified internal compliance documents that affirmatively denied or omitted mention of the tourism activities that they had planned as part of the overseas trip.

According to the SEC’s order, 3M tracked the cost of these trips (“nearly $1 million to fund at least 24 trips” from 2014 through 2017) and their return (“at least $3.5 million from increased sales”). Is that good? I guess about 29% of the revenue from these deals was paid out in bribes?
  [7]
 Bloomberg tells me that 3M’s gross margins were about 48% to 50% in those years, so I suppose the bribes made economic sense, at least before the $6.5 million in fines.

  
    
      Student loans
    
  

This is not any sort of advice, but I feel like a good fraud to do would be to send letters to every 25-to-35-year-old in the US that say “hi, I am your new student loan servicer, student loan payments are coming back, your new payment amount is $437 per month, here’s where you send a check.” That’s what a lot of student-loan servicers are legitimately doing, and how could anyone tell that you were lying? The  Wall Street Journal reports:

Student-loan borrowers are finding out that restarting a $1.6 trillion federal program is much more confusing than switching it off.
With pandemic relief ending, borrowers will start owing interest as of Friday. They are learning of new payment schedules, often via email, from servicers they might have never heard of—and could be reluctant to pay. That is because about four-in-10 borrowers’ loans transferred to a new servicer during the pause that began in March 2020, according to government data.

Obviously don’t do this! But someone probably will, and I look forward to writing about it in a year or two.

  
    
      Things happen
    
  

Mortgage Rates at 7% Are Making 
Everything Worse for US Homebuyers. High hopes, rocky realities: Europe’s new banks struggle to grow up. Conduit bonds. Private Equity Borrows Billions to Bring You  Broadband Internet. OpenAI Launches  Business Version of ChatGPT That Competes With Microsoft.  Lawyers Descend on Maui After Historic Wildfire. Carlsen and Niemann  resolve cheating claim dispute that divided chess. Credit Suisse’s 
Banker to Russian Billionaires Retained by UBS. UBS settles Credit Suisse lawsuit against popular  Zurich finance blog. Brain  worm.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] I say “park it in cash or Treasuries” because futures are a leveraged product: If you buy $100 of Bitcoin futures, you probably put up about $30 of cash to collateralize that bet, and then you post more cash (or get some back) as Bitcoin prices move. The ETF wants to be unlevered, so it will raise $100 from investors, put $30 in the collateral account, and keep the other $70 in cash or whatever. We discussed these mechanics 
back in 2021.


  [2] To be clear, Bitcoin futures trade in lots of places, including crypto exchanges that are not really regulated by anyone, but the US-approved Bitcoin futures ETFs use futures traded on US regulated exchanges.


  [3] CME reports that its Bitcoin futures contracts trade about $1.4 billion notional amount per day. CoinMarketCap reports that Bitcoin trades about $10 billion per day.


  [4] Obviously lots of US-approved ETFs own, like, European or Asian stocks, but the SEC is probably more impressed by the regulation of foreign stock exchanges than it is by the regulation of offshore crypto exchanges, or US crypto exchanges for that matter.


  [5] Grayscale reports a market price of $17.58 per share as of yesterday’s close, versus “holdings/share” of $23.41. The discount narrowed significantly today on news of the court decision discussed lower down in the text.


  [6] Actually I think that nobody involved in any Bitcoin ETF is all that worried about fraud and manipulation in the Bitcoin market — they just want to provide exposure to Bitcoin prices, manipulated or not, and figure that the Bitcoin market is big enough now not to be too manipulated — and this is just a regulatory box to check. But everyone checks it the same way, and the SEC finds that acceptable for some ETFs and not others.


  [7] Well, bribes and travel agency fees. A lot of that $1 million didn’t really go to the clients in the form of bribery/tourism but was wasted on travel agents and running educational activities that the clients didn’t go to.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cjdlug.5imt/acf14dc3.gif" alt="" border="0" /></a>
