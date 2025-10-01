# Money Stuff: Wells Fargo Is in Trouble Again

**Source**: inputs/saved_emails/Money Stuff Wells Fargo Is in Trouble Again_Wed,_21_Dec_2022_13-57-52_-0500_(EST)_185360d7497d9647.eml
**Type**: email
**Created**: 2025-08-25T02:54:01.489092

---

I think often about the time I wrote:If you have U.S. dollars in a bank account at JPMorgan Chase & Co., and I have U.S. dollars in a bank a
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Oh Wells Fargo
    
  

I   think often about the time   I wrote:
If you have U.S. dollars in a bank account at JPMorgan Chase & Co., and I have U.S. dollars in a bank account at JPMorgan Chase & Co., and I want to send you 100 of my dollars, what we do is I tell JPMorgan to subtract 100 from the number of dollars in my bank account and add 100 to the number of dollars in your bank account. This gets dressed up in a lot of procedures, because it would be bad if JPMorgan got the math wrong or if it moved money from one account to another without getting the proper authorizations, but as a matter of, like, computer science, it is dead easy. JPMorgan keeps a list of people and how many dollars they have, and you and I both trust JPMorgan to keep that list (that’s what it means that we bank there!), and so we just tell JPMorgan to update the list to reflect the transaction between us.
And lots of  computer engineers tweeted and emailed to be like “no, actually, it is a hard problem of computer science to have a big database of who has what, and to update it instantly and reliably to reflect transactions from many different sources.” And I was like, sure, fine, I guess. I still feel like I was entitled to be right: A bank is, at its heart, a computer for keeping track of who has money, and for updating its ledger as people send and receive money. And at a high level you and I could describe how we’d expect that computer to work — “if I deposit $100 in an ATM, the bank will increase the number in my account by $100,” that sort of thing — and we will be disappointed if it doesn’t work that way, if the bank loses track of who has the money or how much they have, or if it doesn’t update its ledger promptly or process transactions in the right order. If the bank messes up and says “look I am sorry but keeping track of money is a hard job and you can’t expect us to do it with 100% accuracy,” we will say things like “yes we can” and “that is literally exactly what we expect of you” and “if keeping track of the money is too hard for you then maybe you should not be a bank” and “now you have to pay an enormous fine.” And yet, sure, empirically, banks do sometimes mess it up. It’s not as easy as it sounds.
Wells Fargo, for instance, messes it up a lot:
The Consumer Financial Protection Bureau (CFPB) is ordering Wells Fargo Bank to pay more than $2 billion in redress to consumers and a $1.7 billion civil penalty for legal violations across several of its largest product lines. The bank’s illegal conduct led to billions of dollars in financial harm to its customers and, for thousands of customers, the loss of their vehicles and homes. Consumers were illegally assessed fees and interest charges on auto and mortgage loans, had their cars wrongly repossessed, and had payments to auto and mortgage loans misapplied by the bank. Wells Fargo also charged consumers unlawful surprise overdraft fees and applied other incorrect charges to checking and savings accounts. Under the terms of the order, Wells Fargo will pay redress to the over 16 million affected consumer accounts, and pay a $1.7 billion fine, which will go to the CFPB's Civil Penalty Fund, where it will be used to provide relief to victims of consumer financial law violations.
Here is the CFPB’s  consent order from yesterday, which is basically just a litany of “Wells Fargo’s computers messed up.” For instance:
Respondent also assessed borrowers erroneous fees and interest because of technology, audit, and compliance failures. As an example, from at least 2011 until at least March 2019, Respondent sometimes incorrectly entered the effective date of a payment deferment in, or omitted it from, its servicing system-of-record, which resulted in $26.5 million in erroneously assessed late fees to more than 688,000 borrower accounts.
If you owe Wells Fargo money on a car loan, and you don’t pay it, and you have a payment deferment, they won’t charge you a fee, but if you don’t have a payment deferment they will. But if you have a payment deferment, but they don’t write it down in the right place, they will also charge you the fee, and then they will get in trouble. In some sense this is profit-maximizing behavior by Wells Fargo: If they agree to defer payments, and then charge you the fees anyway, they will make more money in fees. But it doesn’t seem intentional, and the CFPB doesn’t think it was. (Why say you agree to the deferment, and then charge the fees?) It seems like a failure of systems, of “technology, audit and compliance”: Wells Fargo did not do a good job of keeping track of deferments, so it sometimes charged fees by mistake. 
Or:
From at least 2011 through 2022, Respondent experienced other types of servicing errors, which had the potential to contribute to a borrower’s delinquency, and in some cases led to improper repossessions. For example, Respondent repossessed vehicles despite the borrower having made a payment or entering into an agreement to forestall the repossession.
If you are delinquent on a car loan to Wells Fargo, eventually some system at Wells Fargo decides to repossess your car. There is some delay between when this system sets the repossession in motion and when someone actually takes the car. In the meantime, if you make a payment, or sign an agreement with some other person at Wells Fargo to avoid repossession, then some other system at Wells Fargo knows that Wells Fargo should not repossess your car. Do those systems talk to each other? Does the person signing the agreement, or the mailbox receiving your payment, have a way to stop the repossession that is lurching into motion? Meh, sometimes, maybe, but not all the time.
Again, this does not seem like rational profit-maximizing behavior by Wells Fargo; repossessing the car is surely more of a pain than having the borrower start making payments again. No one at Wells Fargo was like “bwahahaha, a clever trick would be to repossess people’s cars even after they start paying their loans back.” Wells Fargo just did it anyway. It is an emergent feature of Wells Fargo’s bureaucracy, and its computers.
Or:
Guaranteed Asset Protection (GAP) contracts are a type of debt cancellation contract (DCC) that generally relieve the borrower from the obligation to pay the remaining amount of the borrower’s loan on the vehicle above the vehicle’s depreciated value in the case of a major accident or theft. The auto dealer markets GAP coverage to the borrower and is paid the GAP fee. However, borrowers often finance GAP fees as part of their auto loan at origination and the GAP contract becomes part of the auto loan contract. If the borrower pays off the loan early, or the GAP contract otherwise terminates, the borrower may be entitled to a refund of the unearned portion of the GAP fee that they financed when first buying the vehicle. Such refund obligations usually are governed by the terms of the GAP contract executed between the borrower and the originating dealer, with GAP contracts sometimes requiring that the borrower make a written request to the originating dealer for a GAP refund. Respondent, as the owner and servicer of the GAP contracts, did not ensure that unearned GAP fees were refunded to all borrowers who paid off their loans early.
That is just, like, Wells Fargo entered into a complicated contract with its auto-loan borrowers, and the contract provided that in certain circumstances, years in the future, Wells Fargo would have to send some money to the borrowers, and Wells Fargo just stuck the contract in a drawer somewhere and ignored it, and so did the borrowers, so it never sent them the money. Very understandable, for the borrowers, who are busy people who have jobs and lives and are not necessarily reading every word of their auto-loan contracts. Less understandable, for the bank, which is a bank.
Or:
Another error occurred from July 2013 until September 2018, when Respondent did not offer no-application modifications to approximately 190 borrowers with Government Sponsored Entity (GSE) loans. Respondent erroneously identified these borrowers as deceased and therefore did not assess their eligibility for modifications. Respondent is paying approximately $2.4 million in remediation to these borrowers.
It is a little hard to tell how that one would work? Like, the rule is something like “certain mortgage borrowers need to be offered this loan modification.” Wells Fargo went through its records to see who needed to be offered the modification, and decided not to offer it to these 190 people because they were dead. They were not dead, so, a failure of record-keeping by Wells Fargo. But also … they were not offered the modification, so they kept paying their mortgages?
  [1]
 Like every month Wells Fargo would get a check from these people whom it had erroneously identified as deceased? If you got a check every month from someone who you thought was dead, you would be surprised, and presumably you would update your views. (You might think “aha, they are not dead,” or you might think “wow ghosts are real and very financially responsible,” or you might call them to say “so are you dead or what?”) But Wells Fargo is not a human with normal human intuitions. It is a big bureaucratic institution with databases that don’t necessarily talk to each other in sensible ways, and it blithely went along cashing checks from people while also believing they were dead. 
