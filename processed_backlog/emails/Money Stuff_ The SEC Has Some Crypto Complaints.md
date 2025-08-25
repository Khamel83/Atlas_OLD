# Money Stuff: The SEC Has Some Crypto Complaints

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Mon, 9 Aug 2021 12:54:53 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff The SEC Has Some Crypto Complaints_Mon,_9_Aug_2021_12-54-53_-0400_(EDT)_17b2bd7142862805.eml
**Processed:** 2025-08-24T19:13:10.009818



  
  
    
      
        
          
            
          
        
      
      
      
    
  
  
  
    
      
        
          
  
    
      SEC v. DeFi
    
  
I have  been saying for a while that the next front in the fight over crypto regulation is going to be about decentralized-finance (DeFi) lending protocols. The rough idea is: 	People put cryptocurrency into a pot.	Some smart contract uses the cryptocurrency in the pot to make a profit, e.g., by lending the cryptocurrency to people who want to use or short it, or as capital for automated market making.	The people who put their cryptocurrency into the pot share in the profit. Generally the pot pays a yield to its investors, either a fixed yield or one based on the returns the smart contract earns.	Also, sometimes, the investors get “governance tokens,” which loosely speaking represent something like equity ownership of the pot, the right to decide how to run the pot, etc.If you replace the words “smart contract” in that description with the word “person” (or “company,” etc.), you have a classic description of an “investment contract.” Under the “Howey test” of U.S. securities law, an investment contract is “the investment of money in a common enterprise with a reasonable expectation of profits to be derived from the efforts of others,” which is, straightforwardly, what this is. An investment contract is a type of security, and a security is subject to regulation by the Securities and Exchange Commission. If you sell securities to the public, you generally have to register them with the SEC, deliver a prospectus, have audited financials, etc. Or you can sell them under some exemption from those rules — for instance, if you only sell them to non-U.S. persons, or if you only sell them to “accredited investors” (meaning, roughly, rich people). It seems to me that it would be quite inconvenient for DeFi to be subject to these rules, and that a lot of people in the DeFi world would prefer to be exempt from them, or ignore them.Now, if you don’t replace the words “smart contract” with the word “person,” I am not quite sure that what you have is a security under U.S. law. Perhaps you could argue that the workings of the smart contract are not “the efforts of others”: Sure the smart contract was written by some programmer, but its operation is (let’s assume) deterministic and open-source; you are (arguably) not investing money because you trust the programmer to do something but because you can read the code and know what it will do. You are not funding a business but putting money into a machine that makes money come out; you can examine all the moving parts of the machine, see how it works, and trust in that rather than in “the efforts of others.” I don’t know that that’s a very good argument — I do not think that the SEC would agree with it — but, you know, it’s an argument; it’s interesting. Also there is the practical point that if investors put their cryptocurrency into a pot controlled by a smart contract, it is not controlled by people, so there is — not quite “nobody for the SEC to sue,” it could sue the programmers who wrote the contract or the people who promoted it on social media, but there is not really an issuer of the security to sue in the same sense that there would be for a stock offering by a company. The point here is that there is some genuine novelty in DeFi; it is really unlike the sorts of securities offerings that were on Congress’s mind when it passed the core U.S. securities laws in the 1930s. But it is mostly analogous to those offerings, so there is going to be trouble.Here’s an SEC action against a DeFi protocol from last Friday:The Securities and Exchange Commission today charged two Florida men and their Cayman Islands company for unregistered sales of more than $30 million of securities using smart contracts and so-called “decentralized finance” (DeFi) technology, and for misleading investors concerning the operations and profitability of their business DeFi Money Market.   According to the SEC’s order, Gregory Keough, Derek Acree, and their company Blockchain Credit Partners offered and sold securities in unregistered offerings through DeFi Money Market from February 2020 to February 2021. The order finds that they used smart contracts to sell two types of digital tokens: mTokens that could be purchased using specified digital assets and that paid 6.25 percent interest, and DMG “governance tokens” that purportedly gave holders certain voting rights, a share of excess profits, and the ability to profit from DMG governance token resales in the secondary market.The defendants settled by paying back $12.8 million that they raised and agreeing to fines of $125,000 each. The SEC order is worth reading for its legal analysis of DeFi protocols. This protocol involved two tokens, one paying a fixed rate and another “governance token”:They sold two types of digital tokens: mTokens, which accrued 6.25% interest, and DMG tokens, which were so-called “governance tokens” that purportedly gave DMG token holders certain voting rights, a share of excess profits, and the ability to profit from DMG resales in the secondary market. Respondents promised to pay a stable interest rate to digital asset owners who purchased mTokens and said they could generate excess profit for DMG token owners. During the Relevant Time Period, they sold approximately $17.7 million in mTokens and more than $13.9 million in DMG tokens to the public, including U.S. investors.The governance tokens “were offered and sold as investment contracts and thus were securities,” says the SEC, and I don’t know how you could argue otherwise. This is not the sort of DeFi protocol where everything operated automatically and deterministically; the “smart contracts” involved here governed the investors’ investments and the promoters’ draws on those investments, but once the promoters took the money they made decisions about how to invest it to try to maximize profits. So, sure, securities.The 6.25%-interest mTokens are a bit of a harder question, because you could argue that those are not an “investment contract” but rather just a loan. If I borrow money from you at a fixed interest rate, that is not necessarily a security, even if I use the money to fund some harebrained get-rich-quick scheme. But the SEC argues that these tokens are “notes,” and the kind of note that counts as a security:A note is presumed to be a security unless it falls into certain judicially-created categories of financial instruments that are not securities, or if the note in question bears a “family resemblance” to notes in those categories based on a four-part test. …Applying the Reves four-part analysis, the mTokens are securities. First, Respondents sold mTokens to raise funds for the general use of its business, namely to purchase income-generating assets to pay interest on redeemed mTokens and excess interest to DMG token holders, and purchasers bought mTokens solely to earn 6.25% interest on their digital assets. Second, mTokens were offered and sold to the general public. Third, Respondents promoted mTokens as an investment, specifically as a way to earn a consistent return of 6.25% on digital assets. Fourth, no alternative regulatory scheme or other risk reducing factors exist with respect to the mTokens.This seems like bad news for DeFi lending protocols. I  wrote last month about a state enforcement action against BlockFi, another DeFi-ish lending protocol that raised crypto from investors and loaned it out to users. “I suppose the question,” I wrote, “is whether the interest accounts are pooled investments (in proprietary trading or lending operations) or just loans to BlockFi denominated in Bitcoin, which would not be a security.” But the SEC says, nope, even if the thing is just a loan to the DeFi protocol, that’s a “note” and counts as a security.Anyway this is an important case in the development of the securities regulation of DeFi, but also separately the facts here are kind of funny? The basic idea of this scheme was that investors would deposit Ether in the DMM smart contract, and DMM would use it to make car loans or something and pay 6.25% interest. But the problem is that no one borrows Ether to buy a car; they borrow dollars. If you borrow $20,000 to buy a car and pay 7% interest, someone could package that into a note, pay 6.25% on the note, and have a bit of extra money to pay profit interests. But there’s a problem if the note is denominated in Ether. If the price of Ether doubles, and you pay back the $20,000, that isn’t enough Ether to pay back the note. Oops!Sometime after publicly unveiling DMM, Respondents realized that their vision of using digital assets to purchase income-generating assets faced a significant roadblock: how to account for fluctuations in the value of the digital assets. While the assets Respondents intended to purchase would generate sufficient income to pay interest, there was a significant risk that the income would not be sufficient to cover appreciation of investors’ principal given a substantial increase in the price of volatile digital assets, such as Ether.More than securities laws, this is a real problem with building a new financial system on top of cryptocurrency: If you use crypto to fund real-world assets, and the price of every cryptocurrency is constantly doubling and halving, every loan repayment is chaos.
  
    
      SEC v. crypto exchanges
    
  
