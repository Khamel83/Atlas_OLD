# Money Stuff: Web3 Takes Trust Too

**Source**: inputs/saved_emails/Money Stuff Web3 Takes Trust Too_Mon,_10_Jan_2022_13-32-56_-0500_(EST)_17e4544f9a6864e9.eml
**Type**: email
**Created**: 2025-08-25T02:54:10.428176

---

Web3The only cryptocurrency that I own is ExcelCoin.[1] ExcelCoin is a next-generation cryptocurrency whose central innovation is that its l
      
    
  
  
    
      
  
    
      
        
      
    
  


        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Web3
    
  
The only cryptocurrency that I own is ExcelCoin.[1] ExcelCoin is a next-generation cryptocurrency whose central innovation is that its ledger is maintained not by proof of work, which is environmentally problematic, or by proof of stake, which has its own problems, but by me. I maintain the ledger in Microsoft Excel. Here is a copy of the ledger as of 9 a.m. today[2]:If you want to buy some of my quadrillion ExcelCoins, send me an email[3]; I will make a market at $0.99 bid / $1.01 offered,[4] though of course that is subject to change with market conditions.[5]Of course ExcelCoin started as a currency, a form of “digital cash,” but what is powerful about the concept is that in principle you could track any sort of asset using the same underlying technology (me typing in Excel). For instance you could extend the ExcelCoin technology to track not merely fungible tokens like coins, but also non-fungible tokens, where each entry in the ledger represents a unique asset. For instance:This is just a toy example — why would you want me to write “a picture of a cat” next to your name on a list? — but with a little imagination you can see how powerful it could be. For instance, we could track real estate this way. I could write down a list of all the houses in my town and who owns them; to transfer ownership we could just update the entries on my list. As of yet my list in Excel does not carry any legal ownership rights; it does not sync up with, or supersede, the legal property registry. But I think that you will agree that it is a much more efficient and technologically advanced system than the old legal system of property registration on paper in dusty archives, so I think in the long run it is likely to win out.This is stupid, why is it stupid. The easy answer is that it is technologically stupid. Actual cryptocurrencies (and blockchain systems for NFTs, proposed blockchains for real estate, etc.) have a distributed consensus mechanism for updating their shared ledger, proof-of-stake or proof-of-work or some other mechanism that lets the participants in the system verify and collectively control the ledger. Whereas I can type whatever I want in Excel. If you buy some ExcelCoins from me and I delete your entry in my Excel ledger, you don’t have any ExcelCoins anymore, and what sort of system is that?A better answer is that it is socially stupid, because the person maintaining the ExcelCoin ledger is me, and I am obviously kidding. You should not trust me to maintain the ExcelCoin ledger, because I invented ExcelCoin as a joke about ledgers. On the other hand millions and millions of people own U.S. dollars,  which means precisely that some bank has a list and there is an entry for them on that list. It’s probably not in Excel, but same basic idea: The bank has a list of dollars in its accounts, the list is not kept via any sort of consensus mechanism or blockchain or whatever; the bank just keeps the list using, uh, Cobol. But you (mostly) trust the bank to maintain the list, because among other things (1) it has a good track record of maintaining the list, (2) it has good commercial incentives to maintain the list, (3) it has powerful regulatory and legal incentives to maintain the list, etc.[6] The bank’s list is not any great shakes technologically, and 100 years ago banks kept very similar lists using pen and paper. This system of lists is not flawless — sometimes the banks mess up the lists! — but it is not howlingly stupid either, in the way that ExcelCoin is. It's very normal and standard and millions of people rely on it without thinking about it.[7] ExcelCoin is stupid not because I keep it in Excel; it's stupid because I keep it in Excel.On Friday Moxie Marlinspike wrote a blog post on “My first impressions of web3.” Marlinspike is a famous cryptographer and computer-security guy, the inventor of the Signal app, etc., and the post has gotten a ton of attention in the Web3 (and Web3-skeptical) world; it’s great and I recommend it highly and I will only scratch the surface of it here. One relevant point is that distributed ledgers are not necessarily a complete technological solution for asset ownership:Most people think of images and digital art when they think of NFTs, but NFTs generally do not store that data on-chain. For most NFTs of most images, that would be much too expensive.Instead of storing the data on-chain, NFTs instead contain a URL that points to the data. What surprised me about the standards was that there’s no hash commitment for the data located at the URL. Looking at many of the NFTs on popular marketplaces being sold for tens, hundreds, or millions of dollars, that URL often just points to some VPS running Apache somewhere. Anyone with access to that machine, anyone who buys that domain name in the future, or anyone who compromises that machine can change the image, title, description, etc for the NFT to whatever they’d like at any time (regardless of whether or not they “own” the token). There’s nothing in the NFT spec that tells you what the image “should” be, or even allows you to confirm whether something is the “correct” image.So as an experiment, I made an NFT that changes based on who is looking at it, since the web server that serves the image can choose to serve different images based on the IP or User Agent of the requester. For example, it looked one way on OpenSea, another way on Rarible, but when you buy it and view it from your crypto wallet, it will always display as a large [poop] emoji. What you bid on isn’t what you get. There’s nothing unusual about this NFT, it’s how the NFT specifications are built. Many of the highest priced NFTs could turn into [poop] emoji at any time; I just made it explicit.The NFT does not by itself convey ownership of the underlying thing in either a legal or practical sense. It conveys ownership in some more metaphysical sense: If you buy a Bored Ape Yacht Club NFT, then the people who are part of the BAYC NFT community will treat you as the owner of your ape. This is essentially a social fact and can be true even if the immutable code of the blockchain says that you don’t own the ape, because you were hacked or whatever. The technology is a scaffolding on which to hang a social system, but the social system is what does or does not convey “ownership” in a meaningful sense.Also the technology is totally centralized? Marlinspike goes on:After a few days, without warning or explanation, the NFT I made was removed from OpenSea (an NFT marketplace). ...What I found most interesting, though, is that after OpenSea removed my NFT, it also no longer appeared in any crypto wallet on my device. This is web3, though, how is that possible?A crypto wallet like MetaMask, Rainbow, etc is “non-custodial” (the keys are kept client side), but it has the same problem as my dApps above: a wallet has to run on a mobile device or in your browser. Meanwhile, ethereum and other blockchains have been designed with the idea that it’s a network of peers, but not designed such that it’s really possible for your mobile device or your browser to be one of those peers.A wallet like MetaMask needs to do basic things like display your balance, your recent transactions, and your NFTs, as well as more complex things like constructing transactions, interacting with smart contracts, etc. In short, MetaMask needs to interact with the blockchain, but the blockchain has been built such that clients like MetaMask can’t interact with it. So like my dApp, MetaMask accomplishes this by making API calls to three companies that have consolidated in this space.For instance, MetaMask … displays your NFTs by making an API call to OpenSea. ...All this means that if your NFT is removed from OpenSea, it also disappears from your wallet. It doesn’t functionally matter that my NFT is indelibly on the blockchain somewhere, because the wallet (and increasingly everything else in the ecosystem) is just using the OpenSea API to display NFTs, which began returning 304 No Content for the query of NFTs owned by my address!The technology behind OpenSea is not quite “OpenSea keeps a list, in Excel, of who owns which NFTs.” The underlying list is kept on the blockchain; it’s just that OpenSea can modify its version of the list however it wants, and its modifications are in practice pretty binding. And in fact there are regular rounds of stories in which (1) some gullible crypto guy hands out his private key to anyone who asks for it, (2) his NFTs get stolen, (3) he complains on Twitter, (4) he gets a major NFT marketplace to lock trading in his stolen NFTs, and (5) everyone writes articles like “ha ha ha you don’t like decentralization so much now do you?” This is fine, though, Web3 proponents argue, because OpenSea’s ability to act arbitrarily is limited by community standards. The open immutable blockchain still exists, so you can compare what OpenSea says to what the blockchain says. (Perhaps not with MetaMask, but the possibility exists.) If OpenSea’s list did not conform to what its customers expected — if it arbitrarily ignored the blockchain, if it let people claim NFTs that weren’t theirs, etc. — then everyone would take their apes elsewhere. But this is pretty much why people trust banks too! The essential protections are social, not technological.Marlinspike:When you think about it, OpenSea would actually be much “better” in the immediate sense if all the web3 parts were gone. It would be faster, cheaper for everyone, and easier to use. For example, to accept a bid on my NFT, I would have had to pay over $80-$150+ just in ethereum transaction fees. That puts an artificial floor on all bids, since otherwise you’d lose money by accepting a bid for less than the gas fees. Payment fees by credit card, which typically feel extortionary, look cheap compared to that. OpenSea could even publish a simple transparency log if people wanted a public record of transactions, offers, bids, etc to verify their accounting.However, if they had built a platform to buy and sell images that wasn’t nominally based on crypto, I don’t think it would have taken off. Not because it isn’t distributed, because as we’ve seen so much of what’s required to make it work is already not distributed. I don’t think it would have taken off because this is a gold rush. People have made money through cryptocurrency speculation, those people are interested in spending that cryptocurrency in ways that support their investment while offering additional returns, and so that defines the setting for the market of transfer of wealth.The people at the end of the line who are flipping NFTs do not fundamentally care about distributed trust models or payment mechanics, but they care about where the money is. So the money draws people into OpenSea, they improve the experience by building a platform that iterates on the underlying web3 protocols in web2 space, they eventually offer the ability to “mint” NFTs through OpenSea itself instead of through your own smart contract, and eventually this all opens the door for Coinbase to offer access to the validated NFT market with their own platform via your debit card. That opens the door to Coinbase managing the tokens themselves through dark pools that Coinbase holds, which helpfully eliminates the transaction fees and makes it possible to avoid having to interact with smart contracts at all. Eventually, all the web3 parts are gone, and you have a website for buying and selling JPEGS with your debit card. The project can’t start as a web2 platform because of the market dynamics, but the same market dynamics and the fundamental forces of centralization will likely drive it to end up there.Similarly, technologically, ExcelCoin is in some ways better than other forms of crypto that rely on distributed consensus mechanisms. But socially it is much worse, not only because I am kidding and have done nothing to build up trust in ExcelCoin, but also because there is an enormous speculative bubble in crypto that does not apply to transparently non-crypto things like my dumb Excel joke. The power of distributed consensus and immutable blockchains is not that they are a better technology than, you know, some large trusted website keeping a list, which is kind of how Web3 works anyway. The power of distributed consensus and immutable blockchains is that they attract money,  which is really how Web3 works.
  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      ChampertyCoin
    
  
