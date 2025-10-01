# Money Stuff: Two Sigma Had a Rogue Calibrator

**Source**: inputs/saved_emails/Money Stuff Two Sigma Had a Rogue Calibrator_Mon,_30_Oct_2023_14-44-06_-0400_(EDT)_18b81e68cc442c5a.eml
**Type**: email
**Created**: 2025-08-25T02:54:00.697167

---

One possibly relevant fact here is that $450 million is more than $170 million? A researcher at Two Sigma Investments adjusted the hedge fun
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Two Sigma
    
  

One possibly relevant fact here is that $450 million is more than $170 million?

A researcher at Two Sigma Investments adjusted the hedge fund’s investing models without authorization, the firm has told clients, leading to losses in some funds, big gains in others and fresh regulatory scrutiny.
The researcher, Jian Wu, a senior vice president at New York-based Two Sigma, was trying to boost his compensation, Two Sigma has told clients, without identifying Wu. He made changes over the past year that resulted in a total of $620 million in unexpected gains and losses, according to people close to the matter and investor letters. Two Sigma has placed Wu on administrative leave.
The Securities and Exchange Commission is examining the matter. …
Wu’s changes led to gains of $450 million in total for some Two Sigma funds—including those in which the firm’s own executives and employees invest, as well as those available to clients. But they also led to a total of $170 million in losses for other funds compared with how they otherwise would have fared—losses largely borne by clients. Two Sigma has made them whole.
People familiar with the situation said Wu was trying to improve the firm’s performance, which would have benefited his career and potential pay.

I mean: Presumably everyone at Two Sigma is trying to improve the firm’s performance, because that would benefit their careers and potential pay? Like, what else are they coming to work for? If you find a tweak to the model that causes some of your funds to reliably make an extra $450 million, while causing some other funds to reliably lose $170 million, then that’s good. Like:
	Ideally, you go and make the tweak to the model for the funds it would help, and leave the model for the other funds alone.	Or if you can’t do that for some reason, then I guess you make the tweak to the model for everyone, and have the benefited funds write a $171 million check to the harmed funds, leaving everyone better off.

I just think that if you tweak the model in such a way that clients make an extra $280 million, net, then that is broadly speaking good work and you might reasonably expect your bonus to go up.
I am kidding, I guess. It’s not that simple. Presumably whatever the guy did did not reliably improve performance; presumably it improved performance over some period but at the cost of higher risk. That Wall Street Journal story adds:
Two Sigma’s top executives this summer became aware of Wu’s changes because they resulted in higher than expected correlations between some of the firm’s trading models. The trail pointed to Wu, who made the changes in two stages over the past year.
If you are in the business of maximizing risk-adjusted returns — or uncorrelated returns — then sometimes higher returns are a leading indicator of trouble.
More generally, there are a lot of stories in finance about rogue traders. Often the story is:
	Some trader would like a bigger bonus.	She does some trades that she is not supposed to do, trades with higher risk (but also higher upside) than her firm wants.	The trades work, she makes money, everyone is pleased.	Eventually the risks come true, she loses more money than she made, everyone is mad and she gets in trouble.

There are variations. One surprisingly popular variation omits Step 3: Some rogue traders lose money pretty much from the beginning, so they keep doubling down. It is widely believed that another popular variation omits Step 4, but you rarely hear about those: A rogue trader who consistently makes money stops being a “rogue” trader and becomes a star trader. (“Sorry I did some trades I wasn’t supposed to, but they all made money,” she eventually tells her bosses, and they say “that’s okay you lovable scamp, here’s a big bonus.”) It is possible that in a modern age of strict risk controls, heavy regulation and careful performance attribution, that approach no longer works the way it used to. But you still don’t hear about a ton of rogue traders who uniformly make money.
Anyway this story (a version of which was  previously reported by Bloomberg News) isn’t that. It’s an alleged rogue-model-updater, or I guess rogue-model-calibrator:

In a letter to clients, Two Sigma described the activity as “intentional misconduct” that violated the firm’s internal procedures. One person close to the situation disputed the firm’s characterization, saying Wu adjusted how Two Sigma’s models were calibrated but didn’t alter the models themselves. Calibration changes can be seen as more routine than a major change to the models.
Big firms such as Two Sigma usually closely monitor and are fully aware of all important changes to its trading models. “In well-run firms, all changes—calibrations or model changes—are governed by procedures so that they must be disclosed and approved by the proper people,” said Aaron Brown, a veteran quant who wasn’t aware of Two Sigma’s situation.

I suppose this is the modern form of rogue trading: If you work at a systematic quantitative firm like Two Sigma, and you go off and do some unauthorized trades, they are going to catch you pretty quick because you’re not supposed to go off and do any trades. The computer tells you what trades to do; only trades blessed by the computer can get done. If you want to be a rogue trader, you have to be a systemic quantitative rogue trader; you have to put rogue signals into the model instead of trading on them yourself. If you want to do rogue trades, you have to rogue calibrate the model so that the computer can tell you to do the trades you want to do.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      VMWare
    
  

Ages ago, in May 2022, VMware Inc.  signed a deal to be acquired by Broadcom Inc. The deal was for half cash, half stock, and VMware shareholders  could choose to take either $142.50 in cash or 0.2520 shares of Broadcom per VMware share. The day before the announcement, Broadcom’s stock closed at $531.63, making the stock consideration worth about $133.97 and the cash a better deal. Last week, Broadcom closed at $838.36, making the stock consideration worth about $211.27 and a much better deal.
But Broadcom only agreed to pay half the consideration in cash: If everyone chooses stock (as you’d expect), then they all get prorated and end up with half cash and half stock. (That is, roughly, $71.25 in cash and $105.63 worth of stock.) Or if almost everyone chooses stock, but some people choose cash, then the cash people get all cash and the stock people get a little bit more than half stock. And if you don’t choose at all, you get whatever nobody else wants (here, cash).
The merger was supposed to close today, but it didn’t. Broadcom and VMware  put out an announcement today:

Broadcom Inc. (NASDAQ: AVGO) and VMware, Inc. (NYSE: VMW) today announced their expectation that Broadcom’s acquisition of VMware (the “Transaction”) will close soon, but in any event prior to the expiration of their merger agreement.
The parties have received legal merger clearance in Australia, Brazil, Canada, the European Union, Israel, Japan, South Africa, South Korea, Taiwan, the United Kingdom, and foreign investment control clearance in all necessary jurisdictions. There is no legal impediment to closing under U.S. merger regulations.

The missing name there is “China”:   Chinese regulators still have not approved the deal, and it’s not clear if or when they will.
Meanwhile  the deadline for choosing cash or stock was a week ago, and once you chose you were not supposed to sell your stock: “Note that you will not be able to sell or otherwise transfer your shares of VMware common stock after making your election,”  VMware explained. This is, I suppose, for VMware’s and Broadcom’s convenience; they can know in advance how many shares to issue, and to whom. And in fact  their announcement today has the results:

VMware stockholders of record of approximately 96% of the outstanding shares of VMware common stock elected to receive the stock consideration and in accordance with the proration procedures in the parties’ merger agreement, (i) approximately 52.1% of such outstanding shares of VMware common stock will be converted into the right to receive 0.2520 of a share of Broadcom common stock per share of VMware common stock and (ii) approximately 47.9% of such outstanding shares of VMware common stock will be converted into the right to receive $142.50 in cash per share of VMware common stock; and
VMware stockholders of record of approximately 4% of the outstanding shares of VMware common stock elected to receive the cash consideration or did not make a valid election or did not deliver a valid election form prior to the Election Deadline. Each such VMware stockholder will be entitled to receive $142.50 in cash per share of VMware common stock.

