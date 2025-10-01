# Money Stuff: Keeping Track of Crypto Is Hard

**Source**: inputs/saved_emails/Money Stuff Keeping Track of Crypto Is Hard_Mon,_21_Nov_2022_14-12-50_-0500_(EST)_1849b9e20e40c56f.eml
**Type**: email
**Created**: 2025-08-25T02:54:09.923030

---

At its core, the vision of crypto is about finding a better way to keep a list of who has money. Society has, over the centuries, evolved so
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Sources of truth
    
  

At its core, the   vision of crypto is about finding a better way to keep a list of who has money. Society has, over the centuries, evolved some decent ways to keep those lists. There are banks, and your money consists mostly of deposits at banks, and the banks keep lists of who has money. In the olden days they would keep the lists on paper, but in modern times they keep the lists on computers. At a high level, their processes are easy to describe: My bank keeps a record of how much money I have, and when I send money to you my bank decreases the money in my account and tells your bank to increase the money in your account. In practice there are ways for this process to be messy and complicated and error-prone. My bank and your bank might run on different systems and have different views of the world, and information and transactions can be delayed, and our transaction might have to happen quickly and with imperfect information, and then later there might have to be a tedious manual reconciliation process where my bank double-checks to make sure I actually had the money in my account, etc. Banks are in a lot of businesses, but one business that they’re in is the technological business of keeping track of the money and making sure that it moves reliably to where it’s supposed to go.
And then crypto came along and promised, among other things, better list-keeping. When I send crypto to you, we do it on the blockchain, a distributed database that keeps a record of who has how much crypto. The blockchain is trustless and decentralized: Instead of relying on a bank to get it right, we can be sure that the code of the blockchain gets things right. It is censorship-resistant: No one makes ad hoc decisions about what transactions to allow or forbid; all transactions that meet the open public requirements go through. It is immutable and public: If I send Bitcoin to you, I can’t take it back, and everyone can verify that you have it and I don’t. There are costs to this — the blockchain is kind of a slow database, and the Bitcoin blockchain wastes a lot of energy — but it keeps a good list.
One thing that this was supposed to do was disrupt banks: If we can send money to each other on the blockchain, who needs banks? But the banks also saw some advantages to this technology. If there was some distributed database that provably contained each transaction in the right order, then a lot of the manual messy error-prone business of banks could be simplified. Instead of you and me agreeing to a trade over the phone, and then our back-office staffs getting together to figure out the details of what we actually traded, everything could happen in real time on the blockchain. In a perfect world, all of the systems at all of the banks would have access to the same single distributed ledger, instead of all keeping their own slightly different lists and struggling to reconcile them.
And so, around 2017, there was a huge vogue for blockchain projects at banks, projects to put stock settlement or loan trading or bank accounts “on the blockchain.” The traditional financial system wanted to learn from crypto, to import its technical best practices, so that it could improve how it kept track of the money. As I said, this was in 2017, and since then no one has really heard much about these projects, so I’m not sure there was all that much for the financial industry to learn. Still, a nice effort.
Meanwhile crypto built its own financial industry, with its own quasi-bank-like institutions, and what is striking about a lot of that industry is that:
	It uses the same basic processes — keeping centralized secret records of account balances on computers, with a certain amount of sloppy manual reconciliation — as traditional banks; and	It is … worse … at it than the banks?