Last year, a bunch of people enjoyed speculating on meme stocks like GameStop Corp. Many of them used Robinhood Markets Inc.’s brokerage app to do it. At one point, Robinhood briefly limited purchases of GameStop and a few other meme stocks  due to clearinghouse issues, which made a lot of people very angry and gave rise to a bunch of conspiracy theories. Some meme-stock investors wanted to sue Robinhood over this, and in fact there was a class action lawsuit that was  dismissed in November.You might look at this dynamic and say: Well, sure, the people who bought GameStop in a speculative frenzy want to sue Robinhood. They want to sue Robinhood because they are angry, and, in America, suing people is a form of catharsis and emotional satisfaction. And they want to sue Robinhood because they think they have a valid claim and want to get monetary compensation for their losses from not being able to buy GameStop stock at, uh, $300 a share I guess. But there is a third desire that they might have, beyond emotional satisfaction and financial compensation: They might want to have another speculative frenzy. They might want to turn their grievance against Robinhood into a speculative asset, and then get rich trading it. You might think that because:	That’s what everyone wants all the time, these days. The lessons of GameStop and AMC and NFTs and Dogecoin and Web3 and ConstitutionDAO are always “people will seize on any excuse for a good speculative trading frenzy.” So if you can turn anything into a speculative trading frenzy, you should.	The people involved in the meme-stock speculative trading frenzy are maybe particularly interested in speculative trading frenzies.Here is a story about a company that wants to do litigation financing and let regular people trade litigation-finance claims, but on the blockchain, blah blah blah, it is very much the usual stuff you’d expect. I tend to think that there is a long list of asset classes that regular people do not trade frequently, and people are constantly saying “what if we built technology to allow regular people to trade this asset class,” and my answer tends to be “they would not trade it because nobody wants this.” (People are constantly trying to get regular people to  trade small slivers of individual office buildings, for no obvious reason.) Litigation finance, sure, whatever, I do not think that there’s a huge audience of people who want to research and bet on individual lawsuits, or that there's a huge pool of plaintiffs who want to finance their lawsuits by conducting a registered securities offering, but that is just one man’s opinion and yeah why not, go nuts. Possibly not this nuts:However, on its website, Ryval focuses all of its attention on the potential return for investors. “Buy and sell tokens that represent shares in a litigation and access a multi-billion dollar investment class previously unavailable to the public,” the company states. Ryval also promises “50%+ Annual Returns,” though Roche admitted the figure “may be a little high” when Motherboard asked him about it.But then there’s this:But it wasn’t until after the initial Apothio ILO was launched that Roche realized the potential of the platform. That occurred in January of last year, when the online trading platform Robinhood temporarily suspended trading of GameStop shares after a massive surge of meme-related interest. The decision led some to accuse the trading platform of unlawful manipulation.  “There was an explosion of ‘When can we ILO Robinhood? We want to hold Robinhood accountable,’” Roche said. “ILO” is “initial litigation offering.” How valuable was a GameStop-driven lawsuit against Robinhood? Well, the actual realized value seems to have been zero dollars, which is also the value that I personally would have predicted last year.[8] But could you have sold it for a bit more than its long-term fundamental value? To GameStop investors? In January 2021? 
  
    
      
        
      
    
  


  
    
      Congressional stock trading
    
  
