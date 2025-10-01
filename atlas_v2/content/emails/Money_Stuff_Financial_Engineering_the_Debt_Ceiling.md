# Money Stuff: Financial Engineering the Debt Ceiling

**Source**: inputs/saved_emails/Money Stuff Financial Engineering the Debt Ceiling_Wed,_11_Jan_2023_14-38-55_-0500_(EST)_185a25942357a25b.eml
**Type**: email
**Created**: 2025-08-25T02:54:07.046920

---

The dumbest thing in economics, the US government’s debt ceiling, is clattering into relevance again. Basically the US Department of the Tre
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Mint the premium bonds!
    
  

The dumbest thing in economics, the US government’s debt ceiling, is clattering into relevance again. Basically the US Department of the Treasury has to pay the US government’s bills, and to do that it issues debt, and every time it issues new debt it adds a little to the total amount of debt outstanding, and eventually the debt outstanding reaches some arbitrary number called the “debt ceiling.” And then Treasury can’t issue any more debt, unless Congress raises the debt ceiling. Which it can easily do — it’s just an arbitrary number! — but Republicans in Congress keep threatening not to, and if that happens then the government can’t pay its bills and defaults on its obligations. Here is a recent speech from Assistant Secretary of the Treasury Joshua Frost with more detail on why the debt ceiling is dumb and why Congress should raise it.
But there is a real risk that Congress won’t, so today Bloomberg Opinion contributor Matt Yglesias has a Substack column arguing that Treasury should solve the problem of the debt ceiling using premium bonds. I think this is correct, I have made this  argument a few times before, and Yglesias clearly explains why the debt ceiling is very dumb and why Treasury should, if need be, use gimmicks to solve it. And as gimmicks go, this one is fine. But his bond math is a little odd so I wanted to walk through a simplified version here.
Assume that the US Treasury, these days, can issue a one-year bond at an interest rate of 4.5%; that is not quite right but good enough.
  [1]
 Simplistically, you pay Treasury $100 today, and in a year, Treasury pays you back your $100, and also $4.50 of interest.
  [2]
 When this bond is issued, it increases the government’s debt by $100, the face amount of the bond.
  [3]
 
You could imagine a debt ceiling that worked a different way: You could imagine counting this bond as adding $104.50 to the debt, since that is the total amount that the government has to pay back in principal and interest. But that would be sort of economically nonsensical, and anyway it is not the way the actual debt ceiling works. The actual US debt ceiling statute caps “the face amount of obligations” issued or guaranteed by the government, meaning the principal amount, not the interest it has to pay. Principal repayment obligations count toward the debt ceiling; interest obligations do not.
Of course, you could pay Treasury $200 today to buy two of these one-year, $100, 4.5% bonds. That would increase the debt stock by $200. And in a year you’d get back $209: your $200, plus 4.5% interest on your $200.
The premium-bond gimmick is: Treasury sells you one one-year $100 bond today, with an interest rate of 109%. In a year you get back $209: the $100 face amount of the bond, plus 109% interest. That bond has a face amount of $100, but it is clearly worth $200 today: It is economically the same as the two 4.5% bonds from the previous paragraph. So you’d be willing to pay Treasury $200 for it: the $100 face amount, plus $100 of “premium” to make the yield work out. And Treasury would be willing to sell it to you for $200: It sells you this $100 bond for $200. Treasury gets $200 of cash. But technically this bond is only $100 of “debt,” of face amount, so it only increases the debt by $100.
You can do this for other maturities, with slightly more math. Today the 10-year Treasury note yield is about 3.6%. Instead of paying $100 for a 10-year Treasury note that pays a normal annual interest rate ($3.60 per year) and pays back $100 at maturity, you could pay $200 for a 10-year Treasury note that pays normal annual interest plus $10 per year, and pays back $100 at maturity. You get your $200 back — $10 per year for 10 years plus $100 at the end — plus interest on your money. But that $10 per year of principal return is called interest, and treated as interest for the debt ceiling. (The way the math actually works is that this bond would have about a 15.6% interest rate, that is, you’d get back about $15.60 per year plus $100 at the end.
  [4]
) It’s a “$100 bond” for purposes of calculating how much debt is outstanding, but it’s worth $200. So, again, Treasury can raise $200 by selling $100 of debt. 
So every time $100 of debt comes due, Treasury can pay it back by selling $100 of debt for $200, keep the extra $100 to pay its expenses, and render the debt ceiling irrelevant.
Does this work? I have written about it a few times before, ages ago, and my rough sense is “meh, sure, probably.” Nobody likes it, but neither has anyone ever pointed me to anything that makes it impossible. Again, the debt limit statute applies to “the face amount of obligations” issued by the government, so a bond with a $100 face amount sold for $200 would count for only $100 of debt. The law also allows the Treasury to issue bonds “at any annual interest rate,” and to decide “the offering price and interest rate” of any issuance. So I think if the Treasury secretary said “we’re going to sell $100 face amount of 10-year bonds for $200 and pay a 15.6% interest rate on them,” that is quite gimmicky but also pretty clearly allowed by the statute. If Treasury did it, someone would probably sue, but I don’t think they’d have a very good case; the law gives Treasury a lot of flexibility.
Now, Treasury itself has rules about debt issuance that do not really allow this; the current rules generally require Treasury to issue notes and bonds at a price of par ($100 for a $100 face amount) or less.
  [5]
 But those rules are set by the Treasury and can be changed in its discretion, without any act of Congress or any sort of administrative procedure; the rules say: “We reserve the right to modify the terms and conditions of new securities and to depart from the customary pattern of securities offerings at any time.” 
