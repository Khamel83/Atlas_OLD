# =?utf-8?B?TW9uZXkgU3R1ZmY6IERlRmkgRGlzY292ZXI=?=
 =?utf-8?B?c8KgTmV3IE1hcmtldCBNYW5pcHVsYXRpb25z?=

**From:** Matt Levine <noreply@mail.bloombergview.com>
**Date:** Wed, 12 Oct 2022 14:32:58 -0400 (EDT)
**Source:** inputs/saved_emails/=utf-8BTW9uZXkgU3R1ZmY6IERlRmkgRGlzY292ZXI==
 =utf-8Bc8KgTmV3IE1hcmtldCBNYW5pcHVsYXRpb25z=_Wed,_12_Oct_2022_14-32-58_-0400_(EDT)_183cd78bd3aa0c93.eml
**Processed:** 2025-08-24T19:13:12.564893



  
  
    
      
        
      
    
  
  
    
      
        The simplest form of market manipulation is: Buy a lot of Thing X, pushing its price up. Sell it at the new high price, for a profit. This, 
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Mango
    
  

The simplest form of market manipulation is:
	Buy a lot of Thing X, pushing its price up.	Sell it at the new high price, for a profit.

This, I frequently   point out, should not work. In Step 1, you push up the price of X by buying it; therefore, in Step 2, you will push the price down by selling it. There are no free lunches that are this simple.
Here is a small modification that seems promising:
	Buy a lot of Thing X, pushing its price up.	
Borrow against your X: If you have 100 million X, and X is now worth $1, then you have $100 million worth of X, and maybe someone will give you, say, a $50 million margin loan against it.	Run away with the $50 million.

The reason this seems promising is that you are not selling X in Step 2, which means you are not pushing down its price. Still it strikes me as doubtful, in the general case. You had to spend a lot of money to (1) accumulate 100 million X and (2) push its price up. If X started at $0.01, and ended at $1, and you bought 100 million of it to get it there, then you probably paid an average price of around $0.50. (You bought your first 1 million at $0.01, your next 1 million at $0.02, etc.) So you paid about $50 million to push the value of your holdings to $100 million. But you can’t borrow the full $100 million: At best, you’ll probably get a margin loan of about $50 million. So you’ll get back roughly what you put in, or realistically less given various frictional costs.
I don’t want to rule this out entirely: This might work if (1) you are good at manipulating the price, in the sense that you know how to make the price move without spending too much money, and (2) someone will give you a margin loan at a high loan-to-value ratio. This approach is roughly   what Bill Hwang is accused of at Archegos Capital Management: He allegedly traded tactically in ways that moved stock prices a lot, and borrowed 90% or more of the value of his positions from his banks. If he played it perfectly — and there is no evidence that he did — then he could have taken out way more money than he put in, leaving his banks with the losses. Overall though this approach seems hard.
But you can work with it. Here is a subtler modification:
	Thing X trades at $0.01.	You go to a not-particularly-busy futures trading platform, open an account and offer 100 million X futures for $0.01. Futures are generally leveraged products, where you don’t have to pay the full amount of the trade upfront. But let’s say you do: You put up $1 million of collateral for this $1-million-notional position.	You walk out of the futures trading platform, put on a fake mustache, walk back in, open a new account and bid to buy 100 million X futures. You put up, say, $1 million of collateral for this position.	The futures platform is not particularly busy, so no one else wants to buy or sell X futures and you end up trading with yourself. You don’t move the price of X or anything, but your two orders cross and you end up both long and short 100 million X futures — in two different accounts — at $0.01.	You go to a regular exchange and start buying X in the open market, pushing the price up to $1. Let’s say X is not all that liquid. You buy 10 million X, starting at $0.01 and ending up at $1. Your average cost is about $0.50, so you spend about $5 million.	You have spent a total of $7 million: $1 million to get long futures, $1 million to get short futures, $5 million to push up the price of X.	Now you put the fake mustache back on, go back to the futures exchange and say “I see that my long futures position is in-the-money by $99 million. I would like to borrow $40 million against my winnings.”	The futures exchange looks at the $1 price on the spot market and says, yep, sure enough, you’re up $99 million. They want to keep some collateral against this position, but they’ll give you some back. So they give you the $40 million, and you stuff it in a suitcase and drive off.	Meanwhile they call you on your other phone number — the number you gave them in Step 2 — to say “hey your 100 million short futures position moved against you by $99 million, could you please send us that money,” but that call goes straight to voicemail and they never hear from you again.	Your net profit is $33 million, the $40 million from Step 8 minus the $7 million from Steps 2, 3 and 5.

