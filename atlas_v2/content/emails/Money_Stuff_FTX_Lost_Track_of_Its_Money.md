# Money Stuff: FTX Lost Track of Its Money

**Source**: inputs/saved_emails/Money Stuff FTX Lost Track of Its Money_Mon,_10_Apr_2023_14-17-55_-0400_(EDT)_1876c6491d1ec368.eml
**Type**: email
**Created**: 2025-08-25T02:54:06.766961

---

What a weird job John Ray has. I suppose that in general, if a company hires a new chief executive officer, the new CEO will have some disag
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      FTX
    
  

What a weird job John Ray has. I suppose that in general, if a company hires a new chief executive officer, the new CEO will have some disagreements with the previous CEO, and some incentive to make a meal of those disagreements. For one thing, CEOs are generally people with strong opinions. Also the new CEO was hired for a reason; quite possibly the old CEO did do something wrong. Also the new CEO can make himself look better by making the old one look worse: The more you say “oh man the previous guy really messed everything up, what a disaster this place is,” the more credit you will get for any improvements.
Also I mean, separately, the former CEO of FTX Trading Ltd. really did mess the place up a lot, so Ray objectively has a lot to complain about. 
Still it is hard to think of a CEO in recent memory who has been more focused on trashing the previous management? (Elon Musk I guess?) Ray was hired as the CEO of FTX to put it into bankruptcy, to steer it through bankruptcy, and to maximize recovery for FTX’s customers and other creditors, and he has spent a lot of his time publishing gleeful reports about how bad everything at FTX is and how incompetent and criminal its former managers, led by former CEO Sam Bankman-Fried, were. Obviously a lot of people — most notably US federal prosecutors, but also FTX’s customers and, you know, journalists — are very interested in how incompetent and criminal those former managers were, and the reports are quite informative and I am glad he’s publishing them. Still they are in a little bit of tension with Ray’s main job of maximizing recoveries. Occasionally Ray and his team will make noises about how they might restart FTX’s business to earn money to pay off creditors, and then they’ll put out a report with a title like “FTX Debtors Discover That FTX Was the Worst Company in the History of Companies,” and that doesn’t feel like great advertising?
Or maybe it is? Maybe the way to win back trust is to be very open about how bad things were before? But I am not sure whether the goal of these reports is to maximize the going-concern value of FTX’s business, or to explain why that’s hard, or just to vent about the problems of previous management.
Anyway yesterday FTX  published another report about its prior incompetence — “FTX Debtors Release Report on FTX Group's Control Failures” — and it is wild reading.
  [1]
 A lot of it is elaboration on stuff we already knew (in part because Ray has   published previous reports about it): FTX was bad at keeping track of its accounts, it was bad at keeping control of its crypto, it handed over lots of money to insiders in unexplained and poorly documented ways, and it let Alameda Research, Bankman-Fried’s trading firm, take a ton of risks with customer money in a way that   ultimately bankrupted FTX.
Still there are new anecdotes that I cannot resist quoting. For instance, we knew that FTX’s accounting was bad, but here’s Bankman-Fried making that point himself:

In an internal communication, Bankman-Fried described Alameda as “hilariously beyond any threshold of any auditor being able to even get partially through an audit,” adding:
“Alameda is unauditable. I don’t mean this in the sense of ‘a major accounting firm will have reservations about auditing it’; I mean this in the sense of ‘we are only able to ballpark what its balances are, let alone something like a comprehensive transaction history.’ We sometimes find $50m of assets lying around that we lost track of; such is life.”
Bankman-Fried’s statements evidence the challenges a competent audit firm would have had to overcome to audit Alameda’s business.