To exaggerate slightly, many of crypto’s “centralized finance” companies learned no lessons from the blockchain, but they also learned no lessons from traditional finance. They were like “hey you know what’s a good way to keep track of customer transactions, we’ll write them down on some scraps of paper, then we’ll shuffle those scraps together and spill coffee on them, that should be great.”
We have   talked a   lot recently about the implosion of FTX Trading Ltd., Sam Bankman-Fried’s crypto exchange, which was until recently considered one of the more regulation-friendly and technologically advanced crypto exchanges. FTX went bankrupt mostly because it turned out it had sent billions of dollars of customer money to its affiliated trading firm, Alameda Research. That’s bad, and there are various ways that it could have been bad (many involving fraud), but Bankman-Fried has claimed that it was bad specifically in a forgetting-where-we-put-the-money way. “It looks like people wired $8b to Alameda and oh god we basically forgot about the stub account that corresponded to that and so it was never delivered to FTX,” was  his summary to Kelsey Piper at Vox. “The FTX Group did not keep appropriate books and records, or security controls, with respect to its digital assets,” was how FTX’s new chief executive officer  put it to the bankruptcy court, and: “Because of historical cash management failures, the Debtors do not yet know the exact amount of cash that the FTX Group held.” Keeping track of how much cash you have: Not as easy as it sounds!
This weekend, FTX disclosed a  list of the top 50 creditors in its bankruptcy. All the names are redacted, so it’s not all that interesting, though the biggest creditor has an unsecured claim of $226.3 million, and the top 10 — all listed as customers — all have nine-digit claims.
  [1]
 The total claims of the top 50 creditors   come to about $3.1 billion. But the list also contains this caveat:
PLEASE TAKE FURTHER NOTICE the Top 50 List is based on the Debtors’ currently available creditor information, including customer information that was able to be viewed but is not otherwise accessible at this time. The Debtors’ investigation continues regarding amounts listed, including payments that may have been made but are not yet reflected on the Debtors’ books and records. The Debtors are also working to obtain full access to customer data.
FTX does have a list of its customers and how much it owes them. But it can’t edit that list, and it is not confident that the list is right. It’s possible that it paid some of those customers back but didn’t write those repayments down. Keeping a list of customer account balances is just about possible, but making sure that the list matches reality at any point in time is hard work, and FTX is not sure that it did it.
Another bankrupt crypto company is Celsius Network LLC, which melted down over the summer. On Saturday, Celsius’s bankruptcy examiner  filed a report about what it did with customer money. Celsius took customer money in two basic ways:
	“Earn,” where customers deposited crypto assets with Celsius and Celsius used those assets to try to make a return, paying the customers interest on their assets. Like a bank.	“Custody,” where customers deposited crypto assets with Celsius and Celsius just held onto them for the customers, not making any use of them to earn returns. “Crypto assets in a Custody account were not eligible for rewards, and under a new Terms of Use, title	remained with the customer; Celsius stated that it would ‘not transfer, sell, loan or otherwise rehypothecate’ those Custody assets.”

Obviously we’ve heard that before and, in crypto, it would not be all that surprising to learn that Celsius took the “custody” assets, which it had promised not to “transfer, sell, loan or otherwise rehypothecate,” and just stole them. But in fact it did not! It did its best to keep the custody assets separate and hold them on behalf of its customers. But its best was not, objectively, great:

Due to time pressure and lack of engineering resources, Celsius chose to rely on manual reconciliations and transfers of crypto assets without robust controls for the Custody program, with aspirations of developing a more effective process later. …
To fund Custody accounts, Celsius moved crypto assets out of its commingled Main wallets into separate wallets designated for the Custody accounts. Because the crypto assets in the Custody wallets all arrived in aggregate transfers from Celsius’s commingled Main wallets, Celsius did not treat any particular asset in the Custody wallets as belonging to any particular customer. And due to the decision not to develop a separate Custody infrastructure, when customers transferred new crypto assets into a Custody account, the crypto assets were deposited in the same manner as they had been under the Earn program. Celsius’s Custody program did not automatically balance the number of coins reflected in Custody accounts to the number of coins held in the Custody wallets. Celsius had to manually reconcile those balances. Celsius performed this reconciliation 53 times during the 83-day period between April 20, 2022 (when it first reconciled the Custody wallet holdings to the Custody accounts) and July 12, 2022 (the day before Celsius filed for bankruptcy). Celsius did not have any memorialized rules or policies to guide this reconciliation process.
Celsius had a shortfall in its Custody wallets on 16 dates between April 20, 2022 and July 13, 2022. To cover these shortfalls, Celsius moved crypto assets from its Main wallets. And when there was an excess in the Custody wallets, Celsius moved the coins back to its Main wallets.

