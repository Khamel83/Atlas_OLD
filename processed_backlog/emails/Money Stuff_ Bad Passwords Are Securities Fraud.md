# Money Stuff: Bad Passwords Are Securities Fraud

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Tue, 31 Oct 2023 14:28:49 -0400 (EDT)
**Source:** inputs/saved_emails/Money Stuff Bad Passwords Are Securities Fraud_Tue,_31_Oct_2023_14-28-49_-0400_(EDT)_18b86fef190dd4e4.eml
**Processed:** 2025-08-24T19:13:11.815352



  
  
    
      
        
      
    
  
  
    
      
        If you are a publicly traded software company, and your customers access your product through a server, and you provide them with a default 
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      SolarWinds
    
  
If you are a publicly traded software company, and your customers access your product through a server, and you provide them with a default password to log into the server, and the default password is “password,” is that securities fraud? You know the answer!	Every bad thing that a public company does is also securities fraud.	Using “password” as your password is pretty bad.	Therefore, using “password” as your password is securities fraud.Yesterday the  US Securities and Exchange Commission sued “software company SolarWinds Corporation and its chief information security officer, Timothy G. Brown, for fraud and internal control failures relating to allegedly known cybersecurity risks and vulnerabilities.” SolarWinds sells network management software to companies and governments, including “an information technology infrastructure and management platform” called Orion. In 2020, Orion was  famously hacked by Russian state actors, who inserted hidden code into Orion software updates and were “then able to remotely exploit the networks and systems of SolarWinds’ customers,” which they used “for the primary purpose of espionage.”That was bad for, among other things, SolarWinds’ stock price. The  SEC’s complaint says:On December 14, 2020, the day it filed the Form 8-K first announcing the SUNBURST attack against the Orion platform, SolarWinds’ stock price dropped more than 16%. It dropped at least an additional 8% the next day. The stock price continued to drop and lost approximately 35% of its value by the end of the month as SolarWinds disclosed more details of the SUNBURST attack, and as news outlets reported that internal sources had warned SolarWinds for several years about the Company’s cybersecurity risks and vulnerabilities.My non-technical theory is that “everything is securities fraud”: If a public company does a bad thing, or a bad thing happens to it, and the stock drops, then that is securities fraud. The stock was high, because investors did not know about the company’s vulnerability to the bad thing. Then the bad thing happened, investors found out, and the stock dropped. Before they found out, they were deceived about the true value of the company, so that was fraud. Here, that is all you really need to know: bad thing, stock down, securities fraud.But that is not technically an accurate description of the law, so the SEC, in suing SolarWinds, needs to argue that SolarWinds made false statements about facts that were material to investors. Thus, for example, “password”:SolarWinds’ Security Statement falsely claimed the Company not only had, but enforced, a strong password policy. Specifically, SolarWinds and Brown stated: “We require that authorized users be provisioned with unique account IDs. Our password policy covers all applicable information systems, applications, and databases. Our password best practices enforce the use of complex passwords that include both alpha and numeric characters, which are deployed to protect against unauthorized use of passwords.” …Contrary to its Security Statement, SolarWinds did not enforce strong password requirements on all of its information systems, applications, and databases, as Brown and SolarWinds knew or were reckless or negligent in not knowing. …In an April 2017 email to the newly hired CIO, a SolarWinds employee expressed surprise that things “like ‘default passwords’ are [still] plaguing us when the product has been in the market [this long,]” explaining, “[m]any of these vulnerabilities seem pretty well amateur hour.” As an example, the employee noted one product for which the default password was “password.” Senior InfoSec Manager E testified that having a default password of “password” is a “poor security practice.”And possibly even better, “solarwinds123”:During the Relevant Period, SolarWinds used an Akamai server to distribute software updates to its customers. In November 2019, an outside security researcher notified SolarWinds that the password for the Company’s Akamai server was publicly available, and that a threat actor could use that public password to infect SolarWinds’ software updates: “I have found a public Github repo which is leaking ftp credential belong[ing] to SolarWinds…. Via this any hacker could upload malicious exe [executable code] and update it with release [of] SolarWinds product.” Senior InfoSec Manager E confirmed the security researcher’s description. The password that was publicly available was “solarwinds123,” an astonishingly simple password that did not comply with the Company’s stated password complexity requirements.“Any hacker could upload malicious exe” is pretty much what ultimately happened and crashed the stock. I am not a cybersecurity expert and I have not followed the SolarWinds hack closely, but I suppose it is possible that Russian intelligence agents were able to hack the Orion updates, and thus spy on US federal government computers, by correctly guessing the password “solarwinds123.” What would  Dark Helmet say?But that’s not the point; the point is that SolarWinds investors were, let us just hypothesize, closely reading the company’s “Security Statement,” a document that was not actually included in SolarWinds’ securities filings or financial reports but that was “posted to the Company’s website.” And, says the SEC, they were deceived:SolarWinds and Brown’s misstatements and omissions regarding password issues were not only false and misleading, but materially so. A reasonable investor, considering whether to purchase or sell SolarWinds stock, would have considered it important to know the true state of SolarWinds’ password policies, especially considering that these issues were longstanding and potentially affected customer-facing areas such as the Akamai server used to send updates to customers.Is that right? It feels not quite right, in the sense that you rarely see equity research notes about public companies that are like “upgrading this company to a Buy based on its strong password policies.” The claim here is not really, not seriously, that investors read SolarWinds’ password policy, and decided to invest based on that policy, and then lost money when the password policy turned out to be fake. The more likely story is that investors blithely assumed most companies have good practices across a range of domains and figured that, if SolarWinds really was just letting anyone into its software, someone would tell them. It’s not just passwords, to be clear. The SEC identifies other kinds of poor security information security practices; the “password” stuff is just the most obvious. The basic idea is that SolarWinds did various careless things, while telling customers and investors that it was careful, and eventually the carelessness caught up to it. And the stock dropped.What is the lesson that companies should take from this case? The SEC complaint says that, even as SolarWinds was publicly saying that it had a good security policy, “Brown and other SolarWinds employees knew that SolarWinds had serious cybersecurity deficiencies.” It cites a bunch of internal emails and messages:An August 2019 presentation warned that “[a]ccess and privilege to critical systems / data is inappropriate.”Presentations in March and October 2020 highlighted “[s]ignificant deficiencies” in SolarWinds’ access controls. …In a July 2020 email to Brown, a member of the Engineering team described being “spooked” by activity at a SolarWinds’ customer. Brown agreed that the incident was “very concerning” and continued, “As you guys know our backends are not that resilient and we should definitely make them better.”A September 2020 Risk Acceptance Form flagged for Brown and others “the risk of legacy issues in the Orion Platform” and warned “[t]he volume of security issues being identified over the last month have outstripped the capacity of Engineering teams to resolve.”In instant messages sent in November 2020, SolarWinds’ Senior InfoSec Manager E expressed his own disgust with the Company’s security posture, lamenting, “[W]e’re so far from being a security minded company. [E]very time I hear about our head geeks talking about security I want to throw up.”In November 2020, a SolarWinds Information Security employee sent an instant message to Senior InfoSec Manager E with a link to a list of vulnerabilities in the Orion platform stating, “The products are riddled and obviously have been for many years.”If you run information security at a software company, would you rather get messages like this, or not? Like:	Ideally your security would be perfect and you would never get messages like this because there are no problems.	If your security is not perfect, wouldn’t you rather get messages like this than not?? For one thing, strong clear intemperate statements like this will alert you to the problem better than diplomatic wishy-washy messages. For another thing, you might want to employ engineers who send messages like this: You want your employees to be morally indignant at security vulnerabilities, to get mad about them, so they are likely to catch and fix them. You want people who are passionate about security, and if you find them you will tolerate their negativity and complaining.But if you run the legal department at a software company, these messages are really bad! They lead pretty directly to securities fraud charges. I   once wrote:If you are trying to build a good engineering culture, you might want to encourage your employees to send hyperbolic, overstated, highly quotable emails to a broad internal distribution list when they object to a decision. On the other hand your lawyers, and your public relations people, will obviously and correctly tell you that that is insane.Everything is securities fraud, and using “password” as your password is securities fraud, but using “password” as your password is especially securities fraud if one of your engineers sends an email saying that it is “pretty well amateur hour.” But it is pretty well amateur hour! It is helpful for someone to point that out. But it gets you sued.
  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Bed Bath from the Beyond
    
  