Here are CFPB Director Rohit Chopra’s  remarks on the enforcement action:

In the CFPB’s eleven years of existence, Wells Fargo has consistently been one of the most problematic repeat offenders of the banks and credit unions we supervise. … 
Put simply, Wells Fargo is a corporate recidivist that puts one third of American households at risk of harm. Finding a permanent resolution to this bank’s pattern of unlawful behavior is a top priority. Today, CFPB is announcing an important step toward that goal: restitution for victims of Wells Fargo’s widespread illegal activities. …
While today’s order addresses a number of consumer abuses, it should not be read as a sign that Wells Fargo has moved past its longstanding problems or that the CFPB’s work here is done. Importantly, the order does not provide immunity for any individuals, nor, for example, does it release claims for any ongoing illegal acts or practices.
While $3.7 billion may sound like a lot, the CFPB recognizes that this alone will not fix Wells Fargo’s fundamental problems. Over the past several years, Wells Fargo executives have taken steps to fix longstanding problems, but it is also clear that they are not making rapid progress. We are concerned that the bank’s product launches, growth initiatives, and other efforts to increase profits have delayed needed reform.

Imagine being the sort of person who gets ahead in banking and becomes a senior executive at Wells Fargo. One of your subordinates comes to you to be like “I have an idea for a new product that will attract a lot of customers and bring in a lot of revenue.” Another one of your subordinates comes to you to be like “sometimes we charge people late fees even after agreeing not to, because our systems don’t talk to each other very well; I have an idea for how to modernize them to make sure that doesn’t happen. It will cost a lot of money, but in exchange we, uh, won’t get to charge as many late fees?” Which subordinate would you want to spend more time with? Who sounds like more fun?

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Oh Elon
    
  

