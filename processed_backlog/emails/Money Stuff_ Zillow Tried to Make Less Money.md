# Money Stuff: Zillow Tried to Make Less Money

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Thu, 18 Nov 2021 13:10:56 -0500 (EST)
**Source:** inputs/saved_emails/Money Stuff Zillow Tried to Make Less Money_Thu,_18_Nov_2021_13-10-56_-0500_(EST)_17d343fca2a6b46a.eml
**Processed:** 2025-08-24T19:13:06.033873



  
  
    
      
        Programming note: Money Stuff will be off tomorrow, back on Monday. Zillow On the one hand, sure, I can see why someone might consider this 
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          Programming note: Money Stuff will be off tomorrow, back on Monday.
  
    
      Zillow
    
  
On the one hand, sure, I can see why someone might consider this a problem:When executives at Zillow Group Inc. pored over the company’s earnings in the spring, they saw a problem: The real-estate firm was making too much money.On the other hand, it does feel like a problem that I would happily take off Zillow’s hands? There are worse problems than making too much money! Making too little money is a worse problem, for instance. Losing money. These are the problems. Making too much money is just interesting.That was the first sentence of the Wall Street Journal’s postmortem about how Zillow ended up losing a bunch of money buying and flipping houses and had to shut down that business. The problem was that “the company’s algorithm, which was supposed to predict housing prices, didn’t seem to understand the market,” and was generating prices that were too low.This had two effects. First, most people declined its offers, which were too low: “Only 10% of people who asked for a Zillow offer and eventually sold their home ended up selling it to Zillow,” and “Zillow was also behind on its target for home purchases” in the first quarter. Second, when people did accept Zillow’s offers — because they were in a hurry, or didn’t have a good sense of the market — Zillow made a ton of money:The first quarter delivered home-sale profits that were more than twice as high as anticipated, the company said. Zillow expected to make money primarily from transaction fees and from services such as title insurance—not from making a killing on the flip. Zillow executives looked at this state of affairs and said, well, this state of affairs is bad, we need to grow our market share and make our algorithms more accurate. We are looking to be a first-choice  market maker in home-selling, and we can’t do that if our prices are too low. So they tweaked the algorithms to generate higher prices. Those prices also turned out not to be particularly accurate, but in the other direction. If you systematically bid too low, you will not do many trades, but you will make a lot of money on each trade. If you systematically bid too high, you will lose money on each trade, and also you will do a whole ton of trades. This is much worse.[1]You could imagine being in that meeting and saying, hang on a minute, are we sure about this? Sure, it’s bad that our algorithms are inaccurate, and it would be better if they were more accurate. But that seems hard. We have smart people working to make them accurate, and so far they have failed. If we tweak the algorithms to generate higher prices, that may just make them inaccurate in the much worse direction.[2] On the other hand right now we have a business that buys houses at below-market prices, flips them, and makes a big profit on each one. A lot of people would like to have a business like that! Sure it would be better if we could do more trades like that, but you’re realistically not going to find tens of thousands of people who will sell you their homes for below market value. But we have found thousands! That’s pretty good!I don’t know, it’s a weird story about technology and scale, about how many businesses — in particular, many public companies — aim to maximize not profit but size. In concept, a business model like “send everyone in America a bid on their house that is too low, and then buy the houses from the minority of suckers who take your bid” seems … obviously … lucrative?[3] Like, I would be happy to do that business? I don’t have the capital for it, but I’m sure there are hedge funds who would do this business if they could.But the only way to actually do it — to generate millions of plausible-but-too-low bids, and to get them in front of potential sellers — is to have the scale and reach and technology of a big online home-information company like Zillow. And once you’re at that scale, doing a few thousand dumb lucrative transactions almost isn’t worth it for you; the only way to justify it is to scale it up until it’s larger, smarter and less lucrative. (Or, in Zillow’s case, larger, equally dumb and disastrous.)Also you probably got to that scale by being a popular trusted source for home information, which is valuable for your main business of selling ads on the internet; sending people lowball bids to try to sucker them into selling to you might not be great for that business. As Ben Thompson wrote: “Because the company felt compelled to push Offers, it was actually leaving most potential sellers with a bad taste in their mouth; this is a big problem given that an Aggregator’s advantage is the fact the end users like it and go there first.”And so Zillow could not do this business model, because the business was too small for Zillow. And I could not do this business model, because I am too small for the business. But for a little while, it was kind of a good business!
  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Dead stock
    
  