That suggests that, if you chose stock, you will get about $110.07 worth of stock (at Friday’s closing price) and $68.26 worth of cash, worth about $178.33 total; if you chose cash (or forgot to fill out the form) you will get $142.50 of cash. But now those shares are locked up in limbo: You can’t sell them, and if you buy any VMware shares they presumably did not make an election and are probably only the $142.50. (If the deal closes.) VMware’s stock price was $155.87 last Monday, before the deadline; it’s $142.03 today.
The risky fun trade was to bet that (1) the deal would be delayed by China and (2) Broadcom and VMware would feel bad about locking up the stock, so they would extend the election deadline. Barron's  reported last week:

There was some curious trading in shares of VMware Tuesday as the stock declined but changed hands above the cash value of the Broadcom offer for the software company.
Investors apparently are betting on the possibility that the stock election period for VMware investors that ended Monday could be extended. 

And the stock traded about 3.4 million shares on Friday, well after the deadline: If you bought at $142.20 on Friday and then got another shot at choosing Broadcom stock, you’d make a quick $36, give or take, if the deal closed. But it seems like neither end of that worked out: The deal has not closed, but it does not look like investors will get another chance to elect stock.

  
    
      Sculptor’s over
    
  

I think? The  situation as of a week ago was that Sculptor Capital Management Inc. had a deal to sell itself to Rithm Capital Corp. for $12 per share, but it had a competing offer from Boaz Weinstein and some of his friends to buy Sculptor for $13.50 per share. Sculptor’s board wanted to stick with Rithm, so it had two options:
	Convince shareholders — and particularly its estranged founder, Dan Och, who still owns a bunch of shares — that Weinstein’s offer is too risky, and that a deal with Weinstein would fall apart because Sculptor’s clients would flee.	Get Rithm to raise its price to $13.51, to outbid Weinstein.

In the event, it split the difference. Last week Sculptor put out its most vehement case that Weinstein’s deal is too risky, with a presentation and additional disclosure arguing that Weinstein would not really close. Sculptor has argued all along that Weinstein’s deal is too risky because it would require consent from Sculptor’s hedge fund clients, and because those clients might say no to Weinstein. Weinstein eventually dropped the consent requirement (for the hedge fund clients), but even so Sculptor worried. “The Consortium was not yet prepared to accept and acknowledge the Consortium-Specific Transaction Risks,” says Sculptor: Essentially, Sculptor wanted Weinstein’s group to sign a merger agreement saying “even if all the clients and employees leave and there’s nothing left for you to buy, you have to buy it anyway,” and Weinstein said no. I don’t know how reasonable an ask that is — surely, in general, if you sign a merger agreement to sell your company, you have some obligation to try to keep your business together until closing? — but it was the sticking point in the negotiations.
  [1]

And then last Friday Sculptor announced a new revised deal with Rithm, which agreed to pay $12.70 per share. The combination was  enough to win over Och:

Sculptor Capital Management Inc. said major shareholder and founder Dan Och and his group agreed to a sweetened deal from Rithm Capital Corp., in what may be the deciding bid for the struggling hedge fund.
Rithm’s amended offer increased the bid to $12.70 a share from $12.00, Sculptor said in a statement Friday. It values Sculptor at about $720 million. ...
Och and his group of former Sculptor executives will throw in their votes — 15% of the outstanding shares — behind the Rithm deal and drop a suit tied to the transaction.

The result is basically that the Rithm deal can probably close by Nov. 17, the day after the scheduled shareholder vote: Och dropped his lawsuit, and between Och, Rithm, and Sculptor’s current managers, almost half of the outstanding shares are committed to vote in favor of the deal. Meanwhile  Sculptor argues that, even if it signed with Weinstein today, “re-starting the clock on regulatory approvals would require up to 6 months,” for a “contingent closing in 2024 following receipt of stockholder, client and regulatory approvals.” It’s plausible that a fairly locked-up $12.70 now is better than a riskier $13.50 in six months. Sculptor’s stock had traded above Rithm’s deal price since Weinstein arrived on the scene, but that ended on Friday, when the stock closed at $12.65, suggesting that shareholders expect the Rithm deal to get done. 
Still it’s not 100%; Bloomberg’s  Katherine Burton and Hema Parmar report:

Weinstein still has a narrow path to victory, if he decides to take it. He could go back to Sculptor with yet another bid, and if the board deems it superior, Och could throw his votes behind the Saba founder.
Alternatively, if a Delaware judge sides with a Sculptor shareholder in a hearing slated for Nov. 9, then Weinstein could stage a tender offer for the hedge fund firm.

But I suspect a lot of people are ready for this to end.


  
    
      Taylor Swift
    
  

I have   written in the past about the oddly discontinuous math of celebrity wealth. There are two ways to measure anyone’s wealth:
	Your wealth is based on your past earnings. Your wealth is the money that you have. You have worked for however many years at your job, you got paid some money each year, you spent some of it on expenses, and what’s left over is your wealth. This is how most people measure their wealth. It’s how I measure my wealth, for instance. I look at my bank account and my investments and add them all up and subtract my debts and that’s my net worth.	Your wealth is based on your future earnings. You have some expected stream of future income, and you can estimate the present value of that income (by doing a discounted cash flow analysis, or just by multiplying it by some reasonable multiple), and that is your wealth today. This is, classically, how startup founders measure their wealth. If you start a company, and you give 75% of the stock to cofounders and investors and employees and keep 25% for yourself, and the expected future earnings of the company are worth $20 billion today, then your net worth is $5 billion. Even if the company has not made a penny yet, even if it loses money every year, even if you take no salary. Your net worth comes from people’s expectations of your future earnings.

Most people use Method 1, and it would be weird for them to try to use Method 2. If you are 22 years old, just out of college, in $200,000 of debt, and starting your first job at an investment bank, you could say “well I will probably go into private equity and make at least $2 million a year for most of the next 40 years, and at a reasonable discount rate, adjusting for the risk of it not working out, that contingent stream of income probably has a present value of about $10 million today; subtract my $200,000 of debt and add the $700 in my bank account and you get a net worth of $9.8007 million, so I am a millionaire.” And you would not really be wrong! And in certain circles you will get a sympathetic ear; some people will say “yes that is an appropriate way to account for your human capital.” But most people will look at you funny.
But   there are ways to switch between methods.
  [2]
 Let’s say you are a doctor in private practice, you make $500,000 per year, and you have $800,000 in the bank. You probably use Method 1, meaning that your wealth is $800,000. But if you sell 10% of your practice to a private equity firm, then (1) they will pay you 10% of the present value of your future earnings and (2) you own the other 90%, which now has a market value. If the private equity firm values your practice at 10 times earnings, then (1) they pay you $500,000 for 10% and (2) the remaining 90% is worth $4.5 million, making you a millionaire. Your net worth increased dramatically — from $800,000 to $5.8 million
  [3]
 — just because someone put a price on your future earnings.
If you are a doctor in private practice and you don’t sell 10% of your practice to a private equity firm, or even go out and get a bid, can you do this same math and say “my practice is worth $5 million so my net worth is $5.8 million”? I mean, I’m not gonna stop you. 
Similarly if you are a working musician and you put your songs on Spotify and you earn $50, you have $50. If you earn $50,000, you have $50,000. But if you earn $50 million, the math changes: Now you have a catalogue of songs worth hundreds of millions of dollars, which is the present value of your expected future earnings. Some music investment firm would probably pay you hundreds of millions of dollars for that catalogue, if you want. Even if you don’t want, Bloomberg will do the math for you and   declare you a billionaire:

Taylor Swift’s Eras tour has generated as much money as the economies of small countries. The movie version is ruling the box office. Her new recording of a nine-year-old album, 1989, is expected to be one of the hottest-selling records of the year. ...
The success of the Eras tour—a Super Bowl-sized event spanning numerous cities that has shattered records, sparked ticket frenzies and even caused the equivalent of a small earthquake—has propelled the pop star’s net worth past $1 billion, according to a Bloomberg News analysis. She’s one of the few entertainers to reach that status based on music and performing alone, the result of work and talent, but also canny marketing and timing.

A lot of the accounting is realized cash earnings (from concerts, streaming, etc.), but $400 million of it is “the estimated value of her music catalog,” based on “a conservative multiple of future royalties.” Also based on comparisons to other artists who have sold their catalogues for nine-digit sums. Swift has not sold her catalogue, but that doesn’t change how the math works. The math is that she has a few hundred million dollars, so she’s a billionaire.

  
    
      SBF Stuff
    
  

Sam Bankman-Fried  testified at his trial on Friday, explaining that the $8 billion of customer money that his crypto exchange FTX Trading lost was all an understandable oopsie. The reviews are … pretty good? Obviously they are all prefaced by “this guy is guilty, but,” but still. “Bankman-Fried’s first full day of testimony probably went as well as could be expected given the weight of the evidence in the prosecution’s case,” says the New York Times. “It was an admirable effort by him and his defense team to present some alternative explanations for some of the more damning incidents that had been raised during the prosecution’s case,”  writes Molly White. Bloomberg News   reports:

Greg Cawthorne, a crypto software engineer traveling from London, arrived around 2:05 a.m. to get a seat in the main courtroom.
“After seeing two days of the trial, I am definitely maybe a little less fully against him,” Cawthorne said. “Now I gotta think maybe there were some more doubts than I thought.”
“Today he seemed almost charismatic - almost, not quite,” Cawthorne said.

It seems like he did a nice job of explaining the bad facts in a way that (1) made him look relatively good but (2) was not too combative. Like he managed to declare his innocence, without quite saying that his former colleagues — who all said he was doing tons of crime — were liars. Just a good-faith difference of opinion. That is not easy! My view is that, just one year ago, Bankman-Fried really was good at getting attention and investors, and in a way that could play well in court: He was not obviously slick and outgoing and charming, but rather had a sort of nebbishy charm that came across as being candid and awkward. No version of charm is going to work that well when you are the defendant in a giant fraud trial, but if your defense is “oops I made a series of bad accidents” then nebbishy awkward oversharing charm is going to come across better than slick charm.
Still, I mean. All those glowing reviews are like “I thought he was 10,000% guilty, but now I only think he’s 99.99% guilty.” And today he is  being cross-examined. I don’t think his efforts will move the betting odds that much. On the other hand, I have always figured that testifying was, for him, basically a zero-risk proposition: If he did not testify he would absolutely be convicted of everything and sentenced to a billion years in prison, whereas if he does testify he has, like, a tiny chance of persuading a juror or two of his innocence. 
The counter-argument to that was that if he testifies, and is obviously lying, and angers the judge, that’s bad: The judge has a lot of discretion in sentencing him, and if he thinks he is lying the sentence will be worse. My view is (1) he was getting a billion years anyway and (2) the apologetic self-effacing defense, and the almost-charisma that impressed Greg Cawthorne, are at least as likely to work with the judge as to offend him.
Elsewhere: “Inside the Vaping, Gambling, and Jeering Wildness of the  SBF Overflow Rooms.” 

  
    
      X Stuff
    
  

Apparently Elon Musk bought Twitter Inc. in 2022 to turn it into … PayPal in 2000?