The report is fascinating in its boring details. Here you have a financial company that is fairly new and inexperienced, with a lot of money coming in and not that many people to deal with it, in a novel and under-regulated corner of finance. It wanted to take crypto from customers and hold onto their crypto for them, but the crypto all came in through the front door and mixed together:

From a blockchain perspective, a customer’s crypto assets were, in fact, not initially transferred to a Custody wallet at Celsius. Instead, as an initial step, the customer’s assets were transferred to a user- and asset-specific bridge wallet. … Celsius then periodically “swept” the bridge wallets, collecting assets transferred there through an automated process and then transferring them into Celsius’s aggregated (or Main) wallet for that currency. Celsius conducted these sweeps “as soon as [it] [could],” but Mr. Tappen [Dean Tappen, a “coin deployment specialist” at Celsius] acknowledged that there was sometimes a delay.
Following the Custody program’s launch, as had been the case pre-Custody, the majority of crypto assets were first swept into Main wallets regardless of whether the customer had marked a transaction for their Earn or Custody accounts. That is, assets in the bridge wallets were swept into the Main wallets for that particular asset, where all assets were commingled with other customer deposits. ...
Celsius did not automatically move crypto assets it had swept into the Main wallet from “Custody” customer bridge wallets to a Custody wallet. Nor did Celsius move coins into a Custody wallet for each deposit that a Custody customer made. Instead, on a periodic basis, Celsius performed a manual reconciliation … between what customers had deposited into (or withdrawn from) their Custody accounts and the amount of each respective crypto asset actually held in Celsius’s Custody wallets in Fireblocks. Based on that aggregate reconciliation, Celsius would either add (if the net Custody balances had increased) or remove (if the net Custody balances had decreased) coins from the Custody wallets. ... 
There was no automated process to carry out any reconciliation—all transfers were done manually by Celsius personnel. At no point in time were a customer’s crypto assets moved into a Custody wallet created for that individual customer because no such individual Custody wallets exist. 

There is some imprecision here due to, among other things, timing: “Although Celsius ran a 24/7 business that operated on a global scale, it did not perform reconciliations over weekends,” and it moved coins between its main and custody wallets once a day. This created a risk that the custody accounts would be underfunded: If people tried to deposit a lot of Bitcoins into custody accounts on a Saturday, those Bitcoins could sit in Celsius’s commingled main wallet until Monday; customers would think they had more custody coins than were actually in the custody wallets. Celsius dealt with this risk crudely, by trying to just overshoot a bit in its daily reconciliation
  [2]
:
Celsius added a “buffer” to this total customer balance, a cushion intended to ensure that the Custody wallets did not suffer a shortfall of coins at any given time. The buffer also minimized the frequency with which it was necessary for Celsius to move coins in and out of Custody wallets. Celsius contemplated a 10% buffer, though in practice it varied based on coin type from between 5% and 10% of the aggregate Custody account balance.
But sometimes there were too few coins in the custody account, and then it had to go borrow them to make up the difference:
 

Celsius transferred crypto assets to cover the shortfall from Main or, if there were insufficient coins in Main (particularly when there was a significant variance in illiquid assets, known internally as a “material break”), they enlisted assistance from its Treasury department. Treasury used its familiarity of the liquidity of each asset based on Celsius’s deployment strategy to determine the most efficient and cost-effective way to access coins and transfer those assets into Custody to “true up” Celsius’s account balances.If there was a surplus in the Custody wallets, Celsius typically moved excess crypto assets from Custody to Main wallets so that it could deploy those crypto assets for its investment activities.
To cover shortfalls for certain crypto assets, Celsius noted a “need to source” the coins. When sourcing coins, Treasury first looked to its undeployed, liquid assets, and transferred those crypto assets to Custody. If there were insufficient undeployed assets to source the coins, Treasury evaluated which strategies to unwind, which could depend on the relative liquidity (i.e., time it would take to unwind) and the annual percentage yield (i.e., the opportunity cost of unwinding the strategy). Treasury could also borrow from DeFi, but Celsius took the position that it would not purchase coins to fund Custody. As a result, Treasury did not always source sufficient coins to cover every shortfall.