Sometimes I read about couples where one spouse works at a bank and the other works at a hedge fund and I think “ugh what a compliance nightmare.” Lots of regulated financial firms (and related firms like law firms, consultancies, etc.) have pretty strict rules about personal trading, to prevent their employees from using inside information inappropriately; they require pre-approval of trades, ban trading in names that employees are working on, or sometimes even ban all trading in individual stocks. And to avoid obvious gaming of these rules, they tend to extend to the employee’s family. If you work at a bank and your spouse is a schoolteacher, this is fine — though if your spouse is also a hobbyist stock trader you might have to make some difficult choices — but if you work at a bank and your spouse works at a hedge fund it seems harder. You can’t really expect the hedge fund to get pre-approval from the bank. I suppose people work this stuff out — there are lots of financial-industry couples — but it does seem like in concept it would be challenging.Anyway:Georgia Sen. Jon Ossoff is looking to introduce a bill that would ban members of Congress from trading individual stocks — a practice that House Speaker Nancy Pelosi has defended as her husband rakes in millions of dollars trading shares of tech companies, The Post has learned.The Ossoff ethics bill, which the Democratic freshman Senator plans to introduce once he finds a Republican co-sponsor, would crack down on conflicts of interest by making it illegal for lawmakers and their families to trade stocks while in office, a Washington, D.C. source close to the situation said. It would also likely require lawmakers put their assets in blind trusts — a step that the 34-year-old Ossoff completed himself months after being elected in January 2021. Seems rough if you’re a congressperson married to a hedge fund manager but perhaps that is a feature, not a bug. I will say though that as far as I can tell most of the useful inside information that congresspeople get is about broad sectoral themes, not individual stocks; if you only own index funds and  get a terrifying secret briefing about Covid, you could profitably dump those index funds without ever trading an individual stock. I guess the blind trust addresses that problem.
  
    
      Oops
    
  