Before DeFi, a major front in the fight over U.S. crypto regulation was initial coin offerings. A lot of people raised money to fund projects by selling crypto tokens, and there was a brief Wild West period where a lot of those people believed that those tokens were not securities and that they could do ICOs without following U.S. securities laws. These people were sort of obviously wrong, and eventually the SEC started  bringing a lot of enforcement actions against ICO issuers for doing unregistered securities sales.So a lot of people who did ICOs got in trouble with the SEC. But there is more trouble to come. If most ICO tokens are securities, then the crypto exchanges that let people trade them are actually securities exchanges, and in the U.S. you need some licenses to operate a securities exchange. Even at the height of the ICO boom, people knew this was a risk, but some exchanges listed these obviously-a-security crypto tokens anyway. Today one of them got in trouble with the SEC:The Securities and Exchange Commission today announced that Poloniex LLC has agreed to pay more than $10 million to settle charges for operating an unregistered online digital asset exchange in connection with its operation of a trading platform that facilitated buying and selling of digital asset securities.The SEC’s order finds that from July 2017 through November 2019, when Poloniex sold its platform, Poloniex operated a web-based trading platform that facilitated buying and selling digital assets, including digital assets that were investment contracts and therefore securities.  According to the SEC’s order, the Poloniex trading platform met the criteria of an “exchange” as defined by the securities laws because the trading platform provided the non-discretionary means for trade orders to interact and execute through the combined use of the Poloniex website, an order book, and the Poloniex trading engine.  The order finds that notwithstanding its operation of the Poloniex trading platform, which was available to U.S. investors, Poloniex did not register as a national securities exchange nor did it operate pursuant to an exemption from registration at any time, and its failure to do so was a violation of Section 5 of the Exchange Act.  The SEC’s order further finds that in or around August 2017, Poloniex employees stated internally that they wanted Poloniex to be “aggressive” in making available for trading new digital assets on the Poloniex trading platform, including digital assets that might be considered securities under the Howey test, in an effort to increase market share.  Further, according to the SEC’s order, in or around July 2018, Poloniex determined that it would continue to provide users of the Poloniex trading platform the ability to trade digital assets that it characterized as “medium risk” of being considered securities in light of the business rewards that would provide to Poloniex.The SEC’s order is light on details in a way that is a little ominous for crypto exchanges. It seems that Poloniex did ask token issuers for legal memos saying that their tokens were not securities:Poloniex regularly informed applicants that it monitored the digital asset community and selected digital assets for “listing” that it believed were part of unique and innovative projects. Poloniex also regularly informed applicants that, as a matter of company policy, Poloniex “cannot list any token that resembles a security” and Poloniex “suggest[ed] token dev[eloper]s familiarize themselves with the Howey Test.”If Poloniex determined there was risk associated with a particular digital asset, including risk that the digital asset was a security, Poloniex would request that the applicant provide a memorandum from a third-party law firm analyzing whether the digital asset could be considered a security under Howey.But the SEC says this wasn’t good enough: Poloniex “stated internally that it wanted to be ‘aggressive’ in making available for trading new digital assets on the Poloniex Trading Platform,” and it “determined that it would continue to provide users of the Poloniex Trading Platform the ability to trade digital assets that were at ‘medium risk’ of being considered securities under Howey.” And so, says the SEC, some securities slipped through:This resulted in Poloniex continuing to make available to Users for trading on the Poloniex Trading Platform Digital Asset Securities, which resulted in the Poloniex Trading Platform operating as an unregistered exchange.You might think that the SEC order would then go on to list a few examples of tokens that Poloniex traded that were securities, and explain why they were securities under U.S. law, but it does not. It just says that some of them were securities. Presumably Poloniex knows which ones, or can guess at least.This is all very ominous! If lots of DeFi protocols are securities (as discussed above), and if a trading platform for crypto securities is a securities exchange (as discussed here), then lots of crypto trading platforms are going to get in trouble.[1]
  
    
      Congress v. crypto tax forms
    
  