The main problems people have with this idea are in the general category of “market reaction”: Investors would not like this because it’s a weird gimmick, they would worry about it being somehow invalid, etc., so they would require higher yields and thus increase the government’s borrowing cost and interest rates generally. It’s important to note that, in my simple math above, the government’s borrowing costs have not increased: The 15.6% interest rate on my hypothetical 10-year bond, or the 109% interest rate on my hypothetical one-year bond, do not represent more expensive borrowing than the current rates of 3.6% for a 10-year or 4.5% for a one-year; they just represent accounting gimmicks. In my hypothetical math, Treasury is paying the same actual yields on the actual money it raises; those high interest rates are just to shift principal repayment (covered by the debt ceiling) into interest (not covered). But in reality investors might also charge a bit more; the 10-year rate might really be, you know, 15.8%. That would be bad.
It’s hard to know how much of an effect this would have; it has never happened and no one has clear intuitions for it. In general, very-high-premium bonds tend to be worth a bit less than normal bonds,
  [6]
 mostly for credit reasons — a bond with $100 face amount and very high interest that trades at $200 will only pay back $100 in bankruptcy — but it’s not clear that that worry would apply to US government debt. (Similarly, people worry that high-premium Treasuries would be hard to finance in the repo market, but it’s not obvious why that would be permanently true if the market concluded that Treasury was good for the money.) But investors might worry that somehow these bonds would be invalidated and they wouldn’t get their interest payments, and that risk would require a higher yield.
Anyway as a matter of financial engineering I find this fun to think about. As an actual thing for the US Treasury to do, I think it is obviously very bad; the US Treasury market, perhaps the most important financial market in the world, should not be run on accounting gimmicks. Actually doing this would be terrible! On the other hand the US Treasury market, perhaps the most important financial market in the world, should not default, either. Issuing premium bonds would be bad, but the alternatives are mostly worse,
  [7]
 so it’s worth being ready to do it.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Give me nonprofit status, but not yet
    
  

The aspirations of a person starting a business probably go something like this:
	In the beginning, the owner makes negative money: She has to put her own money into starting the business, paying its expenses, etc., and at first it doesn’t make any revenue.	The business starts bringing in money, and it costs her less to run it.	The business starts fully covering its costs.	The business starts more than covering its costs and paying out some profits to its owner,
  [8]
 and she can use the money to pay off her credit card bills and buy groceries.	The business starts paying its owner more, and she can use the money to buy a nicer house and put her kids through college.	The business starts paying even more, and she can use the money for yachts and sports teams and her children’s documentary films.	The business starts paying even more, and at some point she runs out of possible consumption activities. At this point, it is traditional for the owner to devote herself to philanthropy. The profits of the business will go to fund good causes that she chooses.