Ha ha ha. Look, if you run a financial institution, and you sometimes finding an extra $50 million of assets lying around, you might say things like “ooh money” and “that’s hilarious” and “such is life.” Finding money feels good! But it is indicative of a deeper problem. “If I sometimes find $50 million of assets lying around that I lost track of,” you might think in more reflective moments, “is it possible that I will sometimes find $50 million of liabilities lying around that I lost track of?” Because that would be bad. In the event,   FTX was undone because, and I cannot emphasize this strongly enough, IT FOUND $8 BILLION OF LIABILITIES LYING AROUND THAT IT LOST TRACK OF, whoops. Better to keep track of all the money!
The report also objects to how FTX held on to its crypto. Like any crypto exchange, FTX was in the business of holding crypto for itself and its customers, and “holding crypto” means basically keeping track of the private keys that allow you to access your crypto. There are some best practices for this sort of thing, if you are holding a lot of crypto for customers: You try to keep most of it in “cold wallets” not connected to the internet, and you write down your private keys in ways that are (1) more permanent and secure than Post-It notes but also (2) less hackable than iPhone notes. FTX’s new management says that FTX’s old management used mostly worst practices to hold on to customer crypto:

FTX Group kept virtually all crypto assets in hot wallets, which are far more susceptible to hacking, theft, misappropriation, and inadvertent loss than cold wallets because hot wallets are internet-connected. Prudently-operated crypto exchanges keep the vast majority of crypto assets in cold wallets, which are not connected to the internet, and maintain in hot wallets only the limited amount necessary for daily operation, trading, and anticipated customer withdrawals. Relatedly, prudently-operated crypto exchanges implement strict processes and controls to minimize the security risks (for example, the risk of hacking, theft or loss) inherent in the transfer of crypto assets between hot and cold wallets.
The FTX Group undoubtedly recognized how a prudent crypto exchange should operate, because when asked by third parties to describe the extent to which it used cold storage, it lied. For example, in 2019, Bankman-Fried falsely responded to a customer question on Twitter by providing assurance that “[we use the] standard hot wallet/cold wallet setup.”

A general theme in the collapse of FTX is that FTX was quite good at sounding like it was a good crypto exchange. It knew how to say the right things, which created the impression that it was also doing them. In   proposals to regulators, and in Bankman-Fried’s   Twitter account, FTX regularly seemed to be thoughtful about managing the risks of a leveraged crypto futures exchange. FTX’s executives clearly thought about the right issues — liquidation of losing positions, hot wallet/cold wallet crypto storage — and so it was natural to assume that they did something about them. Turns out, nope!
Also:

The Debtors identified private keys to over $100 million in Ethereum assets stored in plain text and without encryption on an FTX Group server.
The Debtors identified private keys, as well as credentials to third-party exchanges, that enabled access to tens of millions of dollars in crypto assets that were stored in plain text and without encryption across multiple servers from which they could be accessed by many other servers and users in many locations.
Single-signature-based private keys to billions of dollars in crypto assets were stored in AWS Secrets Manager (a cloud-based tool used to manage sensitive information), and/or a password vault (a tool for secure storage of passwords), neither of which is designed to meet the needs of secure-key storage; any of the many FTX Group employees who had access to AWS Secrets Manager or the password vault could access certain of the keys and unilaterally transfer the corresponding assets.

I don’t know, is storing your secret passwords in Amazon’s Secrets Manager a good practice or a bad one? I could see arguments either way. Also here’s this:
Alameda also lacked appropriate documentation as to the description or usage of private keys. For example, a key for $600 million dollars’ worth of crypto assets was titled with four non-descriptive words, and stored with no information about what the key was for, or who might have relevant information about it. The Debtors identified other keys to millions of dollars in crypto assets that were simply titled “use this” or “do not use,” with no further context.
Incredibly relatable. Who among us has not saved our most precious data in a file titled “use this one”? This works, I guess, imperfectly, if your company is basically a half-dozen friends in a suite in the Bahamas. But it’s not best practices, and in particular, if the friends who run the company all get kicked out for incompetence and criminality and angry professionals come in to clean up the mess, they will be very annoyed to find all the crypto stored like this. 

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      He liked the bonds
    
  

One fun little financial story of 2017 and 2018 involved the bonds of American Media Inc., the publisher of the National Enquirer. AMI was majority-owned by a hedge fund firm named Chatham Asset Management LLC. It had some bonds outstanding. Those bonds did not trade much, but they traded some, and they kept trading at higher and higher prices. By November 2017, some AMI bonds were trading at lower yields than the bonds of Apple Inc.
  [2]
 I am sure AMI is a fine tabloid publisher but it is not Apple, and its bond prices were perplexing. Also in 2018 AMI tried to raise some more money  by selling more bonds, and it eventually sold them at a 10.5% interest rate, which was much higher than the trading yield of its existing bonds. To the naked eye, AMI looked like a small, high-yield newspaper publisher, and when it sold new bonds the prices reflected that. But its old bonds traded in the secondary market at prices that made it look more creditworthy than Apple. What gives?
