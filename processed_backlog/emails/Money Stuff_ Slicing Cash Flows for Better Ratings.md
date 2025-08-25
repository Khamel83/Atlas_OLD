# Money Stuff: Slicing Cash Flows for Better Ratings

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Wed, 18 Jan 2023 14:46:52 -0500 (EST)
**Source:** inputs/saved_emails/Money Stuff Slicing Cash Flows for Better Ratings_Wed,_18_Jan_2023_14-46-52_-0500_(EST)_185c66bfdc34cf86.eml
**Processed:** 2025-08-24T19:13:07.081935



  
  
    
      
        
      
    
  
  
    
      
        We talk from time to time around here about the cash-flow-slicing business. The way it goes is: You have some business that will make somewh
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      CFO ratings
    
  

We talk from  time to  time around here about the cash-flow-slicing business. The way it goes is:
	You have some business that will make somewhere between $75 and $150 next year.	You can sell it to one owner who gets the cash flows from the business. If it makes $75, she gets $75; if it gets $100, she gets $100; if it gets $150, she gets $150; etc.	Her ownership stake is worth some amount of money, presumably between $75 and $150. Let’s say it’s $100. She would pay $100 for this ownership stake.	
Or, you can divide up the cash flows. A senior bondholder gets the first $50 of cash flows: If the business makes $75, she gets $50; if it makes $150, she gets $50. A junior bondholder gets the next $30: If the business makes $75, he gets $25; if it makes $80 or $100 or $150, he gets $30. And then a shareholder gets whatever is left, whatever the business makes above $80: If it makes $75 or $80, she gets zero; if it makes $100, she gets $20; if it makes $150, she gets $70. 	Here, the senior bond is much safer than the unitary ownership claim: In Steps 1-3, the owner puts up $100 and could lose money (get back $75) or make money (get back $150) or somewhere in between, but in Step 4, the senior bondholder always gets back $50. The junior bond is also safer than total ownership, with less variance in its returns: It gets back $30 in almost every case, unless things go quite badly. The shareholder in Step 4, though, takes much more risk than the total owner in Steps 1-3: The total owner always gets back at least $75, while the levered shareholder here might get back $0.	You can sell the senior bond plus the junior bond plus the shares for some amount of money, presumably between $75 and 150. Let’s say it’s $105.	$105 is more than $100 so this is a good trade. You have created $5 of value by slicing the cash flows.

This is one of the main things that happens in finance. It describes how companies work — they issue debt and equity, etc. — and your mortgage, and banks. In its purest form, where you just have some set of cash flows and you slice them up into junior and senior claims, it is often called “securitization,” or “structured finance.”
Why would this work? Why would the sliced-up claims (senior bonds, junior bonds, shares) be worth more ($105) than a single unitary claim ($100)? There is  a famous theorem saying that it shouldn’t work, that the value of the cash flows shouldn’t depend on how you slice them up. But of course people do slice them up.
  [1]
 At least sometimes, it seems, there is more demand for a very safe cash flow plus a very risky cash flow than there is for a single blended kinda-risky cash flow.