This approach is stupid and should not work. It requires:
	A pretty illiquid market for the underlying Thing X, so that you can push the price around without spending much money.	A very sleepy futures market, where you can just trade with yourself without anyone noticing and without moving the price.	A futures market that will let you trade very large size, despite being very sleepy: Given how illiquid and volatile Thing X is in my example, it would be silly for a futures market to actually let you put on a 100 million X futures position, particularly with so little collateral.	A futures market that will cheerfully cash you out on your unrealized gains in Step 7, even though the contract has moved in your favor rapidly and suspiciously. 	A futures market that won’t come after you for your losses in Step 9.

I think you would have a hard time running this trade in, like, the oil market. Still it hangs together in a rough schematic way, which means you can try it in the crypto market. Crypto, particularly decentralized finance, has some key advantages for this, including:
	Weird and fragmented liquidity, so that you can trade with yourself on a futures exchange, and you can move the price of a token a lot on the spot market;	A love of mechanical rules and automated markets, so that if your X position spikes from $1 million to $100 million, some decentralized finance platform will say “yup, now it’s worth $100 million, so it’s good collateral for a $40 million loan”; and	A presumption of anonymity, so exchanges will let you trade with yourself, and won’t be able to come after you for your losses, since they just have some anonymous wallet addresses.

Here you go:

An attacker spirited away about $100 million from decentralized finance provider Mango by manipulating the price of its token in an exploit that wiped out depositors on the crypto platform.
The heist began with two accounts funded with the stablecoin USD Coin, the platform said Wednesday on Twitter. The accounts took large positions in Mango perpetual futures, causing the price of the Mango token to spike.
The price jump stoked an unrealized profit from the futures. The attacker used that to borrow and withdraw roughly a net $100 million from the protocol in a range of tokens -- leaving depositors with nothing, according to Mango.
“This incident has effectively resulted in a total draining of all equity available,” the platform said on Twitter, adding the attackers are communicating with Mango and “indicating a willingness to negotiate.”

Crypto derivatives trader Joshua Lim  explained the exploit on Twitter, and it is pretty much the schematic thing I laid out above. The attacker funded one account on the Mango perpetual futures exchange with $5 million, offered 483 million futures on Mango’s own MNGO governance token, funded another account with another $5 million, and lifted those 483 million futures at a price of $0.0382. Then the “attacker started to move the price of MNGO” on the spot market, by buying MNGO tokens on centralized exchanges. “At MNGO/USD price of $0.91 per unit, account B was in the money by 483mm * ($0.91 - $0.03298) = $423mm,” and “that was enough unrealized P&L to take out a loan of $116mm across a bunch of tokens, which then left Mango and leaves the protocol at a deficit.” 
Look, I had never heard of the Mango token until this morning, which is a crucial advantage for me. If you had come to me and said “I have Mango tokens with a market value of $423 million, I want to use them as collateral for a loan, would you lend me $116 million against these Mango tokens?” I would have said “absolutely not, Mango tokens, not a thing.” And that would have been correct, both in the narrow sense that the “real” market value of 483 million Mango tokens was about $18 million and in the broader sense of, well, why was it even $18 million? But the Mango protocol itself just had some price oracles that connected to some exchanges, and when those exchanges showed that the tokens were trading at $0.91, it believed them. So it computed a value of $423 million, and that was plenty of collateral to support a $116 million loan, and there you go. Mango could look at market prices, but it could not apply common sense, and that was its problem.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      Bored apes
    
  