Look it has been a weird few years. In February 2021, during meme-stock mania, I coined   the Elon Markets Hypothesis,   the idea that “the way finance works now is that things are valuable not based on their cash flows but on their proximity to Elon Musk”:
Musk is the richest person in the world, and in a dynamic, fun, traveling-to-Mars sort of way. It makes sense that his pronouncements have a certain religious character, that his tweets can endow arbitrary objects with mana. If the richest person in the world tweets “Gamestonk!” then I think that means that, if you buy GameStop stock, you will partake in his wealth and dynamism at a remove; you will get rich and have fun doing it. (Not! Investing! Advice!) Maybe that is not how it works on a conscious level—though I think that sometimes it is?—but surely at some subconscious level people want to order their lives in accordance with the cryptic instructions of a charismatic flying zillionaire.
Now, uh, things are different? Tesla Inc., Musk’s main company, was worth as much as $1.2 trillion at the start of this year; it’s now worth about $440 billion, and Musk is no longer the richest person in the world. One possibility — one that sort of fits within the spirit of the Elon Markets Hypothesis — is that Elon Musk no longer seems all that dynamic or fun or even interested in traveling to Mars; now he spends all his time moderating a niche internet message board and getting in fights with posters, and absolutely no one aspires to that.
Another possibility is that this entire hypothesis was (1) stupid or (2) a low-interest-rates phenomenon. When capital is cheap and plentiful and a dollar in the distant future is worth as much as a dollar today, the guy who promises robot taxis and Mars colonies can easily create value with a tweet. When it isn’t, he can’t.
On Twitter this weekend, investor Ross Gerber complained that Tesla’s stock isn’t doing that well, and  Musk replied:

Go back and read your old Securities Analysis 101 textbook
In simple terms: As bank savings account interest rates, which are guaranteed, start to approach stock market returns, which are *not* guaranteed, people will increasingly move their money out of stocks into cash, thus causing stocks to drop.

People quickly  pointed out that in fact rates have gone down, and competitors’ stocks have gone up, since Musk closed his deal to buy Twitter Inc., even as Tesla’s stock has plunged; Tesla is down because of Musk, not rates. Still it is interesting to see Musk endorsing Securities Analysis 101. Less than two years ago, it looked like Musk might have transcended Securities Analysis 101. If Musk’s businesses are valued based on the expected value of their future cash flows then that’s fine, I guess, but it is a disappointment. Tesla is apparently worth $440 billion based on its cash flows; it was worth $1.2 billion based on the Elon Markets Hypothesis.
Anyway Musk does seem to be pretty full time at Twitter, though he has said that   he will step down as chief executive officer as soon as he can find a replacement CEO. That is a hard position to fill; I   summed it up the other day by saying:
So the proposition is … what? You take all of your money, you give it to Musk to buy equity in his company at a price that you all agree is absurd? And then you get to work for him, running a sullen and broken Twitter according to his ever-shifting whims, until he changes his mind and fires you? And when he fires you he denies you severance and dares you to sue, and accuses you of being a sex criminal? 
But it’s actually a little worse than that, because, as CEO, not only will you answer to Musk (as the owner of Twitter), but you’ll also be his boss. He  tweeted yesterday: “I will resign as CEO as soon as I find someone foolish enough to take the job! After that, I will just run the software & servers teams.” So … like … if you are Twitter’s “CEO,” and you meet with your senior executives and decide that you need to update the software to attract advertisers or to comply with the law, what do you do? You walk down to the hardcore software-engineering floor, tiptoe into Musk’s nap room, shake him gently to wake him up, and say “Elon sir here is my software request”? And then he looks at it and says “what is this woke mind virus nonsense, never!” and runs out to yell at his engineers to build more   Twitter polling analytics tools so he can have a more fine-tuned sense of which Twitter users love him and how much? What are we doing here? Musk is going to hire a CEO of a software company, but the CEO won’t be in charge of the software? 
Also if you are a Tesla shareholder, the thing that you are mad about is that the CEO of Tesla is now working long hours as the CEO of Twitter, and I am not sure that you will be happier to learn that the CEO of Tesla will instead work long hours as a senior manager at Twitter? Like, I mean, at Tesla, the people who make the cars seem to have important jobs, while the CEO can apparently be absent for months at a time without impacting production too much. (Impacting the stock price, sure.) You could imagine Musk being CEO of Twitter as a part-time job, the way it is at Tesla, where he tweets a lot and makes some policy decisions but is not in the weeds of every engineering decision. But, no, he is in the weeds of every engineering decision, and wants to continue that even after he steps down as CEO.
Also if Musk does a bad job as head of software and servers, can the new CEO fire him? To be clear I would never, ever, ever want to be CEO of Twitter — even before Musk took it over, and certainly not after — but wouldn’t it be a little tempting to be CEO just so you could fire Musk? Like obviously he would then fire you, more or less immediately; you are both his boss (you’re the CEO and he is the head of a division) and his employee (you’re a manager and he’s the majority shareholder). But you’d have, like, 15 minutes. You could order security to escort him out of the building; you could put out a press release; you could tweet from the official account “Elon has been fired for not being hardcore enough,   let that sink out.” Oh then he’d fire you and deny you severance and call you a sex criminal; your life would be horrible forever. But for a minute it would be very funny.

  
    
      
        
      
    
  


  
    
      Not now, Coinbase
    
  