One reason to sell a stock short is that you think it will go to zero. You think it’s a fraud, a pump-and-dump, complete vapor; it will get shut down by regulators or file for bankruptcy in short order. This is a dangerous reason to short a stock! Not just because you might be wrong, and not just because, you know, frauds are sometimes run by unpleasant people who will take it personally that you are shorting their stock.But also because, what if you’re right? The way you make money in short selling is, you borrow the stock, you sell it, you wait for it to go down, and then you buy it back. You have to borrow the stock from a stock lender, and you post collateral and pay a running fee to borrow it; when you buy the stock back, you deliver it to the stock lender to close out the transaction. If the stock goes down from $10 to $0.01, this all works, you make $9.99 and you are happy. But if it goes down from $10 to “regulators have shut down trading in this stock, this company is banned, let us never speak of it again,” then … how do you buy it back? If it doesn’t trade, you can’t buy it back, so you can’t deliver it to your stock lender, so you have to keep posting collateral and paying borrow fees forever. “But the notional value of the stock is now zero, so the borrow fee is 0.25% of zero or whatever, and the collateral I owe is zero,” you say, but, you know, prove that to your prime broker in the absence of a trading market.We have talked about this problem before; there are some short sellers out there who have made short bets so successful that they can never be closed, sort of defeating the purpose of the short bets. Now they just sort of walk the earth, complaining about their brokers and paying stock-borrow fees. Here’s another one:Jefferies Group LLC overcharged and then “hijacked” the prime brokerage account of its client IsZo Capital Management, the activist hedge fund claimed in an arbitration filing. The investment bank held back $5 million of IsZo’s money, later reduced to $2.5 million, to secure seven short positions in securities that are now worthless, IsZo claimed in an arbitration claim filed this week with the Financial Industry Regulatory Authority, or Finra.The conflict arose in June, when IsZo, which manages more than $300 million, tried to close its Jefferies account and move its cash and holdings to another prime broker. Jefferies told the hedge fund that the illiquid positions couldn’t be transferred and would have to remain open, subject to minimum net equity and collateral requirements, according to IsZo. It’s a problem that can arise when a short-seller is too successful -- betting against a company that goes bankrupt, while prime brokerages continue to charge fees. In the cases cited by IsZo, the market for the securities of those companies disappeared, leaving them unable to cover their position. IsZo calls it “little more than a theft.”Also here is a novel reason for collateralizing short positions against defunct stocks forever:In an August Zoom call, Jefferies executives told IsZo that the funds were needed to protect the firm “in case any of the stocks traded like ‘meme stocks’” -- companies favored by retail traders that have seen wild price action in their shares this year.“Even the barest modicum of diligence would have revealed that there is no danger that any of the 7 legacy short positions could ever become a meme stock,” IsZo said in the filing. “The securities – to the extent that they even exist – have no trading market at all.”Yeah it’s hard to make a stock into a meme if you can’t buy it? And if you could buy those stocks, IsZo would! To close out its shorts!
  
    
      
        
      
    
  


  
    
      They didn’t kill Kenny
    
  
Elsewhere  in meme stocks:Citadel Securities and Robinhood Markets Inc. won dismissal of a proposed class action by retail investors who accused the firms of colluding during January’s meme-stock frenzy.U.S. District Judge Cecilia Altonaga in Miami said the plaintiffs failed to show there was any agreement between Citadel Securities and Robinhood to act in concert. She dismissed the case without prejudice, giving the investors until Dec. 20 to possibly file an amended complaint.The lawsuit alleged that Citadel Securities amassed a substantial short position in GameStop Corp. and other stocks that exploded in value, and that the market-maker pressured Robinhood to stop customers from purchasing those shares, which the online brokerage did on Jan. 28.Citadel Securities said it first learned of Robinhood’s trading restrictions on certain stocks during January’s meme-stock frenzy from Twitter, rebutting accusations that the two firms colluded. The judge said the plaintiffs were only inferring such pressure was applied based on “a few vague and ambiguous emails between two firms in an otherwise lawful, ongoing business relationship.”That strikes me as completely correct but unlikely to do much to dampen the conspiracy theories. Ooh, but some people at Robinhood talked to some people at their main market maker as markets were going haywire, ooh ooh ooh. Here is the opinion.
  
    
      Governance, fraud, constitutions, etc.
    
  