When did the shares of Bed Bath & Beyond Inc.’s stock become worthless? I think a reasonable answer would be January 2023: Bed Bath & Beyond breached its debt covenants in December 2022, hired financial advisers to find a potential buyer (in bankruptcy), and came up empty. By January, it was planning to file for bankruptcy and liquidate its assets, which would bring in some money for creditors, but not enough to pay them in full, and certainly not with anything left over for shareholders.But Bed Bath & Beyond found a way to delay the inevitable: It had enthusiastic retail meme-stock investors, and it did a series of  weird deals to sell them an absolute ton of stock, for ever-declining prices, to raise a bit more money to hand over to its creditors. This was pretty clearly the plan, and it was pretty clearly disclosed; Bed Bath was not tricking shareholders about what it was doing. But it did it anyway, and the shareholders happily tricked themselves, pouring money into a worthless company for it to hand over to creditors. This went on for a few months, and then Bed Bath & Beyond did file for bankruptcy in April. I  wrote at the time:This is the peak of meme stocks. Bed Bath & Beyond sold 50 million shares a week for three months with, as far as I can tell, no story, no plan, nothing but “a troubled financial situation and nostalgia value.” Bed Bath saw that its retail shareholders wanted to throw their money away, and that its sophisticated lenders wanted to get their money back, and realized that there was a trade to be done that would make everyone, temporarily, happy. So it did the trade.But why stop there? By April, Bed Bath & Beyond shareholders had been buying worthless stock, for meme and confusion reasons, for months; why would bankruptcy stop them? And so in fact investors  spent hundreds of millions of dollars trading Bed Bath & Beyond stock after it filed for bankruptcy, possibly out of pure confusion, though possibly out of optimism that there would end up being some recovery for shareholders. That is not a theoretical impossibility — notably shareholders got paid in  the Hertz Global Holdings Inc. bankruptcy — but it was vanishingly unlikely, and it did not in fact happen. On Sept. 29, 2023, Bed Bath & Beyond exited bankruptcy with an approved plan that resulted in zero recovery for shareholders. It  said in a securities filing:As a result of the Confirmed Plan becoming effective, all of the Company’s equity interests, consisting of outstanding shares of common stock and Series A Convertible Preferred Stock of the Company and related rights to receive or purchase shares of common stock, were cancelled on the Effective Date without consideration and have no value. That same day, it  terminated the registration of its stock, which, I hope, stopped it from trading. The last price that I see for Bed Bath & Beyond stock on Bloomberg was on Sept. 29, with a closing price of $0.0789 per share, 8.8 million shares traded and a market capitalization of  $62 million.But why stop there? Fidelity Investments, the retail broker,  removed Bed Bath & Beyond shares from its customers’ accounts on Oct. 18, because those shares really were canceled. (Presumably other brokers removed them too.) And you can go to Fidelity’s Twitter account and  find people complaining. “A stock broker like #Fidelity should not remove #BBBYQ shares from holder's accounts nor their P&L statement if there's a possibility of restructuring or corporate action in the near-term future.” (There is not.)  And: “Mine have disappeared… @Fidelity Replace my shares, please.”  And: “What do you mean expired? How can shares held in cash account expire?”Some of these people are probably kidding. I suspect some aren’t, though. Presumably the people who paid actual money to buy Bed Bath & Beyond shares in September, or June, or even February, were not kidding, but it didn’t make much more sense then.Possibly the meme stock craze was … bad? The run-up in meme stocks in 2021 might have over-taught the lesson that financial markets are a random casino, that anyone can make a lot of money for no reason, and that if for some reason you lose money it’s probably the fault of evil hedge funds protecting their power. And so now you can buy stock in a bankrupt company, and the company can cancel its stock because it doesn’t have enough money to pay off creditors, and you can get mad about it.
  
    
      SBF Stuff
    
  