After the collapse of FTX, what is the path forward for crypto regulation? I have no idea! The basic situation in the US is that regulators — mainly, the US Securities and Exchange Commission — are  pretty hostile to  crypto, and if a crypto exchange comes to the regulators and says “how can I set up a full-service, innovative, but regulatorily compliant crypto exchange for US customers” the regulators will say “I’m so glad you came in, welcome,” and then  throw them in a dungeon. After FTX, you could have two views of that approach:
	If US regulators had been more accommodating, more crypto trading would have moved to US-regulated exchanges that were transparent, audited, and carefully supervised by US regulators, and the result would have been that FTX would not have lost billions of dollars of customer money. Or:	If US regulators had been more accommodating, crypto exchanges like FTX would have had a lot more access to US customers, and would have lost a lot more of their money.

I think both of those views probably have some merits, but the overall tone of the discussion these days favors the second. Last month FT Alphaville published an influential op-ed from Stephen Cecchetti and Kim Schoenholtz titled “Let crypto burn”:

In the aftermath of the collapse of FTX, authorities should resist the urge to create a parallel legal and regulatory framework for the crypto industry. It is far better to do nothing, and just let crypto burn.
Actively intervening would convey undeserved legitimacy upon a system that does little to support real economic activity. It also would provide an official seal of approval to a system that currently poses no threat to financial stability and would lead to calls for public bailouts when crypto inevitably erupts again. …
Attempts to create a separate structure for regulating and supervising crypto will just make the financial system less, not more, safe.
This is true for two reasons. First, it will encourage banks both to purchase crypto assets and to lend against them as collateral, making the banking system vulnerable to plunging market values. In contrast, even the ongoing collapse of crypto values and institutions has had virtually no impact on the wellbeing of the traditional financial markets and firms.
Second, new rules would lead to a migration of financial activity from traditional finance to the still less regulated, but newly sanctioned, crypto world.

It does not help that Sam Bankman-Fried, FTX’s now-imprisoned founder, was one of the leading advocates, on Capitol Hill and at regulatory agencies, for clear and comprehensive US regulation of crypto. FTX held itself out as a regulator-friendly crypto exchange, one that was interested in working with US authorities to find a way to do its business in the US in a compliant way. And then it turned out to be stealing customer money, oops. The authorities have been burned. It is much less appealing now than it was three months ago for a regulator or congressperson to take smiling photographs with crypto exchange operators, or to put out announcements about how they are working with those operators to bring sensible common-sense regulation to crypto. 
Anyway here’s a blog post from Brian Armstrong, the founder of Coinbase Global Inc., on “Regulating Crypto: How we move forward as an industry from here.” It is, frankly, on its merits, not at all written to appeal to actual US regulators. Armstrong’s proposals include:
	Congress passing a law saying that most crypto tokens are not securities — “If the primary purpose of the crypto asset is some other form of utility (voting, governance, incentivizing actions of a community, etc) then it is very unlikely to be considered a security” — and so not subject to the jurisdiction of the SEC. The SEC  very strongly disagrees with this premise.	Making all of decentralized finance and smart contracts immune from regulation: “Creating decentralized protocols ... should be equivalent to publishing open source code, which is protected by freedom of speech in the U.S. … The role of financial regulators should be limited to centralized actors in cryptocurrency, where additional transparency and disclosure is needed. In an on-chain world, this transparency is built in by default, and we have an opportunity to create even stronger protections. With the internet, we got better regulation through Uber's star ratings system than we had with taxi medallions. Crypto has the potential to take this idea even further, by encoding trust on-chain in a cryptographically provable way.”

If Coinbase had proposed these things three months ago they would have seemed like a wild libertarian crypto-maximalist wish list. But then FTX collapsed! Nobody wants to hear this stuff now. It is fine for people in crypto to say “the collapse of FTX, a centralized exchange, proves that DeFi is the future,” but imagine a congressperson, now, saying “I have met with the CEO of a crypto exchange and decided that encoding trust on-chain is good enough for me, so I am proposing a law forbidding the SEC from regulating decentralized crypto exchanges.” 

  
    
      Taxi front-running
    
  