Everyone kind of knew the answer, which is that the AMI bonds didn’t trade that much, and they seemed to trade mostly within Chatham:Chatham, the majority equity owner of AMI’s stock, also owned most of its bonds, and sometimes Chatham would sell the bonds to itself at ever-increasing prices. This didn’t cost Chatham much — it was basically just overpaying itself — and made AMI’s credit look good. But of course when AMI wanted to raise money by selling more bonds, Chatham was not going to buy those bonds at a 2% interest rate; it wanted a regular interest rate, like 10.5%. 
This is not particularly legal, and last week Chatham and its founder Anthony Melchiorre settled with the US Securities and Exchange Commission, agreeing to  pay $19 million for doing this. Why did Chatham do this? The story that  the SEC tells is basically that Chatham liked the bonds a lot and didn’t want to let them go. Chatham ran a bunch of different accounts — some hedge funds, some liquid alternatives funds — and held large AMI bond positions in all of them. Sometimes some accounts would need to sell AMI bonds: They had concentration limits that meant they couldn’t have too much of their money in AMI bonds, or customers took money out and Chatham needed to sell bonds to pay them. When this happened, Chatham did not want to let the bonds go, so it sold them to other Chatham accounts so they could stay in the family.  The SEC says:
Generally, when Chatham was forced to sell a high conviction AMI Bond in these circumstances, Chatham desired to purchase the AMI Bond for another Client because Chatham still believed in the merits of the investment and would not otherwise be selling the AMI Bonds if it were not for the portfolio restrictions or cash needs of the selling Clients.
As a general matter, selling bonds to yourself is allowed, but awkward: If you really believe in some bonds but have to sell them from one account, and you want to buy them in another account, you are not forbidden from doing so, but there are lots of ways for it to look bad. Generally the ways for it to look bad are (1) you overpay for the bonds, making money for the selling account at the expense of the buying account (and causing the reported trading price of the bonds to be wrong) or (2) you underpay for the bonds, making money for the buying account at the expense of the selling account (and causing the reported trading price of the bonds to be wrong). The solution is generally to sell yourself the bonds at a fair market price, neither underpaying nor overpaying. Broadly speaking two ways to do that are:
	Sell the bonds into the market at market prices, and then buy them back a bit later from the market at market prices: You don’t trade with yourself at all, but only with arm’s-length counterparties; or	Figure out a fair market price using outside sources (trading pries, pricing services, quotes from dealers, etc.) and sell the bonds to yourself at that price. 

The first option is probably better, but it requires an active market; if you’re the only real buyer or seller of the bonds it’s hard. 
Anyway Chatham sort of … waved in the direction of doing this the right way?
Recognizing that there were legal restrictions on trading between RICs
  [3]
 and their affiliates, which included other Chatham Clients, Chatham and Melchiorre sought advice from a compliance consultant on how to facilitate the Rebalancing Trades. The consultant advised Chatham to conduct the trading either through a single broker over more than one day or through multiple brokers if on the same day. The foundational principle underlying the advice was to ensure that the transactions occurred at independently-derived market prices. 
Yeah I mean that’s good generic advice, but when you are the market for the bonds it doesn’t work out great. Also Chatham did not necessarily go all in on the spirit of that advice:

Around the time that Chatham began to execute the Rebalancing Trades, Melchiorre generally explained the purpose of the Rebalancing Trades to the Rebalancing Brokers. Melchiorre informed each of the Rebalancing Brokers to whom he sold a Client’s AMI Bonds that he likely would have an interest in repurchasing that same AMI Bond he was selling for another Client. Over time, an understanding developed on the part of the Rebalancing Brokers that whenever Melchiorre placed an order to sell one of the AMI Bonds for a Client, he would repurchase it for another Client, either directly the following day or days, or indirectly through another broker.
The Rebalancing Brokers engaged in the Rebalancing Trades because they expected Melchiorre to repurchase the bonds. The business model of several of the Rebalancing Brokers was to “match” buy and sell orders from their customers. Those Rebalancing Brokers ordinarily did not purchase securities for their own inventory—i.e., put the firm’s own capital at risk—or they did so on a very limited basis. Nonetheless, the vast majority of the Rebalancing Trades involved at least one Rebalancing Broker that purchased bonds into its firm’s inventory. For example, some of the Rebalancing Brokers would at times agree to purchase securities from Chatham even though the Rebalancing Broker may not have lined up the other leg of the transaction. These brokers’ willingness to do so was based on their expectation that Chatham would repurchase the bonds, either directly or through another broker.
The purchasing Rebalancing Brokers generally did not offer the AMI Bonds to other customers in the market. Instead, in virtually every case, they resold the securities to Chatham or to another broker who they understood was purchasing for Chatham.
As Chatham’s need to conduct rebalancing in its various Client Accounts increased over time, Rebalancing Trades became routine. When Melchiorre wanted to sell an AMI Bond to one particular Rebalancing Broker (“Rebalancing Broker A”) and then repurchase it the following day, he would send Rebalancing Broker A a message indicating that he wanted to sell an AMI Bond in the “usual drill.” Rebalancing Broker A then would purchase the AMI Bond into the firm’s inventory until Melchiorre repurchased it the following day.

In the abstract, selling bonds to a broker one day and then buying them back for a different account a day or two later could be a good way to do everything at arm’s-length market prices: The broker will pay, and charge, prices that reflect market levels; it won’t overpay to buy from you or undercharge to sell to you.
But in practice, if you are the only buyer and the only seller and you call up a broker and say “hey it’s the usual drill,” you are not really getting a fair market price. The broker doesn’t care what the buying price or selling price is, as long as you pay a commission. You can just pick whatever price you want:

Melchiorre proposed the price for the Rebalancing Trades and the Rebalancing Brokers agreed to it without first soliciting bids from other market participants.
When proposing a price for Rebalancing Trades, Melchiorre considered a number of factors, which included the prior day’s price as reflected in prices published by a pricing service. Those published prices would have been influenced, to some extent, by Chatham’s own trading. When purchasing the AMI Bonds, Melchiorre also added a spread to compensate the Rebalancing Brokers. For example, in the case of a Rebalancing Trade executed through a single Rebalancing Broker overnight, Chatham would repurchase the AMI Bonds for a small spread above what it had sold the AMI Bonds to the broker the day before.

One consequence of this is that the compliance consultant’s basic idea of selling to brokers to get market prices was not really working. Another consequence is that the prices kept going up: The only trades were Chatham’s trades, and it kept trading at higher prices to compensate its brokers. Eventually this became absurd:

Over the Relevant Period, Chatham and Melchiorre engaged in over one hundred Rebalancing Trades in AMI Bonds, accounting for approximately 81 percent, on average, of the customer trading (i.e., not broker-to-broker trading) in such securities.
Over time, the frequent Rebalancing Trades and repeated mark-ups to compensate the Rebalancing Brokers resulted in the market price of AMI Bonds increasing at a faster rate than prices of similar securities. For example, by November 2017, two of the AMI Bonds traded in Rebalancing Trades at implied yields lower than the prevailing London Interbank Offered Rate (“LIBOR”). Such yields ordinarily would have been associated with a bond of a much higher creditworthiness than the AMI Bonds.

A third consequence is that Chatham’s assets under management kept going up: It charged clients fees based on the value of its assets, and as it kept increasing the prices of these bonds, that value kept going up. The SEC says:

Chatham was compensated for its advisory services to the [hedge] Funds with a management fee and a performance fee, and to the [liquid alts funds] with a management fee. The management fee charged to certain Clients was set at a percentage of the [net asset value] of those Clients.
In order to calculate each Fund’s NAV, Chatham used an independent pricing service to determine the value of each of the portfolio securities, including the AMI Bonds. The LAF administrators calculated their own NAVs, also using the same pricing service Chatham used.
Chatham and Melchiorre understood that the pricing service that Chatham and the LAF administrators utilized was based to some extent on recent trading prices and that the Rebalancing Trades accounted for virtually all of the trading in the Bonds during the Relevant Period. Because the Rebalancing Trades at times increased the prices of the AMI Bonds, the NAVs of the Client accounts also were increased by that amount on those occasions.
Accordingly, the Clients paid Chatham an estimated $11,000,000 in performance and/or management fees that they would not have in the absence of Chatham’s Rebalancing Trades. Chatham in turn paid approximately 55 percent of such fees to Melchiorre.