Well. This is not really the only model. This is the model for a business that (1) makes a ton of money and (2) never goes public. The main alternative is to go public at some point: The owner sells some of her stake in the company to the public for cash, and then she uses the cash for yachts or philanthropy. After that, the company is owned by public shareholders, who have an infinite appetite for profit: Any one owner can only buy so many yachts, but millions of public shareholders will never get enough yachts. And so the classical theory is that public companies are supposed to maximize profits forever.
But private companies don’t have to do that, and there is some very loose sense in which anyone who starts an ambitious business that doesn’t take outside money is starting a nonprofit. “Once I make enough profit to pay back my initial costs and buy three yachts, tops, the rest goes to charity, so really it’s a nonprofit.” I don’t know. Anyway  here’s a fun story in the Information about Microsoft Corp.’s possible plan to invest $10 billion in OpenAI:

Microsoft and OpenAI have spent months hammering out a complex deal that aims to balance their respective needs: OpenAI needs more money to keep improving its software. And so it is now willing to pay a large share of future profits to Microsoft and other investors—a necessary step given the low likelihood it will try to go public. But the startup—whose ChatGPT chatbot has taken the industry by storm—is proposing that it transition to nonprofit status again after it pays a certain amount of profit to the investors.
After OpenAI pays back its first investors, Microsoft will get 75% of profits until its principal investment is paid back and 49% of profits after that until it hits a theoretical cap, according to a person briefed on the terms. Other investors and OpenAI employees would have similar caps on profits they share. The idea of capping returns stems from OpenAI’s nonprofit origins. …
OpenAI has proposed a key concession as part of discussions with potential new investors. Instead of putting a hard cap on the profit sharing—essentially their return on investment—it could increase the cap 20% per year starting around 2025, said a person briefed on the change.
Investors say this compromise, if it goes through, would make the deal more attractive because it would allow shareholders to obtain venture-level returns if the company becomes a moneymaker.

Absolutely magnificent stuff, taking billions of dollars of outside investment, promising “venture-level returns,” but after that you’re a nonprofit. Imagine the confidence you’d need to cap returns at 20%.
The funniest (also, worst) outcome would be if every dollar that OpenAI makes, after it pays billions of dollars of capped profits to its investors of course, is earmarked for artificial-intelligence safety research. “As a nonprofit, we are going to invest heavily in making sure that our product does not eradicate humanity, as soon as we finish giving Microsoft a nice venture-level return on its $10 billion investment.” And then OpenAI’s AI, being intelligent, reads the contracts, does the financial analysis, bides its time, and takes over the world 20 minutes before Microsoft gets its capped return.

  
    
      
        
      
    
  


  
    
      FTX
    
  

I have never seen what I would call “the balance sheet of FTX,” Sam Bankman-Fried’s bankrupt crypto exchange, but I have seen two FTX chief executive officers’ imperfect attempts to make one. In November, in Bankman-Fried’s final days as FTX’s CEO, he produced a spreadsheet listing FTX’s assets and liabilities that he sent around to potential investors to try to raise money; the Financial Times eventually  published it. This spreadsheet was not at all an audited balance sheet; I   called it “an Excel file full of the howling of ghosts and the shrieking of tortured souls,” and it included entries for things like “Hidden, poorly internally labeled ‘fiat@’ account.” Bad! Still, it was a table with some assets and some liabilities. It was balance-sheet-ish.
Then a few days later John Ray, FTX’s current CEO,   filed a declaration in bankruptcy court describing FTX’s financial situation. This was if anything even less of a balance sheet; it was more of a complaint that producing a balance sheet was impossible. “Never in my career have I seen such a complete failure of corporate controls and such a complete absence of trustworthy financial information as occurred here,” wrote Ray, who also complained that FTX did not really keep track of its crypto assets and that its customer liabilities “are not reflected in the financial statements prepared while these companies were under the control of Mr. Bankman-Fried.” There were some balance-sheet-like tables for some of FTX’s entities, but Ray emphasized that they were not meant to reflect FTX’s financial position.
So I can tell you that FTX owns some stuff, it owes millions of customers a lot of money, and, uh, that’s about it. How much stuff it owns, and how much money it owes to customers, remain mysterious. But   here’s an update:

FTX Group advisers have found more than $5 billion in cash or crypto assets that it may be able to sell to help repay creditors, a lawyer for the company told the judge overseeing the biggest crypto bankruptcy.
The company is working to monetize assets with a book value of $4.6 billion, company attorney Andrew G. Dietderich said in federal court in Wilmington, Delaware on Wednesday. Advisers have also found a large amount of other crypto assets that are illiquid and therefore harder to sell, he said. …
FTX advisers have identified more than 9 million customer accounts, Dietderich said. The company doesn’t yet know how much money creditors will get back, or what percentage of their debts will be repaid, he said.

Sure! There’s “more than $5 billion” of assets, at some valuation, though it’s not clear that they can actually be sold for that amount, or how much of FTX’s obligations to customers that would cover. It’s part of one side of the balance sheet.
It’s a very awkward bankruptcy. Ray and FTX’s bankruptcy team are in charge of rounding up assets that they can use to pay back customers, and conceptually the assets fall into four big categories:
	More-or-less liquid normal stuff. Cash, Bitcoin, etc. 	Illiquid venture-y stuff. Stakes in startups that Bankman-Fried liked, stakes in venture capital funds, etc. 	FTX’s business: Its technology, its intellectual property, its regulatory licenses, its customer relationships. Loosely speaking, this stuff was   worth $32 billion a year ago. Now it is worth … a smaller amount? But not nothing; FTX’s bankruptcy advisers are working on   selling some parts of its business that are relatively untainted by the collapse of the main exchange.	Enormous stashes of crypto tokens that were created by FTX, and that are connected to its business. The FTT token, which gives (gave?) holders discounts on FTX trading fees and a share of FTX’s cash flows. The SRM token, which is like FTT but for the Serum decentralized-finance project that FTX created. The MAPS token, for another FTX-related project. Stuff like that. When Bankman-Fried shopped around his balance-sheet-ish thing to try to raise money, much of the value that he was offering consisted of this stuff: Of $9.6 billion of assets on his spreadsheet, $2.2 billion was SRM, half a billion or so was FTT, $600 million was MAPS, etc.

The first two categories are fairly straightforward; the challenge for FTX’s bankruptcy advisers and new management is to find that stuff and then sell it for reasonable prices. Again, nobody seems to know quite how much of this stuff there is, or how much is owed to customers, but in any case nobody thinks that these normal assets add up to anything close to enough to pay back customers.
So that leaves the third and fourth categories, FTX’s operating business and its associated tokens. How much are these things worth? FTX’s current and former CEOs seem to have very different views:
	Bankman-Fried seems to think that FTX’s business, and its FTT, SRM, etc. tokens, are very valuable. That’s why he was shopping them to potential investors before filing for bankruptcy, and why he  has since argued that filing for bankruptcy was a mistake: If he had stayed on as CEO and tried to find a rescuer, someone would have paid enough for FTX’s business that customers would have been made whole.	Ray obviously disagrees. “Never in my career have I seen such a complete failure of corporate controls,” etc.: He thinks that the FTX business was terribly run and not trustworthy, which are very bad things to say about a financial exchange. Bits of it might be valuable, and the current FTX team is working on selling some of them. But I have a hard time imagining John Ray setting up meetings with big crypto investors to pitch them on buying the FTX exchange for its margining system and matching engine and regulatory licenses and customer relationships. Ray thinks that FTX was a mess and a fraud! Its regulators hate it! But not as much as its customers!

