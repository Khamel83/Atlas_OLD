# Money Stuff: CDS Bet Bites Carl Icahn

**Source**: inputs/saved_emails/Money Stuff CDS Bet Bites Carl Icahn_Mon,_16_Oct_2023_14-34-52_-0400_(EDT)_18b39c511d26b49d.eml
**Type**: email
**Created**: 2025-08-25T02:54:02.939564

---

Credit default swaps have two related functions: You can trade CDS to bet on the creditworthiness of some company (or country, or type of st
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Icahn CDS bet
    
  

Credit default swaps have two related functions:
	You can trade CDS to bet on the creditworthiness of some company (or country, or type of structured credit, etc.). When the company reports good earnings or otherwise seems to be more creditworthy, its CDS price will go down, and people who sold CDS will have a mark-to-market gain. When the company reports bad earnings or otherwise seems to be falling apart, its CDS price will go up, and people who bought CDS will have a mark-to-market gain.	CDS works as insurance against default. If the company (country, pool of loans, etc.) defaults on its debt, then CDS is “triggered,” the people who sold CDS have to pay some money to the people who bought CDS, and there is some fairly complex   auction process to determine how much.

Thing 1 sort of works by backward induction from Thing 2: As the creditworthiness of the issuer goes down, it becomes more likely that the CDS will trigger, which makes it more likely that CDS sellers will have to pay CDS buyers, and in broad strokes the auction process in Thing 2 means that the sellers pay buyers more the worse things end up being for the issuer. 
But that is approximate, and these things are not that tightly coupled. The actual payout mechanism, upon a default, is not simply “the CDS pays more the worse the default is.” In fact there might be an auction with different deliverable securities, and there can be a certain amount of gamesmanship in the auction, and there are various ways to affect the result to make the payout higher or lower than you might intuitively expect. We   talk from   time to   time around here about companies or investors buying or creating or hoarding or releasing securities in order to get the price of the auction closer to what they want. The outcomes can get weird. A company that collapses in a pile of rubble could have CDS that pays off zero cents on the dollar; a company that is basically fine could do a technical default and have CDS that pays off 100 cents on the dollar.
Broadly speaking, CDS is a generic bet on the issuer’s creditworthiness as long as it isn’t too close to default, but it is a hyperspecific bet on auction mechanics and deliverable securities and intra-creditor game theory when the issuer is in default. And there is a transition zone where, as the issuer’s credit gets worse, people who were reading the issuer’s financial statements to bet on its business have to switch over to start reading its bond documents to bet on the mechanics. 
And so if you buy CDS on some issuer as a bet against its economic fundamentals, and those fundamentals deteriorate, then the price of CDS will go up and you will have a big paper gain on your bet, because you are still in the zone where the CDS acts as a bet on fundamentals. Perhaps you should sell your CDS and take your profits! Or you can hold on, but as the fundamentals get even worse, they will also get less important, and the dark arts of CDS auction mechanics will become more important. 
Here’s a Wall Street Journal story about Carl Icahn:

Four years ago, legendary Wall Street investor Carl Icahn made a huge bet against the future of the U.S. shopping mall in what was called the Big Short 2.0. His wager pitted him against huge asset managers and hedge funds that routinely deal in a notoriously complex and contentious market.    
The bet used credit-default swaps, essentially insurance policies insuring bonds against losses, tied to an index tracking bundles of loans to malls and other commercial properties. Purchasers pay a monthly premium, but the policies can pay out potentially huge sums if the bonds take a loss. …
Now, Icahn, 87 years old, is watching some of his jackpot slip away. In 2022, Icahn Enterprises’ credit-default swap positions took a $742 million paper loss, according to corporate filings, and the firm’s short credit positions have also been losers so far in 2023. Adding insult to injury: When Crossgates [Mall]’s debt recently sold for nearly $100 million less than its previous value, the price was just high enough to avoid triggering a payout on some derivatives Icahn used to bet against malls.
He now claims this twist shows the deck was stacked against him by his trading counterparties, though veterans caution that markets like this one are rife with disputes of this sort.
“In many instances, it’s just a rigged market for billions and billions of dollars,” Icahn said in an interview. 

Icahn bet against the CMBX 6, an index of commercial mortgage-backed securities that was heavily weighted toward risky shopping malls, in 2019. It worked out great:

When Covid-19 hit the following year, the index crashed and the value of its derivative CDS contracts surged. Some other funds shorting the CMBX 6 sold out of positions for big profits, while Icahn’s positions gained about $900 million for the year. 
Icahn increased the size of his bet, according to financial filings. 
“A lot of these bonds now are in grave danger,” Icahn told CNBC. “It’s like selling insurance to someone who’s going to go to the electric chair in a couple of months.”

And then loans to Crossgates Mall defaulted in May 2023, and they were sold at auction, and “the servicer received a stalking horse offer of $162 million from a small Connecticut hedge fund called Cannae Portfolio Advisors,” $40 million higher than the next bid and “just enough to ensure that one of the three Crossgates securitizations would avoid losses that would trigger a CDS payout tied to certain tranches of the debt.”
Icahn bet that mall debt would perform poorly, and it did, and he made money. And then he kept the bet on, and increased it. But meanwhile the bet itself shifted: It was no longer a bet that mall debt would perform poorly; it was now a bet on how an auction for one particular loan would clear. It stopped being a bet on macroeconomic conditions, and became a bet on a poker game. He should have gotten out while he was still right.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Crypto lending
    
  

At a very high level, the way banking works is:
	People have money and would like to earn interest on it.	They put the money in the bank, which lends it to other people, who do stuff — run businesses, buy houses — with the money and pay interest to the bank.	This funds economic activity, and over time, the economy mostly grows. There are more people, more productivity, more stuff. If I take $100 from you and use it to buy a house or start a business, and I promise to pay you back $110 with the proceeds of my house or business, there’s a pretty good chance that I will be able to do that, that the thing I buy now will be worth more later. I invest the $100 in productive enterprises, those productive enterprises pay off $120, I pay back the loan with interest and have $10 left over for myself.	Obviously sometimes this doesn’t work — my business fails, my neighborhood gets cheaper — but the successes should outweigh the failures, and if banks are diversified and well capitalized they’ll be fine and can pay back their depositors.	Occasionally the whole system overreaches — all the banks decide, at once, to bet all their money on home prices going up — and the bet goes wrong and  there’s a financial crisis.

Broadly, banking is a levered bet on economic growth, and the bet is risky but usually pays off.
How does crypto banking work? I think there are three broad ways to conceive of it:
	“Crypto” and “banking” simply don’t go together. The strict view of some early crypto adopters is that crypto is an alternative to the leverage of traditional banking. Traditional banks hold your money for you and use it to make levered bets on economic growth, and that is risky, and if you don’t like it you can use crypto. You hold your money for yourself, nobody is making any bets with it, everything is transparent and on the blockchain, there are no intermediaries, there is no hidden leverage or risk of financial crisis. It feels quaint to me to even type this, but I think this view was pretty influential in the early days of crypto.	Crypto banking is just like regular banking, a levered bet on economic growth: There are crypto firms, quasi-banks, that hold people’s cryptocurrency for them and pay them interest, and they use that crypto to invest in productive enterprises that grow the economy and return enough to pay the interest. They lend out crypto to people who want to start businesses or buy homes or open factories. Anything is possible! I know from experience that if I write “you don’t hear much about people borrowing crypto to start real-world businesses or buy houses,” someone will email me to say “I have a firm that lets people borrow crypto to buy houses on the blockchain.” But … I mean … not so much?	Crypto banking is purely financial, a levered bet on the size of the crypto market. There are crypto firms, quasi-banks, that hold people’s cryptocurrency for them and pay them interest, and they use that crypto to invest in more crypto. They lend out crypto to hedge funds that want to make levered bets on crypto, and as long as crypto prices generally go up those hedge funds will make enough money to pay back the loans with interest and get rich themselves. But nothing productive is happening with these money flows; people are buying tokens but not doing any activity that makes anyone better off in the real world. Crypto prices go up because people speculate on crypto, so there is more money in crypto, so it is easier to borrow more money to make more levered bets on crypto, so prices keep going up, etc., until a slight breeze blows it all over and there’s nothing left.

I don’t want to say that that Version 3 is entirely right. Obviously some of the money that flowed into crypto produced some stuff that is still used. The market capitalization of all crypto, which peaked at   over $3 trillion in late 2021, is  about $1 trillion now, a huge crash but still a lot of residual value.
But I do think that Version 3 basically explains the crypto credit bubble and crash of 2022. Everyone in crypto wanted to pay, and receive, interest, but nobody who was paying that interest even considered investing in productive real-world businesses.
  [1]
 And so a group of crypto hedge funds sprang up that would go to crypto quasi-banks and say “we would like to do leveraged speculation on crypto” and the quasi-banks were like “great, perfect, please take all of our money,” and the hedge funds would take all the money and use it to buy, like, Luna, and then   Luna went to zero and the hedge funds were vaporized and so were the lenders.
Last week the US  Commodity Futures Trading Commission and  Federal Trade Commission brought enforcement cases against Stephen Ehrlich, who ran Voyager Digital Ltd., one of the bankrupt crypto quasi-banks. The  FTC case is straightforward but insane: Voyager was going around telling customers that their deposits of crypto at Voyager were backed by the Federal Deposit Insurance Corp., but they were not. That’s it. Voyager went bankrupt and customer money was frozen:

In another letter to the bankruptcy court, a consumer lamented that he had put his life savings as well as a portion of his paycheck every month into Voyager for the last few years. As he put it, “I used Voyager to replace my savings account as it was advertised as FDIC insured, I am now filled with regret for doing so and fear that I pretty much lost everything for trusting this company.” …
To date, consumers have not been able to recover any loss of assets through Voyager’s supposed FDIC insurance.

The  CFTC case, though, is more about the details of Voyager’s operations; the gist is that Voyager was desperate to gamble away its customers’ money, and did:

Voyager transferred large volumes of pooled customer assets to multiple high-risk third parties (including Firms A–D), without conducting sufficient diligence. In some instances, Voyager got lucky—for example, Firms B, C, and D and certain others repaid Voyager.
With respect to Firm A, Voyager was similarly reckless but, unfortunately for Voyager’s customers, far less lucky. Voyager transferred Firm A over $650 million worth of digital assets commodities—an amount sufficient to bankrupt Voyager in the event of nonrepayment—without conducting any meaningful diligence, and without obtaining even the minimal materials (such as audited financials) requested in its bare-bones DDQ [due diligence questionnaire].

Firms A through D were crypto trading firms that borrowed from Voyager to speculate on cryptocurrencies. Firm A was Three Arrows Capital,
  [2]
 perhaps the most spectacular   crypto-trading-firm failure until Alameda Research. We have   talked before about an amazing interview that Three Arrows co-founder Kyle Davies gave after the crash, in which he gloated about how little due diligence or collateral lenders demanded before giving him money. The CFTC’s Voyager complaint lays this out from Voyager’s side:
In or around February 2022, Voyager began discussing with Firm A a potential “loan” of significant assets to Firm A. However, instead of proceeding cautiously as a responsible steward of its customers’ assets, Voyager at the time focused more on the profit potential of the relationship and doing whatever was needed to clear Firm A’s onboarding process and diligence of Voyager. For example, on approximately February 7, 2022, a Voyager senior executive (“Executive 1”) communicated with Firm A regarding Firm A’s efforts to onboard Voyager for lending to Firm A and/or affiliates Firm A controlled. A second Voyager senior executive (“Executive 2”) forwarded that email to relevant Voyager personnel, writing “this one could be huge for us. Is it possible to make this a high priority item?”
Voyager tried to do some due diligence, but Three Arrows politely declined:

On approximately February 16, 2022, Firm A emailed Executive 1, Executive 2, and others, noting that Voyager would need to remove the requirement in the draft Master Loan Agreement to provide audited financial statements: “[A]s communicated we don’t send financials to lenders . . . .” Executive 2 forwarded that email internally at Voyager, asking “Let us know what you think of the attached statements. They are providing us with a [net asset valuation” (“NAV”)] statement in place of audited financials.”
An “NAV statement” was not a responsible replacement for audited financials. Instead of dozens or hundreds of pages of financial information audited by a certified public accountant, a Firm A cofounder provided a letter titled “AUM Letter” containing the following single sentence with zero supporting documentation:

The AUM letter is a bit famous; it goes like this:

To Whom It May Concern,
We confirm the following for [Firm A] as at 1-January-2022 in millions of USD.
NAV 3,729

The CFTC continues:

On February 16, 2022, the same day that Firm A responded to Voyager’s request for audited financial statements with a one-sentence letter, Firm A emailed Executive 2 and others noting that Firm A needed additional documents from Voyager to complete Firm A’s onboarding process. Executive 2 forwarded to the Voyager employee who was compiling onboarding documents as well as Ehrlich, asking the Voyager employee “Can you please help get this over the line ASAP? This is a high priority for us as they are going to be a huge borrower. Copying Steve [Ehrlich] for awareness and to let him know if you need any of his documents directly from him.” …
During the Firm A diligence process, Voyager personnel did not receive Firm A income statements, cash flow statements, balance sheets, or even a debt-to-asset ratio. Voyager did not conduct any stress testing of Firm A’s liquidity. Numerous individuals involved in the diligence process did not have a background in credit risk evaluation.

It was not just Three Arrows; Voyager was sending customer money to lots of crypto hedge funds with limited due diligence, and those funds collapsed too:
During this period, Voyager’s counterparty diligence process was broken, reflecting an inability or unwillingness to accurately assess counterparty risk. For example, on approximately January 28, 2022, Voyager completed limited diligence on Firm C, concluding it was “low risk.” Firm C later went bankrupt. Similarly, on approximately February 22, 2022, Voyager completed limited diligence on Firm B, concluding it was “low risk.” On June 13, 2022, while still officially concluding Firm B was low risk, Ehrlich privately confided to a professional athlete, “My biggest fear is that [Firm B] is a house of cards. Not for us but will blow up the industry[.]” Firm B later went bankrupt. Similarly, in connection with a prospective business relationship with Firm D, Voyager evaluated Firm D as a “low risk” counterparty. Firm D also went bankrupt in 2022.
The story here is the one Davies told: Crypto lenders were desperate to find a way to pay interest on their deposits, and had no useful place to put them. So they put them at Three Arrows, which was doing insanely risky crypto speculation and shared no information with lenders, but which had been around for a relatively long time (for crypto), and was famous, so it looked relatively safe. Relative to what, though? 
Anyway! Bloomberg’s   Olga Kharif and Anna Irrera report today:

Crypto exchanges seeking to bolster sagging revenues are stepping up lending, potentially seeding the market with fresh risks less than a year after the last major crisis.
Recently launched programs from the likes of Coinbase Global Inc. and Binance come in many different guises, from margin loans meant to stimulate trading to facilitating borrowing through their platforms to making direct loans to clients.
Crypto lending is still small compared with the leverage bubble that took down large swathes of the sector when it burst in 2022, and executives say they’ve taken pains to avoid a repeat. Yet the comeback risks creating new opaque pockets of leverage across crypto markets that could exacerbate the impact of any major correction in prices.

I suppose one broad question you could ask here is not, like, “what collateral are they getting for these loans” but rather “what sort of productive economic activity are these loans funding?” If the answer is “they are designed to encourage more trading on crypto exchanges” then, uh. 

  
    
      Bitcoin ETF
    
  

The regulatory situation in the US is that there are exchange-traded funds that allow people to speculate on Bitcoin (and Ether), but those funds hold Bitcoin (or Ether) futures, not actual Bitcoins. The US Securities and Exchange Commission has, so far, declined to approve spot Bitcoin ETFs (funds that just hold Bitcoins). It has said that this is because the spot Bitcoin market is largely unregulated and so there is a risk of manipulation, whereas Bitcoin futures trade on regulated US exchanges and so are safer. This has always   struck me as incoherent (manipulating the spot market also manipulates the futures), and in August   a federal appeals court ruled that it was “arbitrary and capricious,” which probably means that the SEC will have to approve spot Bitcoin ETFs pretty soon.
But it hasn’t yet! Bloomberg’s   Vildana Hajric reports:

Bitcoin reversed an earlier gain of as much as 10% after BlackRock said that its application for an exchange-traded fund that invests directly in the cryptocurrency is still under review.
“The iShares Spot Bitcoin ETF application is still under review by the SEC,” a spokesperson said. Bitcoin was up about 3% to $28,000 as of 10:12 a.m. in New York on Monday after briefly jumping to $30,000.
Speculation swirled on social media that BlackRock, which in June submitted an application for a spot-Bitcoin ETF, received a green-light from the US Securities and Exchange Commission to launch the first such product in the US. That spurred the surge in the largest coin, though Bitcoin quickly reversed the majority of those gains after the rumor was debunked.
Still, the episode suggests that there remains a lot of excitement and hope for a spot-Bitcoin product in the US, which regulators have in the past refused to allow. They’ve previously cited market manipulation, among other reasons, for not granting an endorsement. However, the incident also serves as a reminder that Bitcoin’s price can easily be moved by gossip or hearsay.

Again, I am not that sympathetic to the SEC’s objections to a spot Bitcoin ETF. But this story makes me a little more sympathetic? The price of Bitcoin jumped by 10% because people on social media were saying, falsely, that BlackRock’s spot Bitcoin ETF was approved. Seems like the sort of thing that could be manipulated!
Obviously the Chicago Mercantile Exchange front-month Bitcoin futures also briefly jumped above $30,000 today. If you want to move the price of Bitcoin futures with gossip and hearsay, that is pretty much exactly as easy as moving the price of spot Bitcoin with gossip and hearsay, because they are kind of the same price.

  
    
      Two sandwiches
    
  

I used to work at an investment bank and, well, I don’t want to say that I witnessed anyone abusing their meal allowance, but let’s say that I can easily imagine how it might come about. You finish work early but stay at the office an extra 15 minutes just to be able to claim your  $30 dinner allowance. Or you order your dinner and take it home to eat, rather than being chained to your desk as the meal allowance assumes. You order two cheap items, eat one, and bring one home for your partner, or for lunch tomorrow. You order dinner for a group of analysts on your desk, it comes to more than $30 per person, and you throw in the names of a few analysts who aren’t there so you can use their allowance too. Or you do one of the seven more creative minor abuses that my readers are going to email me about today.
Again, I am not saying that I witnessed any of this behavior, necessarily, in so many words. But I can imagine it. I can even imagine that the bank wouldn’t mind it that much. The numbers involved are small, relative to bankers’ pay and to the value of keeping them at work late; an analyst scheming to stay later at work is probably good for the bank. Also a certain risk appetite and ethical flexibility probably help too. It’s probably not even worth it for the bank to audit any meal receipts. If it’s under the allowance, just pay it, who cares.
On the other hand, if a bank does aggressively audit meal expenses, it might find, let’s say, many many many cases of mild meal-allowance abuse. And then it can send every involved analyst an email saying “hey it looks like you ordered two entrees with your allowance, we’re gonna deduct $11.95 from your paycheck, don’t do it again.” And then the bank would save $11.95 per analyst.
Which is not worth it. But it would also get a few analysts who write back indignantly with elaborate fictional stories about the chain of events that led to them ordering two entrees with their meal allowances. And then it could investigate those stories, and if they turn out to be false, it could fire those analysts, which is good, because they are a real compliance risk. 
Here’s  this guy:

Citibank has won an employment lawsuit against a banker who was dismissed for submitting an expenses claim that included coffee and sandwiches for his partner and lying about it.
Szabolcs Fekete, a senior analyst, sued the bank alleging unfair and wrongful dismissal after he was ousted over the expenses he submitted after a three-day work trip to Amsterdam in 2022. ...
Fekete, who had worked at Citi since 2015, travelled with his partner, who was not a bank employee, on his trip to Amsterdam the tribunal noted. He submitted his expenses claim in late July and claimed that the amounts were well within the bank’s €100 a day limit. However, a senior manager informed him that his expenses claim would be rejected because he believed the meals on the receipt had been for two people.
According to the ruling, which was made public on Friday, Fekete replied by email that: “I was on the business trip by myself and that I had 2 coffees as they were very small.”
The senior manager questioned his answer, saying: “The receipt appears to have two sandwiches, two coffees, and another drink . . . Are you advising that this was all consumed by you?”
Fekete replied: “Yes that is correct . . . On that day I skipped breakfast and only had 1 coffee in the morning. For lunch I had 1 sandwich with a drink and 1 coffee in the restaurant and took another coffee back to the office with me and had the second sandwich in the afternoon . . . Which also served as my dinner.” ...
The ruling noted that after further queries from the manager, Fekete replied: “All my expenses are within the €100 daily allowance. Could you please outline what your concern is as I don’t think I have to justify my eating habits to this extent.” ...
Later in August, Fekete confirmed that some of the food had been consumed by his partner and Citi’s investigation in October concluded that he had breached the company’s expense management policy and had lied during an internal investigation. …
The judge said in the ruling: … “I am satisfied that even if the expense claim had been filed under a misunderstanding, there was an obligation upon the claimant to own up and rectify the position at the first opportunity. I accept that the respondent requires a commitment to honesty from its employees.”

Should a senior manager have spent time haggling over a €100 meal bill? Not as such, no. Should a senior manager have spent time investigating and firing a guy who invented elaborate lies to tell his boss in order to cover up an unjustified free sandwich? Yes? That’s bad? Being aggressive with expense reports, meh, whatever, maybe on balance a good trait in an investment banker. But writing tons of easily checkable lies in email and being indignant about it just seems like a bad compliance risk.

  
    
      Zuzalu
    
  

I guess some foundational questions in crypto are, if you got all the most dedicated crypto enthusiasts in the world together in one place and let them build a new society together, would that new society run on the blockchain? Would it use cryptocurrency for payments? Lol, no. Ethereum founder Vitalik Buterin threw a two-month-long Ethereum conference at a resort in Montenegro, and his report on the experience is thoughtful and candid:
Crypto payments, a long-time dream of the Bitcoin and Ethereum communities, were present but limited. No one even considered governing Zuzalu with a DAO, a decentralized autonomous organization running on a blockchain. A two-hundred-person community lasting for two months was either too short, too small, or both for such a thing to really make sense. But these two dreams are important enough that future experiments, whether run by the Zuzalu community or by independent spinoffs, will undoubtedly make a much more concerted effort to realize them.
Blockchain governance and crypto payments might still conquer the world, but they couldn’t conquer the two-month Ethereum co-living experiment.

  
    
      Compass
    
  

I do not have that much occasion to cover financial-industry-adjacent puzzle hunts in this newsletter, but I do have a   little, so  I will mention that the Compass hunt was this past weekend. Sadly I missed it   again, but congratulations to Midnight Marauders, this year’s winning team. 

  
    
      Things happen
    
  

The   Goldman Banker on a Crucial Mission to Help Juice Its Stock.  Trading Stocks Loses Its Thrill: ‘I Would Get Burned.’ Ozempic Is Obviously Good For Business. How  Evergrande’s Chief Tried to Turn Things Around—and Failed.   Rite Aid Files for Bankruptcy as Debt Load, Opioid Risk Rise. These Companies Are Being  Squeezed by Higher Rates. Time Is Running Out for the ‘  Year of the Bond’ as Losses Mount. SEC’s New   Hedge Fund Rules Lack an Accountant’s Precision. Citigroup’s Fraser Plans to Remove   Five Management Layers in Reorganization.   Schwab’s Net Interest Revenue Falls 24% From Client Cash Moves. Why the U.S. Government Has  $5 Billion in Bitcoin. M.B.A. Job-Offers in Short Supply as Tech, Finance, Consulting  Dial Back Recruiting. The Ivy League  Doesn’t Want Frasier Crane. Introducing The Businessweek Show With Max Abelson. 
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] Except, ironically,   FTX and Alameda Research, who were sending customer money into all sorts of non-crypto venture investments, a few of which — in artificial intelligence, for instance — might pay off. Oh and possibly   Tether, who for all I know might have been investing a lot of crypto money in   Chinese real estate.


  [2] You can tell because the “NAV statement” cited in the CFTC complaint  is famous.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cjo8xk.5hv0/3b97cff3.gif" alt="" border="0" /></a>