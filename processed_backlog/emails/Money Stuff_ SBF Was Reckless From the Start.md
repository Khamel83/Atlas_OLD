# Money Stuff: SBF Was Reckless From the Start

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Wed, 4 Oct 2023 13:02:55 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff SBF Was Reckless From the Start_Wed,_4_Oct_2023_13-02-55_-0400_(EDT)_18afba5fc06128a9.eml
**Processed:** 2025-08-24T19:13:11.157641



  
  
    
      
        
      
    
  
  
    
      
        I am about halfway through Going Infinite, Michael Lewis’ book about Sam Bankman-Fried, and I am very much enjoying it. Many of the reviews 
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      SBF Stuff
    
  

I am about halfway through Going Infinite, Michael Lewis’ book about Sam Bankman-Fried, and I am very much enjoying it.  Many of the  reviews that I have read of the book complain that Lewis does not sufficiently explain that Bankman-Fried is Guilty and Bad, Actually, but that is not the book that he wanted to write or the one I want to read.
  [1]
 He wanted to understand and explain Bankman-Fried’s psychology and tell a good story. If you want to read a moral condemnation of crypto theft, you can get that anywhere. You go to Michael Lewis for character and story.
Also, reading those reviews you would think that the book is a defense of Bankman-Fried, but it is actually quite damning. (Less damning than most of what is written about Bankman-Fried these days? Sure.) There is an anecdote (which has been reported before) from the early days of Alameda Research, the crypto trading firm that Bankman-Fried started before his crypto exchange FTX, the firm whose trades with FTX customer money ultimately brought down the whole thing. At some point Alameda lost track of $4 million of investor money, and the rest of the management team was like “huh we should tell our investors that we lost their money,” and Bankman-Fried was like “nah it’s fine, we’ll probably find it again, let’s just tell them it’s still here.” The rest of the management team was horrified and quit in a huff, loudly telling the investors that Bankman-Fried was dishonest and reckless.
And then Alameda eventually did find the money and it was fine. The lesson that Bankman-Fried, and everyone else who stayed at Alameda, seems to have taken from this episode was something like “Bankman-Fried is infallible, and it’s fine if he takes wild risks and does fraud because it always works out in the end.” I wonder how that approach will play out in the second half of the book!
There is another strange anecdote from Bankman-Fried’s even earlier days, as an intern at Jane Street Capital, the proprietary trading firm.
  [2]
 Jane Street wants to teach its interns to think in bets, so they are encouraged to bet against each other all the time. To prevent disaster, there is a rule that no intern can lose more than $100 in a day.
  [3]
 One morning, another intern, called “Asher” in the book, offers to bet Bankman-Fried on the maximum amount any intern will lose that day. “This cannot settle above one hundred or below zero, right?” confirms Bankman-Fried. And then he buys at 65: If any intern loses more than $65 that day, Bankman-Fried will pay Asher that intern’s losses above $65; if none do, Asher will pay Bankman-Fried the difference between $65 and the maximum loss. If an intern loses $100, the maximum, then Bankman-Fried gets $35. If the biggest loser loses only $50, he pays Asher $15.
Of course Bankman-Fried can easily win this bet by losing $100 himself. That is not optimal, for him, but he can use that fact to manufacture a good trade. He immediately turns to the other interns in the room and offers them $1 to take an even-money coin flip for $98. Somebody (Bankman-Fried or his counterparty) will lose $98 on this bet, so Asher will have to pay him $33 ($98 minus $65). If Bankman-Fried wins, he gets $98 (from winning the coin flip), plus $33 (from Asher), minus $1 (he paid the other intern a premium to do the coin flip), for a net gain of $130.
  [4]
 If he loses, he loses $98 (coin flip) plus $1 (payment) but gets back $33 (Asher), for a net loss of $66.
  [5]
 That’s a very positive-expected-value bet for him: Bankman-Fried has a 50/50 chance of winning $130 or losing only $66. But it’s also positive-expected-value for his counterparty on the coin flip. Lewis writes:
To the Jane Street way of thinking, Sam was offering free money. A Jane Street intern had what amounted to a professional obligation to take any bet with a positive expected value. The coin toss itself was a 50-50 proposition, and so the expected value to the person who accepted Sam’s bet was a dollar: (0.5 x $98) - (0.5 x $98) + $1 = $1.
Bankman-Fried easily saw how to manufacture the bad outcome for Asher. This is a key skill in trading, but especially in crypto trading. “Asher was now clearly deeply embarrassed.”
Bankman-Fried finds a taker, wins the coin toss and collects $98 from the other intern. Then he goes again:

To maximize Asher’s pain, some intern needed to lose one hundred dollars.
I’ll pay a dollar to anyone who will flip me for ninety-nine dollars, Sam shouted.
Now he had a machine for creating wagers in which both parties enjoyed positive expected value. That machine was named Asher. Interns were lined up to take the bet. “People get so obsessed with free dollars when you frame it correctly,” said Sam. … “If I’d have spent the rest of the internship flipping that coin, I’d have been satisfied.” And for a while it appeared that he might, as he won the second coin flip too.
I’ll pay a dollar to anyone who will flip me for ninety-nine fifty, shouted Sam.
The other interns clearly felt obligated to take the bets, but the mood in the room was shifting in response to Asher’s feelings. … But Sam won the third coin flip too, so to his way of thinking the gambling wasn’t yet over.
I’ll pay a dollar to anyone who’ll flip me for ninety-nine seventy-five, he shouted.
It wasn’t until the fourth flip that Sam lost — and by then everyone except Sam was unsettled by Asher’s humiliation.

The point of this story in the book is that Bankman-Fried gets in trouble with his bosses for being mean to Asher, which he thinks is unfair: “What he’d done to Asher was no more than what Jane Street was doing to competitors in financial markets every day.”
But there are two much weirder things in this anecdote.
First: “A Jane Street intern had what amounted to a professional obligation to take any bet with a positive expected value”? Really? I feel like, if you are a trading intern, you are really there to learn two things. One is, sure, take bets with positive expected value and avoid bets with negative expected value.
But the other is about bet sizing. As a Jane Street intern, you have $100 to bet each day, and your quasi-job is to turn that into as much money as possible. Is betting all of it (or even $98) on a single bet with a 1% edge really optimal?
  [6]
 
People have thought about this question! Like, this is very much a central thing that traders and trading firms worry about. The standard starting point is the  Kelly criterion, which computes a maximum bet size based on your edge and the size of your bankroll. Given the intern’s bankroll of $100, I think Kelly would tell you to put at most $10 on this bet, depending on what exactly you mean by “this bet.”
  [7]
 Betting $98 is too much.
I am being imprecise, and for various reasons you might not expect the interns to stick to Kelly in this situation. But when I read about interns lining up to lose their entire bankroll on bets with 1% edge, I think, “huh, that’s aggressive, what are they teaching those interns?” (I suppose the $100 daily loss limit is the real lesson about position sizing: The interns who wipe out today get to come back and play again tomorrow.) 
But I also think about a Twitter argument that Bankman-Fried had with Matt Hollerbach in 2020, in which Bankman-Fried scoffed at the Kelly criterion and said that “I, personally, would do more” than the Kelly amount. “Why? Because ultimately my utility function isn’t really logarithmic. It’s closer to linear.” As he tells Lewis, “he had use for ‘infinity dollars’” — he was going to become a trillionaire and use the money to cure disease and align AI and defeat Trump, sure — so he always wanted to maximize returns.
But as Hollerbach pointed out, this misunderstands why trading firms use the Kelly criterion.
  [8]
 Jane Street does not go around taking any bet with a positive expected value. The point of Kelly is not about utility curves; it’s not “having $200 is less than twice as pleasant as having $100, so you should be less willing to take big risks for big rewards.” The point of Kelly is about maximizing your chances of surviving and obtaining long-run returns: It’s “if you bet 50% of your bankroll on 1%-edge bets, you’ll be more likely to win each bet than lose it, but if you keep doing that you will probably lose all your money eventually.” Kelly is about sizing your bets so you can keep playing the game and make the most money possible in the long run. Betting more can make you more money in the short run, but if you keep doing it you will end in ruin.