You wouldn’t know it from a quick look at Bloomberg, but the stock of AeroCentury Corp. closed at $47.99 on Friday. Then over the weekend it completed a 5-for-1 stock split, so Bloomberg’s historical price page retroactively adjusted to show a Friday closing price of $9.598. Then people woke up for pre-market trading this morning and … uh …NYSE Arca Equities in conjunction with other UTP exchanges, have ruled to bust all erroneous trades in ACY - AeroCentury Corp, executed between 4:00:00 - 4:04:00 ET today, at or above $11.52. This ruling is not eligible for appeal.Basically what seems to have happened here is you have a computer program to buy and sell AeroCentury stock, and the program merrily goes along and closes Friday thinking that AeroCentury is trading at $47.99, and then based on that and developments over the weekend it thinks “I will buy AeroCentury at $47 or sell it at $49” or whatever (actual numbers not important), and then before Monday morning you either do or do not update the program to be like “don’t forget to divide everything by 5.” And some people do and some people don’t. And the people who don’t, their programs wake up at 4 a.m. with a $47.00 / $49.00 market for AeroCentury, and the people who do, their programs wake up at 4 a.m. on Monday with a a $9.40 / $9.80 market for AeroCentury, and the people who think about it for a moment longer wake up with a $9.40 / $45.00 market for AeroCentury and sell some stock to the people who forgot at comically inflated prices. And then the stock exchanges bust the trades because this stuff — setting up to profit from other people’s ignorance and fat fingers — is really  more of a crypto thing.
  
    
      NFT Stuff
    
  