Every decision here is understandable, but annoying. There is no horrific malfeasance; there are just, like, Google Sheets:

In May 2021, Celsius began tracking its assets and liabilities in a Google Sheets workbook, referred to as the “Freeze Report.” Celsius prepared these reports initially on a weekly basis and then more frequently over time.The Freeze Report provided a moment-in-time “snapshot,” an approach deemed necessary because the amounts and value of Celsius’s, and its customers’, crypto assets were constantly changing. …
Prior to the creation of the Freeze Reports in May 2021, Celsius did not have a method to track its assets and liabilities in a single location, but instead went “into each wallet” manually to check balances. Celsius created the Freeze Report as part of a broader effort to “build a more organized process,” including a variety of financial reports aimed at informing “more educated” decisions. …
Following the April 15, 2022, launch of Celsius’s Custody service, Celsius began reporting Custody asset balances in the Freeze Report, drawing on the balances of Celsius’s Custody wallets. That is, the Freeze Report pulled data directly from the Fireblocks API, which showed exactly how much of each crypto asset Celsius actually held in its Custody wallets. Accordingly, this data represented the amount of crypto that Celsius actually held in Custody accounts (i.e., assets), rather than the amounts reflected in individual customer Custody accounts (i.e., liabilities).
Celsius did not track coins held in Custody accounts as a separate liability on the Freeze Reports until May 9, 2022, 24 days after Custody’s launch. Beginning on May 9, 2022, Celsius added a new column to the Coin Stats sheet that compared the dollar value of Custody assets (as pulled from Fireblocks) to the Custody liabilities, calculated on a coin-by-coin basis. This data point— which allowed Celsius to determine whether customer Custody assets exceeded what Celsius had placed in the Custody wallets—was referred to as the “Custodian Reserve” balance. Of note, on the first day Celsius recorded the Custody liability, it recorded a negative Custodian Reserve of $103,300.

One thing that I say a lot around here is that crypto is engaged in re-learning the lessons of traditional finance. The last few weeks have been very educational! There have been some good lessons about the value of things like lenders of last resort and public disclosure and regulation. But I want to say here that one lesson crypto is relearning is about the value of having a good accounting system for keeping track of where the money is. Naively you might have expected crypto to already know that!
  [3]
 Naively you might have expected crypto to be better at that than traditional banking; naively you might have expected that to be a particular strength of crypto. But, nope. 

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Blockchain blockchain blockchain
    
  

Well, it is more embarrassing to have anything to do with crypto today than it was two weeks ago. Two weeks ago, if you were at a traditional financial institution, and you were working on their blockchain project, look, that was a lot less cool than it was in 2017 when everyone launched their blockchain projects, but it was fine. “Oh right the blockchain project,” people would shrug. Today, less so.  Anyway:

Australia’s stock exchange has apologised for abandoning a years-long plan to upgrade its clearing and settlement system to a modern blockchain-based platform after a series of delays.
The Australian Securities Exchange’s move to drop the upgrade of its clearing housing system calls time on a project that critics say has cost the country its head-start in developing a more efficient trading system.
Damian Roche, chair of ASX, apologised for the disruption caused by the botched upgrade. “We have concluded that the path we were on will not meet ASX’s and the market’s high standards. There are significant technology, governance and delivery challenges that must be addressed,” he said.

I feel like “upgrade its clearing and settlement system to a modern blockchain-based platform” sounded very plausible and cutting-edge in 2015, when this actually launched, but now it has a weirdly retro feel.

  
    
      
        
      
    
  


  
    
      Grayscale
    
  