Part of the $19 million settlement is paying back that $11 million to investors. But the SEC doesn’t quite say that this is why Chatham did this. You could argue that this sort of thing — trading bonds back and forth with yourself in a way that raises their prices — is market manipulation, that the goal was to raise prices to charge higher fees. But the SEC doesn’t say that: It says, more or less in so many words, that the reason for the trading is that Chatham really liked the bonds, that it “still believed in the merits of the investment” even when it had to sell them, so it kept buying them back. The higher prices and higher fees were just a happy byproduct.

  
    
      APE Endgame
    
  

You know the story. AMC Entertainment Holdings Inc. became a meme stock, so it sensibly sold a ton of stock to raise money and pay down debt. Eventually it   ran out of stock to sell: Its corporate charter authorizes about 524 million shares of common stock, and it has sold basically all of them. Shareholders did not seem interested in amending the charter to authorize more shares, because they were worried about dilution and/or because they are retail investors who tend not to vote their shares at all. The way it works is that a majority of the outstanding shares need to approve the charter amendment to issue new shares, so not voting is the same as voting no.
But AMC’s charter also allows the board to issue “blank-check” preferred stock, that is, preferred stock with any terms the board wants. So AMC   started issuing a new type of preferred stock called APEs, AMC Preferred Equity Units, which are meant to be identical to the common stock: They have the same economic rights, same voting rights, etc. AMC did a quasi-stock-split in which shareholders got one APE for each common share they held, and then it started selling new APEs to raise more money.
Part of the plan here was just to sell APEs to raise money, but another   part of the plan was to   get the APEs to vote to amend the charter to allow AMC to issue more common shares. If that happens, the APEs will all be converted into common shares; since now the APEs trade at a discount to the common, this will be good for the APEs (and presumably bad for the common stock). Because (1) there are more APEs than common shares, (2) the APEs and common shares all vote together on all issues, including whether to amend the charter, (3) the APEs are more likely to be held by professional investors who actually vote, (4) voting to authorize more shares is strictly good for the APEs and (5) the APEs have   a clever voting mechanism where a trustee votes them even if their actual holders forget to vote, so that not voting is not like voting no — AMC figured that if it held another vote to authorize more shares, the proposal would pass with the APEs’ support.
And so AMC scheduled that vote, and   some holders of common shares sued, arguing that this is all an obvious way to disenfranchise actual shareholders. And AMC’s basic argument is, no, this is a way to enfranchise shareholders; the problem is that most retail shareholders just don’t vote one way or another, so it’s impossible to get anything done, even things that most shareholders actually want. After the shareholders sued,   AMC agreed to a “status quo order” banning it from amending the charter, issuing new shares or converting the APEs until after a hearing in Delaware Chancery Court on April 27 — but meanwhile AMC could hold the vote, basically to see what shareholders actually want. 
It held the vote last month, and   AMC, let us say, won. As a technical matter, AMC got plenty of votes to amend the charter, issue new shares and convert the APEs: A majority of the APEs voted yes, and when you throw in the clever trustee voting mechanism you get 91% of the APEs voting yes, along with 25.5% of the common stock, making up a majority of the total voting shares. And as a moral and equitable matter, the important thing is that 25.5% of the common shares voted yes and only 9.1% voted no: Most common shares didn’t vote, but almost three-quarters of those that did voted to convert the APEs.
Where does that leave us? Well, in kind of a weird place:
	It seems clearly good for AMC to authorize more shares, convert the APEs, and go back to being a normal company with normal common stock (and a lot of it to sell). Also it seems reasonably clear that this is what AMC’s shareholders — its APE holders, certainly, but also most of its common shareholders — want. This is not free from doubt — most of the common shareholders didn’t vote at all — but judging by the actual votes, it seems true.	Therefore it would be kind of bad for the court to declare the APE structure illegal: It’s a mess, it’s hard to undo, and AMC would sort of be stuck with it forever, as it seems hopeless to get the common shareholders to vote for anything.	On the other hand, it would be kind of bad for the court to declare the APE structure legal: It is a way for AMC to get around the legal requirement that a majority of its shares vote to approve new shares, and if you allow this stuff it is a potential slippery slope to other, possibly worse uses of blank-check stock. The Delaware court is not going to want to set a precedent like “if the board of directors of a company doesn’t like the way its shareholders vote, they can mess with the voting mechanics until the vote comes out the way they like.” The APEs are not quite that, but they’re not quite not that either.