Bored Ape Yacht Club (BAYC) is an entity that owns the intellectual property rights to some cartoons and tries to make money by 
licensing them to Seth Green or whatever. BAYC issues several sorts of financial instruments, including “Apes,” which convey certain intellectual property rights to particular cartoons, and “ApeCoins,” which give you the right to vote on things like (1) who BAYC should license its cartoons to and (2) how the money should be spent. These instruments trade on financial markets, and the more demand there is for the cartoons (and the more money BAYC makes), the more valuable Apes and ApeCoins will be.
That is a loose description of the situation, and you could quibble with some details. Still I think it is more right than wrong. What legal conclusions can you draw from it? It’s never legal advice around here, but here are some thoughts:
	ApeCoins are shares of stock in the BAYC entity, and are therefore securities under US law;	Apes are arguably securities under US law, though it is debatable.

A security is “the investment of money in a common enterprise with a reasonable expectation of profits to be derived from the efforts of others.” Is an Ape — which conveys certain rights to one particular cartoon — an investment in the “common enterprise” of BAYC, or is it more like buying a particular work of art that you can then do with as you please? I think there’s a pretty good case that it’s more like a work of art, like buying a cartoon — even though the value of that cartoon will obviously depend on the collective value of BAYC and the efforts of its managers. But the ApeCoins — which are fungible and carry voting rights to do things like  elect the board of directors of BAYC — I mean, what could they possibly be but securities of the entity that is BAYC? 
 Anyway:

The US Securities and Exchange Commission is investigating Yuga Labs Inc., the creator of the popular Bored Ape Yacht Club collection of NFTs, over whether sales of its digital assets violate federal law.
The SEC is examining whether certain nonfungible tokens from the Miami-based company are more akin to stocks and should follow the same disclosure rules, according to a person familiar with the matter, who asked not to be named because the probe is private. Wall Street’s main regulator is also examining the distribution of ApeCoin, which was given to holders of Bored Ape Yacht Club and related NFTs. The cryptocurrency was created in part for web3, a vision of a decentralized internet built around blockchains.

Now I think that BAYC has some good defenses here. “Certain nonfungible tokens from the Miami-based company” (Apes, and various spinoff cartoons) may in fact be “more akin to stocks,” but I think there’s a good argument that they’re not. (They’re works of art, let’s say.)
Meanwhile ApeCoin seems like stock to me, but for the most part Yuga/BAYC did not sell it for cash: ApeCoins were given away to holders of Apes, without payment, so there was no investment of money and no offering for cash. Meanwhile hundreds of millions more ApeCoins were given to the BAYC treasury (to be sold to raise cash for the entity), to Yuga Labs (to reward the corporation for its investment in building BAYC) and to its founders and other “launch contributors,” all of which can be sold for cash, but most (not all) of those were locked up for 12 months or more, so Yuga and BAYC have an argument that they did not do an illegal securities offering.
  [1]
 “Sure we gave out stock, but we didn’t sell it, so it’s fine,” is roughly the defense, which is not perfect but also not ridiculous.