Last week  we talked about a Twitter poll that Elon Musk did, asking if he should sell 10% of his Tesla stock. “I will abide by the results of this poll, whichever way it goes,” he tweeted. I wrote some discussion questions. Here were two of them:7. If Musk does not abide by the results of this poll — if he does not sell 10% of his stock, as a majority of 3.5 million randos on Twitter told him to — would that be securities fraud? In answering this question, consider who might have been defrauded, and how. Consider also how much time Musk should get to abide by the poll: If he sells 1% of his stock per year for 10 years, would that count?8. If your answer to Question 7 was “yes” — i.e., if you think it would be securities fraud for Musk to tweet a poll and say he’d abide by the result and then not do it — then does that mean that the Twitter poll was in fact legally binding? More generally, is anything that the chief executive officer of a public company says on Twitter legally binding, because if it is not true then that’s securities fraud?For what little it’s worth, my answer to both of those questions is a very cautious “probably?” (Nothing here is legal advice, etc.) If I were a law professor teaching a contracts class this semester, I would definitely discuss these tweets in class, and I’d add a few more lawyer-y questions. “What happens to the doctrine of  consideration when anything you say on Twitter creates legally binding obligations under the law of securities fraud,” would be one of them.I’ve got some more hypotheticals. For instance let’s say you buy stock from a company in a publicly registered initial public offering. The prospectus for the offering says, repeatedly and prominently, that there is only a single class of stock and that every share gets one vote. The company’s certificate of incorporation says that there are two classes of stock, Class A, which is sold to the public in the IPO and gets one vote per share, and Class B, which is retained by the founder and gets 1,000 votes per share. After the IPO, the founder wants to do something, the shareholders want to do something else, and the founder says “haha, surprise, I’ve got 1,000 votes for share and I’ll do what I like!” Is she correct?I think as a matter of corporate law — as a matter of what the certificate of incorporation says — sure, she is correct. But if she does anything that the other shareholders don’t like, they will sue her for securities fraud, and they will win and get piles of money in damages. Also the Securities and Exchange Commission or the Justice Department might investigate her blatant fraud, and she might go to prison. It’s not quite as good as having the certificate of incorporation say what it’s supposed to say. But for most practical purposes it is a good substitute. She will go use her 1,000 votes to amend the certificate to say what it’s supposed to say, because there are powerful enforcement mechanisms if she doesn’t.Or if a company issues a bond with a prospectus saying “this bond pays 5% interest,” on the cover and repeatedly throughout the prospectus, but the indenture says “this bond pays 3% interest,” and page 67 of the prospectus says “this prospectus is qualified by reference to the indenture, which actually governs the terms of the bond,” what is the interest rate on the bond? I think the contract-law answer is 3%, the rate in the indenture, the actual contract that governs the bond. I think the securities-law answer is 5%, the rate prominently displayed in the marketing of the bond. “But we said in a cross-reference on page 67 to check with the indenture!” No, come on. Either you pay 5% or you get sued for securities fraud and you lose and pay damages of, effectively, 5% interest.Incidentally neither of these hypotheticals would ever, ever, ever happen, because if you’re doing an IPO or a bond offering you’ll hire lawyers, and the underwriters will hire lawyers, and all the lawyers will work hard to make sure that the legal rights are properly reflected in the prospectus,[4] because they are very concerned with not doing fraud. But that’s sort of the point.The point is that the law of fraud — here securities fraud, but more generally “wire fraud” or just “fraud” — creates a sort of backup to contract law, corporate law, partnership law, etc. If you go around telling people “hey, sign this contract and you’ll get a pony,” and they sign the contract and it actually says “you will never get a pony,” they will not have much ability to sue you under the contract, but someone will probably go after you for fraud, depending on things like how many people you marketed it to and how unsophisticated they were and how high-pressure your marketing was and and how complicated the contract was and how much money you got out of them.People complain about this from time to time; in particular, it is common for fraud defendants to say “this is not a case of fraud, but a simple contract dispute in which we disagree with our counterparties about what our obligations were under the contract.” There is a lot of overlap between those things.I think this is an interesting situation — related to but distinct from “everything is securities fraud” — for, like, corporate governance and Elon Musk and executives on Twitter. I think that corporations and their executives are, in broad terms, obligated to do not only what their contracts and corporate documents say they have to do, but also what they have said publicly they are going to do (and particularly what they have said to investors they are going to do), because if they do something else they’ll get sued for securities fraud.But I suppose it is also an interesting situation for things that don’t have contracts or corporate documents. We  talked a bit the other day about ConstitutionDAO, a decentralized autonomous organization that is raising money from crypto people to buy a copy of the U.S. Constitution. (Here is  a Bloomberg News story about it.) People are interested in the legal structure of this thing. Basically it seems like there is a Delaware limited liability company that will take ownership of the document (if they win the auction), and there’s a tax-exempt organization called Endaoment that will act as the LLC’s “fiscal sponsor” and actually buy the document from the auction house and hold it on behalf of the LLC. These are normal legal entities, and the LLC’s members — in effect, the legal owners — are some of the humans who have promoted the DAO.But the DAO itself is a decentralized autonomous organization, a blockchain thing with governance tokens that can vote on what the DAO will do and smart contracts to aggregate those votes. And the connection between the DAO and the LLC is a little vague:The LLC is currently legally owned by DAO community members Alice Ma and Julian Weisser, who are representing the wider DAO community for this agreement. The DAO will advise the LLC owners on all actions taken. This structure is intended to be temporary and can be changed according to the DAO community’s wishes after the auction is complete. “Advise.” You can vote your governance tokens in the DAO, and then the two particular humans who run the LLC that owns the copy of the Constitution will take your votes under advisement. It’s not quite the sort of trustless decentralized blah blah blah that crypto promises.So what’s to stop those two humans from running off with the money, or the Constitution?[5] The answer absolutely cannot be “the immutable code of a smart contract on the blockchain,” because the Constitution is a piece of paper (parchment? whatever) that does not live on the blockchain, and a smart contract cannot stop someone from pocketing it and walking away. (And since the money for the purchase needs to be in dollars in a dumb old bank account, the smart contract probably can’t stop someone from stealing it either.) Conceivably the answer is “the DAO is actually a limited liability company under Delaware law, and the LLC agreement and Delaware law constrain the members of the LLC to do what the DAO says.” It’s not clear to me whether or not this is the case. It is tricky to do that, but a lot of lawyers are very much working on things like this, mechanisms to integrate DAOs and crypto-token voting into traditional business-entity and contract law. (Wyoming has a “DAO LLC” legal entity, though ConstitutionDAO chose not to use it.) Eventually one assumes that a world of crypto companies will have to operate like this: There will be smart contracts on the blockchain, and legal entities that carry out the smart contracts’ desires in the real world, and there will be well-understood interfaces between them, and statutes and case law that allow the smart contracts to govern the entities and so forth.But right now I suspect the main legal answer is the backup answer[6]: If they pocket the money, that sure looks like wire fraud, and the DAO investors can probably sue for fraud and also probably get prosecutors interested. The enforcement mechanism is: “If you market a thing with promises, and raise a lot of money from strangers based on those promises, you’d better try hard to do what you promised or you’ll get in trouble for fraud.” Not always! In particular, if you are ripping people off on the blockchain, there’s a decent chance that courts and prosecutors will laugh at your victims rather than throwing the book at you. But if you raise enough money in a high-profile enough way, you should probably try to do what you say you’ll do.
  
    
      Fearless Girl
    
  