Another big fight over U.S. crypto regulation is happening over the infrastructure bill, which apparently contains a provision saying that anyone who looks at or thinks about cryptocurrency has to file tax reports for everyone they meet:The current version of the crypto reporting provision in the bill would broaden the definition of a “broker” to any entity in the cryptocurrency industry that facilitates the transfer of digital currencies for another person. Opponents of the provision have said that it would force miners and hardware and software developers to track transactions of individuals who aren’t their direct customers.Seems bad? It is still being fought over. I have not followed this one closely, but I would be sad if I end up having to file 1099s for every Money Stuff subscriber every time I write about crypto.Bloomberg’s Joe Weisenthal writes about “Why Some Bitcoiners Don’t Care About Changing the Infrastructure Bill.” The answer is basically that they think their glorious code is immune from puny human laws:Basically, the hardcore Bitcoin maximalist types believe that they’ve spent considerable money, time and engineering resources in building a decentralized system that’s robust against state attacks. Whereas other coins have zoomed up thanks to get-rich-fast yield-farming systems, and speculative dog tokens, Bitcoin is being built like a clock designed to tick for a thousand years, ready to withstand any kind of attack. Therefore legislative defense is seen as an implicit subsidy toward networks and coins that haven’t invested as much on antifragility.Okay. “Bitcoin doesn’t need Presidents, but Presidents need Bitcoin,” is the title of this Anthony Pompliano post. Okay.
  
    
      How’s Bill Hwang doing?
    
  