When a big crypto company goes bankrupt for misusing customer money, there are at least two possible vectors for contagion:
	Other big crypto companies that were customers of or lenders to that big crypto company might have lost money, possibly rendering them insolvent, and there will be rumors and worries about what companies were exposed and how bad things could be.	Other big crypto companies will get questions like, “well, wait, if those guys were a big scam, does that mean that you are also a big scam?”

The Grayscale Bitcoin Trust is a publicly traded investment company registered with the US Securities and Exchange Commission that just holds a bunch of Bitcoin. It files  audited financial statements saying how many Bitcoins it has. Do you believe those statements? Should you? Here I want to emphasize that nothing in this column is ever investing advice, particularly about crypto, dear lord, but still I must confess my bias that I think that most audited financial statements of most US public companies are mostly true. Obviously one can get up to a lot of nonsense with accounting, but Grayscale’s accounts are extremely simple, and presumably the audit consists mostly of checking to see if the Bitcoins are there. Is it possible for auditors to get that one wrong? I mean, the probability is not zero. Me, though, I like an audit.
Grayscale is now trading at about a 45% discount to its net asset value, meaning that $100 of Bitcoin in Grayscale’s pot of Bitcoin is worth just $55 on the stock market. Part of the reason for this is market concern about  contagion to Grayscale’s parent company, Digital Currency Group, whose Genesis trading unit paused redemptions last week due to FTX fallout. But part of it seems to be about not trusting anyone.  CNBC reports:

Grayscale, the asset manager running the world’s largest bitcoin fund, said in a statement that it won’t share its proof of reserves with customers.
“Due to security concerns, we do not make such on-chain wallet information and confirmation data publicly available through a cryptographic Proof-of-Reserve, or other advanced cryptographic accounting procedure,” said a statement Friday.
Following the implosion of FTX and its subsequent bankruptcy proceedings exposing that customer funds were missing, multiple crypto exchanges have jumped to release proof-of-reserve audits in order to assuage investor concerns over the safety of their funds. Others, like Binance, say they soon plan to do so.
Grayscale wrote in a tweet that it realized that failing to disclose a proof of reserves would be a “disappointment to some,” but added that a “panic sparked by others is not a good enough reason to circumvent complex security arrangements” that have kept its investors’ assets “safe for years.”

Here is Grayscale’s statement on “Safety, Security, and Transparency”: 
Due to recent events, investors are understandably inquiring deeper into their crypto investments. Custody of the digital assets underlying Grayscale’s digital asset products is unaffected, and our products’ digital assets remain safe and secure. 
It links to  this letter from Coinbase Custody Trust Co., which holds Grayscale’s Bitcoins for it, and which “writes … to reaffirm that the assets underlying all of Grayscale’s digital asset products held at Coinbase Custody, as listed in the table below, are secure”:
As background, Coinbase Custody is a wholly-owned subsidiary of Coinbase Global, Inc. (NASDAQ:COIN), and is licensed to custody client digital assets as a New York-chartered limited purpose trust company. Coinbase Custody has been regulated by the New York State Department of Financial Services since 2018, the same regulator that oversees the United States’ biggest banks. Coinbase Custody also services as a fiduciary, which means that it is required to always act in its clients’ best interest under New York Banking Law.
Does any of this stuff count as proof that the Bitcoins are there? I mean, yes, in the sense that I am used to. This is several people representing, in effect:
	We work at big regulated financial institutions and have a lot to lose.	We say the Bitcoins are there.	Regulators are aware of these statements, and if we are lying they will notice.	If they notice that we are lying, we will get in bad trouble.