I   wrote yesterday that the reviews of Sam Bankman-Fried’s testimony at his trial, on direct examination, were basically pretty good. But I figured the reviews of his performance on cross-examination would be less good. They were less good. “It's not going well,”  writes Dan Primack. “Partially because SBF keeps trying to sound like the smartest guy in the room, and partially because he seems to believe the entire proceeding is beneath him.” “During an approximately four-hour cross-examination led by prosecutor Danielle Sassoon, Bankman-Fried appeared to suffer from memory loss, evaded questions, and gave downright unhelpful answers,”  writes Tracy Wang. “When confronted with a difficult question, Bankman-Fried would often rely on his vast vocabulary of weasel phrases.” Here’s  Bloomberg News:Bankman-Fried was asked whether he fired anyone for spending $8 billion of customer funds. “No,” he said. When asked how the money was spent -- exclusively for margin trading or not -- Bankman-Fried said, “I am not sure.” He evaded other questions, such as whether he would agree he wasn’t transparent with customers about risks posed by FTX. “It wasn’t our policy to disclose customer account details,” he replied. ...“I am not sure” made more than one appearance, with Bankman-Fried often not replying directly to questions. The prosecutor and judge at times had to ask the same question over and over to get an answer. Bankman-Fried also frequently repeated that he didn’t remember what he had seen or said.And here’s  the Wall Street Journal:The trial proceedings shifted quickly after Assistant U.S. Attorney Danielle Sassoon began her cross-examination and sought to confront Bankman-Fried with a litany of his past public statements whose truthfulness she questioned.“Would you agree that you know how to tell a good story?” Sassoon asked.“I don’t know. It depends on what metric you use,” Bankman-Fried responded. Correct? Like if you judge Bankman-Fried’s ability to tell a story by its maximum payoff at any point in time, he was better at telling stories than almost anyone else in human history? If you judge it by its final payoff, quite bad. Similarly:The prosecutor appeared to be goading Bankman-Fried at certain moments, pointing out FTX’s meteoric rise, his onetime status as a billionaire and his college degree from the Massachusetts Institute of Technology. “You think of yourself as a smart guy?” she asked.“In many ways. Not in all ways,” he replied. Same basic analysis. And here is  the Financial Times:He admitted to calling a “specific subset” of crypto investors “dumb [expletives]” and conceded he had referred to his advocacy for crypto regulation as “just PR” in the days leading up to his arrest last December.He also admitted to writing “[expletive] regulators” to a reporter in November 2022.If you call your investors “dumb [expletives],” does that prove that you are doing fraud on them? No. Is it a good look, at your fraud trial? No. Is it helpful to clarify that you were only referring to a “specific subset” of your investors that way? Probably not that much?Elsewhere, here is a  profile of Tiffany Fong, the “reluctant crypto content creator” who spent a lot of time talking to Bankman-Fried while he was on house arrest:Fong and Bankman-Fried reconnected in November 2022, when his FTX empire swiftly and dramatically imploded. On November 11, the day FTX filed for Chapter 11 bankruptcy, Fong reached out to Bankman-Fried. “I just said something like, ‘Hey, obviously, there’s been a lot of news about FTX. Would you be willing to chat with me and tell me your side of the story?’” recalls Fong. “I really did not think that Sam would ever get back to me.”A few days later, Fong was on a late-night date at a Brooklyn dive bar when Bankman-Fried responded. He sent her a heart emoji and said he’d be free to chat with her for the next hour or so. “I was like, ‘What? No, there’s no [expletive] way’,” says Fong. She said to her date that evening, “I don’t even know what to ask him. I’m kind of drunk right now.” Her date, who she’d met through crypto and had substantial funds stuck on FTX, offered, “Ask him where my [expletive] money is.”Still elsewhere, Bloomberg’s   Emily Nicolle reports:As the trial of FTX co-founder Sam Bankman-Fried unfolds, the relationship between his exchange’s trading outfit Alameda Research and stablecoin issuer Tether is under the microscope of crypto sleuths.Alameda was Tether’s largest non-exchange customer between 2020 and 2022, with blockchain data showing it received almost $40 billion in transfers of its stablecoin USDT directly from the company — equal to roughly 20% of all USDT tokens ever issued.The vast amount has raised questions about where Alameda got the money to fund the issuance of the stablecoin, which is typically used as a dollar proxy and is the world’s most traded cryptocurrency. That even led to speculation Alameda might have used other means to help fund the purchases, similar to its bets on startups or dealings with lenders.I feel like eventually Tether is going to be an incredibly interesting story, but I still don’t know what it is.
  
    
      Ares
    
  