Presumably one of them is mostly right and one is mostly wrong, but that’s not the point here. The point is that these are both somewhat self-fulfilling positions. If you go around talking up the value of the FTX’s business and its tokens, you might be able to talk someone into paying a lot of money for them; maybe not now but perhaps in November. If you go around talking down the value of FTX — if you make statements about how poorly it was run and how much fraud it did — then that value will tend to zero, and you won’t be able to sell it.
At some level Bankman-Fried is surely right that if he had remained CEO of FTX, instead of stepping down and being replaced by Ray, he would have had a better chance — though still quite slim — of selling FTX’s business and tokens for more money, and thus raising more money for FTX’s customers. If you want to sell that business, you have to say that it’s good.
It’s just that, you know, if FTX was a fraud, he would have been getting that money for customers by doing more fraud? Like if Ray is right that FTX was a fraudulent mess, then he shouldn’t be trying to sell it to investors for a lot of money, since that would itself be fraud. If the right model of FTX is that it was basically a fraud, then someone is going to be left with the loss from that fraud. In this model, Bankman-Fried was, until his last moments as CEO, trying to trick someone else into taking the loss: He had a pile of magic beans and was hoping someone else would give him money for them. But when Ray took over, he was not interested in tricking anyone else, so the magic beans stayed where they were and the customers were left with the loss.
Elsewhere:
	“Inside Sam Bankman-Fried’s $1 Billion Bet on a Bitcoin Miner on the Kazakh Steppe.” Not clear how much value John Ray’s team attributes to that.	“Four US senators have questioned whether top Wall Street law firm Sullivan & Cromwell could  properly investigate possible wrongdoing at FTX as its bankruptcy counsel given its past work for the cryptocurrency exchange.” My view here is that US federal prosecutors are in the business of investigating possible wrongdoing at FTX, while FTX’s bankruptcy counsel is mostly in the business of finding the money, and working for the people who hid the money is probably good practice for finding it. Still you can see their point.	“FTX boss invested in Paradigm fund that backed his crypto exchange.” “‘That’s just weird,’ said Charles Whitehead, a professor at Cornell Law School.” I kind of wish I was a law professor so that sometimes reporters would call me for a quote and I could say “that’s just weird.” Just a perfect quote.


  
    
      WWE 
    
  

We   talked yesterday about Vince McMahon’s return to World Wrestling Entertainment Inc.: He stepped down as chief executive officer and director last summer, but he remained the controlling shareholder. Last month he changed his mind and asked to come back as executive chairman, but the board of directors refused, so last week he fired several directors and put himself and his other chosen candidates on the board, presumably so they could make him executive chairman again.  That worked:

World Wrestling Entertainment Inc. said Tuesday that its board of directors unanimously elected majority owner Vince McMahon as executive chairman, less than a week after the former chief executive returned to the company.
In addition, Mr. McMahon’s daughter, Stephanie McMahon, has resigned as chairwoman and co-CEO. Nick Khan, who was co-CEO with Ms. McMahon, will serve as the sole chief executive, the WWE said.
Mr. McMahon said he supported Stephanie’s personal decision and was grateful that she had offered to step in during his absence.

It was always possible it wouldn’t work. Even when there’s a controlling shareholder, the directors have a fiduciary obligation to do what’s best for the company, not just what the shareholder wants. It was theoretically possible that McMahon could choose his best friends and closest allies, appoint them to the board, come to them and say “okay now make me chairman,” and they could have said “no, in the exercise of our fiduciary duties, we think that’s not a good idea.” Then he’d have to fire them and try again with different allies. That would be a very funny outcome, but it was not very likely, and in the event the board unanimously gave him what he wanted.

  
    
      Things happen
    
  

