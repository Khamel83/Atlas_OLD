# Money Stuff: Financial Engineering for Green Energy

**Source**: inputs/saved_emails/Money Stuff Financial Engineering for Green Energy_Mon,_29_Jan_2024_14-35-48_-0500_(EST)_18d56b89472a123e.eml
**Type**: email
**Created**: 2025-08-25T02:54:10.256490

---

The way that the US government encourages a lot of green energy projects is by giving them tax credits. If you build a power plant that runs
      
    
  
  
    
      
        
          
          
        
        
          
            
          
        
      
  
    
      
        
      
    
  


      
      
    
  
  
  
    
      
        
          
  
    
      Basel endgame vs. green equity
    
  

The way that the US government encourages a lot of green energy projects is by giving them tax credits. If you build a power plant that runs on certain sorts of renewable resources, the Internal Revenue Service will give you some money — call it 0.3 cents per killowatt-hour
  [1]
 — for generating that power, which you can use to reduce your taxes. 
That is a reasonably safe stream of cash flows. Not totally safe — your plant could burn down, prices could collapse or costs could rise so much that it is no longer economical to run it, the tax code could change — but broadly speaking you can estimate how much power the plant will produce  per year and then multiply that by 0.3 cents to get a fairly predictable annual tax credit. 
Finance being what it is, if you are building a green energy project, you will probably sell that tax credit. If your project will generate a quasi-guaranteed stream of cash flows of $X per year for the next Y years, then you can compute the present value of those cash flows and sell them, today, for that amount. This is good because you probably need a lot of cash, today, to build the green energy project. The government wants to encourage you to build the project, but the government doesn’t just hand you the money to do it. Instead the government promises to pay you $X per year if you succeed in building the project, and you need to take that promise and exchange it for cash today in order to actually build the project.
  [2]