Two fundamental questions of bank regulation are:	Would you rather have some class of loans made by banks, which are subject to comprehensive regulation and supervision, or by relatively less regulated non-banks?	Would you rather have some class of loans funded by demand deposits, which could flee at any time, or by pension funds, which can’t?These questions are largely the same question. Here’s Bloomberg’s Allison McNeely:Ares Management Corp. raised $6.6 billion for its second asset-based credit fund, as it seeks to snap up portfolios from banks that want to sell them to comply with higher capital requirements.The firm’s Pathfinder Fund II, which exceeded its $5 billion target, will invest in portfolios of assets that offer steady cash flows, Ares said in a statement Monday. That could include pools of auto loans, credit card receivables, mortgages and other bundles of loans. …Ares has been actively negotiating with banks that aim to offload loan portfolios that have high capital charges, which makes them less profitable to hold on their balance sheets.It recently closed on a so-called capital relief trade for a portfolio of more than $5 billion of “super-prime” auto loans from a large regional bank, according to Joel Holsinger, co-head of alternative credit at Ares. He predicts a rush of deals before year-end.“This is no different than where direct lending was in 2011 or 2012,” Holsinger said in an interview. He added that a “fragmentation” ensued after the 2008 financial crisis and that “excessive regulation” has pushed certain asset classes out of banks. …For institutional investors, asset-based credit offers diversity and uncorrelated risk beyond traditional direct loans to companies, Keith Ashton, co-head of alternative credit at Ares, said in an interview. … In five years, most pensions will allocate 2% to 4% of their portfolios toward asset-based credit, Holsinger said.Is this good? On the one hand it is not hard to find people complaining about the rise of private credit and arguing that firms like Ares are less regulated, and more willing to take risks, than banks are. On the other hand, banks really are   funded by deposits! That has caused problems this year: If you borrow short-term to lend long-term, you can   run into trouble. Whereas if you raise money from pension funds to buy auto loans, you really can hold those auto loans to maturity. 
  
    
      Coins
    
  