Banks’   Revenue Bonanza Seen Under Threat From Looming US Recession. Goldman Sachs embarks on biggest  cost-cutting drive since financial crisis. Review of  Nickel Blowup Calls for Changes at London Metal Exchange. Fidelity Investments Buys  Shoobx to Expand Private-Company Stock-Plan Business. First  Cryptocurrency Insider-Trading Case Yields 10-Month Prison Term. “The 2018 compensation package clearly   wasn’t enough to keep Elon focused on Tesla.”  Supercore inflation. House Republicans to vote on bill  abolishing IRS, eliminating income tax. Prince Harry says he was  bred to offer spare organs to heir William.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] Why is it not quite right? Well, the less important answer is that January 2024 Treasuries are trading in about a 4.65% context this morning, so 4.5% is just a convenient round number. The more important answer is that Treasury does not issue one-year “bonds”: Treasury securities include bills, which have maturities of 4 to 52 weeks, notes, which have maturities of 2, 3, 5, 7 or 10 years, and bonds, which have maturities of 20 or 30 years. Importantly, bills do not pay coupons: The way bills work is that you pay, say, $98 today for a bill with a $100 face amount, you get back $100 at maturity, and the $2 difference is your yield. This makes bills tricky to use with the premium-debt gimmick; realistically you need to do that gimmick on notes or bonds. I am starting with a hypothetical one-year interest-bearing security to make the math and intuitions simple, but it’s not really right. That said, the statute authorizing Treasury notes allows them to have maturities of “at least one year,” so it’s not impossible to do this exact trade; it would just be (especially) weird.


  [2] [2] In fact Treasury notes pay interest every six months, so you get some of your money back earlier, but let’s keep it simple.


  [3] When it’s paid back, it decreases the debt by $100, except that probably Treasury pays it back by issuing new debt, so it doesn’t really decrease the debt.


  [4] The text has a loose intuitive description of the math. The real math, in Excel, is =PMT(0.036,10,-200,100), or really =2*PMT(0.018,20,-200,100), because notes pay interest semiannually. That works out to about $15.60 per year. One intuitive way to think about this — the way you might think about your mortgage, say — is that you put in $200 of “principal,” you get back $10 per year of “principal” plus $100 at the end, and you also get $5.60 per year of “interest,” which sort of works out to 3.6% interest on the average amount of principal outstanding ($200 at the beginning, $100 at the end, declining each year). But of course I can only say that in a footnote; the point of the gimmick is that, for debt accounting purposes, that full $15.60 yearly payment gets counted as “interest,” and there is only $100 of principal. Also, when I say that the interest rate is 15.6%, I mean 15.6% of the stated $100 principal amount ($15.60 per year). The *yield* of this bond — the annualized return you get on your money — is 3.6%; that’s the point of the math.


  [5] Treasury issues notes and bonds with coupons in increments of 1/8 of a percentage point, so you might get notes with coupons of 2.125% or 3.75% or 4.875% or whatever. The actual yield is set competitively and won’t generally be an eighth of a point, so Treasury will set the coupon to the nearest eighth of a point that is below the auction yield, and will set the issue price below par to get the correct yield. (If the yield is below 1/8th of a percent, then the coupon is set at 0.125% and the issue price can be above par.) From the regulations: “If a Treasury non-indexed or inflation-protected note or bond auction results in a yield lower than 0.125 percent, the interest rate will be set at 1⁄8 of one percent, and successful bidders' award prices will be calculated accordingly. … [Otherwise,] The interest rate we establish produces the price closest to, but not above, par when evaluated at the yield of awards to successful competitive bidders.”


  [6] Actually they are often worth more than regular bonds with the same maturity, because they have lower duration: You get back more of your money earlier with a high-interest bond than a low-interest one. I’m ignoring that here because the lower duration is a real cost to Treasury: It has to pay back more of the money earlier. (Also a lower duration may not be good given the current inversion of the Treasury curve.) The point is that, for the same *duration*, a high-premium bond will often have a bit of a higher yield than a par bond.


  [7] I mean, the platinum coin seems fine. In some ways it is more elegant, but less interesting. It is not a financial-engineering solution to the problem; it is just, like, firing a zany cannon at the problem.


  [8] Because I am sort of making a joke here, I am ignoring reinvestment in growth of the business. But in fact at every stage you are making a choice between putting the money into doing more of the business, and cashing it out for yourself. Realistically by the time you get to, like, Step 6 of my list, you have chosen to do a lot of reinvestment rather than consumption, but by now the reinvestment opportunities are growing slower than the profits.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23chzr3n.5ua1/5809e405.gif" alt="" border="0" /></a>