Those things, to me, are persuasive; they more or less qualify as proof in the US legal and financial system. But they will not necessarily be persuasive to every crypto investor. Some people want cryptographic proof.
One thing that I will say is that, while crypto in theory is supposed to avoid the need to trust centralized intermediaries, in practice there is a huge market for trusted central intermediaries in crypto. It is just sort of a diverse market; there are many flavors of trust, with different people looking trustworthy in different ways to different audiences. Alex Mashinsky, who ran Celsius, appealed to people who do not trust traditional finance: “Either the bank is lying or Celsius is lying,”   he told them about his promised above-market interest rates, possibly with a straight face. Sam Bankman-Fried, who ran FTX, appealed to people who like traditional finance (he came from Jane Street and pushed for more regulation) but also want to shake it up a bit (he wears shorts and played video games during pitch meetings). 
Grayscale and Coinbase, meanwhile, appeal to people who trust SEC filings, people who trust regulation and audits and the legal system and the traditional social systems of trust. There are people in the world, and I guess I am one of them, who think things like “ah, right, an audited balance sheet filed with the SEC under penalty of fraud charges, that's probably pretty reliable.” That is sort of the main way that trust works in the traditional financial system. In crypto there are alternatives, and there are trends in trust. Sometimes everyone trusts everything. Other times, nobody trusts anything.

  
    
      Elsewhere in FTX
    
  

On Friday,  FTX announced that it was “launching a strategic review of their global assets to begin to maximize recoverable value for stakeholders,” engaging Perella Weinberg Partners LP to try to sell “many regulated or licensed subsidiaries of FTX,” the ones that “have solvent balance sheets, responsible management and valuable franchises.” If you run a big sprawling crypto trading enterprise, and your main enterprise loses a ton of money on bad trades and finds itself insolvent, then there might be lots of other barely-related businesses that are perfectly solvent and keep operating normally, and you can sell them off to raise money to pay off creditors of the main business. If on the other hand the main enterprise steals a bunch of customer money, that sort of makes everyone else look bad? Harder to find buyers, in that case. I suppose the argument is that the more regulated subsidiaries were not in on any wrongdoing.
Elsewhere, “People Are Already Buying Depositor Claims on FTX,”   reports Joe Weisenthal:

It looks like some traders who have money stuck on the fallen cryptocurrency exchange FTX are already selling their claims in over-the-counter trading.
Thomas Braziel, the founder of 507 Capital, who has been active in past crypto bankruptcies, says he’s currently seeing claims being sold “between 5 cents and 8 cents on the dollar” in private offerings. …
To Braziel, the math behind a good scenario would look something like this: If you figure there’s something around $10 billion of total stuck deposits, the hope would be that the venture-capital portfolio ends up at around $1.5 billion in value, the liquid crypto portfolio hits $1 billion, and creditors are able to claw back $1 billion from individuals and related entities. Lop off, say, $500 million for legal fees and expenses, and you’re left with $3 billion, which would price deposits at roughly 30 cents on the dollar.

All bankruptcies are expensive but $500 million just seems like a lot? It does feel like, if FTX had done a better job of keeping track of its assets and its customers, it might be able to save a bit of money now on legal fees? As it is, its current management has to sort of reconstruct the business from scratch, and that’s expensive.
And in limits-to-arbitrage news,   here is Bloomberg’s Justina Lee:

The wild-west days of crypto markets are back again as the large trading houses that once thrived on arbitraging price gaps pull back in the wake of FTX’s collapse. That’s opening up profitable opportunities for anyone that still dares to trade. 
Prices for essentially identical assets on various platforms are diverging in a clear sign the dominoes are still falling across the crypto trading world. The gap between the funding rates of identical Bitcoin futures on Binance and OKX, for instance, has been as wide as an annualized 101 percentage points and remained at least 10, compared with mostly single-digit gaps last month. 
It’s a throwback to the early days of crypto, when speculators -- including former FTX Chief Executive Officer Sam Bankman-Fried himself -- found easy money simply buying one asset on an exchange and selling it for more on another. It’s a lucrative form of quantitative trading, which uses algorithms to profit from these price gaps. But as more sophisticated Wall Street converts entered the crypto markets, those differences shrank, making it harder to make money on the strategy.
Now with FTX’s demise sending chills through cryptocurrency markets, these players -- including both big and obscure quant funds -- are shrinking positions or even closing shop, causing these mispricings to stick around for longer. 