Why would that be? You could tell psychological stories, stories about conservative investors wanting safe assets and aggressive investors wanting risky assets and nobody wanting stuff in the middle. But it is often useful to think about a story of ratings and regulation. Schematically:
	You are a bank or an insurance company; you are in the business of taking money (deposits, premiums) from customers and investing it until they need it. You use the money to buy investment assets, and you make money if the assets return more money than you need to give back to the customers. Your regulators require you to have a certain amount of capital: For every $100 of assets that you own, you can have, say, $92 of deposits and $8 of your own money. The $8 is your capital.	But the regulators “risk-weight” your assets: Really, you need capital equal to 8% of your risk-weighted assets, and different assets count differently. US Treasury bills might get a 0% risk weight: You can buy $100 of Treasury bills with $100 of deposits and $0 of capital. Business loans might get a 100% risk weight: You need $8 of capital to buy $100 of loans. Bitcoin might get a  1,250% risk weight: You need $100 of capital to buy $100 of Bitcoin; you can’t use depositor money at all.
  [2]

	Capital is, by general agreement, expensive. All else equal, you would rather buy $100 of assets with $99 of deposits and $1 of your own money than with $80 of deposits and $20 of your own money. On the other hand, you’d rather buy higher-yielding assets than lower-yielding assets. Higher-yielding assets are often riskier, which means they have higher risk weights and require more capital.	Your job is to optimize this: You want to get the highest yields with the lowest capital requirements. If there are two investments with the same risk and returns, but one of them has lower capital requirements, you should choose that one.	Someone offers you an attractive, kinda risky investment. It has a 50% risk weight. If you buy $100 of it, it counts as $50 of risk-weighted assets, so you need $4 of capital.	Some financial engineer finds a way to slice that investment into a very safe senior bond and a very risky equity investment. The slicing produces 80% senior bond and 20% risky equity. The senior bond has a 0% risk weight — it’s as good as Treasury bills — and so requires $0 of capital. The very risky equity has a 200% risk-weight: If you buy $20 of it, it counts as $40 of risk-weighted assets, so you need $3.20 of capital.	You buy $80 of the safe bond and $20 of the risky equity, so you need a total of $3.20 of capital. You have saved $0.80 of capital.	But you bought the same thing. You had $100 of stuff that required $4 of capital, you sliced it into an $80 tranche and a $20 tranche, and somehow magically those two tranches add up to require $3.20 of capital.

It is not quite true that the story of the 2008 financial crisis is “instead of making mortgage loans, holding them, giving them a 50% risk weight and holding 4% capital against them, banks made mortgage loans, sliced them up into securitizations, bought highly rated tranches of them, and held much less capital against them,” but it is kind of true, and worth keeping in mind.
  [3]

Similarly, if you are an insurance company, some private equity  firm might come to you and ask you to invest $100 in a private equity fund or a high-yield private credit fund. And you will say, sure, sounds great, but I am a regulated insurance company, and my regulators prefer that I mostly invest my money in safe bonds. I can do some private equity investing, but not too much; mostly I just buy bonds with good credit ratings. 
And then the PE firm will say: Okay, what if we sliced our fund into junior and senior tranches? You can invest in both. The senior tranche is a bond, which pays back your money with interest as long as our private equity fund doesn’t perform disastrously. And the junior tranche is an equity upside stake, which pays back whatever the return on the fund is, minus whatever the bond pays. You put, say, $80 into the bond and $20 into the equity stake. 
This is the same thing: Buying a whole stake in the fund is economically identical to buying (1) a senior claim on the fund plus (2) a junior claim on the fund; you are just slicing up the cash flows. But now you can go to your regulator and say “oh no it’s not $100 of equity; it’s $20 of equity and $80 of bonds.” Your regulator is much more comfortable with you buying bonds than buying equity, so you get better regulatory treatment and can do more of it. You go and get the bonds rated by a credit ratings firm, and from your regulator’s perspective you have transformed $100 of risky scary private equity investment into (1) $80 of safe A+ rated corporate bonds plus (2) $20 of risky scary private equity investment. 
We  talked a while back about a form of this trade, called a “collateralized fund obligation,” or CFO. (I am oversimplifying it: Often you don’t just slice up one private equity investment; you put a bunch of different private equity investments into a box and slice up their total cash flows.) Yesterday the Financial Times reported that  insurance regulators don’t like it:

US regulators are cracking down on investment vehicles used by private equity groups over fears that rating agencies are downplaying the products’ dangers, exposing insurers to undue risks.
The vehicles are known as “collateralised fund obligations”, a name that echoes the “collateralised debt obligations” that played a big role in the 2008 financial crisis. They parcel up stakes in hundreds of private equity-owned companies into products intended to diversify risk and so obtain better credit ratings.
A year-long investigation by the National Association of Insurance Commissioners, a US regulatory group, has found that rating agencies can understate the risk of CFOs to insurers, which are among the vehicles’ main investors, according to people familiar with the matter.
The NAIC, which coordinates US insurance regulators, has now decided to assess the risk of individual CFOs, supplanting credit rating agencies — a similar initiative to steps the regulator took to rein in mortgage-backed securities in the wake of the financial crisis.

The NAIC report is  here (in Microsoft Word download format, sorry), and it doesn’t exactly find “that rating agencies can understate the risk of CFOs to insurers.” Instead, what it finds is that this is too good of a regulatory arbitrage:

These investments are being reported as bonds and receiving a bond risk-based capital (RBC) factor based upon the mechanical assignment of NAIC Designations that rely upon Credit Rating Provider (CRP) ratings through the filing exempt process. The use of CRP ratings would not be permitted for the fund or equity investments which underly these notes if the equity or fund investment were held directly. ...
The structure may permit in-substance equity and fund investments to obtain improved RBC treatment than what would be received if the investment had been directly reported.  In addition to improved RBC treatment, the structures could permit entities to hold more underlying equity / fund investments than what would be permitted under state investment law. …
Equity and fund investments that are structured through another legal entity have been able to qualify as ‘bonds’ under the current definition due to their legal form (instead of substance as with the proposed bond definition) and bypass reporting requirements for equity and fund investments. These structures have sometimes been referred to generically as “Rated Notes”, but they may be called other names. The name may change but the general framework is the same: an equity or fund investment is transformed into what the insurer reports as a bond through the insertion of an intervening entity, which issues a note that, due to a CRP rating, receives the statutory treatment of a bond for accounting, reporting, RBC and NAIC Designation purposes. This process exploits the inherent weakness within the Filing Exempt process where anything with a CRP rating is assumed to be a “bond” and automatically treated as such despite its underlying assets, structure, or risk. …

It gives an example of an insurance company investing in a private credit fund that lends money to risky companies with B credit ratings. Just investing directly in that fund is risky — it’s single-B credit investing — and has high capital requirements. But if you slice that fund into a 90% senior claim and a 10% junior claim, and then sell “‘investment units’ comprised of 90% Senior Notes and 10% limited partnership interest,” the senior claim is safe, the junior claim is risky, and the combined “unit” has a lower capital requirement than investing directly in the fund:
By investing in the investment units issued by the Debt Feeder Fund, an insurer is able circumvent regulatory guidance by transforming the Main Fund’s investments in “B” rated loans into a much higher rated note due to the intervening legal entity.  An insurer investing in the investment unit (note and equity) would be able to dramatically reduce its risk-based capital versus reporting an LP Interest investment in the main fund holding “B” rated loans but be exposed to identical economic risk. … The insurer making this investment could reduce its risk-based capital by 56.6%, an RBC factor reduction of 5.40%, if it invested in the investment unit (note and equity) with the note rated by a CRP instead of investing in the underlying assets directly while maintaining the exact same economic exposure.
Yep, that's the game! Finance is, in large part, about finding new ways to slice cash flows that will get better regulatory treatment than the old ways to slice cash flows. And financial regulation is, in large part, about noticing the new ways that people are slicing cash flows, and adjusting the regulations so that the new ways get treated the same as the old ways. Or worse! Part of the goal here is logical consistency and treating economically similar things similarly, but part of the goal is to deter people from doing this, so the regulators might want to treat the new ways worse.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      FTX
    
  

FTX Trading Ltd., Sam Bankman-Fried’s bankrupt crypto exchange, has been under new management since filing for bankruptcy last November,
  [4]
 and the new managers have two related but distinct jobs. One job is to maximize the recovery of the bankruptcy estate: They have to round up all of FTX’s assets, sell them for as much money as possible, and give the money to FTX’s creditors (meaning mostly its customers). The other job is to explain what went wrong to land FTX — which a week before filing for bankruptcy looked like a large, stable and successful crypto exchange — in bankruptcy. The explaining itself might help maximize recovery — if the explanation of what went wrong is “prior management stole the money,” the bankruptcy estate can sue the prior managers to get the money back — though that is not its only purpose. It can also help prosecute prior management, and provide a certain emotional and intellectual closure.
Yesterday  FTX “announced that their top level management and advisors met with the members of and advisors to the Official Committee of Unsecured Creditors” to give the creditors an update on what they have found. Here is  the update,
  [5]
 prepared by FTX’s advisers (Alvarez & Marsal, Sullivan & Cromwell and Perella Weinberg Partners), which covers both recoveries and explanation. I want to start with the explanation part. The   basic explanation of   what went wrong at FTX is that FTX loaned billions of dollars to Alameda Research, a trading firm founded and mostly owned by Bankman-Fried. Alameda lost the money, rendering FTX insolvent. And now FTX’s advisers say that they “have uncovered the mechanics behind how Alameda Research had the ability to borrow without collateral effectively unlimited amounts from customers and how a small group of individuals had the ability [to] remove digital assets from the exchange without being recorded on the exchange ledger.”
