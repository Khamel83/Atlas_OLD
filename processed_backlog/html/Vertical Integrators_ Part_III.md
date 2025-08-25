# Vertical Integrators: Part III

**Source:** inputs/old stuff/Docs/Vertical Integrators PartIII_091024.html
**Processed:** 2025-08-24T19:49:09.546924

# Vertical Integrators: Part III

*Welcome to the **212 newly Not Boring people** who have joined us since last week! If you haven’t subscribed, join **231,929** smart, curious folks by subscribing here:*

[![](https://substackcdn.com/image/fetch/w_40,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideCheck%3Fv%3D4%26height%3D40%26fill%3Dtransparent%26stroke%3D%25230c2427%26strokeWidth%3D3.6)Subscribed](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubm90Ym9yaW5nLmNvL2FjY291bnQiLCJwIjoxNDg3MjMyMjAsInMiOjEwMDI1LCJmIjp0cnVlLCJ1IjoxNjI4MzU0OSwiaWF0IjoxNzI1OTcyOTkyLCJleHAiOjE3Mjg1NjQ5OTIsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.SxhF3Dbl7kp6TOFWwDqtztgnmf5le19Vgw92q2wEK7E?)

**Today’s Not Boring is brought to you by… [Attention](https://substack.com/redirect/08564cef-91cc-4563-8ea4-33ec336b9d86?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)**

[![](https://substackcdn.com/image/fetch/w_402,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5e3d10d-a496-44c1-b4f2-cd68d7148c98_1600x394.png)](https://substack.com/redirect/08564cef-91cc-4563-8ea4-33ec336b9d86?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

*[Attention](https://substack.com/redirect/08564cef-91cc-4563-8ea4-33ec336b9d86?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) is an AI-powered call recorder trusted by sales teams at industry giants like Snowflake, Datadog, and Stripe. Simply put: you can close more deals with Attention.*

*[Attention](https://substack.com/redirect/08564cef-91cc-4563-8ea4-33ec336b9d86?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)’s AI captures and analyzes every sales conversation, revealing how and why your deals succeed. It not only identifies winning strategies for your team but also empowers you to act on them.*

*With Attention, you can automate key workflows based on customer interactions: generate personalized follow-up emails after calls, populate your CRM with crucial deal information, alert stakeholders to potential churn risks, create coaching scorecards for your sales reps, send weekly executive reports on deal outcomes, and more.*

*Unlike other tools that merely provide insights, Attention delivers both insights and the actions needed to close more deals. Sales is hard. Attention makes it a little easier.*

[Try Attention Today](https://substack.com/redirect/08564cef-91cc-4563-8ea4-33ec336b9d86?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

Hi friends 👋,

Happy Tuesday!

The deeper down the Vertical Integrator rabbit hole I go, the more fun I have exploring. Today’s Part III was supposed to be the last in the series, but as I started writing about the challenges of building a Vertical Integrator, I realized there are enough to fill a whole book, let alone an essay.

If you haven’t read [Part I](https://substack.com/redirect/d31bc5aa-752e-49ba-b3ce-44d9cfc72342?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) and [Part II](https://substack.com/redirect/eedd8a4f-4990-4db4-95ab-3512c27cd9ac?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), do that first. Those are a little more theoretical and much more optimistic. Today, we’re getting into the nitty gritty.

This one is all about the challenges, and I just scratched the surface. As excited as I am about the opportunity for Vertical Integrators, building one is as hard as it gets. Before jumping back into excitement mode for the fourth and final (I promise) installment next week, I want to scare us straight.

Let’s get to it.

[![](https://substackcdn.com/image/fetch/w_2416,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F113da057-138c-4785-888b-b06755001327_1208x608.png)](https://substack.com/redirect/a1a94000-df86-49b9-9b03-a4f6246bde14?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

It’s a rare treat when one of your favorite writers on the internet also happens to have worked at one of the most spectacular failures of the model you’re writing about. I have this treat: [Brian Potter](https://substack.com/redirect/55117b3b-34df-4dd9-8ae2-08bf306fcbe1?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), the author of [Construction Physics](https://substack.com/redirect/148c45b9-9650-4d60-835f-0a7f0a2f14bb?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), worked at Katerra.

[![](https://substackcdn.com/image/fetch/w_1816,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4cb5ee2-841a-40bf-974c-aaaaee265f1d_908x516.png)](https://substack.com/redirect/06df6d8e-8ef5-4ee8-82ae-a880bf805f98?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

*Katerra Factory*

When the company shut down in 2021, after having raised over $2 billion from investors including SoftBank’s Vision Fund, Potter wrote a retrospective on the company,  What it reveals as much as any of the specifics is that building a Vertical Integrator is really fucking hard, even when it seems like the best strategy.

Michael Marks, the CEO of $14 billion contract manufacturer Flex, started Katerra in 2015 to source building materials in bulk in order to sell them to homebuilders more cheaply than they had been buying them in their previously fragmented, one-off fashion. That didn’t work, as Potter writes:

> *Architects and designers weren’t willing to specify Katerra’s products, they wanted to use what they were familiar with. **So early on Katerra pivoted to become a completely vertically integrated construction company.** They would still source their own materials, but use them in Katerra designed and built buildings.*

If this sounds familiar, it’s because it’s exactly what I’ve been calling for in [Part I](https://substack.com/redirect/d31bc5aa-752e-49ba-b3ce-44d9cfc72342?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) and [Part II](https://substack.com/redirect/eedd8a4f-4990-4db4-95ab-3512c27cd9ac?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)! Find an industry that’s large and outdated, maybe try to fix a piece of the system, and when that doesn’t work, go all-in and vertically integrate a better solution.

Here’s Potter on why and how Katerra planned to do that:

> *Compared to the electronics manufacturing world, I’m sure the construction world looked astonishingly primitive, and modernizing it became another key part of Katerra’s value proposition. Instead of laboriously constructing buildings one at a time, by hand, buildings would be built the way everything else was built - prefabricated in a factory, designed specifically to be manufactured as efficiently as possible. Instead of designing buildings from scratch every single time, Katerra would have building products: standard, off the shelf buildings that could be customized for a client’s needs, the same way mass produced cars offer a wide variety of trim options.*
>
> *This was the Katerra playbook when I joined the company. They would design a series of building products that could be mass-produced in their own factories, leveraging economies of scale and advanced manufacturing to build more efficiently than conventional construction. These products would be full of Katerra-supplied materials - everything from lightbulbs, to countertops, to bathroom fixtures, to appliances would all be Katerra brand. They would acquire general contractors in different markets to give them a nationwide construction footprint, and hire the various trades to self-perform all the construction work. **At the time, I thought this was the exact right strategy needed to change the construction industry - it couldn’t be done piecemeal, it needed to be done all at once, simultaneously attacking every stage in the process.***

It all made so much sense on paper. Despite the best laid plans, however, and even because of them, Katerra failed. It had capital, incredibly talented people motivated by the mission, an experienced founder who’d scaled a manufacturing business, and it had even signed a [$650 million deal](https://substack.com/redirect/d3dda448-d9a0-448d-bd9f-f201f1a69017?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) to build 8,000 houses for Saudi Arabia in 2020, part of a larger non-binding $40 billion agreement. And still, Katerra couldn’t make it work.

Potter provided a few theses as to why: the company didn’t find product-market fit for its houses, its costs were too high, and it was too slow. With so many different departments, it moved at the pace of an older company when it needed to iterate at the speed of a younger one.

It seems to me that **one of the fundamental mistakes was building a bunch of components, each of which seemed promising individually, without understanding if or how they would work as a system**, and then scaling that loose constellation up before it had become something that people were willing to pay for. Katerra tried to do too much, too soon. It’s possible to start out *too* vertically integrated.

I share Katerra’s story not because it’s particularly unique, and certainly not to demean the effort, but because, after two weeks of excitement about Vertical Integrators, **I want to make it abundantly clear how hard it is to build them.**

The default outcome for any startup is failure. It takes tremendous force of will, execution, strategy, smarts, and luck to overcome very long odds. Vertical Integrators turn all of that difficulty up to 11.

[![](https://substackcdn.com/image/fetch/w_1816,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec3ac75d-89d0-4fb6-ae53-3c7d144e532e_908x445.png)](https://substack.com/redirect/2aa6ad41-c648-49ba-8094-0495295954f3?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

Anil Varanasi runs [Meter](https://substack.com/redirect/db9cda00-27bd-4ba2-8efd-2fde9038b021?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), one of my favorite Verical Integrators, with his brother Sunil. He told me that there’s something like a [Great Filter](https://substack.com/redirect/96c30fc9-386a-4ad1-8b03-468c2b4a37e9?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) for Vertically Integrated companies: “Almost all of the largest companies are vertically integrated. Almost none of the small ones are.”

Robin Hanson dreamed up the Great Filter to address a mystery: where are the aliens?

> *Humanity seems to have a bright future, i.e., a non-trivial chance of expanding to fill the universe with lasting life. But the fact that space near us seems dead now tells us that any given piece of dead matter faces an astronomically low chance of begating such a future. **There thus exists a great filter between death and expanding lasting life.***

In his telling, as we discussed in the [Deep Dive on Fuse](https://substack.com/redirect/92537c65-8ed7-42ef-b84d-1210bb324c21?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), something must get in the way between where we are now, on the cusp of universal expansion, and actually realizing that potential to expand. Maybe it’s climate change. Maybe it’s nuclear war. Maybe it’s global pandemic.

There are a number of reasons a civilization might not make the leap from computers, rockets, and nuclear power to intergalactic travel. Better understanding them may help us pass through the Great Filter and out into the universe.

Similarly, there are many reasons a Vertical Integrator may not make it from small, complex, wildly ambitious startup to large, dominant company. Understanding them may help companies pass through that Great Filter of their own.

So in the third of our four-part series on Vertical Integrators, we’ll dig into what makes them so challenging.

While the specific difficulties faced by modern Vertical Integrators are more numerous than the companies themselves, there are seven categories that I want to focus on:

1. It requires building at least two companies: software and hardware.
2. Hardware by itself is just really hard.
3. Incumbents are good at what they do and have advantages.
4. Figuring out the right level of integration is not obvious.
5. You can’t pivot nearly as easily.
6. Something better might come along.
7. Getting to revenue takes a lot of money.

### **Building at Least Two Companies**

The first thing about building a modern Vertical Integrator is that you have to build at least two companies: software and hardware. This sounds relatively simple – every company uses software nowadays – but it’s not.

There’s a paradox in building a Vertical Integrator: software lets you build entirely new systems, but you can’t just sell the software because there are no customers other than yourself who operate the same system, so you need to build the hardware and do the whole thing yourself.

The idea of vertically integrating hardware and software is not new or novel. Apple has been doing it since at least 1984, when the company launched the Macintosh with the graphical operating system that was the predecessor to MacOS.

[![](https://substackcdn.com/image/fetch/w_550,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3d189a2-9878-4352-86b1-ae8ecd0810ed_800x450.gif)](https://substack.com/redirect/28b3b793-1637-4d69-a02b-5c524f018754?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

*Apple 1984 Commercial*

Forty years later, Apple is the world’s most valuable company, with a $3.3 trillion market cap. Yesterday, it announced iPhone 16, which deeply integrates AI into the hardware and gives the company a big advantage in personal AI agents. The benefits of hardware-software integration are not a big secret.

What’s funny, though, is that with all of those years of development, all that money, all of Apple’s talent, and all of that integration, Apple’s software still kind of sucks.

Maybe that’s unfair, the software is OK. Open up your phone real quick though. Do you use Apple Calendar, Apple Mail, Apple Stocks, or Apple Maps, or an alternative built by the millions of developers throughout the rest of the world? Do you use Apple Music or Spotify? Open your computer. Do you use Keynote, Pages, or Numbers, or an alternative product. If you use Numbers instead of [Excel](https://substack.com/redirect/6e5ce0df-b69d-4791-b2bb-362c0ba0a09b?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), I would love to hear from you.

Of course, Apple wins either way. It charges 30% of all sales through the App Store. But the fact that Apple makes the world’s best hardware but isn’t the best in the world at making the software that runs on that hardware shows a few things.

First, hardware and software require different skills, and even different DNA. It’s hard for a software company to be a hardware company, and vice versa.

Second, no matter how good you are at software, chances are someone out there can build software better than you can. If you’re building software for your very specific need, you’re probably not using the best software you could be using.

Third, even if you’re really good at both software and hardware, keeping the two in sync is a hard problem. Sometimes the software team moves faster, others the hardware team leaps ahead. Software has to run well on many generations of hardware, which forces trade-offs.

To keep it simple, we’re just talking about two things: hardware and software. In reality, it’s more complex than that. Anil suggested that one of the reasons small vertically integrated companies don’t pass through the Great Filter is that it’s unnatural for small companies to have 15 departments, to think about, excel at, and balance 15 different things at the same time. It goes against all startup advice, which suggests becoming excellent at one thing.

Plus, dependencies and relationships scale quadratically. Fifteen departments means 105 connections between departments. It gets messy quickly.

[![](https://substackcdn.com/image/fetch/w_1216,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da307a3-69da-452c-8442-18a79f8e92d3_608x591.png)](https://substack.com/redirect/db401a8a-9324-40d7-9ccf-155366b1d3e4?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

In *[When to Dig a Moat](https://substack.com/redirect/3cce6b29-9494-4054-9bb7-0305e03fb503?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)*, we discussed the idea that startups’ advantages are uncertainty and speed. They need to move quickly to build a product and dig moats before competitors have the time to react.

[![](https://substackcdn.com/image/fetch/w_1826,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4309d5fc-7583-4459-9512-d179ace06bdd_913x346.png)](https://substack.com/redirect/3589f758-6bb6-4961-9508-fa9fc4861941?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

Adding so much complexity while there’s so much uncertainty often leaves you with a dangerous combination of uncertainty and lethargy. This combo seems to be one of the main contributing factors to Katerra’s demise. The company didn’t have a well thought out [strategy](https://substack.com/redirect/da1aee62-c7c9-47e5-91f0-51b63f06fd69?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), so it executed in a number of directions without gaining forward momentum.

[![](https://substackcdn.com/image/fetch/w_1816,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddea1326-1517-4316-b354-4b90c90e1eb0_908x651.png)](https://substack.com/redirect/5c1e9532-b7e1-4a6a-aa64-ef01768d99f3?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

Katerra offered ten building types (like garden apartments or industrial buildings with CLT homes) and twelve building systems (like the prefab bathroom kit or CLT facade system), and built three software systems for construction management, design automation, and tenant management.

“Ideally, early stage product development involves rapid iteration and prototyping, to figure out what needs to be built as quickly as possible,” Potter wrote. “But **the pace of product development at Katerra always felt sluggish**.”

Katerra tried to do too much, too soon. It went slow when it should have been going fast. Maybe the right amount of functions to vertically integrate at the beginning is as simple as this: **as many as you can without slowing down the pace of iteration until you have a product that customers want to buy at a price they’re willing to pay.**

Getting it right isn’t impossible. SpaceX and Tesla have done it, even if there have been bumps along the way, Anduril, Meter, and others seem to be doing it now, and Apple has been doing it for a long time.

In the beginning, it takes exceptional founders with a clear vision who can keep the whole thing straight in their heads and communicate it crisply to a growing team.

The good news from the Apple story is that if you can do both hardware and software at a certain level, the integration of the two creates a product that’s hard to beat. Apple is excellent at hardware, pretty good at software, and by integration both, has created an unmatched experience and the world’s most profitable product. During yesterday’s iPhone event, Craig said that Apple Intelligence “is only possible because of our integration between hardware and software.”

There’s actually more good news on the software-hardware integration front if you get it right, but I’ll save that for Part IV. This part is about the challenges.

And there aren’t many things harder for startups than building hardware.

### **Hardware is Really Hard**

This point is so well-appreciated that I won’t spend much time on it here: hardware is hard.

Hardware must obey the laws of physics. It also relies on complex and often global supply chains, in which any one link can snap and bottleneck the entire process. Iteration cycles are long. Upfront costs are high. You can’t build a hardware company on your laptop: you need machines and materials. Depending on what you’re building, operating in the physical world will mean interacting with regulations and regulators that dramatically slow down or block what you’re doing. It’s usually for good reason – you don’t want your hardware blowing up or falling from the sky – but it’s still an issue. In some cases, like nuclear, dealing with regulators takes years, at least tens of millions of dollars, and challenging uncertainty.

If you can figure all of that out, and get a product that works at small scale, you then need to scale manufacturing. Elon Musk went on Joe Rogan last year, and the thing I remember most is how many times he said just how hard scaling manufacturing is:

![](https://substackcdn.com/image/fetch/w_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Fthumbnail-play.png)

![](https://i.scdn.co/image/ab6765630000ba8a5107e1edf55737e944fb9af4)

#2054 - Elon Musk

Joe Rogan

Episode

Getting from nothing to something is hard, expensive, and uncertain. Getting from something to a lot of things, at a cost that’s competitive, is harder, more expensive, and if not more uncertain, then at least more grueling.

Sunil at Meter said that this is actually one of the hardest things about building a Vertical Integrator:

> *Non-vertically integrated companies can say we’ve solved a thing and move on. That’s not possible with vertically integrated companies. Every time you solve something, you’ve just bought a little time before you need to solve it again at the next level of scale.*
>
> *As you’re scaling up, you need to solve everything from components to circuit design to supply chain to production every nine months.*

In practice, that’s even harder than it sounds, because people like working on new problems, not solving the same old ones over and over. You need to re-orient teams to understand that scale is the new problem and get them so excited about mastering it that they don’t slow down, get out of sync, and make costly mistakes.

All of that is really hard for new companies to figure out. Worse, the companies you’re competing against have been doing all of that for a very long time.

### **Strong Incumbents**

A mistake that people in tech make, that I certainly make, is believing that imcumbents are incompetent sitting ducks, blissfully unaware of technology and unprepared for what’s going to hit them once startups figure out a new and better way of doing the thing they’ve always done.

Certainly, many incumbents have issues. We’ve beaten up on Boeing plenty, but more generally, as Carlota Perez pointed out, incumbents are entrenched in a techno-economic paradigm that’s worked really well for them and can be slow to adopt new technologies.

At the same time, however, these companies have been around for a very long time and have gone through cycle after cycle to produce their products as efficiently and at as low a cost as possible. They often own the pieces of their supply chains that give them the biggest advantages, have built out networks of modular suppliers that depend on their business for the rest, have tremendous amounts of information, enjoy both contracts and relationships with the biggest customers in their industries, have even written the legislation that governs them in a way that makes it especially difficult for new entrants to compete on equal footing, and employ thousands of people in states across the country, which gives them sway with lawmakers.

Over the past couple of months, I’ve read or re-read Henry Ford’s  (the history of Koch Industries), *[Cable Cowboy](https://substack.com/redirect/f1063e4f-fb0d-4e98-8d3d-c7f3e5d712b7?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)* (the biography of TCI/Liberty Media founder John Malone), and *[The Prize](https://substack.com/redirect/03359448-1bdc-43a6-b754-c7af7e75a8cc?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)* (the history of oil and its biggest companies). I would recommend reading them and other industry-relevant company histories to anyone looking to build or invest in Vertical Integrators to give yourself an appreciation for just how sharp these companies and their leaders are.

[![](https://substackcdn.com/image/fetch/w_2042,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8012bfe-9a6f-4aa0-a5f4-c4bb8b14e51c_1021x383.png)](https://substack.com/redirect/64f77c81-0a33-4ed8-a654-8ea9d466e62f?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

Incumbents will go to great lengths to protect what’s theirs and have the resources to do so. Building versions of what they’ve built that are slightly better on one dimension won’t win. Even a slightly cheaper product won’t win – they can lower prices and sustain losses to bleed you out.

These companies have mastered the last Techno-Economic Paradigm. Your only shot is building something radically better with the tools of the new one based on a prediction about where the market is going and then iterating like hell to a scaled solution before they adjust and catch up.

Just how long you have until they adjust and catch up depends on the specific incumbent and their circumstances. Building a Vertical Integrator in a space full of incumbents requires an incredibly deep understanding of each of their strategies before even deciding to jump in.

What are they focused on? Have they made commitments to certain architectures that will be hard to get out of? Have they promised investors that they’ll move in a direction that takes them away from the prize you’re pursuing? How strong is their team? Are star employees leaving?

You can’t assume your competitors are idiots, but you can make a very educated guess about whether they’re in a position to shift their resources in your new and better direction, and do whatever you can to [counter-position](https://substack.com/redirect/97dc494f-2810-4ad4-a4bd-cbd123d4807f?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) yourself against them.

[Anduril](https://substack.com/redirect/3944af58-60d1-4845-ae92-7eb8ea7c2558?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), for example, takes risk on its own balance sheet to develop programs that it believes the DoD will buy in the near-future so that it’s in the position to win those contracts against Primes that operate on a cost-plus model and therefore need to wait until there’s a contract to begin development.

But in the beginning, while you’re still operating with the advantage of uncertainty, the best you can do is form hypotheses, make predictions, and sprint.

Those predictions are hard to get right. Building a new system out of a number of very new technologies and inputs is harder than it sounds on paper.

### **The Right Level of Integration is Not Obvious**

I started Part II with a story about [Hadrian](https://substack.com/redirect/4cf0d393-4d2a-4458-ad6e-3f58716e69fb?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) to make one point: software alone isn’t usually enough to solve the problem. What I didn’t cover is that ***too much*** **vertical integration, too soon, is an issue, too.**

In that [Deep Dive on Hadrian](https://substack.com/redirect/4cf0d393-4d2a-4458-ad6e-3f58716e69fb?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), I highlighted that two of the company’s lead investors, Lux and Founders Fund, had previously backed a company trying to automate parts manufacturing: Plethora. The company, founded in 2013 to build the **factory of the future** by creating “a manufacturing system that turns customer designs into custom parts using robotics and advanced software that we’ve developed in-house,” failed.

There were three lessons from Plethora’s failure, according to investors and former employees:

* *They tried to do **everything in software,** cutting the humans out of the loop, which meant years of wasted time trying to solve “**hobby problems**” that humans could easily do.*
* *The offering was **too broad** – from prototypes to parts, different materials, different shapes, high-end and low-end, not precision-focused – Plethora wanted to do everything.*
* *It was a little **too early**, both in terms of customer demand for high-precision parts and in terms of the financing market for a business like this.*

In short: **Plethora tried to do too much, too soon, too early.**

This rhymes with Katerra’s failure: too much, too soon, if not too early (people will always want cheaper houses).

Katerra also likely vertically integrated too deep into the materials supply chain. As Potter points out, the company invested ~$100 million into a Cross-Laminated Timber (CLT) factory that could produce ~10% of the world’s supply of CLT. In addition to being a big investment of limited resources, it locked the company into a product that he said ended up getting cut out of plans in value engineering too often because it’s an expensive material.

A lesson might be this: **vertically integrate to whatever level will give you the best product at the lowest cost (lower than legacy alternatives) before integrating further with scale.**

But that’s about a billion times easier to write than it is to do.

Plethora likely believed that fully automating would let it produce the best products at the lowest cost before running into all of the challenges of actually building a fully automated manufacturing process. Katerra likely believed that its breadth and ownership of the supply chain were these interlinked things that, if everything went just right, would allow it to achieve the scale required to build the best product at the lowest cost.

There’s probably no shortcut but experimentation at fast iteration speed. You need to form a hypothesis, try it out, and adjust. The problem is, unlike software, the “minimum viable product” requires a ton of commitment in one direction.

### **Pivoting is Not Easy**

In other words, pivoting is not easy. The first-of-a-kind (FOAK) product or plant will never run at the costs that the nth product or plant will, and the only way to figure out whether the benefits you think you’ll get from scale are real is to actually build the thing, and then scale.

The other four points on why Vertical Integrators are so hard to build are magnified by the fact that you can’t simply change course once you run into issues.

Of course, you can iterate. You have to iterate. SpaceX is famously OK with blowing up rockets in order to learn and improve. But even SpaceX didn’t decide that it would start building space elevators instead of rockets, or even that it would stop building reusable rockets in favor of some new approach after its first few rockets blew up. It iterated towards the same product vision.

Traditional software is full of stories of companies that pivoted from one thing to another. Instagram was Blendr. Slack was Tiny Speck. Twitter was Odeo. Pinterest was Tote. YouTube was a video dating site. Shopify was a snowboarding ecommerce store.

Such dramatic pivots are harder in hardware, and practically impossible with Vertical Integrators. It takes too much upfront capital invested in one direction and too much specialized talent hired with one system in mind to simply switch course when something isn’t working.

There’s an ongoing debate about whether strategy matters for startups. I picked my side in *[In Defense of Strategy](https://substack.com/redirect/da1aee62-c7c9-47e5-91f0-51b63f06fd69?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)*, but I can squint and see that for certain software products, just getting the very best developers around the table and executing like mad until you find product-market fit with something. I don’t think that approach is at all feasible for Vertical Integrators.

A sound strategy is critical for Vertical Integrators. You need to work out as much as you possibly can on paper before enshrining it in metal. As a great example, check out the [Base Power Company Deep Dive](https://substack.com/redirect/bff36cf0-d0d1-4fae-a631-a774772bfbc5?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU). Zach and Justin banged on the idea as many ways as they could, and talked to as many people as they could, before expanding the team and putting a product into market.

If you get it wrong, it might be up to the next company to get it right. This is another reason for “Why Now?” for Vertical Integrators that we didn’t cover in Part II. If each individual Vertical Integrator is limited in its ability to pivot, a new wave of entrepreneurs can incorporate the lessons from previous attempts into fresh approaches. Plethora informed Hadrian. Katerra informed [Cuby](https://substack.com/redirect/0a141410-d4cc-475a-a398-9028ad1d4d4f?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) (on which more soon). Previous entrepreneurs have tried and failed to do build companies that sound similar in their goals to today’s Vertical Integrators.

While it’s easy to look at failed attempts as proof positive that “this will never work,” I think **one of the best signals that a category is investable is a previous failure with clear and actionable lessons.**

That’s small comfort for the companies that took the arrows, burning years to learn expensive and valuable lessons.

But say you don’t need to pivot. You have something that works, that scales, and that seems to be significantly better than incumbents can offer.

You’re not done yet.

### **Something Better Might Come Along**

This might be the most pernicious of the challenges.

Imagine doing all of the hard things required to get a Vertical Integrator to enough scale to get product quality and costs to a competitive level and then having a new entrant come along, using *your* hard-earned lessons and some newfangled technology to promise something even better or cheaper than what you’ve built.

With the pace of technological advancement happening right now, that’s always a very real possibility.

One of my favorite questions to ask founders is, “What sci-fi technology are you most worried about obsoleting your approach?”

It’s an absurd question on its face, but [sci-fi has a way of coming true](https://substack.com/redirect/eb5707bf-a43c-4c93-993d-5a13f51c982b?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), and the absurdity helps me get to the question I’m going for, which is: how close to the best possible approach is what you’re planning to build.

As a non-Vertical Integrator example, think about building an AI product. If your answer is “If GPT-5 is as much of an improvement over GPT-4 as GPT-4 was over GPT-3, we’re in trouble,” then you’re probably in trouble. If it’s “AGI might be an issue if it’s able to do everything in the world,” you might be safer.

In energy, if the answer is “[Nikola Tesla’s free energy](https://substack.com/redirect/3348a13f-501b-4caa-896b-ae13b3a140b6?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU),” then that’s just a chance you have to take.

[![](https://substackcdn.com/image/fetch/w_1816,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59ed2fd5-26bf-4e88-880f-9b63a1d59fb2_908x683.png)](https://substack.com/redirect/20c1893b-beaa-40de-96ec-ef6903d20394?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

*Smithsonian*

If it’s, “Commercial fusion power would blow us out,” then you can underwrite the company based on how long you expect commercial fusion to get to grid-scale generation. If it’s “If people actually start bringing nuclear reactors down the cost curve, that would be a problem,” then you might have a real problem.

The answers usually aren’t that black-and-white. In some cases, there may be competing approaches, each pursued by equally smart people with equally well-thought-out strategies and roughly equal abilities to execute. In some cases, those two companies may end up owning different parts of the market – one approach might work slightly better for one use, and the other for another. Sometimes, it’s just going to be a race: who can get their product into customers’ hands quickly enough to begin to scale and then get to scale quickly enough to underprice their competitor soonest.

The fact that there may be a better approach unlocked by one or two more technological advances is just something to be aware of, and to take advantage of if possible. This is one of the reasons that I prefer investing in Vertical Integrators over Deep Tech companies as defined in [Part I](https://substack.com/redirect/d31bc5aa-752e-49ba-b3ce-44d9cfc72342?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU). A Vertical Integrator should be in a position to incorporate the new and better technology into their system if and when it comes to fruition.

And ideally, if they’ve executed well, they’ll have enough momentum, scale, and capital to make it even more difficult for the next company to compete unless they have anything short of Tesla’s free energy machine.

### **Getting to Revenue Takes a Lot of Money**

Building a Vertical Integrator is expensive. It requires hiring world-class people with very specific skillsets across a variety of disciplines, buying machines and materials, hiring lawyers, and occasionally, blowing up very expensive machines.

It can also take a long time to build a product that someone will buy. Whereas a pre-seed software company can – not always, see Figma, but can – start generating revenue very quickly, there are plenty of Vertical Integrators that raise their Series B without ever having earned a dollar of revenue.

They need to convince venture capitalists to give them money based on their idea and their experience, and then on the team that they are able to hire, and then on the progress that that team is making on building the complex system that they’re trying to build, without the easy-to-evaluate “revenue go up” hockey stick charts software companies at a similar stage can rely on.

This isn’t always the case. Sometimes, Vertical Integrators can earn money on an early, scaled-down version of their product. Sometimes, with enough capital and speed, Vertical Integrators can start earning revenue quickly. As I mentioned in Part II, Hadrian is on track for $30 million in revenue this year as a three-year-old company. [Varda](https://substack.com/redirect/38573afb-7d28-4a37-88d8-d0b5b5be339e?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) set a goal to generate revenue within three years, and was executing on $60 million worth of DoD contracts within that window.

Revenue or no revenue, fundraising can’t be an afterthought for Vertical Integrators. It needs to be baked into the strategy from day one.

Founders need to understand what it will take to get to the point at which their company can count on debt and project financing to scale, and then convince venture capitalists to fund them to that point, even though they may have very little revenue to show for it in the interim.

Vertical Integrators face a well-known “Valley of Death” between those exciting early days when the idea exists on paper and in the heads of a fresh, world-class team and when the reality of executing on the plan has set in before real revenue has come in. Many companies overcome a number of early challenges only to run out of the money they need to bring the product to customers.

As I touched on in [Part II](https://substack.com/redirect/eedd8a4f-4990-4db4-95ab-3512c27cd9ac?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), though, I actually think that venture capital is lining up perfectly to provide the equity capital these businesses will need, and that Vertical Integrators are less dilutive than people expect because they can tap non-dilutive sources of funding including grants, debt, government contracts, project financing, and of course, revenue. And getting most of the investors willing to fund this kind of all-or-nothing bet on your side means that it’s even harder for someone new to come in and knock you off in-flight.

This financing challenge is, like all of the others, one that flips to an advantage if you can overcome it.

Luckily, very, very, very hard is not the same thing as impossible. It just takes very talented people executing relentlessly to show the difference.

### **Hard but Not Impossible**

Alright, have I scared you enough for one day?

These are just seven categories of challenges. We didn’t even touch on some big ones, like regulation or logistics, that may be more applicable to some Vertical Integrators more than others. And I suspect that if there are people out there reading this who are actually building Vertical Integrators instead of just writing about them, they’ll say that I actually missed a lot of the really hard things, or the little annoyances that really gum up the works in the day-to-day.

I’ve been through this myself. Breather was vertically integrated: we leased office spaces, undertook construction and design, even produced our own furniture, built an app that let customers book and access spaces, and backstage software that helped our team manage operations, and ran an in-house team of Operations Associates who cleaned and maintained our spaces after hundreds of bookings across 500 spaces in ten cities across the world.

Some of the little things I remember include showing up to a building to set up a new space only to realize that our moving company didn’t have the right insurance and getting sent back to the warehouse, watching Backstage in horror as an operations associate got tied up in one location and miss a job at another, meaning that customers walked into a space that the previous ones had left a mess, and fielding angry phone calls from customers who were locked out of a space before an important meeting because the app went down.

It’s not just the big, splashy things that you need to get right, but all of the little details. The surface area for problems is massive, and in an integrated system, a small problem in one place can have big consequences on the whole thing.

And yet… a lot of very smart, talented people who are eyes-wide-open about the challenges and have plenty of opportunities to do something easier choose to build Vertical Integrators.

Theodore Roosevelt said that **“Nothing in the world is worth doing unless it means effort, pain, difficulty.”** He might have been talking about Vertical Integrators: during his presidency, U.S. Steel was formed, Ford was born, and Standard Oil, General Electric, and Westinghouse Electric grew substantially.

Today’s Vertical Integrators face even greater challenges in many ways than those faced by the Second Industrial Revolution’s industrialists. Instead of a wide-open and fragmented landscape, they face competition from well-resourced, powerful, and experienced incumbents. Instead of just building hardware, they need to build hardware and software.

Against the odds, though, some of them even make it through the Great Filter to build big, important companies. On the other side, assuming you picked the right problem to solve, the outcome is proportional to the difficulty it took to get there.

[![](https://substackcdn.com/image/fetch/w_1774,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F404cd6f8-e9a0-48fa-be5c-ae178d72a6ac_887x625.png)](https://substack.com/redirect/65ff6cb4-d465-438f-a0bc-441767850b75?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

Next week, in the fourth and final installment of our Vertical Integrators series, we’ll talk about what it takes to pull it off, the advantages to vertical integration that lie on the other side of the challenges we discussed today, and the size of the prize for pulling off the near-impossible.

*Thanks to Anil, Sunil, and Sep for your insights, and to Claude for editing.*

That’s all for today. We’ll be back in your inbox on Friday with a Weekly Dose.

Thanks for reading,

Packy