I don’t know what actually happened at Jane Street that day. I assume that the anecdote in Going Infinite comes from Bankman-Fried. “People get so obsessed with free dollars when you frame it correctly,” he says; he is the one framing this story. What I take from this story, and from other anecdotes here about his early trading career, is that Bankman-Fried is good and facile and clever at calculating expected value, and at finding ways to inflict pain on counterparties, but he is … not even bad at trade sizing; he just doesn’t think about it at all. It is not a part of his life. He goes all in on everything. In his model of the world, if you are offered a bet with a 1% edge, you should put all of your money on it, over and over again, until you lose everything. How will that play out in the second half of the book?
Here’s the other weird thing about the anecdote: These bets obviously have negative expected value?
Not for his counterparties, who get paid $1 to take a fair coin flip, but for Bankman-Fried. And not the first one; that one is fine; the math above is right. He pays $1 to play, he gets a fair coin flip, he makes $33 from Asher, fine, good trade. But then he keeps going to eke out a few marginal pennies from Asher.
  [9]
 When he wins the first flip, Asher owes him $33, the difference between their $65 strike price and the $98 that the first intern lost. When he wins the second coin flip, Asher owes him an additional one dollar: Their bet is on the maximum loss, not the total loss, so finding another intern to lose $99 increases the payoff by only $1.
  [10]
 The second flip is an even-money proposition for Bankman-Fried: He pays $1 to do it and gets an extra $1 from Asher. The third and fourth flips, where he pays $1 to get 50 and then 25 cents from Asher, have negative expected value. The last flip, which he loses, costs him $100.75 and brings in nothing.
  [11]

Again, I don’t really know what happened. Perhaps I have misunderstood how the bets worked, or perhaps Lewis did, or perhaps Bankman-Fried misremembered, or perhaps he really did get these bets wrong. But isn’t this version of the story revealing? In this story:
	Bankman-Fried found a perfect trade, for him: It was risky but it had a lot of edge, it made him look smart, and it made his counterparty look dumb.	He did it, it paid off, he looked smart, his counterparty looked dumb, all was right with the world.	It was so intoxicating to be right that he kept doing the trade.	He never noticed that the trade stopped being good: The glow of being right persisted long after he became wrong.	Eventually he lost the bet and everyone was mad at him.

Everything about Sam Bankman-Fried’s life was perfectly optimized for becoming a famous billionaire and an infamous criminal defendant, in that order. 

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      SEC silly season
    
  

I made some dumb jokes   yesterday about how the US Securities and Exchange Commission sure brings a lot of enforcement actions just before the end of its fiscal year (Sept. 30), to pad its numbers for the year. I compared this to “earnings management” and “window dressing” for public companies, which are frowned upon, by the SEC, when companies do them.
On that note, readers pointed out two things. One is that there is of course a literature. Here’s a recent paper by Dain C. Donelson, Matthew Kubic and Sara Toynbee on “ The SEC’s September Spike: Regulatory Inconsistency within the Fiscal Year”:
We examine whether performance reporting leads to inconsistent enforcement at the Securities and Exchange Commission (SEC). In a sample of over 13,000 SEC enforcement actions, we show that SEC staff respond to performance-reporting pressures and file more enforcement actions in September, the final month of the SEC’s fiscal year, than in any other month. The increase in case volume in September is not fully explained by staff filing more procedural cases or accelerating case filings. Instead, SEC staff pursue less complex cases and agree to more lenient financial and non-financial sanctions to increase case volume in September. We attempt to rule out alternative explanations for our results, including natural SEC workflow and resource constraints. Overall, our findings suggest that performance reporting creates agency conflicts that lead to regulatory inconsistency within the fiscal year.
The idea is that the SEC’s performance is measured, and its budget set, based on the number of cases filed in the previous fiscal year:
The SEC receives its funding from Congress and must submit a budget justification report as part of the appropriations process (see, e.g., SEC, 2020b). Consistent with the Government Performance and Results Act of 1993’s objective of ensuring regulatory effectiveness, the budget justification report outlines the SEC’s proposed allocations of requested funds, actual outlays from the prior year, and a summary of performance for the most recent fiscal year. The most prominent performance metric in both the SEC’s annual reports and the budget justification reports is the number of cases filed (see SEC, 2018, 2019, 2020a). The number of case filings also receives attention in congressional testimony and from the press.
And so the SEC has incentives to maximize that number, and to cram cases into the end of the fiscal year. One way to cram in cases is by settling. Defendants know this, though, and they can use it to their advantage: They can drag their feet on cases early in the year, and then drive a hard bargain in September because they know the SEC is desperate to settle.