Elon Musk wants X to be the center of your financial world, handling anything in your life that deals with money. He expects those features to launch by the end of 2024, he told X employees during an all-hands call on Thursday, saying that people will be surprised with “just how powerful it is.”
“When I say payments, I actually mean someone’s entire financial life,” Musk said, according to audio of the meeting obtained by The Verge. “If it involves money. It’ll be on our platform. Money or securities or whatever. So, it’s not just like send $20 to my friend. I’m talking about, like, you won’t need a bank account.” …
The original plan for X.com is clearly on Musk’s mind. “The X/PayPal product roadmap was written by myself and David Sacks actually in July of 2000,” Musk said on Thursday’s internal X call. “And for some reason PayPal, once it became eBay, not only did they not implement the rest of the list, but they actually rolled back a bunch of key features, which is crazy. So PayPal is actually a less complete product than what we came up with in July of 2000, so 23 years ago.”

Imagine if Twitter/X becomes the center of the financial world by the end of next year. The joke will really be on me. 
Also I still do not understand why Elon Musk spent $44 billion to buy Twitter to turn it into Vintage Paypal? Why not buy … I mean literally PayPal Holdings Inc. has an equity market capitalization of about $56 billion today; that’s more than $44 billion, but it also has earnings before interest, taxes depreciation and amortization of more than $5 billion a year, so he could probably have gotten some banks to lend him more of the money. Robinhood Markets Inc. has an $8 billion market capitalization and a meme-y audience of people who already trust it with their money, which is just extremely not true of Twitter. There are financial technology startups that are positively cheap! Or you can start one! Buying Twitter to (1) get rid of its employees, (2) get rid of its name and branding and (3) pivot to payments seems bizarrely profligate.

  
    
      Things happen
    
  

The Hunt for Crypto’s  Most Famous Fugitive. People are worried about   Bitcoin market liquidity. The Big Bond Market Event   Wednesday Is at Treasury, Not the Fed. ‘ Buy the Dip’ Investing Mantra Lives On—in the Bond Market at Least. Inside the War Between  Square and Cash App at Dorsey’s Block.  Peltz’s Push for Disney Board Seats Boosted by Perlmutter’s Shares. Middle-Class Americans Are   Rattled by Fed’s Fight Against Inflation. BlackRock warns investor  disdain for mining threatens green transition. The Mortgage Market Is So Bad Lenders Want Ex-Employees to  Give Back Their Bonuses. How Saudi Arabia’s   Wealth Fund and MBS Aim to Build a Post-Oil Future. Nigeria Plans   New FX Rules in Hopes of Naira Reaching ‘Fair Price’ by End of 2023. Law firms under pressure to make more women partners.   Rolex Trolls Omega With Deal to Buy Home of Arch-Rival's Flagship Store. “When managers  use humor on an earnings call, stock market returns and analyst forecast revisions following the call are more positive, primarily because of a muted response to negative earnings news.” Naked Professional Baritone Opera Singer Tasered In Lytham. Happy birthday to dogs.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] The new disclosure also explains why Sculptor   never let Weinstein speak to its clients to *ask* if they would consent: “Meetings between the Consortium and the Company’s clients could be highly disruptive and potentially cause clients to redeem their investments even prior to the Consortium executing a definitive agreement with the Company, causing damage that would reduce the likelihood of closing the Transactions with Rithm,” and “No other bidder involved in the sale process (including Rithm) had been permitted to speak with any of the Company’s clients,” and “Certain members of the Consortium operate businesses that are competitive with elements of the Company’s business, and allowing the Consortium to speak to the Company’s clients could cause competitive harm if a deal were not ultimately reached with the Consortium.”


  [2] Overwhelmingly, people would rather be richer, so the normal move is to try to switch from Method 1 to Method 2. But we did   talk last year about Yvon Chouinard, the owner of Patagonia, who tried to switch from Method 2 to Method 1. He didn’t like being called a billionaire (“I was in Forbes magazine listed as a billionaire, which really, really pissed me off. … I don’t have $1 billion in the bank. I don’t drive Lexuses.”), so he gave away his Patagonia ownership.


  [3] I am ignoring taxes here. In fact Method 2 is generally more tax-efficient than Method 1: For taxes, it’s generally better to own a business than to get paid for labor.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cjrh1z.62on/c8e5bd8f.gif" alt="" border="0" /></a>