Fine? I don’t know,  here’s a story about how he is hanging out on his porch thinking about all the money he lost, but it does not quite answer my main question about Bill Hwang, which is how much money he kept. There are tantalizing hints that it’s a lot. Hwang’s family office, Archegos Capital Management,  lost $20 billion of net asset value in a couple of days in March; it made heavily levered bets on a handful of stocks, and the banks that provided the leverage also lost at least $10 billion. So in rough numbers Archegos went from positive $20 billion to negative $10 billion.You might think that when a guy’s family office goes from positive $20 billion to negative $10 billion, that guy would no longer be a billionaire. That is sort of the naive intuitive reading of things: You’ve got a “family office,” that’s where your money is, you make very levered bets with that money, those bets go to — and through — zero, you don’t have money anymore. But that is not necessarily true:The size of Bill Hwang’s fortune remains uncertain. Former employees have been grousing that while they’ve been wiped out, Hwang, through private investments and other holdings away from Archegos, could still be a billionaire. ...Banks are haggling with Hwang’s team to figure out the size of his remaining wealth and whether they can claw back any of it. Credit Suisse has said it will seek to recoup money from Archegos and its related entities and individuals. The Swiss bank also flagged in its findings that Hwang’s firm took out more than $2 billion in excess margin from its account with the lender in the days before the collapse.You don’t have to keep all your family’s money in your family office. You have the family office, it is a legal entity (Archegos Capital Management), it enters into contracts (swap confirmations, credit support annexes) with its banks. The contracts presumably say things like “if Archegos’s positions end up being worth a negative amount of money, it will pay that money to the banks.” But it — Archegos — is on the hook. Not necessarily you. If Archegos — the legal entity — doesn’t have any more money to pay to the banks, then what happens? Maybe the contracts include personal guarantees, or maybe there is some other legal theory by which the banks can sue Hwang personally to make him responsible for Archegos’s debts. Or maybe there isn’t. Maybe when Archegos went to (below) zero, Hwang could walk away whistling, leave his banks holding the bags, and keep … billions of dollars? … of wealth that he held outside of Archegos. Maybe when he took $2 billion of winnings off the table from Credit Suisse, days before it all blew up, he rolled that money into new heavily levered bets at other banks that then went to zero. Maybe he didn’t. Maybe he buried it in his backyard, you know?Anyway, I am always a big fan of the financial-journalism trope that fancy hedge-fund billionaires live like ordinary people,[2] so I was pleased to see that Hwang, who was (is?) a billionaire, lives like a regular multimillionaire in Tenafly:He’s been lying low here in New Jersey, in this tidy borough of 15,000, beyond The Palisades cliffs that rise above the Hudson River. He is not exactly a Wall Street Napoleon exiled to Elba: Hwang has lived here for years, in the same house, with cobwebs in the eaves and hedges out front. A Mercedes sits in the driveway. “Black Lives Matter” signs dot neighbors’ manicured lawns. Homes on this tree-softened street tend to sell for a few million dollars — a modest price, for a billionaire.I want to read a profile of a cryptocurrency billionaire that is like “he has not let his success get to his head; he still drives the same Lamborghini that he bought six months ago.” 
  
    
      Reverse repo
    
  