We find that defendants receive lower financial sanctions—both disgorgement and civil penalties—when they settle in September. On average, our results suggest the SEC discounts financial sanctions for cases filed as settled charges in September by approximately $132,000—an economically meaningful discount, given that the average financial sanction is $270,000. We also find an 11% lower likelihood of a large financial sanction in September.
Our evidence suggests that SEC staff compromise in settlement negotiations in order to file cases before the fiscal year-end. This predictable leniency has important practical implications. The revolving door between SEC enforcement and industry likely increases defendants’ awareness of the pressure on the SEC at the fiscal year-end (deHaan et al. 2015), and such awareness may incentivize them to delay settlement negotiations to obtain more favorable outcomes.

The other point is that, while we talked yesterday about a bunch of the year-end enforcement actions that the SEC brought last week, we didn’t discuss all of them. Embarrassingly, one that I missed was  about earnings management:

The Securities and Exchange Commission [Friday] charged Newell Brands Inc., a Georgia-based consumer products company and its former CEO, Michael Polk, with misleading investors about Newell’s core sales growth, a non-GAAP (Generally Accepted Accounting Principles) financial measure the company used to explain its underlying sales trends. Both parties agreed to settle the SEC charges.
The SEC’s order finds that, in 2016 and 2017, Newell and Polk took actions that increased the company’s publicly disclosed core sales growth in ways that were out of step with Newell’s actual but undisclosed sales trends, allowing the company to announce “strong” or “solid” results in quarters it internally described as disappointing due to shortfalls in sales. According to the order, Newell pulled sales forward into earlier quarters without adequate disclosure and engaged in accounting practices that were inconsistent with GAAP, while overriding its internal accounting controls. Collectively, these measures gave the misleading appearance that Newell had achieved core sales growth in line with its targets and deprived investors of information relevant to an accurate and complete understanding of Newell’s actual sales trends. 

Don’t want to pull sales forward into earlier quarters!

  
    
      Bonds
    
  

One psychological difference between stocks and bonds is that people buy stocks largely for capital appreciation and they buy bonds largely for yield. So if you look at a stock and see that it was $10 yesterday and is $15 today, you will think “ah this stock is good at appreciating capitally” and buy it. And if you look at a bond and see that it yielded 4% yesterday and yields 5% today, you will think “ah this bond is getting yieldier” and buy it. These are somewhat inverse thought processes. (Bond prices move inversely to yields, you know.) Bonds get more attractive as they get cheaper; stocks get more attractive as they get more expensive.
Oh, I kid, I kid, none of this is totally true, and you can always find Warren Buffett or whoever going around like “I love to buy stocks when they are on sale.” Still as a crude model of retail investor psychology this seems plausible? There are meme stocks, because everyone loves to pile into a stock that has gone up. There are not meme bonds.
Bond yields more or less never went up during my lifetime, but now they have, and on this crude model people should be rushing to buy bonds.  And yet:

Asset managers have been counting on what BlackRock calls a “generational opportunity” in the bond market, now that yields are at decade-plus highs. 
Investors ranging from pension funds to retirement savers should be buying longer-term bonds to lock in higher rates, their thinking goes, spurring a flood of inflows to bond funds. BlackRock, for one, has projected assets under management at its bond exchange-traded funds to triple to $2.5 trillion by 2030.
There is just one problem: Those flows have yet to materialize. Relentless losses in the bond market have spooked investors who appear hesitant to jump in until they feel more confident that rates have peaked. 
Investors pulled $78.6 billion from U.S.-based taxable bond funds in the 12 months through August, according to Morningstar. That is well below the nearly $300 billion they pulled from equities over the same period but a painful sum, regardless, for asset managers hoping for a windfall.

Also here’s a good stock-style quote about bonds being “on sale”:
“When you’re in an environment where bond yields go up every day, it starts getting a little nasty,” said Steve Sosnick, chief strategist at Interactive Brokers. “I don’t see people rushing in to buy bonds right now just because they’re kind of a falling knife. They’re on sale and lower prices should create demand, but we’re not seeing that.”

  
    
      Nessie
    
  

