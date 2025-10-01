# Weekly Dose of Optimism #109

**Source**: inputs/old stuff/Docs/Weekly Dose of Optimism109_083024.html
**Type**: article
**Created**: 2025-08-25T02:53:52.899283

---

# Weekly Dose of Optimism #109

[![](https://substackcdn.com/image/fetch/w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc717a1b5-b9a5-406a-abde-71731cc6df19_1200x600.png)](https://substack.com/redirect/137de709-7200-4a53-869e-7867ff20a313?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)


[![](https://substackcdn.com/image/fetch/w_2912,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc6799dbe-eed8-4cd7-b50b-07b50e06ded0_1600x1198.jpeg)](https://substack.com/redirect/fb5175b0-e3e6-4a4c-9c09-4e1f1a830ee8?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

*Wander Petra Island, designed by Frank Lloyd Wright*

*If you have a trip coming up, you need to [check if there’s a Wander where you’re going](https://substack.com/redirect/f00d77d3-d03b-442e-9b8f-a693d109f238?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU). With over 100 homes throughout the country, chances are, there is.*

*[Wander](https://substack.com/redirect/f00d77d3-d03b-442e-9b8f-a693d109f238?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) is like staying inside of Architectural Digest. Just [look at them](https://substack.com/redirect/f00d77d3-d03b-442e-9b8f-a693d109f238?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU). Wanders combine the quality and convenience of a luxury hotel with the comfort and privacy of your own home, but even that sells it short. The homes on Wander are like the places you see on those high-end real estate shows on Netflix and assume that you’ll never be able to live in, but with [Wander](https://substack.com/redirect/f00d77d3-d03b-442e-9b8f-a693d109f238?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), you can, at least for a few days.*

*Summer ends this weekend, but your vacation doesn’t have to. And if you really need to work, Wanders come equipped with fast wifi and work stations, plus gyms, saunas, pools hot tubs, and more. You don’t even have to clean up after yourself (or pay a cleaning fee). Prices start at $400/night and Fall ushers in some of the best prices of the year.*

*Wander is giving all Not Boring readers $300 off when you use the code **NOTBORING** and book before September 30th. And if you create an account today at our [special link](https://substack.com/redirect/f00d77d3-d03b-442e-9b8f-a693d109f238?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU), you’ll be entered to win a free 5-day trip and $10,000. Treat yourself.*

[Go Wander](https://substack.com/redirect/f00d77d3-d03b-442e-9b8f-a693d109f238?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

Hi friends 👋,

Happy Friday and welcome back to our 109th *Weekly Dose of Optimism.*

A real smorgasbord of good stuff this week — everything from Chinese fusion projects to Gavin Baker going *very* deep on AI. We never know exactly what is going to make it into the *Weekly Dose* until Thursday afternoon, or even Friday morning. Once we think we’re done, someone goes out and does something else we need to figure out how to squeeze in, like Magic. Humans rock.

Let’s get to it.

*Nous Research*

> *Nous Research is proud to release a preliminary report on DisTrO (Distributed Training Over-the-Internet) a family of architecture-agnostic and network-agnostic distributed optimizers that reduces the inter-GPU communication requirements by 1000x to 10,000x without relying on amortized analysis, and matches AdamW+All-Reduce in convergence rates. This enables low-latency training of large neural networks on slow internet bandwidths with heterogeneous networking hardware.*

[![](https://substackcdn.com/image/fetch/w_2400,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c53833a-c21c-4162-a565-5c2d448d6041_1200x999.jpeg)](https://substack.com/redirect/6d52bfa9-8dd2-42e3-966a-7b182cf89589?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

The team at Nous Research released its preliminary report on DisTrO, a method for distributed AI training that significantly reduces the need for communication between GPUs, enabling efficient training of large models even with slow internet connections and different hardware setups. Their approach is architecture-agnostic and matches standard optimization methods in performance, promoting more open, decentralized, and collaborative AI development. Any time you can reduce something by 1,000x-10,000x … that’s a pretty big deal. And when that thing your reducing by 1,000x-10,000x has to do with training AI models, welp, that’s a very big deal.

DisTrO works by reducing the amount of data that needs to be shared between GPUs during model training. Instead of constantly syncing large amounts of info, as is the current approach, it optimizes the process to use much less communication. Using DisTrO even large models can be trained efficiently at slower internet speeds and worse hardware, without losing performance. Ideally, with DisTrO, a much larger swath of teams could train large models, not just the teams with tens of billions of dollars at their disposal.

DisTrO is not yet commercialized and Nous team is refining their methodologies. But the current plan is to make the work open-source so that any one could train models more resource efficiently, which could mean this development is a very *very* big deal.

—

In other AI news, [Magic announced LTM-2-Mini](https://substack.com/redirect/f1aa21c7-f17d-4cae-835b-8c481dffaf4e?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) with a **100 million token context window** — enough for to million lines of code or 750 novels. Most models learn things during training, Magic’s model can learn in-context during inference. Dump your full codebase or library of books in, and it can learn from them practically on the fly. Magic.

*Jeff St. John for Canary Media*

> *Luckily for the 22 million power customers reliant on ERCOT’s grid, solar power generation also hit a near-record level of 20,799 MW on August 20, just below the 20,832 MW record set two days before. That flood of solar power kept supply matched to demand throughout the midday hours — and because solar is the cheapest source of electricity on the grid today, wholesale electricity prices remained low.*

[![](https://substackcdn.com/image/fetch/w_2336,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4be0d790-89b9-4948-93b9-d006fb9c18ef_1168x652.jpeg)](https://substack.com/redirect/26c804dc-3b7f-4998-9015-65f4b0b7befa?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

During what has been a record-breaking hot summer, Texans have been cranking up the AC and putting record-breaking demand loads on the power grid. Luckily, grid performance has been solid and prices have been reasonable. How?

Solar energy during the day, stored battery power in the evening. That’s a Texas 1-2 punch that rivals cold beer on a Friday night and a pair of jeans that fit just right. So here’s generally how this works: Texas gets hot as shit in the summer, Texans blast AC during the day (as the Good Lord intended), cheap solar meets the increased demands from AC during the day, and as the AC still blasts into the night, discharging stored energy from batteries kick in to meet demand. Just like we discussed in our Deep Dive on [Base Power Company](https://substack.com/redirect/9f995c2c-496e-414e-b750-fa1e9dc9b636?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU).

Texas: Land of the solar, Home of the batteries!

*Gemma Conroy for Nature*

> *At the same time, China is fast pouring resources into its fusion efforts. The Chinese government’s current five-year plan makes comprehensive research facilities for crucial fusion projects a major priority for the country’s national science and technology infrastructure. As a rough estimate, China could now be spending $1.5 billion each year on fusion — almost double what the US government allocated this year for this research, says Jean Paul Allain, associate director of the US Department of Energy’s Office of Fusion Energy Sciences in Washington DC. “Even more important than the total value is the speed at which they’re doing it,” says Allain.*

[![](https://substackcdn.com/image/fetch/w_1534,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9ae0ad4-5a73-45f8-9958-ead8494a3693_767x575.jpeg)](https://substack.com/redirect/71c25c88-f01a-4672-bb0b-52b55a1c39c0?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

As Texas (and the world generally) expands solar capacity, China is placing a massive, long-term bet on fusion power—a technology that could eventually surpass solar. After all, why depend on sunlight when you could generate the sun’s energy directly in a lab?

China is involved in international efforts, namely ITER, but is also developing facilities like EAST and planning the China Fusion Engineering Test Reactor (CFETR), in an effort to establish itself as the global leader in nuclear. The country is currently spending $1.5B annually on its fusion efforts, double the U.S. budget.

And its investment is starting to pay off. An MIT nuclear scientist cited in the article stated, “China has built itself up from being a non-player 25 years ago to having world-class capabilities.” China is very good at setting national priorities, pouring tons of resources into those priorities, and quickly catching up to or leap-frogging competitor nations in the process. It is doing that in nuclear fusion.

That said, state-led efforts can only get you so far in terms of innovation and with commercial fusion still a few major breakthroughs away from being viable, we’d still bet on the U.S. approach: innovation and competition. Currently, 80+ companies, most of them American, are currently [racing to commercial fusion power](https://substack.com/redirect/52b911cb-ede6-47dc-934a-0daa263069d7?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU).

While more clean, abundant energy anywhere in the world is a positive for humanity, America can’t afford to lose the races to build out (and export) fission or to harness fusion to China. Hopefully, this serves as a wakeup call. A battle to generate the most abundant energy is a Great Power Conflict we can get behind.

—

In related atomic news, Switzerland is lifting its ban on nuclear power plants. Why? Geopolitical tensions (it’s not safe to rely too heavily on Russian gas), climate targets, and growing energy demand. Turns out, nuclear is reliable, clean, and able to produce huge amounts of electricity consistently. Welcome to the party, Switzerland!

*Invest Like the Best Podcast*

![](https://substackcdn.com/image/fetch/w_72,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Fthumbnail-play.png)

![](https://i.scdn.co/image/ab6765630000ba8ad99239879e64bac57e80880c)

Gavin Baker - AI, Semiconductors, and the Robotic Frontier - [Invest Like the Best, EP.385]

Colossus | Investing & Business Podcasts

Episode

Sometimes you listen to a business podcast, and the guest just regurgitates well-trodden perspectives on a topic or gives vague, probably unhelpful advice on business management. Sometimes you listen to a business podcast, and are reminded that some people really, really know their shit. Like knows their shit at a deeper level than anyone else knows their shit on their respective topic. The recent *Invest Like the Best* episodewith Gavin Baker is an example of the latter.

Gavin has been covering tech, and specifically semiconductors, for nearly 25 years and he can speak to the players, products, and strategies in a more detailed manner than anyone I’ve come across. You should listen to the full episode if you haven’t already. But in case you don’t have time, I am sharing 5 key insights from the episode below *(summarized by ChatGPT, which feels appropriate here, given the nature of the conversation)*

> * **AI Competition Among Tech Giants**: The "Magnificent Seven" tech giants are in a business shootout due to the general-purpose nature of AI, where each company sees creating a "Digital God" as existential.
>
> > *"If you create that first Digital God, we could debate whether it's tens of trillions or hundreds of trillions of value...but that is what they believe."*
>
> * **Importance of Scaling Laws in AI Development**: Scaling laws will continue to drive AI advancements until there is evidence they are slowing, heavily tied to GPU performance improvements.
>
> > *"They believe scaling laws are going to continue...and because they have that belief, they're going to spend until there is irrefutable evidence that scaling laws are slowing."*
>
> * **Data Centers and GPU Clusters as AI Bottlenecks**: Future AI advancements depend on building larger and more efficient GPU clusters, requiring breakthroughs in networking, storage, and cooling technologies.
>
> > *"We’re going to need profound breakthroughs at every step...Otherwise, it's going to be wasted, and MFU is going to be 3% to 5%."*
>
> * **Emergence of Humanoid Robotics and FSD**: Humanoid robots and fully self-driving (FSD) vehicles, especially leveraging LLMs, will significantly disrupt labor and industry, potentially even more than AI-driven white-collar automation.
>
> > *"I think humanoid robots may be the biggest disruption in our lifetime... because the humanoid robot could do any task that a human can."*
>
> * **Investment Opportunities in AI Infrastructure**: The most promising investments lie in companies improving AI infrastructure efficiency, such as networking and storage, rather than just at the application layer.
>
> > *"Invest in next-generation networking, storage, and memory technologies, particularly in networking...that's where I am targeting my dollars."*

*From [@hud\_zah](https://substack.com/redirect/4ae83411-2726-49bb-a811-ea5e8fb88492?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU) on X*

> *in a couple weeks, i built a nuclear fusor in my bedroom – with zero hardware experience **the secret?** Claude sonnet 3.5 + projects a glimpse into the process below*

[![](https://substackcdn.com/image/fetch/w_2912,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d1028b5-d8bf-4117-aa68-988fba336449_1674x1454.jpeg)](https://substack.com/redirect/a0de2370-b285-4ab4-b674-a8678c22a092?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)

You can lead state-led fusion programs like China or you can spend 25 years covering an industry like Gavin…but you still might get beat out by folks like [Hudhayfa Nazoordeen](https://substack.com/redirect/51b3549b-aea2-4a41-b1e3-051f70c78f71?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU). With zero hardware experience, a few years of math undergrad under his belt, and access to Anthropic’s Claude Sonnet 3.5, Hudhayfa managed to build a nuclear fusor in his bedroom.

A **nuclear fusor** is a device that uses an electric field to accelerate ions to high speeds, causing them to collide and undergo nuclear fusion. While fusors are cool and can produce fusion reactions, they are not efficient enough for practical power generation. They’re mainly used for research, education, and fun.

In the case of Hudhayfa, *what* he pulled off is not groundbreaking but it’s about *how*, and how fast, he pulled it off that gives us hope. Take a smart kid, give him a Claude Sonnet 3.5 subscription, a couple of weeks of free-time, and boom anything is possible.

The world is going to be a fun place when every ambitious kid in the world has access to models 10x more powerful than Sonnet 3.5. Can’t wait.

Have a great weekend y’all.

Thanks to ***[Wander](https://substack.com/redirect/58dedd7c-167e-43c3-8220-00d39b8b85b8?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU)*** for sponsoring! We’ll be back in your inbox on **Tuesday**.

Thanks for reading,

Packy + Dan