We  talked the other day about some criminals who stole 2 million dimes and were like “ugh, now we have to convert these into money.” The conversion was terribly labor-intensive and also got them caught. If you stand at the CoinStar machine all day pouring in dimes, people will have questions. Coins, in the US, are money, but only in pretty small amounts. Once you get above roughly a pocketful of coins, their moneyness starts to fall off.A forklift-full of coins, for example, is somehow the opposite of money:Pennies, nickels, dimes and quarters might be legal tender but more than 6,500 pounds of loose change is not a proper form of payment, a Colorado judge ruled last week after a defendant attempted to deliver $23,500 in coins to settle a legal dispute.The judge, Joseph Findley, of Larimer County, said that the delivery of more than three tons was done “maliciously and in bad faith,” and that the defendant, a welding company, must now pay more for its act. ...JMF Enterprises attempted to make a “nighttime delivery” to Fired Up Fabrications but company officials rejected it because they at first thought it was a forklift being delivered, according to the judge’s order.On Aug. 28, the following Monday, “an attempt was made to deliver a heavy metal container of coins that required a forklift to move” to lawyers for Fired Up Fabrications, the order said, but it was “physically impossible” to deliver. …In the order, Judge Findley said that while coins were legal tender, paying such a large settlement in coins would reduce the settlement because of the time and expense required to accept it.He said photographs showed that the coins had also been removed from neatly organized boxes and dumped “loosely and randomly” into a metal container.The judge ordered JMF Enterprises and Mr. Frank to pay additional fees related to the costs of extending the case and dealing with the coin payment.Surely everyone who has lost a lawsuit has briefly fantasized about paying in pennies. Surely Elon Musk had someone look into paying $44 billion for Twitter in pennies. But here’s some legal precedent. If you try to pay someone with 6,500 pounds of coins, (1) you will have to pay them again with real money, (2) you will have to pay them more and (3) you’ll be stuck with all the coins.
  
    
      Things happen
    
  
The Money Has Stopped Flowing in  Commercial Real Estate. Banker Bonuses for ECM Shops   Looking Abysmal With Light Issuance. Oil industry megadeals open  fee gusher for Wall Street advisers. Europe’s Junk-Rated Firms Get   Cash from Owners as Refinancing Pressure Mounts. In Texas, Bitcoin Springs from  Gas Wells. Biden’s  ‘Junk Fee’ Crackdown Comes for Retirement Advice. Carlsberg says Moscow ‘ stole’ its Russian business. Russia tightens  capital controls on western companies. Russia’s Richest Man Potanin Bids To Dodge Massive UK   Divorce Claim.  Odey Asset Management to close down after sexual assault allegations against founder. Saudi Arabia Is Set to Be  Sole Bidder for 2034 World Cup.If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cjrs01.5je5/ef22d7c7.gif" alt="" border="0" /></a>