That discussion is on slide 19:


    

If you were a normal customer at FTX, you were not allowed to have a negative balance in your account. If you put up $100 of money to buy $200 of crypto, and your crypto lost $50 of value, then your account balance was $50. If it lost another $50 of value, then your balance was $0 and you were liquidated. Your account could never be worth -$10; you got liquidated before that.
If you were a market maker on FTX, though, you were allowed to have a negative balance: Effectively, FTX would lend you the money so you could open a position without depositing the money first, or have the market move against you without instant liquidation. In FTX’s code, most accounts had a “borrow” flag set to zero, meaning that they could not have negative balances, but some 4,000 accounts had the borrow flag set to some positive number, meaning that FTX would lend them the money up to some credit limit. Of those 4,000 accounts, 41 had credit limits of $1 million to $150 million. One — Alameda — had a higher limit. Alameda’s limit was $65 billion. (Slide 18 shows a code snippet, showing that the actual limit was $65,355,999,994.) “FTX will allow Alameda to have a negative balance of up to $65 billion” is functionally equivalent to “Alameda can use as much of FTX’s customer money as it wants.”
There was another flag in the code, though, “can_withdraw_below_borrow.” The “borrow” flag determines how negative your account can be and keep trading: If your borrow flag is set to $10 million, and you put on some trades and they move against you and you end up with a balance of negative $5 million, then you can keep the trades on. But if you went to FTX and tried to cash out $4 million to spend on groceries — giving you a total balance of negative $9 million, still within your credit limit — FTX wouldn’t give you the money. You could use your credit limit to trade on FTX, but not to take out cash. “No, you still owe us $5 million, pay us that first, we’re not letting you take any cash out before you pay us what you owe,” FTX would quite reasonably say. Unless you had the “can_withdraw_below_borrow” flag set to “true.” Then FTX would say “sure, here’s the money.”
One account had that flag set, says the presentation: Alameda. To the tune of $65 billion. Setting the borrow flag to $65 billion and the can_withdraw_below_borrow flag to true is functionally equivalent to “Alameda can take as much of FTX’s customer money as it wants, remove it from the exchange, and spend it on whatever.” (Slides 16 and 17 give you a sense of what “whatever” meant, including $253 million of Bahamas real estate — including $12.9 million for “The Conch Shack”??? — and $93 million of political donations.)
The presentation describes this setting as “God Mode,”
  [6]
 which I am not sure is a technical term found in FTX’s actual codebase or documentation, but you get the idea. FTX   built a video game for other people to trade crypto, but FTX — or rather its affiliate Alameda — had a cheat code. Everyone else got to trade crypto, and if they made money, they could take out the money that they made. Alameda got to trade crypto, and it got to take out as much money as it wanted, whether or not it made money. It was playing in God Mode.
But most of the presentation is about recoveries: how much stuff FTX has found, what it thinks it’s worth, and how much it can pay to creditors. The headlines here are “FTX Debtors have identified approximately $5.5 billion of liquid assets to date,” consisting of $1.7 billion of cash, $3.5 billion of “liquid crypto currency and FTT tokens” and $0.3 billion of securities. But “investigation has confirmed shortfalls at both International and U.S. Exchanges.”
Two points here. One is that we have   previously discussed the importance of FTX US. Basically all the stuff above about borrow flags and credit limits applies to what is sometimes called FTX International, FTX’s main exchange, which is based the Bahamas and meant to serve non-US customers. FTX International is definitely insolvent; it loaned all that money to Alameda, which lost it. But FTX US is a separate, tamer, more regulated business that was meant to serve US customers. It had much less in the way of margin and futures trading; in a loose sense its business was just taking customers’ money, converting it into crypto, and holding the crypto for the customers. If FTX International is missing customer money, then that can perhaps be explained as “it’s hard to run a futures exchange, we were extending credit to traders, and one trader blew up.” That’s a thing that happens in finance sometimes, though obviously the “God Mode” stuff is bad. But if FTX US is missing customer money — as FTX’s management says it is — then that can only really be theft.
And so Sam Bankman-Fried, who is facing criminal charges for blowing up FTX, has a strong interest in arguing that FTX US is fine. Yesterday  he replied to the FTX’s presentation on his Substack, mainly to argue that FTX US is still fine. Specifically:

In the presentation that S&C formally filed on the Delaware Chapter 11 court docket, S&C failed to include $428m in FTX US’s bank accounts as an asset:
1. $181m of digital assets, not including $428m USD in banks
2. More than $181m of customer balances, including USD
3. Thus, they concluded that FTX US had a “shortfall”
Later in the same report, S&C reveals that FTX US has an additional $428m USD in bank accounts, on top of the $181m of tokens—for roughly $609m of total assets.
Customer balances are likely around $199m, and certainly less than $497m (which they were a day earlier before massive withdrawals).
Thus FTX US had at least $111m, and likely around $400m, of excess cash on top of what was required to match customer balances.

I suppose if FTX US customers had crypto balances of $200 million and FTX US had $180 million of crypto and $400 million of cash, that would be weird — why wasn’t FTX US just holding all of their crypto in a box for them? isn’t that mismatch risky? — but more or less fine.
  [7]
 What’s bad is if the customers had balances of $200 million and FTX US had only $180 million total; then you’d have to conclude that the extra $20 million went missing in bad ways. Bankman-Fried argues that it did not.
The other point is that, when FTX was floundering into bankruptcy, I was rather harsh about Bankman-Fried’s insistence that its huge stash of FTT tokens was valuable. I wrote   things like:

FTX issues a token called FTT. The attributes of this token are, like, it entitles you to some discounts and stuff, but the main attribute is that FTX periodically uses a portion of its profits to buy back FTT tokens. This makes FTT kind of like stock in FTX: The higher FTX’s profits are, the higher the price of FTT will be. It is not actually stock in FTX — in fact FTX is a company and has stock and venture capitalists bought it, etc. — but it is a lot like stock in FTX. FTT is a bet on FTX’s future profits.
But it is also a crypto token, which means that a customer can come to [FTX] and post $100 worth of FTT as collateral and borrow $50 worth of Bitcoin, or dollars, or whatever, against that collateral, just as they would with any other token. …
If you think of the token as “more or less stock,” and you think of a crypto exchange as a securities broker-dealer, this is completely insane. If you go to an investment bank and say “lend me $1 billion, and I will post $2 billion of your stock as collateral,” you are messing with very dark magic and they will say no. The problem with this is that it is wrong-way risk. (It is also, at least sometimes, illegal.) If people start to worry about the investment bank’s financial health, its stock will go down, which means that its collateral will be less valuable, which means that its financial health will get worse, which means that its stock will go down, etc. It is a death spiral.

 And:
It is striking that the balance sheet that FTX circulated to potential rescuers consisted mostly of stuff it made up. Its balance sheet consisted mostly of stuff it made up! Stuff it made up! You can’t do that! 
One thing I will say about this harshness is that it is very context-dependent. In 2021, when FTT traded near $80 per token, and when FTX looked like a successful and widely respected crypto exchange, it … well, it would still have been a bad idea for FTX to lend money to Alameda secured by FTT tokens, fine, but it would not have been crazy to say things like “Alameda is worth many billions of dollars because of its huge stash of FTT tokens.” The FTT tokens were valuable, the source of their value — market confidence in FTX’s future cash flows and utility — seemed reasonable, Alameda had a lot of them, it’s all fine.
In November 2022, though, when FTX was hurtling toward bankruptcy and Bankman-Fried was seeking rescue financing, I thought it was pretty weird for him to market Alameda’s stash of FTT tokens as being worth hundreds of millions of dollars. Once you are days from bankruptcy, you can’t expect to get hundreds of millions of dollars for your stock. Your stock is probably going to be wiped out in bankruptcy. FTT is close enough to FTX stock that, in November 2022, FTX could not really count on getting much money for it.
Now it’s January 2023 and FTX is very much in bankruptcy and still, when FTX’s advisers list its $3.3 billion of liquid crypto assets, the second-biggest single holding (behind $685 million of Solana tokens) is $529 million of FTT. Those tokens are valuable to the extent that (1) FTX comes back as a popular exchange and the FTT tokens let holders get valuable discounts on FTX fees and (2) FTX comes back as a popular exchange and uses some of its fee revenue to buy back FTT tokens. How likely are those outcomes? How likely do you think FTX’s bankruptcy advisers think those outcomes are? FTX is going around showing the world the code that allowed Alameda to take all of its customers’ money. Confidence in FTX is not coming back, not if FTX’s current managers have anything to say about it. They are going to have a hard time shopping their stash of FTT tokens. The explanation undermines the recovery.

  
    
      
        
      
    
  


  
    
      10% of everything is securities fraud
    
  

