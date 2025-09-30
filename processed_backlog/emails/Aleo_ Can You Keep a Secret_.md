# Aleo: Can You Keep a Secret?

**From:** Not Boring <notboring@substack.com>
**Date:** Tue, 13 Dec 2022 13:55:08 +0000
**Source:** inputs/saved_emails/Aleo Can You Keep a Secret_Tue,_13_Dec_2022_13-55-08_+0000_1850bc541728248c.eml
**Processed:** 2025-08-24T19:13:10.796482

View this post on the web at https://www.notboring.co/p/aleo-can-you-keep-a-secret

Welcome to the 1,252 newly Not Boring people who have joined us since our last Monday post! If you haven’t subscribed, join 176,385 smart, curious folks by subscribing here:
🎧  For the audio version, subscribe on Spotify [ https://substack.com/redirect/39d17735-ede6-466a-81c5-fa8d845cd405?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] or Apple Podcasts [ https://substack.com/redirect/c5c4ac0c-7497-44f8-ab07-05c13fff600c?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] (later this week)
Hi friends 👋,
Happy Tuesday! This post is coming to you a a day late because it’s the longest I’ve essay I’ve ever written about the most complex subject I’ve ever written about.
There have been many times in Not Boring’s brief history when I’ve realized just how lucky I am to get to write for an audience of smart, curious nerds like you. It takes a special kind of nerd to read multi-thousand word deep dives on topics ranging from blockchains to robots week after week. One of those times that stands out in my memory was in June 2021, when Jill Gunter [ https://substack.com/redirect/6a53bf10-f26d-4a72-b811-5cf3ed175322?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] and I wrote a piece on Zero-Knowledge Proofs called, creatively, Zero Knowledge [ https://substack.com/redirect/2a8263e1-b10e-4188-8a17-71e29a368319?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ]. 
Zero-Knowledge Proofs are wonky. For the first thirty or so years of their lives, they existed only deep in the research labs of academic cryptographers. They involve math that I couldn’t begin to understand, let alone explain, and when we wrote that piece, their use cases were still almost purely speculative. Despite that, and despite the fact that there were only 56,891 of us here at that time, Zero Knowledge has been viewed 113k times and was our most popular piece of the month by a landslide. 
In the piece, we gave an overview of Zero-Knowledge Proofs, and predicted that you’d be hearing a lot more about them over the next five years. Fast-forward 17 months, and the zero-knowledge zeitgeist is upon us. Starkware, zkSync, Aztec, Espresso, ImmutableX, Polygon’s zkEVM, and Aleo are either live on mainnet or in various stages of testnets. If they hit their timelines, Zero Knowledge Proofs could be one of the breakout technologies of 2023. 
Today, we’re going to go deep on one of the most promising companies in the zero-knowledge space: Aleo [ https://substack.com/redirect/bdaa4a75-3cd6-4200-882a-d509d4e1922e?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ]. Aleo is a L1 blockchain that uses zero-knowledge proofs to let developers build private-by-default applications. Its developers view zk-powered blockchains as the third wave. First, there was Bitcoin. Then, there was Ethereum. Now, there’s Aleo.  
This essay is a Sponsored Deep Dive. While the piece is sponsored, these are all my real and genuine views – there’s no perfect blockchain; it’s all about making the right trade-offs to serve the target audience and use cases. I expect to write about other L1s and L2s, including zk Rollups, in the future. I am a maximalist minimalist. 
You can read more about how I choose which companies to do deep dives on, and how I write them here [ https://substack.com/redirect/64c33754-4b9c-4ec8-a14f-7c3e61a49f4f?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ].
Please, please for the love of God note that this is not investment advice. Aleo doesn’t have a token live, but it will at some point. When that time comes: please do not look back at this piece as investment advice. I am a terrible trader. This is a sponsored piece. a16z, where I’m an advisor, is an investor in Aleo. I have no idea where Aleo Credits will be priced when trading starts. I’m just fascinated by the technology and the potential applications of zero-knowledge proofs. 
K? Let’s get to it.
Aleo: Can You Keep A Secret?
Imagine a Bizarro Internet that’s exactly like the internet you use today except for one detail: everything you do, send, or store on this Bizarro Internet is totally public. 
When you buy a new pair of underwear on Amazon, your purchase is posted to a website that anyone with the desire and some basic skills can search.
Your balance at Bank of America is right there, too, for anyone to see. 
You saddle up to the online poker table only to realize that you can see everyone’s cards… and they can see yours. This game sucks. 
You message your wife and tell her you’ll be up for dinner soon and, of course, anyone who wants to see that you messaged your wife can. 
Before you forget, you schedule a doctor’s appointment to get that thing checked out, and fill out an intake form online and, you guessed it, now anyone can peep that form in all its gory detail.
This Bizarro Internet would be practically unusable for anything besides public forums and showing off things that you don’t mind if other people see. 
This Bizarro Internet is web3 as it stands today. 
For most of the applications built on web3 to date, that level of transparency is fine, and even novel and good. If you own a CryptoPunk, you want people to know that you own a CryptoPunk. If you’re trading on a DEX, you’re mostly fine with people knowing what you bought and when. If you’re casting on Farcaster, you want that to be public anyway. 
But that’s a bit circular. The web3 products built to date are almost definitionally the ones for which privacy isn’t a big deal. Zoom out to the broader internet, and you’ll find privacy at the core of every product that touches money or personal information. 
If web3 is going to grow beyond these early experiments, and if decentralized networks are going to come to replace more centralized services, adding in a bit of privacy would be helpful.
That’s where Zero-Knowledge Proofs (ZKPs) come in. 
A zero-knowledge proof is a type of cryptographic protocol that allows one party (the Prover) to prove to another party (the Verifier) that they know a certain piece of information, without revealing any information about the actual content of that information. 
ZKPs are a way to prove that you know something, own something, or have done something without revealing any information about that something. They’re a valuable primacy primitive that were too theoretical and expensive for practical use until very recently. 
As people survey the crypto wreckage, zero-knowledge proofs are a bright spot. Good bubbles leave infrastructure in their wake for the next wave to build upon, and ZKPs seem to be a treasure in the bubble’s rubble. 
Zero-knowledge proofs are both a generally useful tool, and a tool tailor-made to help avoid the kind of fraud perpetrated by FTX. 
Under the charmingly awkward title Having a safe CEX [ https://substack.com/redirect/bc2ae92e-6ce3-478e-af15-34e18980856f?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ], Vitalik sketched out some ideas around a 2015 concept from Dan Boneh’s team at Stanford called Proof of Solvency [ https://substack.com/redirect/35a658e1-b92e-469b-b3bc-ae840befa4e8?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ], a way for centralized exchanges to prove that they have the funds to pay back their depositors without revealing any sensitive or proprietary information. 
At the core of the proposed architecture sit zkSNARKs (short for Zero-Knowledge Succinct Non-Interactive Argument of Knowledge), a specific type of ZKP. This is how Vitalik introduced ZK-SNARKs: 
ZK-SNARKs are a powerful technology. ZK-SNARKs may be to cryptography what transformers [ https://substack.com/redirect/849eed8c-a277-485f-aead-6ddbac60ce46?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] are to AI: a general-purpose technology that is so powerful that it will completely steamroll a whole bunch of application-specific techniques for a whole bunch of problems that were developed in the decades prior.
One more time for those in the back: “ZK-SNARKs may be to cryptography what transformers are to AI.” 
That’s a big statement. If you’ve been living under a rock, there’s something of an AI renaissance underfoot. At the heart of all of the insane progress being made is a new architecture: transformers. (Anton [ https://substack.com/redirect/e26640d7-ae6f-4624-969a-03dbf4111571?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] explains here [ https://substack.com/redirect/24c1d11b-95cb-40f0-81a5-4192acacec90?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ])
For blockchains specifically, ZKPs have two useful applications: scalability and privacy.
Together, those features mean that ZKPs let blockchains approach the performance of centralized services, and exceed their security and privacy, while maintaining the benefits of decentralization. 
There are no free lunches, of course, and that comes with a trade-off. Here, the biggest trade-off is the cost of privacy. It’s historically been more expensive to generate a ZKP than to just run the computation natively, as ZKPs require more complex and computationally expensive mathematical operations, and because they rely on more specialized hardware. 
By building a private-by-default L1, Aleo is making the bet that there’s enough demand from developers who are willing to pay a higher cost to build privacy into their applications, until they can shrink the cost. The team is working to grow demand by “commoditizing its complement,” specifically hardware optimized to solve zero-knowledge proofs quickly and cheaply. 
ZKPs are simultaneously incredibly complex to understand at a technical level (like, way beyond my abilities) and simple to understand at the usefulness level. They mean faster blockchains and applications that are open and private. As a testament to their flexibility, zero-knowledge proofs are invoked as a solution to both too little transparency (i.e. FTX → Proof of Solvency) and too much transparency (i.e. the fact that, without them, everyone knows your full on-chain balance and transaction history). 
Zero-knowledge proofs will play a major role in the future of crypto, and potentially, in the future of the internet. They were really hard to figure out, but now that they have been, they provide solutions that are strictly superior to the alternatives. How, exactly, they’ll be implemented is still up for debate. 
One approach is to build zkRollups on top of existing L1 blockchains, like Ethereum. Leading players like Matter Labs (zkSync [ https://substack.com/redirect/7c2ef4ed-c2d5-4343-8b09-ed322493ff18?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ]), Starkware [ https://substack.com/redirect/2b5601ca-5b1b-4ad2-b393-c3fb39706f5f?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ], and Aztec [ https://substack.com/redirect/3b5acdb9-3f57-4876-98f7-94ac3f5d968f?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] are taking this approach. 
Another is to start from scratch and build new L1s with scaling and privacy baked in at the base layer. That’s what Aleo [ https://substack.com/redirect/bdaa4a75-3cd6-4200-882a-d509d4e1922e?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] is doing.
Aleo was initially conceived as an L2 on Ethereum, but ZKPs on Ethereum are larger – they have to consume the full state of the application – and Ethereum doesn’t support SNARK-friendly primitives – hash functions and elliptic curves – so the team rewrote the plan and decided to build its own L1 in order to deliver cheaper ZKPs. 
Aleo is taking the most radical approach to building a zero-knowledge-based blockchain from the ground up. Instead of building an EVM-compatible chain on which developers can build apps in the familiar Solidity programming language, it created its own virtual machine, snarkVM, and programming language, Leo. Instead of relying on existing consensus mechanisms like Proof of Work (PoW) or Proof of Stake (PoS), it uses a combo of both, with a useful tweak on PoW called Proof of Succinct Work. The result should be ZKPs that are far cheaper on Aleo than they could be on top of Ethereum. 
The bet it’s making is that developers will be willing to learn new tricks in order to acquire scaling and privacy superpowers. 
It’s a bet that requires you to believe that not only will ZKPs be a nice feature, but that they’re foundational to a third way to build blockchains: 
Wave 1: Bitcoin
Wave 2: Ethereum
Wave 3: Aleo
Understanding why Aleo is making that bet is a great way to explore the details and implications of zero-knowledge proof technology. So today, we’ll go deep on zero-knowledge, Aleo, and the future of the internet: 
Zero-Knowledge Refresher
Zero Knowledge, Many Applications 
From Berkeley to Blockchain
DIZK & Zexe
Aleo: Private by Default
How Aleo Works
Commoditize Your Complements: AleoBFT & ZPrize
The Zero-Knowledge Landscape
Aleonomics 
Risks & Regulation
The Decade of Zero Knowledge
Now it’s time to melt our brains a little bit by diving back into zero-knowledge proofs, just in case you’ve gotten a little rusty since Jill and I wrote about them twenty months ago. 
Zero-Knowledge Refresher
Zero-knowledge proofs are a fancy bit of cryptography that allows one party (the Prover) to prove to another party (the Verifier) that it knows something, without revealing any information about that thing. They let someone prove that they know a secret without giving up any information about that secret.
Those secrets can take many forms, from passwords to positions on a Battleship board to dollars in a bank account. In Zero Knowledge [ https://substack.com/redirect/2a8263e1-b10e-4188-8a17-71e29a368319?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ], Jill and I used a toy example: me proving that I have enough money to lease an apartment without giving the real estate agent my bank records and financial history. 
That ZKP box in the image is doing a lot of work. What’s going on in there? 
There are a bunch of different ways to explain how ZKPs work without going into the “moon math.” In Zero Knowledge, we used the “Color Blind Friend” example. 
My color blind friend and I are looking at balls on a table that are identical except that one is red and the other green. He is not sure that he believes me when I tell him they are two different colors. We decide to establish that they are, in fact, different colors by playing a game: 
I give him the two balls to hide behind his back. 
He takes one ball out and shows it to me. 
Then he puts this ball back behind his back, withdraws his hand again, shows me a ball and asks, “Did I switch the balls?” 
If we repeat this game enough times, and if I answer correctly every time, then I will demonstrate to him that the balls are almost certainly two different colors. Importantly, here, I have proven this to him without revealing any other information. Perhaps frustratingly for him, he still doesn’t know which ball is red and which ball is green.
For much, much more detail on Zero-Knowledge Proofs, including another explanation, an overview of potential applications, the riveting adventures of Howard and Alex, Aleo details including consensus, economics, and progress, how Aleo is commoditizing its complement, risks, regulation, and so much more…
Thanks as always to Dan for editing, to Alex, Howard, Daniel, Drew, and Ali for input on the piece, and to Jill for introducing me to the wonderful world of ZKPs.
That’s all for today! See you Friday for the most optimistic Weekly Dose yet, and on Monday for my last essay of 2022!
Thanks for reading,
Packy

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubm90Ym9yaW5nLmNvL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3hOakk0TXpVME9Td2ljRzl6ZEY5cFpDSTZPRGc0TkRFMk5UQXNJbWxoZENJNk1UWTNNRGt6T1RjeU1Dd2laWGh3SWpveE5qY3pOVE14TnpJd0xDSnBjM01pT2lKd2RXSXRNVEF3TWpVaUxDSnpkV0lpT2lKa2FYTmhZbXhsWDJWdFlXbHNJbjAubzEtV25UakdTWWhtUFI3MTVJc0QwOFpaeVIwOWRRTGVWNU5tTVpDbkpDTSIsInAiOjg4ODQxNjUwLCJzIjoxMDAyNSwiZiI6dHJ1ZSwidSI6MTYyODM1NDksImlhdCI6MTY3MDkzOTcyMCwiZXhwIjoxNjczNTMxNzIwLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.INoo-j6U1cgAjbgYR1l-sisDH3OVjnjwFf75jvxlkz8?