Here is a story about how the Federal Reserve’s reverse repo facility is very popular now:Investors such as money-market funds and banks are parking over $1 trillion in spare cash overnight at the Federal Reserve. That is the most on record since the Fed opened its facility for these reverse repurchase agreements in 2013.The scale of the moves has some analysts warning that the markets for short-term funding are vulnerable to disruption. The cause for this summer’s rush into the Fed’s reverse repo facility appears to be the central bank’s decision in June to nudge up the amount of interest it pays, from 0% to 0.05%—though usage had already been rising in the spring.Repurchase agreements, or repos, are the market’s main mechanism for moving cash from those who have it to those who need it. The Fed also uses them to influence short-term interest rates; the flood into reverse repo means banks and investors have extra cash and the Fed is vacuuming it up. ...Bill Nelson, chief economist at BPI and a former top Fed staffer, said heavy usage of the reverse repo facility increases the systemic importance of money-market mutual funds, a sector the Fed sees as a financial stability risk. It is a sign that financial markets continue to change and that investors and policy makers must redouble their efforts to keep up.“From its conception up to the great financial crisis, the Fed borrowed mostly from the public in the form of currency. After the crisis. the Fed has also been borrowing from banks in the form of reserve balances,” said Mr. Nelson. “Since March, the Fed is borrowing heavily from money funds.”You could tell a simple dumb story that goes like this:	In the olden days, banks liked to do risky things. This caused trouble in 2008, and now there are stronger capital regulations to keep banks from doing risky things.	These capital regulations also prevent banks from doing some safe things — they need to have capital against even Treasury-bond positions — so the business of “take a bunch of deposits and park the money somewhere safe” is harder for banks to execute.	Money market funds are a form of shadow banking, a way to do the basic work of banking (issuing deposits) without banking regulation or bank capital requirements.	In 2008 they also caused trouble, so now there are more regulations to keep them safe. But, crucially, they still don’t really have to have capital like a bank. A money market fund can issue $100 of money-like claims to fund $100 of investments.	So money market funds are still good at the business of “take a bunch of deposits and park the money somewhere safe,” like reverse repo.	There is a lot of cash, so the demand for that business is really high, and money market funds are in a better competitive position to offer it.In other words, in 2006 banks and shadow banks were competing with each other to fund risky synthetic mortgage-backed securities; in 2021 banks and shadow banks are competing to literally lend money overnight to the Federal Reserve at 0.05%. In either case, it is easier to compete if you are not subject to bank regulation and capital requirements, so the shadow banks have an edge.
  
    
      Things happen
    
  
The  Debt-Ceiling Farce Is a Headache Investors Could Do Without. SoftBank deals unleash internal compliance tensions: ‘If Masa said yes, who am I to object?’ Jefferies Raises Junior Pay to Match Goldman Sachs at Top of Wall Street. How Big Promises And Fat Fees Turned Private Equity Into A Lousy Investment. “Over a 7-year period, women make up on average 10.5% of lead legal advisors for buyers in M&A.”  Nikola’s Indicted Ex-Chairman Milton Sells $77 Million of Stock. Earnings Day Matters for  AMC Even If Its Actual Results Don’t. McDonald’s Pushes Diners to Use Trays as Food Bags Run Tight. Virgin Galactic Space Flight Tickets to Start at $450,000 a Seat.If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] Some of them will be decentralized exchanges, which will create another set of “but who does the SEC sue?” problems.[2] I  wrote earlier this year: “By the way, my favorite thing in financial-industry profiles is the unwritten rule that everyone except Chase Coleman has to be described as not fitting in with all those other, stereotypical bankers and hedge funders. The classic of the genre is, like, Warren Buffett lives in a normal house, but lots of bankers and hedge-fund managers in fact live in fancy houses so you have to stretch a little. There is the  hedge-fund consultant whose ‘most obvious indulgence is a Maserati Ghibli,’ or the hedge-fund manager whose ‘unique position, with one foot inside the lucrative hedge-fund industry and one foot out of it, is perhaps most plain on weekends during the summer,’ when — I swear — he only sometimes takes a private plane to his house on Nantucket.”
        
      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like Money Stuff? | 
Get unlimited access to Bloomberg.com, where you'll find trusted, data-based journalism in 120 countries around the world and expert analysis from exclusive daily newsletters.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cep9hb.5jkn/d444cc68.gif" alt="" border="0" /></a>