Sure: 

[Alexander] Dyck is a professor of finance at the University of Toronto, who just published a provocative new study on the pervasiveness of corporate fraud. The study has been passed around in the world of academia in recent weeks, and has become a fascination among general counsels, corporate leaders and investors.
It suggests that only about a third of frauds in public companies actually come to light, and that fraud is disturbingly common. Mr. Dyck and his co-authors estimate that about 40 percent of companies are committing accounting violations and that 10 percent are committing what is considered securities fraud, destroying 1.6 percent of equity value each year — about $830 billion in 2021.
“What people don’t get is how widespread the problem of corporate fraud is,” Dyck said about his study, which was published in the Review of Accounting Studies this month.

Here is the study, “ How pervasive is corporate fraud,” by Dyck, Adair Morse and Luigi Zingales.  Basically the idea is that Arthur Andersen didn’t catch fraud at Enron, and then Enron went bankrupt and Arthur Andersen disappeared as a result, so all of Arthur Andersen’s old clients needed to find new auditors, and those new auditors had strong incentives to catch frauds at Arthur Andersen clients, and you could use the resulting increase in fraud-catching to estimate how much otherwise uncaught fraud there is:
Our evidence suggests that in normal times only one-third of corporate frauds are detected. We estimate that on average 10% of large publicly traded firms are committing securities fraud every year, with a 95% confidence interval of 7%-14%.
I am not sure I am persuaded. But I am committed to the bit, and I often say that “everything is securities fraud,” that every bad thing that a public company does can be characterized as securities fraud, because public companies do not disclose all of their bad actions in real time. Do 10% of public companies do undisclosed bad things each year, things that would lead to securities fraud lawsuits if they were discovered, but that mostly go undiscovered? Sure yeah seems reasonable.

  
    
      Where all the children are above average
    
  

If you meet all of the expectations of your job at Meta Platforms Inc., then you have not met all the expectations, because there is an unstated (well, somewhat stated) meta-expectation that you will exceed expectations. The Information  reports:

Company leaders have told some managers that employees who receive a “meets all expectations” grade in their performance review have to up their game, said a current manager. In the past, employees receiving such a grade were told that was a positive sign.
The new message comes amid one of the most intense performance-review cycles in the company’s history, in which Meta managers are ratcheting up pressure on the workforce. It follows Meta’s layoff of 13% of its workforce, or 11,000 people, in November. Now, as fears of a recession mount, some employees worry more job cuts could be on the horizon.

This is semantically irritating — shouldn’t “meets all expectations” include meeting the meta-expectation that you exceed the other expectations? — but practically reasonable; the message is “you have to blow us away every day if you want to keep working here,” which is a nice thing to aspire to. (Also I mean, fine, grade inflation is everywhere.) Incidentally Meta’s highest performance grade (above “exceeds expectations” and “greatly exceeds expectations”) is “redefines expectations,” which I am not sure is entirely a good thing. “This person makes me expect things I had never expected before”: Could go either way.
I was going to make a joke about how it is hard to run a company where you fire your average employees every year, but actually that seems plausible in big tech in 2023? Like, you have 90,000 employees, you rank them, you fire the bottom 50,000, now you have 40,000 employees, you rank them next year, you fire the bottom 25,000, now you have 15,000 employees, you rank them the next year, you fire the bottom 8,000, etc., I don’t know, the Elon Musk Twitter experience teaches that you can repeatedly fire half of your workforce and it might be fine, or fine-ish. 
Speaking of the Elon Musk Twitter experience, Twitter is   selling off its office espresso machines? And here is a  New York Magazine cover story about Musk’s “extremely hardcore” regime at Twitter that I found kind of upsetting to read? Like I feel like there are, in the world, cushy jobs, and there are hardcore jobs, and some people want hardcore jobs building rockets for SpaceX and other people want cushy jobs selling ads at Twitter. And if you start a company, you can start a hardcore company or a cushy company or something in between, but if there’s an already-existing large public company it is very hard to transition it from one end of the scale to another.
  [8]
 When you select yourself into a cushy job and it suddenly, through the market for corporate control, becomes hardcore, that’s pretty rough on you. Apparently thousands of Twitter employees who six months ago were working reasonable hours for good pay with great snacks have decided “okay guess I’ll be sleeping at the office from now on,” but presumably thousands of others had arranged their lives in such a way that they had to go home and see their families at night? I just don’t understand how you can take a cushy company and turn it hardcore without replacing all the employees and giving the new employees something inspiring to be hardcore about.

  
    
      Things happen
    
  