The person giving you the cash — the person paying you money up front today in exchange for a promise of the future tax credit — is probably a big US bank, for a few reasons. For one thing, banks are where the money is, and this sort of thing — providing financing today in exchange for a reasonably safe promise of future steady cash flows — is what banks do. And financial engineering — looking at a provision of the tax code and being like “yeah we can wring some profits out of that" — is also what banks do.
Also, in the 2020s, a big part of what banks do is (1) promise to finance renewable energy projects and (2) deflect criticism for financing fossil-fuel projects. (And, in the US,  vice versa.) So buying these tax credits — paying the upfront costs of green energy projects in exchange for the future green-energy tax credits — is a good way for the banks to make money, do financial engineering, and show their shareholders and critics that they are financing green energy projects. 
I have suggested that the banks are buying the credits, and that the people building the projects — the “sponsors” — are selling them, but that is not the correct terminology. You don’t go around selling tax credits, and your tax lawyers will get mad if you say that. (Nothing here, of course, is tax advice.) The tax credit is not your property; it is an artifact of US tax law. The only way for the bank to get the tax credit is by qualifying for the tax credit, and  the way to qualify for the tax credit is by owning the renewable energy project. 
And so the way this actually works is that the renewable energy project is set up as some sort of partnership or limited liability company or joint venture, and the sponsor is a co-owner and the bank is another co-owner. And the partnership agreement says that the sponsor gets most of the profits (and risk) from running the business and finding customers and selling electricity at market rates and so forth, and the bank gets the tax credit. They are not exactly joint owners, but they are joint owners enough for the bank to take the tax credit. They have murmured the proper incantations to call themselves co-owners and take the tax credit.
The IRS actually gives instructions on what sorts of incantations you have to say. The IRS is in sort of a weird position here. On the one hand, it wants to prevent abusive tax shelters and generally uphold the aesthetic coherence of the tax code, so it does not want to allow people to just go around selling tax credits. 
On the other hand, the IRS does want to encourage these projects to get built, which does, practically, requiring selling the tax credit. So it  provides guidance on, like, what is the least you can do to qualify. The bank does need to take some risk, to share in the downside of the project; the sponsor can’t guarantee the tax credits. But the usual way it works, according to the  American Council on Renewable Energy, is that the bank and the sponsor form a project partnership, the bank “provides between one-third to two-thirds of the total capital,” and the bank gets back “99% of the tax attributes and a minority share of the cash, typically between 5% and 30%,” for a while. This ends either when the bank reaches its target return (a “yield-based flip”) or after an agreed amount of time (a “time-based flip”), after which the bank’s share of the tax credit goes down (“usually to about 5%”) and the sponsor can buy it out.
This is called “tax equity financing,” because for tax-law-incantation purposes, the bank is an equity owner of the partnership. But for practical purposes, people kind of think of it as debt financing, because the bank is providing upfront money in exchange for a reasonably certain, reasonably fixed, reasonably time-limited return. It does not really share in the upside and the downside of the project; it’s just putting up money to buy the tax credit.
That’s how financial engineering works: You build a thing that looks like debt to the sponsor, and that looks like debt to the bank (so it’s happy to “lend” the money), but that looks like equity to the IRS (so the bank can get the tax credit).
But nothing is that simple. Banks are doing a lot of financial engineering behind the scenes, too, particularly for their capital requirements. A bank funds itself with a mix of cheap debt (deposits, etc.) and expensive capital (shareholder equity), and capital regulation determines how much capital it needs. The capital regulation is focused largely on the riskiness of the bank’s assets: A bank that holds mostly Treasury bills needs very little capital, while a bank that holds mostly Bitcoin needs a ton. This is called “risk-based capital,” and it is expressed in terms of “risk weights”: Treasury bills have a risk weight of 0%, because they are safe, while   Bitcoin has a risk weight of 1,250%, because it is risky. Standard corporate loans usually have a risk weight of 100%, which is in some sense the “normal” risk weight. The crude rule of thumb — not particularly accurate, but a useful shorthand — is that banks need to have capital of 8% of their risk-weighted assets. So a bank with $100 of corporate loans needs at least $8 of equity capital; it can borrow the other $92. A bank with $100 of Bitcoin needs $100 of equity capital; it can’t use any deposits at all to buy those Bitcoins.
These risk weights are set by regulation and are necessarily somewhat arbitrary; the regulators try to estimate the riskiness of various classes of things, and to assign higher risk weights to riskier things, but there’s only so much nuance they can manage. Some corporate loans are riskier than others, but will be lumped in with the same risk weight.
And so a big part of the bank’s financial engineering operation is optimizing risk-based capital. For instance: If a bank has $100 of stuff that gets a 100% risk weight, and can somehow split it into $80 of stuff with a 0% risk weight and $20 of stuff with a 300% risk weight, then that’s good, that’s what it wants, that reduces its risk-weighted assets from $100 to $60, which reduces its capital requirements, which increases its ability to return money to shareholders. And this is the explanation for  capital relief trades, and also in some loose sense the explanation for  the 2008 financial crisis: If you slice your risky thing exactly right, you will end up with a collection of new things that look less risky, to capital regulators, than the original thing. 
If you are a bank with a big tax equity financing business, a natural question to ask is, well, how risky is this? Specifically:
	Is it like a corporate loan, since it’s an investment in a series of predictable cash flows, at some agreed yield, from a business?	Or is it like equity in a private company, since, technically, that’s what it is?

There is no particularly correct answer to that; the answer is just “whatever you can convince the capital regulators it is.” But obviously the answer that you want, as a bank, is that it’s a loan. And in fact that seems to be the answer in US capital regulation: Tax equity financing normally  gets a 100% risk weight. In fact, the Office of the Comptroller of the Currency, which regulates banks, allows these deals “only if the transaction is the functional equivalent of a loan,” and it does allow them: From the bank capital regulators’ perspective, tax equity financing is a loan.
That’s really how financial engineering works: You build a thing that looks like equity to the IRS (so the bank can get the tax credit), but that looks like debt to the capital regulators (so it gets a lower risk weight). You check the equity boxes for the IRS and the debt boxes for the OCC. You thread the needle so that it looks like different things to different regulators, looking like debt when debt is better and like equity when equity is better.
But US capital regulators have launched a big revision of capital requirements, so the answer might change. Bloomberg’s Natasha White and Alastair Marsh report:

Senior Wall Street bankers are warning that a plan by US regulators to rewrite the rules of tax-equity investing will deliver a major blow to a market dominated by JPMorgan Chase & Co. and Bank of America Corp.
At issue is the perceived risk of tax-equity investments, which are a form of financing in which banks provide capital to green projects in exchange for tax credits. It’s a market in which JPMorgan and BofA have been estimated to do more than 50% of the roughly $20 billion worth of annual transactions. 
Last July, the three agencies that decide bank capital requirements in the US (the Federal Reserve, Federal Deposit Insurance Corp. and Office of the Comptroller of the Currency) unveiled what’s come to be known as the Basel 3 Endgame. ….
A part of that broader proposal is a requirement that banks quadruple the risk weights they assign to tax-equity investments, forcing them to significantly raise the amount of capital they set aside for renewable energy projects. ...
Law firm Clifford Chance has warned that the risk-weight proposal would make it “prohibitively expensive” for banks to continue doing certain tax-equity investments, which is “certain to have a harmful” impact on green finance. ACORE, a trade group that represents renewable project developers, has said the plan threatens to “derail the clean energy transition.”

Here are the Clifford Chance memo and the  ACORE report. The point is that “non-publicly traded equity exposures,” like co-owning a green energy joint venture, normally get a 400% risk weight. Tax equity financing somewhat accidentally got loopholed into the 100% risk-weight category before, but the new rules will close that loophole and it will get a 400% weight.
  [3]

Unless the banks complain loudly enough that the regulators hear them and put back a loophole for tax equity financing. And why not? None of this is real; none of it has any objective truth; tax equity financing isn’t “really” equity or “really” debt. If you want more tax revenue, you make it harder to sell the tax credit; if you want more green energy financing, you make it easier to sell the tax credit. If you want better capitalized banks, you raise the capital requirements for tax equity financing; if you want more green energy financing, you lower the requirements. Banks obviously know what they want, and they engineered a product to get it; now the question is what policymakers prefer.

  
     
       
         
       
    
  
  
    
      
      
        
          
             
               
                 
               
            
          
        
      
      
    
  


  
    
      FTC vs. AI
    
  

One way to think about the artificial intelligence business is:
	Everybody, by now, has an intuitive understanding of how new software products are created in the US. New ideas in software come from visionary entrepreneurs who can work pretty cheap. You need a couple of engineers, some desks at a WeWork, some laptops, some energy drinks, a modest cloud-computing budget. You build the thing, you try to find product-market fit, and if it works you scale rapidly. The marginal cost of distributing one more copy of your app, or serving one more instance of your social media website, is basically zero. If your thing takes off, it can take off quickly, and it’s all profit.	Everything in US tech finance is oriented around that understanding. Talented tech workers want to be founders, because founding your own company is the way to fame and riches in tech. Venture capital firms invest in risky early-stage software companies, because (1) those companies don’t need that much capital to figure out if their idea works, and (2) if the idea does work it will return many times the investment.	Generative AI … maybe does not work like that? It is extremely capital-intensive, by which I mean that you need a very large cloud computing budget to build and train an AI model that will do anything at all. And then scaling it is also quite expensive; you need a ton more computing power to serve each new customer. Building an AI model is more like building a car than it is like building Facebook.

If I asked you in the abstract “I have a potentially lucrative and important business idea, but it requires like $10 billion of startup capital and does not scale cheaply like software, how should I finance it,” your first answer might not be “venture capital.” You might say something like “well this sounds like a big industrial project, what you should do is go get a job at a big industrial company with a ton of money, and start a division there that will do this project.” And if I said “well it’s a tech idea,” you’d say “ah, even better, get a job at Google or Amazon or Alphabet, they have absolutely tons of money, more than they know what to do with, they can totally fund your $10 billion project, no problem. Is it a virtual reality headset by any chance?” 
But the problem with AI is that it is, mostly, made in the Bay Area by tech-industry types, so it does default to the startup mode, so you do have startups running around building AI. But to fund their billions of dollars of cloud computing costs, they 
	take billions of dollars of investment from cloud computing companies (Microsoft, Amazon, Alphabet), 	take a lot of that investment in the form of cloud computing capacity rather than money, and 	probably have some sort of understanding with those companies that there will be some commercial relationship between them, so that for instance Microsoft has rights to include OpenAI models in its software.