Do you  remember  Fearless Girl? State Street Global Advisors, the big investment firm, commissioned a bronze statue of a girl with her hands on her hips staring down, originally, the Charging Bull statue in downtown New York. (The sculpture has  since moved.) The statue was meant as an ad for State Street’s commitment to putting women on corporate boards, but it became pretty popular well beyond fans of asset management, and I think most people who think about Fearless Girl think of her as a general symbol of feminist empowerment rather than as an ad for State Street. For instance here is Kristen Visbal, the sculptor who made Fearless Girl:Visbal said, “I do feel she is an unofficial symbol for the women’s movement. We needed a symbol. That’s why she took off.”On the other hand, you know who does not think that Fearless Girl is a general symbol of feminist empowerment, and wants to make sure that she is associated only and always with State Street? State Street:Visbal made twenty-five editions of “Fearless Girl” and two artist’s proofs. She sold eight replicas, for up to two hundred and fifty thousand dollars, including one to the law firm Maurice Blackburn, in Melbourne, Australia, and one to an investor in Oslo, who put the statue in front of the city’s Grand Hotel, which he owns. Visbal also sold more than a hundred miniature versions for about six thousand dollars each, and took a resin copy to the Women’s March in Los Angeles in January, 2019. A month later, State Street sued Visbal, accusing her of breach of contract, and of causing “substantial and irreparable harm” to Fearless Girl and to State Street by selling copies. Visbal filed a counterclaim, alleging that State Street was hampering her ability to spread Fearless Girl’s message of gender equality.She should make another statue of herself staring down State Street, and put it next to Fearless Girl.
  
    
      Things happen
    
  