So the obvious good outcome here is an out-of-court settlement in which (1) AMC gets to convert the APEs into common stock, (2) the aggrieved common shareholders get a little something to make them feel better, and (3) the court doesn’t have to rule one way or another on whether this is all legal. 
And so last week AMC  announced a settlement that would do that: The lawsuit would go away, the charter would be amended, the APEs would be converted, and the aggrieved common shareholders would get an extra share of common stock for every 7.5 shares they currently hold.
  [4]
 The result of this is effectively to have the APEs convert into common stock but at slightly less than a one-for-one conversion rate: Each APE becomes one share of common stock, but each share of old common stock becomes 1.13 shares.
  [5]
 The APEs effectively convert at about a 12% discount to the common. The average price of the APEs over the last four weeks was $1.48; the average price of the common stock was $4.60.
  [6]
 So a 12% discount is much tighter than the market discount, though also much wider than the identical economic rights that APE holders were originally promised.
And then AMC and the suing shareholders went to the Delaware judge and asked her lift the “status quo order” and let this all happen, and on Wednesday  she said no. I suppose she will wait for a hearing to decide whether to approve the settlement. There are clearly some awkward elements here:
	If the APEs were illegal, then that’s bad, and I guess she should stop them?	If the APEs were legal, then converting them at less than a one-for-one ratio to the common stock seems a little bad. (Would the APEs have voted overwhelmingly to convert last month, if they had known that the common shareholders would get some extra stock? The answer is yes, of course, but still it feels weird.)

To me those awkward elements are a good reason for the court to want a settlement — let AMC and its shareholders work this out and don’t get too involved — but I guess once the court is involved this much she has to make sure that what she’s signing off on is legal.

  
    
      Black swans
    
  

The basic idea of a “black swan fund” is that you have $100 invested in normal assets somewhere else, and you pay the black swan fund like $1 a year for insurance. In a normal year, your normal assets go up 15% or whatever and you make $15, and your black-swan premium is just an expense; you lose the dollar, for a net return of 14%. And in a catastrophic year, your normal assets go down 20% or whatever and you lose $20, but your black-swan insurance pays out and you get back $20, for a net return of 0%, which is pretty good.
What is the performance of the black swan fund in the normal year? Well, negative 100%, give or take. (These are stylized schematic numbers, don’t take them too seriously.) But the black-swan manager doesn’t think of it that way, and you probably shouldn’t either. Instead the argument is something like: “If you didn’t have this black-swan insurance, you’d have to invest much more conservatively, keep more assets in cash, etc., so your return on your $100 of normal assets would only be like 8%. But the insurance gives you the confidence to invest more aggressively, so you made 15% on your normal assets, though you paid 1% for that insurance. So really the black swan fund added 6% to your overall return.”
Fine. What is the performance of the black swan fund in the catastrophic year? Oh ha it is absolutely +1,900%, come on, it made $19 on $1 of premium. Bloomberg’s Justina Lee reported last week on   the returns at Mark Spitznagel’s Universa Investments:

Sure, all hedge funds like to put a positive spin on performance, and that’s well understood by their sophisticated clientele. But critics like Saba Capital Management founder Boaz Weinstein and Citadel’s former global head of fixed income, Derek Kaufman, say Miami-based Universa goes a step too far, cherry-picking data to burnish results. ...
The latest spat broke out on Twitter in the wake of Spitznagel’s January missive to clients. As he touted the virtues of Universa’s style of hedging, he claimed a small allocation to the money manager equated to an “annuity paying 114% a year.”
Considering that when Covid hit in March 2020, the firm said it returned 3,612% in a single month, that didn’t seem like much. But it appears to have been a final straw for naysayers such as Weinstein and Kaufman.
“None of what they are saying makes sense,” tweeted Kaufman, while Weinstein — who runs his own tail-hedge strategy in the credit realm — called the firm out for the way it calculates its figures. “Name another hedge fund or tail hedge fund that talks in returns on premia spent over some interval instead of return on assets,” he tweeted. ...
“While we cannot comment on returns, Universa Founder and CIO, Mark Spitznagel’s recent book, Safe Haven, explains in detail that the point of what Universa does is raise a portfolio’s rate of returns as a direct consequence of lowering its systematic risk,” Brandon Yarckin, chief operating officer at Universa, wrote in an email. “Contrary to Modern Portfolio Theory, this is the metric that matters, and it is demonstrably what we have done in Universa’s 15 year life to date.” …
What Universa in effect does is calculate the return on an insurance policy using only one month of premium. Conveniently ignored there is the reality that clients typically pay Universa for protection for years — a process so painful it’s known as the “bleed” — before ever cashing in. …
To compound the confusion, Universa’s AUM — now $16.4 billion — is actually defined in a regulatory filing as the “amount of equity market risk that a client seeks to protect.” That means the assets at the firm’s disposal are in practice far smaller. 

Universa’s clients have $16.4 billion of assets (somewhere else) that they protect by paying premium to Universa, and “what Universa does,” in the long term, “is raise [that $16.4 billion] portfolio’s rate of returns as a direct consequence of lowering its systematic risk.” But what Universa does in any particularly disastrous month for the stock market is earn a 3,612% return on that month’s premium. Most of the time Universa leads with the first thing — lowering systemic risk — but in the months where it 36x’s its money it leads with that.

  
    
      Things happen
    
  

First Republic  Suspends Dividends on Preferred Stock. A $1.5 Trillion Wall of Debt Is Looming for   US Commercial Properties.  European commercial real estate: the cracks are starting to show. Declines in Loan Values Are Widespread Among Banks. Lenders  Lost $301 for Each Mortgage They Made Last Year.  Deposit insurance maximization as a service. Auditors  Didn’t Flag Risks Building Up in Banks. China’s financial sector rocked by expansion of  anti-corruption drive. Private Equity’s  Food Binge Goes Sour. “The  private equity business model keeps getting democratized.” “Forty-six percent of consumer brand marketers say they will increase their  metaverse budgets this year, and only 12% say they will spend less.” “Being able to sense someone  messing with a website in real-time, moving the menu items around and forgetting to close an HTML tag here and there, is a neat feeling.” Scaramucci’s  SkyBridge Capital Was Spiraling, and Then Came FTX. Fyre Festival  II.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] The full report  is here (pdf), or you can find it at document 1242 on  the bankruptcy docket.


  [2] Data on the relevant AMI bonds is a little hard to find these days — they matured a while ago — but the SEC complaint says that “by November 2017, two of the AMI Bonds traded in Rebalancing Trades at implied yields lower than the prevailing London Interbank Offered Rate.” I don’t know what that means really, but 3-month US dollar Libor was in the 1.5% neighborhood in November 2017, and Apple’s 3% bond due 2024 traded at around 2.7% that month. Also I *remember* someone showing me these bonds and noticing they traded tighter than Apple.


  [3] “Registered investment companies,” which is the SEC’s term for mutual funds. Chatham ran a variety of funds, including hedge funds, but also including liquid alternatives funds that were registered as mutual funds.


  [4] There is also a 1-for-10 reverse stock split involved, so it’s more like if you have 750 shares now you’ll have 75 after the reverse split, and then get an extra 10 for the settlement.


  [5] That is, each share of old common stock gets a bonus of 1/7.5 = 0.1333 shares. Again, there is the reverse split, so it’s more like 10 APEs become one common share and 10 common shares becomes 1.1333 common shares.


  [6] Those are taken from Bloomberg’s HP pages (for AMC Equity and APE Equity) for 3/13/2023 through 4/06/2023.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Matt Levine's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23ciizb0.5ing/b1efdaad.gif" alt="" border="0" /></a>