I think of arbitrage as being a necessarily leveraged strategy: The only reason you are buying widgets at $100 one place and selling them for $100.01 somewhere else, making a 0.01% profit, is because someone is lending you most of the $100.
  [4]
 When banks get nervous about lending to hedge funds, arbitrage spreads open up, because the leveraged players who usually close them can’t afford to anymore. When everyone in crypto is nervous about lending to everyone else in crypto, nobody can do the arbitrage trades.

  
    
      Things happen
    
  

Disney Shares Soar on   Iger Return as CEO After Shock Ouster. Was This $100 Billion Deal the  Worst Merger Ever? Companies Brace for  Onslaught of New Activists After Change in Proxy-Voting Rules. Onetime Trump Appointee Helps Spark Sweeping   ESG Backlash. Masayoshi Son owes $4.7bn to SoftBank following tech rout. Paramount  Won’t Support Appeal of Ruling That Blocked Simon & Schuster’s Sale to Penguin. Hedge Fund  Sculptor Resolves Legal Fight With Its Billionaire Founder. Tesla Board’s View That  Elon Musk Is Irreplaceable Emerged in Pay Trial. Musk Fires More Twitter Sales Workers After   ‘Hardcore’ Purge. Eli Manning Gets Into Dealmaking Mode By  Practicing PE Pitches With Family. Desperate for Growth, Aging Casino Company Embraced ‘Degenerate Gambler.’ From Trinity to  Liquidity. How Colleges and Sports-Betting Companies ‘Caesarized’ Campus Life. Jacques Derrida Loves This  Banana Bread. Guy Linked to Huge Crypto Meltdown Says It’s Just a Coincidence That He’s Hanging Out in a Country With No Extradition to United States.  Helium founder races cars while the crypto startup is on collision course.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] In dollars. All of the claims are in dollars; it’s not clear to me if FTX owed some of these creditors amounts denominated in crypto, or exactly how its new management converted those claims to dollars.


  [2] The buffer created its own problems, since 5% to 10% of the coins in each custody wallet belonged to Celsius, and — outside of its custody business — Celsius was in the business of lending, trading, hedging, etc. its cryptocurrency. So it had some trouble keeping track of its own coins when they lived in the custody wallets: "This initial imbalance created accounting issues for Celsius. As Chris Ferraro, Celsius’s then-Head of Financial Planning & Analysis and Investor Relations and now Interim CEO, explained in an email on April 19, 2022, 'custody is not on our balance sheet' and 'so should not be part of net exposure we manage from deployment/risk perspective.' Dean Tappen, Celsius’s Coin Deployment Specialist, responded that 'currently we have sent more coins to our custody account than Users balances flagged as Custody' and that 'methodology … is making it really difficult to access our net positions.'"


  [3] By the way. Back in 2019, I made fun of a JPMorgan Chase & Co. blockchain initiative, and in the course of doing so   I wrote: “If you have U.S. dollars in a bank account at JPMorgan Chase & Co., and I have U.S. dollars in a bank account at JPMorgan Chase & Co., and I want to send you 100 of my dollars, what we do is I tell JPMorgan to subtract 100 from the number of dollars in my bank account and add 100 to the number of dollars in your bank account. This gets dressed up in a lot of procedures, because it would be bad if JPMorgan got the math wrong or if it moved money from one account to another without getting the proper authorizations, but as a matter of, like, computer science, it is dead easy.” I got a  frankly hilarious amount of pushback from computer scientists saying that this is not at all a trivial problem, that maintaining this list in a way that is uniform and consistent and accessible across JPMorgan is hard computer work, and that I was being naive in thinking that it’s easy for JPMorgan to do arithmetic to its list of dollars. Reading the Celsius examiner’s report drives home that they were right. One can’t just write down a list of account balances and update it for transactions! 


  [4] And, often, the widgets: Arbitrage trades often require short selling.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23chpywq.5iq2/a67c12ee.gif" alt="" border="0" /></a>