There is so much more miscellaneous crypto stuff; a sample of headlines:	“For Wine This Year Expect a Champagne Shortage,  NFT Surplus.”	“NFTs Offered by Candidates as  Crypto Creeps Into U.S. Politics.” 	“This crypto-backed start-up golf club just raised $11 million. Next up: buy a golf course.” 	“Pudgy Penguins  NFTs Infighting Turns Ugly as Crypto Mania Cools.” Do you like wine? Buy an NFT of wine. Do you like your senator? Buy an NFT of your senator. Do you like golf? Buy an NFT of a golf course. Uh … penguins? Everything. 
  
    
      Things happen
    
  
World’s Biggest  Crypto Fortune Began With a Friendly Poker Game. Inside private equity’s race to go public. The EU vs the City of London: a slow puncture. Rocket Grew Into America’s Biggest Mortgage Lender, but Now Comes the Hard Part. THG hands FCA dossier on City ‘conspiracy’ over share price plunge. Dirty-Money Ties  Worried Some at Swedbank While Bosses Kept Mum. Two Chinese Startups Tried to Catch Up to Makers of Advanced Computer Chips—and Failed. McKinsey’s Top Executive Wants to Change How the Firm Operates. London law firms struggle to fill jobs as competition for applicants soars. Time for some game theory. Meet the man who runs a moist towelette museum out of a planetarium. If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks![1] I gather that there is at least one other thing called “Excelcoin” that appears on CoinMarketCap etc., though it seems only barely to exist. To be clear I do not own that, do not endorse it, etc. I own the ExcelCoin that trades on my own copy of Microsoft Excel, which I made up as a joke in 2017. I am sure that, as a matter of parallel discovery, other people also made it up as a joke, or not as a joke.[2] It appears to be traditional to give Buterin some coins, as a tribute, whether or not he asks for them. He did not ask for these. Vitalik Buterin has no idea that he owns 20 ExcelCoins. Someone should tell him I guess.[3] Don’t actually.[4] To be clear, if Buterin wants to sell, I’ll absolutely Venmo him $19.80 for his 20 ExcelCoins. The ExcelCoin market does not support short selling at this time.[5] If I manage to sell any my bid is gonna drop to zero, is what this means. No refunds! All sales final![6] If a bank president went into her bank’s list and changed it so that she owned all the money in all of her customers’ accounts, she would definitely go to prison for a long time. A good exercise is, when I go into my Excel spreadsheet and change the ExcelCoin ledger so that I own everyone else’s ExcelCoins, is that illegal or what?[7] Also I mean not to nitpick but the incidence of lost bank dollars is a whole lot lower than the incidence of lost Bitcoins.[8] I guess I did. “If Robinhood was legally obligated to let you buy all the stocks you want whenever you want, it would have been sued into oblivion long ago,”  I wrote on Jan. 29, when the suit was filed. “They write the contracts better than that.”
        
      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      
  
    
      
        
      
    
  




  
    
      
        
        
Like Money Stuff? | 
Get unlimited access to Bloomberg.com, where you'll find trusted, data-based journalism in 120 countries around the world and expert analysis from exclusive daily newsletters.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  

  
    
      
      
      
      
      
    
  



<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23cfo3x6.5tlq/408ca487.gif" alt="" border="0" /></a>