The New   Bankers to the World Aren’t on Wall Street.   Bonuses Will ‘Absolutely’ Fall, Says JPMorgan’s Co-Head of Investment Banking. Solomon Says Goldman Pushed Too Quickly Into   Consumer Banking. Big Banks Might Face  Breakup, Top Regulator Says. Credit Suisse Chief   Not Concerned Over Conflicts in Klein Deal. A  Crypto Magnate Saw the Risks and Still Was Hammered.   Party City Files Bankruptcy After Pandemic Recovery Falters. “Now imagine the frozen buffalo chicken tenders are cryptocurrency, the buckets we put the chicken tenders in are digital wallets, our parents are the bank, the individual magnets are one record of a transaction, the fridge is a ‘block’ of transactions,  the process of launching the fridge into space is ‘mining,’ the reward for launching the fridge into space is one cryptocurrency, and the record of launching each fridge into outer space is the ‘chain’ that connects the ‘blocks’ that are the fridges.” Prostitutes  gather in Davos for annual meeting of global elite - where demand for sexual services rockets during economic summit.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] An important answer that I am not going to discuss further here, but that is often important in real life, is taxes. Generally, in the US, companies can deduct the interest they pay on debt, but they can’t deduct dividends to shareholders. My dumb toy schematic doesn’t mention interest explicitly, but in fact the deductibility of interest is a major exception to Modigliani-Miller and part of the reason that a lot of companies use debt financing. 


  [2] This stuff is all in the ballpark of right, for US banks, but don’t take it too literally. Actual capital requirements are more nuanced, and there are backup regimes so that you can't really buy T-bills with zero capital. 


  [3] Friedman and Kraus’s “Engineering the Financial Crisis” is a book on related topics. And here is a  US Government Accountability Office report from 2016 titled “Mortgage-Related Assets: Capital Requirements Vary Depending on Type of Asset.”


  [4] Technically FTX appointed a new chief executive officer, John Ray, moments *before* filing for bankruptcy, but it was part of the same process.


  [5] In auto-downloading PDF format, sorry. You can find it on  the docket site under “January 17, 2023 – Maximizing FTX Recoveries: Management & Committee Meeting Presentation.”


  [6] It also describes a different setting — that allowed a “small group of individuals” to “move assets (crypto) by accessing the private keys to initiate a direct on-chain transaction.” Obviously one simple way to steal customer money from a crypto exchange would be to use the exchange’s private keys to send all of its crypto to your own wallet, but that doesn’t seem to be a big part of the FTX story. Though there seems to have been some draining of accounts shortly after the bankruptcy filing, and “Investigation is underway to determine whether any off-ledger misuse of such access occurred.”


  [7] Also I’m not sure that’s what happened; the presentation doesn't get into details but it’s conceivable that FTX US’s situation was, like, $181 million of crypto customer balances, $50 million of dollar customer balances, $181 million of crypto assets and $400 million of cash, exactly matching the customer exposures but with some extra cash cushion. That doesn’t seem to be what the FTX presentation implies, but it doesn’t quite rule it out either.


  [8] Are there examples of a company jarringly transitioning from extremely hardcore to extremely cushy? I am tempted to say “investment banks after 2008,” but I know that’s not true. Presumably some hard-charging startups have been bought by big companies and then started coasting, but that’s not really the same.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23ci16p9.5ryk/6e9c86f2.gif" alt="" border="0" /></a>