SEC  Moves to Reverse Trump-Era Rule Chided by Activist Funds. Pressure's on 9th Circuit to revisit ‘direct listing’ in Slack decision. NFT Marketplace OpenSea Offered $10 Billion Valuation.  Gemini Crypto Exchange Seeks Funding at $7 Billion Valuation. SEC Investigating Cassava Sciences, Developer of Experimental Alzheimer’s Drug. JPMorgan suggests Credit Suisse bonuses could be low forever. “Some of the stolen crypto was used to  purchase a ‘rare’ online gaming username, which eventually led investigators to uncover the identify of the account holder.” Why Paul Rudd edged me out as sexiest man alive. “The German shepherd, whose main home is in Tuscany, joins in with the real estate agents' meetings, travels on private jets, and has meals cooked by a chef.”If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] I mean, you could make the case that it’s better? “We’ll underprice our thing, sell a lot of it at a loss, become huge, dominate the market, and be able to jack up prices” is a standard sort of aspirational business story. It seems hard to do in home-buying, it does not seem to have been Zillow’s conscious intent, and it is not generally how financial traders think. But in tech startups, sure, that's a thing.[2] In fact, Zillow’s tweaks do not seem to have been, like, driven by a deep understanding of markets and sophisticated modeling: “Analysts whose job it was to confirm the prices of homes found that they were routinely overruled, those people said, because the company had retooled the system to raise the analysts’ suggested prices. Automatic price add-ons coded into the company system, including one called the ‘gross pricing overlay’ that could add as much as 7%, would boost offering prices to get more home sellers to say yes.”[3] I know, I know, the traders are saying: “No, this is stupid, your algorithms will not be 100% precise, some of your ‘lowball’ bids will in fact be too high, and those will be the ones that sellers accept. You’ll get adverse selection and end up losing money.” But that was not Zillow’s actual experience in the first quarter! The actual experience is presumably that *some* people accidentally got too-high bids, realized they were good and accepted them, but *mostly* Zillow sent too-low bids to everyone, and some people, for whatever irrational reason — market ignorance or financial necessity or laziness or whatever — accepted the too-low bids. The general point is that there is no reason at all to think that the people on the other side of these trades from Zillow are generally *better informed* than Zillow is. Sure they know more about their houses than Zillow does, but Zillow knows more about the market, and has more money. The business model I describe in the text is not *easy*; you need a good algorithm to find prices that are plausible but too low. But it is *good*.[4] Occasionally they will  get it wrong in amusing technical ways, though.[5] This section was inspired by a Twitter exchange about this question with Felix Salmon and others this morning.[6] Of course there are non-legal answers. Scott Lewis tweeted: “i might say threats exist, but on different vector. you see how the names and social profiles of the multisig and projects starters are very visible? they are staking social capital. (i and others know many of them personally) if they rug, their reputations will suffer greatly.” But of course people do fraud using their Twitter handles all the time; this is not a perfect enforcement mechanism. 
        
      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like Money Stuff? | 
Get unlimited access to Bloomberg.com, where you'll find trusted, data-based journalism in 120 countries around the world and expert analysis from exclusive daily newsletters.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cfbxzn.5i16/2bc9fe48.gif" alt="" border="0" /></a>