I  don’t know, man:
At all times relevant to this Indictment, taxi drivers who sought to pick up a fare at JFK were required to wait in a holding lot at JFK before being dispatched to a specific terminal by the Dispatch System. Taxi drivers were frequently required to wait several hours in the lot before being dispatched to a terminal, and were dispatched in approximately the order in which they arrived at the holding lot.
Doesn’t that sound bad? If you drive a taxi and want to pick up a customer at John F. Kennedy International Airport, you have to wait several hours in a holding lot first? Wasting time that you could be spending, you know, driving your cab for money? Wouldn’t it be better if JFK had a dispatch system that let cabs go directly to the terminal and pick up customers? Like, instead of waiting in the dispatch lot until you are needed, you just keep driving fares around until you’re needed, and then you go right to the terminal? Like if there were a system for matching supply and demand in real time, instead of keeping lots of cabs idle in a parking lot? 
So two enterprising Queens men, Daniel Abayev and Peter Leyman, “with the help of Russian hackers,”  allegedly fixed the system:

At various times between November 2019 and November 2020, ABAYEV and LEYMAN, working with others, successfully hacked the Dispatch System.  They used their unauthorized access to alter the Dispatch System and move specific taxis to the front of the line, thereby allowing drivers of those taxis to skip other taxi drivers waiting in the line.  ABAYEV and LEYMAN charged taxi drivers $10 each time they were advanced to the front of the line.  Taxi drivers learned that they could skip the taxi line by paying $10 to members of the Hacking Scheme through word of mouth, and members of the Hacking Scheme offered some taxi drivers waivers of the $10 fee in exchange for recruiting other taxi drivers to pay the $10 fee to skip the taxi line.  The Hacking Scheme also used large group chat threads in order to communicate with taxi drivers.  For example, when the Hacking Scheme had access to the Dispatch System for the day, a member of the Hacking Scheme would message the group chat threads, “Shop open.” …
ABAYEV and LEYMAN’s scheme resulted in large numbers of taxi drivers skipping the taxi line.  Over the course of the scheme, they enabled as many as 1,000 fraudulently expedited taxi trips a day.

“I know that the Pentagon is being hacked[.].  So, can’t we hack the taxi industry[?],” Abayev allegedly texted one of the Russian hackers, before they actually did. Like, fine, fine, you’re not supposed to hack the dispatch system, they were stealing the money, sure. But surely it was worth $10 to these drivers to skip a multi-hour wait for a fare? Arrest these guys, fine, but shouldn’t JFK be copying their idea? 

  
    
      Things happen
    
  

Palantir’s SPAC Bets Backfire, Hitting Company’s Growth. FTX clients to  vie for priority payouts in US bankruptcy case. FTX Wants to  Claw Back Sam Bankman-Fried’s Donations. Sam Bankman-Fried to   Fly to US Wednesday, Escorted by FBI Agents. FTX Claims Are Luring Some Big Players in the Distressed Market. Core Scientific   Declares Bankruptcy as Crypto Winter Lingers. Citadel, Other  Hedge-Fund Winners in 2022 to Return Some Profits to Clients. Short Seller  Carson Block Sues the SEC. Some Turkish Banks Are Now Literally   Giving Out Free Money. The   Golden Age of Cocaine Is Happening Right Now. 
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] To be fair it’s entirely possible that they were *not* paying their mortgages, that they were supposed to be offered a modification to enable them to pay or defer their mortgages, and that Wells Fargo thought they were dead because they weren’t paying. But eventually they must have paid something, which is why Wells Fargo has to pay them remediation averaging $12,600 each. Like if Wells Fargo was just not in contact with them at all then it is hard to see how it could have harmed them; the harm is taking their money, which is a weird thing to do if you thought they were dead.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23chw1bz.5l16/746b4e37.gif" alt="" border="0" /></a>