Still I guess the main points here are (1) governance tokens of crypto projects are probably securities and (2) the SEC has noticed.
One other thing. I have called BAYC an “entity,” which is a nice generic term, but it appears to  call itself a DAO, a decentralized autonomous organization. There are some advantages to calling your entity a DAO rather than a corporation. For one thing, shares of stock of corporations are obviously securities subject to SEC regulation, while governance tokens of DAOs are … also obviously securities subject to SEC regulation, I think, and the SEC thinks, but some people seem to disagree. So you can say “what, it’s a DAO, governance tokens, not stock, no securities here,” and maybe someone will believe you. For another thing, it is good marketing: The people buying your DAO governance tokens believe in a future of crypto and decentralization, and they’d be disappointed to buy shares of stock in a corporation. They want some “decentralization” branding on their shares, so you give it to them.
But there is also a big disadvantage to calling your entity a DAO rather than a corporation. A corporation is a particular sort of legal entity that has one key feature, which is limited liability. If you own shares of a corporation, you are not generally responsible for (1) the debts of that corporation or (2) its crimes. (If you are also an executive and you do the crimes, you are responsible, but simply being a shareholder does not make you responsible for the actions of the corporation.) This is a special feature of corporations (and some other entities like limited liability companies or limited partnerships), and corporations have to take affirmative steps (file incorporation documents, pay fees, etc.) to get this protection.
If you don’t do that — if you just get together with your buddies and start a business without incorporating it — then you don’t get those protections. Instead, you have the default form of business organization, just a group of people doing a business without paperwork, which might be called a “general partnership” or an “unincorporated association.” A general partnership  does not have limited liability. If your partnership incurs a debt — if one of your partners borrows money on behalf of the partnership and then loses it — then you are responsible for it. If the partnership does crimes, you might get in trouble.
This is why people, in traditional business, tend to do the paperwork to form corporations (or limited liability companies, limited partnerships, etc.). In crypto business, some combination of libertarianism, naivety, we’re-doing-stuff-no-one-has-seen-before exceptionalism, and a desire to evade securities laws leads people to avoid that paperwork. And then you have a DAO with no paperwork, which is a general partnership, and oops.
And so last month the US Commodity Futures Trading Commission  brought an enforcement action against a decentralized finance platform called bZeroX and a DAO called Ooki DAO, and said:
The Ooki DAO is an unincorporated association comprised of holders of OokiDAO Tokens (“Ooki Tokens”) who vote those tokens to govern (e.g., to modify, operate, market, and take other actions with respect to) the bZx Protocol (which the Ooki DAO has renamed the “Ooki Protocol”). 
The CFTC’s view is that just buying governance tokens doesn’t make you a general partner in the DAO, but buying those tokens and voting them does. As one CFTC commissioner  said in dissent:
Under the Commission’s definition, [a token holder who votes] has now become a member of the unincorporated association and (possibly unknowingly) assumed personal liability and is subject to CFTC sanctions for any violations of the [Commodity Exchange Act] by the Ooki DAO.
It is possible that DAOs are just the worst of all worlds: Their tokens are similar enough to corporate shares to be subject to securities laws, but different enough to create unlimited liability for their holders.

  
    
      
        
      
    
  


  
    
      Oh Elon
    
  

Look, I think that Elon Musk is going to close his deal to buy Twitter Inc. by the end of the month. He   has said he will, Twitter (presumably) wants that, he has the money, he will get extremely in trouble with the Delaware Court of Chancery if he does not, he seems to have a renewed enthusiasm for messing with Twitter, I think it will happen. (Not, ever, investment advice!) That said lots of people are understandably skeptical, and he changes his mind a lot, so I keep reading theories about how he might still wiggle out.
Here I want to discuss two of them briefly, not because I think they are great theories but because people keep asking me about them. One is that Musk has put a lot of effort recently into  spreading Russian and Chinese propaganda? On Twitter, he has  endorsed most of Vladimir Putin’s war aims in Ukraine, and in a lunch interview with the Financial Times he  called for China to annex Taiwan. (There is also  a sketchy report, which he has denied, that Musk talked to Putin before endorsing his annexation of parts of Ukraine.) He is a man with many weird hobbies, but this is a particularly odd hobby, and as far as I can tell a new one. One possibility here is that (as he says) he is worried about the risk of nuclear war and wants to defuse geopolitical tensions by tweeting polls or whatever. Another possibility is that China is a critical market for Tesla Inc., and he is seeking China’s favor.
But the fancier possibility is that he is trying to get American government officials worried, so that they will step in to block the Twitter deal. “We can’t let Twitter, the ‘town square’ of American political discourse, be owned by a guy who might be a Chinese or Russian agent, so we have to block the deal,” people think Musk thinks the government will think. By winkingly hinting that he might be doing Vladimir Putin’s bidding, the theory goes, Musk will force the US government to block his acquisition of Twitter. Which would get him out of it, which is — perhaps — what he wants.
I don’t really buy this — I don’t think that the US government has much of a mechanism to block the deal at this point, and I think it would be too controversial for anyone to touch — but it is a funny theory so I am passing it along. On the other hand, if you don’t believe this theory, and I don’t, then you are left with an alternative theory like “Musk really does like spreading Chinese and Russian propaganda, and now he’ll own Twitter,” and that’s perhaps not ideal.
The other, less funny theory is that Musk will tank his debt financing for the deal by refusing to deliver a solvency certificate. Musk’s obligation to close the deal is conditional on his banks funding their $13 billion loan commitment, and their obligation to fund is conditional on — well, it’s conditional on very little; there are almost no excuses for them not to fund, but there is one. There is a condition in  the commitment letters that requires that, before funding:
Customary legal opinions, customary officer’s closing certificates (including incumbency certificates of officers), organizational documents, customary evidence of authorization and good standing certificates in jurisdictions of formation/organization, in each case with respect to the Borrower and the Guarantors (to the extent applicable), customary requests for borrowing and a solvency certificate (as of the Closing Date after giving effect to the Transactions and substantially in the form of Annex E-I attached hereto, certified by a senior authorized financial officer of the Borrower) shall have been delivered to the Lead Arrangers.
That is, before the banks will lend money to Twitter so that Musk can buy it, they’ll need some paperwork saying things like “Twitter is a real company” and “Twitter wants to borrow this money” and “the person who signed the document on Twitter’s behalf actually works at Twitter and is authorized to sign that document.” And they will need some paperwork — the solvency certificate — saying that:
	The sum of the liabilities (including contingent liabilities) of the Borrower and its restricted subsidiaries, on a consolidated basis, does not exceed the present fair saleable value of the present assets of the Borrower and its restricted subsidiaries, on a consolidated basis.	The fair value of the property of the Borrower and its restricted subsidiaries, on a consolidated basis, is greater than the total amount of liabilities (including contingent liabilities) of the Borrower and its restricted subsidiaries, on a consolidated basis as such liabilities become absolute and mature.	The capital of the Borrower and its restricted subsidiaries, on a consolidated basis, is not unreasonably small in relation to their business as contemplated on the date hereof.	The Borrower and its restricted subsidiaries, on a consolidated basis, have not incurred and do not intend to incur, or believe that they will incur, debts including current obligations beyond their ability to pay such debts as they become due (whether at maturity or otherwise).