A tension in antitrust law is:
	It is illegal for two companies to get together and agree “we won’t cut our price below $10 if you won’t.” That is a classic conspiracy in restraint of trade.	If the two companies just independently decide to price their thing at $10, that’s fine,  that’s just competition. But in practice, two companies selling the same thing are probably going to sell it for around the same price. Also in most cases it’s not like the prices are secret. So if you monitor your competitors’ prices, and set your price where they set theirs, that’s probably fine. (Not legal advice!) 	These things are not so different? If your competitor calls you up and says “our price is $10, is yours also $10?” and you say “sure $10 is good” then you are conspiring. If your competitor just puts out a sign saying “our price is $10” and you drive by and see the sign and put up your own sign saying “our price is $10,” then you are competing. But the content of those two things is kind of the same?

So the US Federal Trade Commission has  this question and answer on its website:

Q: Our company monitors competitors' ads, and we sometimes offer to match special discounts or sales incentives for consumers. Is this a problem?
A: No. Matching competitors' pricing may be good business, and occurs often in highly competitive markets. Each company is free to set its own prices, and it may charge the same price as its competitors as long as the decision was not based on any agreement or coordination with a competitor.

But if you are monitoring their prices and they are monitoring your prices and you are always responding to each other, that might not be “agreement,” but is it “coordination”? The better you get at monitoring and unilaterally predicting their prices, the more it might look, to the naked eye, like coordination. Guess who’s  really good at it?

Amazon.com used an algorithm code-named “Project Nessie” to test how much it could raise prices in a way that competitors would follow, according to redacted portions of the Federal Trade Commission’s monopoly lawsuit against the company.
The algorithm helped Amazon improve its profit on items across shopping categories, and because of the power the company has in e-commerce, led competitors to raise their prices and charge customers more, according to people familiar with the allegations in the complaint. In instances where competitors didn’t raise their prices to Amazon’s level, the algorithm—which is no longer in use—automatically returned the item to its normal price point.


  
    
      Money laundering
    
  

The basic idea is that, if you are doing crime, you are probably getting paid in cash or in cryptocurrency or in, like, someone else’s bank account. If you do crime quite successfully, you will have a lot of cash or cryptocurrency or tainted bank money. You will want to turn that cash or crypto into some more convenient and usable and legitimate-seeming form of wealth: money in a clean bank account, most of all, but stocks and bonds and real estate and art can also work. The law is aware of this, and there are anti-money-laundering rules in most places that basically tell banks — but also crypto exchanges and stockbrokers and real estate agents and art dealers — “if someone comes to you with an enormous sack of cash, or crypto, or a wire transfer from North Korea, maybe ask some questions about where it came from and report it to the authorities.” 
On the other hand if you do crime and have sacks of cash and take some cash out of a sack and go to a deli to get a sandwich and pay cash, the deli will not report you to anyone. You can’t really launder your money through sandwiches. 
There is some intermediate zone between “sandwiches” and “Central Park South penthouses” where, you know, you could be laundering money, or you could just carry around a lot of cash and want to spend it. It is a line-drawing exercise, and sometimes the line moves:

Singapore may subject luxury assets, including cars, watches and handbags, to anti-money laundering controls and increase scrutiny of single family offices as the Asian financial hub reels from a S$2.8bn (US$2bn) money-laundering scandal.
In response to questions in parliament on Tuesday about the probe, Singapore’s government said it would examine extending anti-money laundering requirements, such as tough know-your-customer due diligence checks, to high-value assets including vehicles, handbags and alcohol. Such items are not currently regulated, unlike precious stones or metals.

If you have ill-gotten money, you might park it in diamonds, so if you walk into a diamond dealer they will ask you “is this money ill-gotten?” Or you might park it in, like, Pappy Van Winkle. The liquor store will not necessarily ask you “is this money ill-gotten?” before selling you a bottle, but maybe they should.

  
    
      Things happen
    
  