It is a Silicon Valley-style compromise between “all new software must be built by startups” and “actually giant companies with tons of money and smart employees and complementary capabilities probably do have some advantage in building this particular expensive thing.”
We   talked about this dynamic last week, in part because Silicon Valley venture capitalists have been complaining about it: “MANG” (Microsoft, Amazon, Nvidia, and Google/Alphabet) have been some of the biggest investors in AI startups, and have advantages over traditional VCs in making these investments (mainly that they get to make them in the form of computing power), and the traditional VCs feel a bit priced out. 
Others also have complaints. If Microsoft had just announced one day “we are going to build large language models to incorporate into our search engine and Office suite, we hired a bunch of people, we gave them a lot of computing power, away we go,” well … I don’t want to say that would be no problem from an antitrust perspective, and in fact tech companies (including Microsoft) do sometimes get in antitrust trouble for bundling their own products together. But in general it is not an antitrust problem for a big company to launch a new product.
But since Microsoft instead pumped billions of dollars into OpenAI, a nominally independent sort-of-nonprofit startup, antitrust regulators can go around raising their eyebrows and questioning whether Microsoft and OpenAI are colluding with each other in a way that is bad for competition. (We   talked about this last month, when UK competition regulators were asking about it, and when Microsoft was arguing that, due to the weird corporate structure, in fact it doesn’t own any OpenAI shares at all.) Doing stuff with two companies always raises more antitrust risk than doing the same stuff   within one company, and the AI business seems to lend itself to two-company situations.
Similarly:

The Federal Trade Commission opened an inquiry on Thursday into the multibillion-dollar investments by Microsoft, Amazon and Google in the artificial intelligence start-ups OpenAI and Anthropic, broadening the regulator’s efforts to corral the power the tech giants can have over A.I.
These deals have allowed the big companies to form deep ties with their smaller rivals while dodging most government scrutiny. Microsoft has invested billions of dollars in OpenAI, the maker of ChatGPT, while Amazon and Google have each committed billions of dollars to Anthropic, another leading A.I. start-up. ...
The F.T.C. said it would ask Microsoft, OpenAI, Amazon, Google and Anthropic to describe their influence over their partners and how they worked together to make decisions. The agency also said it would demand that they provide any internal documents that could shed light on the deals and their potential impact on competition.

Here is  the FTC’s announcement. I think we’ll all be interested in Microsoft’s influence over OpenAI and how it makes decisions — that has, uh,   come up a lot lately — but the point is that if these companies were just building AI in-house, none of this would really come up.

  
    
      Byju’s
    
  

Some incredible numbers here:

Byju’s, the world’s most valuable edtech startup, has cut its valuation ask by 99% in a rights issue it launched Monday as the Indian firm works to address its working capital needs. The startup is looking to raise $200 million in the rights issue, capital it said was “essential to prevent any further value impairment.”
The startup, once India’s most valuable, is resetting its valuation to “next to nothing” in the rights issue, where all existing investors have an opportunity to participate, according to a source familiar with the matter. If Byju’s succeeds in raising $200 million, the post-money valuation of the startup will be in the range of $220 million to $225 million, a 99% drop from the $22 billion value that the startup had attained in 2022, according to the source, who requested anonymity sharing nonpublic information.
Byju’s founder Byju Raveendran told shareholders in a letter Monday that he and other founders of the edtech group have invested $1.1 billion into the Bengaluru-headquartered startup in the last 18 months and seek continued support from the investors to keep the business afloat. “We have made immense personal sacrifices for the sake of the company. We have spent our lives building this company and are fervent believers in its mission,” Raveendran wrote in the letter, seen by TechCrunch. …
The rights issue comes as Byju’s looks to secure capital amid a severe funding crunch. The startup, which spent $2.5 billion acquiring more than a dozen firm in 2021 and 2022, has raised more than $5 billion in equity and debt from backers including Peak XV, Lightspeed, Chan Zuckerberg Initiative, BlackRock, UBS, Prosus Ventures and B Capital. Byju’s said in a statement that it expects the rights issue to close in 30 days.