Here I am quoting from the “Form of Solvency Certificate” in Annex E-1 to the commitment letters; “the Borrower,” here, means Twitter, though Twitter “after giving effect to” Musk’s acquisition. It is not entirely clear to me who has to sign this certificate — technically, it’s an officer of Twitter — but people seem to think that Musk can say “well, if I take over Twitter, I will appoint myself as chief financial officer, and then I will refuse to sign this certificate, and then the banks won’t lend, so I can’t take over Twitter.” That is convoluted but, fine, I guess, I don’t know.
Could he do this? I mean, (1) not investing advice! but (2) no? He agreed — last week! — to pay $46 billion for Twitter, so it would be hard for him to argue that it’s not worth more than $13 billion, the amount it will borrow. And while Twitter will have to work a bit to pay its debt — “Twitter now faces an annual interest burden of nearly $1.2 billion,” reports   Bloomberg’s Paula Seligson, and “might not become free-cash-flow positive until 2025” — it has a lot of cash on its balance sheet and is unlikely to run out of money to pay interest anytime soon. Twitter will have a lot of debt, but it seems hard to argue that it’s insolvent. Also, just, Musk’s lawyers told a court last week that they expected the banks to fund; if he blows that up now he’s going to have a lot of explaining to do. I don’t see it, but I pass it along to you because I know nothing and there are still like two weeks left on this thing. Presumably something will happen that surprises me.

  
    
      Things happen
    
  

Gilts sell off as Bank of England reiterates plan to  end bond-buying scheme. BOE Credibility on the Line Amid   Pension Deadline Confusion. White House Weighs Ban on   Russian Aluminum Over Ukraine War Escalation. That Sky-High  I Bond Interest Rate Will Be Coming Down to Earth.  CVC’s biggest bet yet: the fiercely private buyout firm set to go public. Nigeria Exploring   Restructuring Some Debt, Finance Minister Says. Credit Suisse Shares Drop on   US Tax Probe Over Accounts. Nike to Crack Down on  Sneaker-Buying Bots, Dealing a Blow to Resale Market. Crypto Exchange  Bittrex to Pay $29 Million Over Violating Sanctions. Musk Launches New ‘Burnt Hair’ Perfume With Fragrance of ‘Repugnant Desire.’ Fake Russian Astronaut Duped Woman Of Rs 24 Lakh, Said He Needed Money To 'Return To Earth.'
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] There is a  rough rule of thumb that if you get securities from an issuer and wait one year before selling them, then they are exempt from registration and you can sell them freely. This is not legal advice and there are many exceptions, but it’s part of why many crypto projects have one-year lockups on tokens that they sell to investors.


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like getting this newsletter? 
Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23chh3x7.69il/57e9f697.gif" alt="" border="0" /></a>