The 4 Billion   Pieces of Paper Keeping Global Trade Afloat.   Reverse-Mortgage Lawsuit Claims Feds Reneged on Loan Promises. Blackstone funds legal action over  soured Bain Capital deal. SoftBank’s Son Says Artificial General Intelligence Will Soon  Surpass Humans.   Tech IPOs Could Burn Firms Who Bought Into Hot Startups Too Late.   Steve Cohen’s Mets Flop While Orioles Win With New Breed of Moneyball. You Can Now Invest in  ‘Shrek’ Music Rights the Same Place You Buy Stocks. “ Plogging—a sport that combines running with trash collecting.”
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] Several reviews recommend my Bloomberg colleague Zeke Faux’s crypto book, “Number Go Up,” which I endorse. Faux’s book is great, and hilarious, and morally scathing, and also way more skeptical about crypto and Bankman-Fried than Lewis is.


  [2] An awkward aspect of this book is that, with Bankman-Fried as the protagonist and Jane Street as his formative trading experience, Lewis portrays Jane Street in a very admiring way. But of course Lewis also wrote “Flash Boys.” This necessitates a funny footnote on page 64, in which Lewis basically says “I know that I wrote a whole book where the premise was that high-frequency traders are Bad, but for purposes of *this* book they are Good.” (Or, at least, those *other* HFT firms are Bad, but Jane Street is Good.)


  [3] I assume that this is operationalized as like “you cannot have more than $100 of independent exposure out at one time, and if you have lost $X in a day then you can’t have more than $(100 - X) of exposure out for the rest of the day.” Note that in the anecdote we are going to discuss, Bankman-Fried has $65 of exposure on his initial bet and $98 of exposure on his coin flip, both of them unresolved, but of course they are not independent: If he wins *or* loses the coin flip, he wins $33 on his initial bet; there is no way for him to lose both bets. There’s, like, a portfolio margining concept for the intern bets.


  [4] That is how Lewis does the math. I think technically the other intern lost $97, though? He lost $98 on the flip but got paid $1 to take it, so his net payoff is negative $97? So Asher should pay Bankman-Fried $32? It depends on whether you think the $1 payment is part of the bet, but I think it clearly is.


  [5] Again I think technically Bankman-Fried has lost $99 so the side bet should pay $34, but whatever. Also I suppose there is an argument that you should net the $33 (or $34) from Asher against his losses here, leaving him with losses of only $65, and thus making Asher the winner of the bet? But if you do that then he doesn't have the $33, so his losses are $98, so he does win the bet? Very paradoxical.


  [6] I am being a little inaccurate here, because $100 is not *really* the intern’s entire bankroll. Jane Street interns are well paid and can probably afford to lose $100 in a day, and if they do then they can come back tomorrow with a fresh $100. Your job is to maximize returns (or learning, or whatever) over the whole summer, not over any one day. So it is plausible to think that your $100 is, you know, 1/60th of your bankroll or whatever, and so it’s not so bad to bet $100 on a 1%-edge bet. (It is more than Kelly however.) If you do that each day, you will in expectation end up with a profit of $60 for the summer. (You win $101 30 times, and you lose $99 30 times.) That’s … not … great? 


  [7] I am taking some liberties here in specifying what the bet is. What I mean in the text is: If you are offered a flat $1 to take an even-money coin-flip bet, and your bankroll is $100, and you can set the size of the bet, then $10 is the number that roughly works in the Kelly math. The Kelly proportion of your bankroll to bet is (probability of win - (probability of loss / payoff)), where “payoff” is the proportion of the bet that you get back on a win (even money is 1.0). With a $10 bet, you lose $9 if you lose and win $11 if you win (due to the extra dollar payment), making this “really” a $9 bet from your perspective, and (0.5 - (0.5/(11/9)) = 0.09, and 9% of your bankroll is $9 (which is a $10 bet with the extra $1). This is counterfactual, though; Bankman-Fried did not offer $1 to bet $10, and there are other ways to specify the counterfactual bet. If you just do Kelly on like “coin flip with 1% edge” (that is, 50.5% chance of winning 100% and 49.5% chance of losing 100%), it would tell you to bet 1% of your bankroll, or $1.


  [8] Here is a blog post with more about Bankman-Fried’s odd interpretation of bet sizing. “With Kelly we aren't really making any assumptions about utility function: our assumption is effectively that the median is the correct expectations operator.”


  [9] Why did he not just start with a $100 bet? (Or $99, I guess, if his $1 payment counts against his own maximum loss.)


  [10] Also, what if Bankman-Fried loses that toss? He goes from positive $98 from the first flip to negative $1 after the second, or really negative $3 if you include the premiums he paid. He's not the biggest loser; the biggest loser is still the guy who lost $98. So Asher doesn't owe him any more money.


  [11] See the previous footnote: Asher doesn't owe him the extra 25 cents because he's still up on the day. Actually he's still up a lot, and it is plausible that his utility curve was such that a chance of inflicting 25 cents more pain on Asher was worth losing $100.75 of house money for him. But! That’s weird!


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cjlo5l.648g/37c7a782.gif" alt="" border="0" /></a>