Last week Bloomberg  reported a 90% cut — “a price that values the firm at less than $2 billion, … down from $22 billion at its previous round in late 2022” — but I guess things are moving fast, and in the wrong direction? On these numbers, the people who put in $5 billion back in the good times will own less than 10% of the company, while the people who put in $200 million in the bad times will own 90%. 
The point of a rights offering is to be coercive: Existing investors have the right to put more money in at the rights price, which here is basically zero, and if they don’t put more money in then they get diluted by the people who do. Here, if you put up $1 billion for 5% of the company back when it was worth $20 billion, Byju’s will come to you and ask you to put in $10 million more to keep your 5% stake; if you say no, you’ll be diluted down to about 0.5%. If you’ve already thrown away $1 billion, what’s $10 million more? On the other hand, if Byju’s has already reduced your $1 billion investment to zero, why would you give them any more money? Getting diluted doesn’t matter if the stock is going to zero; owning 5% of a company worth zero is no better than owning 0.5% of it. The main questions in the rights offering are: Do you trust that the company has a plan to turn things around, and that this one last contribution is enough to see it through? And also: How mad are you about what happened to the rest of your money?

  
    
      Things happen
    
  

Evergrande Will Be Dismantled, a ‘Big Bang’ End to Years of Stumbles. Evergrande   Liquidation Is a Big Test for International Creditors. Banker Bonuses Are Down Again—but It Stings This Time. US  regional banks hope for profit revival as pain from SVB fallout eases. Credit Suisse’s Restructuring Deal With   Sanjeev Gupta's GFG In Doubt. Amazon Drops $1.4 Billion   iRobot Deal After EU Veto Threat. Reddit Advised to Target at Least $5 Billion Valuation in IPO. Chinese regulators  curb short selling as market downturn deepens. Traders Line Up for ‘Once-in-a-Generation’   Emerging Markets Bet.  Sotheby’s trial provides a peek behind the curtain of private art sales. Unhappy Workers Cost US Firms $1.9 Trillion. The Jujitsu Champ Who Got Nearly $500 Million From  Sam Bankman-Fried. Why Elon Musk Is Comparing Index Fund Consultants to  ISIS.
If you'd like to get Money Stuff in handy email form, right in your inbox, please subscribe at this link. Or you can subscribe to Money Stuff and other great Bloomberg newsletters here. Thanks!
        
  [1] That’s the statutory number in Internal Revenue Code  section 45, though it can increase with inflation, there are other factors, and in fact the  IRS provides yearly guidance with different amounts for different types of renewables, etc.


  [2] This is oversimplified, and in fact there will probably be a construction loan for the construction, etc., but the tax equity financing will generally be early in time and not exactly at the bottom of the capital structure.


  [3] Clifford Chance  points out that the regulators could put in an intentional loophole for green energy, which in fact they do for other sorts of debt-like equity financing: “The change is made more troublesome by the fact that the Agencies proposed to retain the 100% risk weight for community development investments (including LIHTC Investments) and investments in small business investment companies under ESRWA on the basis that such investments ‘generally receive favourable tax treatment and/or investment subsidies that make their risk and return characteristics different than equity investments in general.’ In maintaining this treatment for such investments, the Agencies also ‘recogniz[e]… the importance of these investments to promoting important public welfare goals….’ Such rationale would appear to apply equally to clean energy and infrastructure tax equity investments.”


      
    
  


  
    
        
          
            Follow Us
            
              
            
            
              
            
            
              
            
          
          
          
            
              Get the newsletter
            
          
        
    
  


  
    
      
      


  
    
      
        
        
Like getting this newsletter?  Subscribe to Bloomberg.com for unlimited access to trusted, data-driven journalism and subscriber-only insights.



Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the Terminal delivers information and analysis that financial professionals can’t find anywhere else. Learn more.



Want to sponsor this newsletter?  Get in touch here.

      
    
  



        
           You received this message because you are subscribed to Bloomberg's Money Stuff newsletter.
        
        
          Unsubscribe | Bloomberg.com | Contact Us
        
        
          
            
              
                
                  
                    
                  
                
                
                  |
                
                
                  
                    
                  
                
              
            
          
        
        
          Bloomberg L.P. 731 Lexington, New York, NY, 10022
        
      
    
  
  


<a href=""><img src="https://link.mail.bloombergbusiness.com/img/607f07ceef4b8524a319a23ckc7nf.5jdo/c844b226.gif" alt="" border="0" /></a>