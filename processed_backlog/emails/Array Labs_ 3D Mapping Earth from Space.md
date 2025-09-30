# Array Labs: 3D Mapping Earth from Space

**From:** Not Boring <notboring@substack.com>
**Date:** Tue, 26 Sep 2023 12:56:17 +0000
**Source:** inputs/saved_emails/Array Labs 3D Mapping Earth from Space_Tue,_26_Sep_2023_12-56-17_+0000_18ad1904dd4b1fc0.eml
**Processed:** 2025-08-24T19:13:12.175648

View this post on the web at https://www.notboring.co/p/array-labs-3d-mapping-earth-from

Welcome to the 116 newly Not Boring people who have joined us since last Tuesday! If you haven’t subscribed, join 211,981 smart, curious folks by subscribing here:
Today’s Not Boring, the whole thing, is brought to you by… Array Labs [ https://substack.com/redirect/40dec0ea-6455-4f3b-848c-69ec93150823?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ]
If you get as fired up reading this essay as I did writing it, you can simply go build radar satellite clusters to map the Earth in 3D by joining Array Labs:
Hi friends 👋, 
Happy Tuesday! It’s fall in New York City, the Eagles looked great on Monday Night Football, and I get to bring you a deep dive that’s been melting my brain for weeks.
If I’ve spoken with you over the past few weeks, chances are I’ve told you about Array Labs. It was designed for me. A deeply Hard Startup, riding exponential technology curves, to build distributed systems for space, to enable businesses on Earth, with a strategy as thoughtful as its hardware.
Nothing makes me happier than banging my head against a complex company like Array for weeks to understand it well enough to share it with all of you. This is a longer essay that I’ve written in a while, because fully appreciating what Array is trying to do requires some knowledge of the earth observation market, how satellites work, how radars work, business strategy, the self-driving car market, and more.
This is a Sponsored Deep Dive. I’ve always said that I’d only write them on companies I’d want to invest in — and I hope to invest in Array Labs when they raise next — and as Not Boring Capital’s thesis has tightened to Hard Startups that can bend the world’s trajectory upwards, so has the deep dive bar. Array clears that bar by hundreds of kilometers. You can read more about how I choose which companies to do deep dives on, and how I write them here [ https://substack.com/redirect/3da1d5d3-8923-45c1-905b-9046ca7ec780?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ].
So throw on some appropriate music…
And let’s get to it.
Array Labs: 3D Mapping Earth from Space
A real-time, 3D map of the world is the holy grail of earth observation (EO). 
Possessing such a map would enable new applications and technologies, from self-driving cars to augmented reality. It would improve climate monitoring, disaster response, construction management, resource management, and even urban planning. 
Access to a real-time global 3D map would confer significant strategic and economic advantages to whoever possesses it. The US government has spent untold billions of dollars over decades for more accurate and timely information about the state of the world. Real estate developers, insurers, and energy producers could turn the data from that map into dollars. 
But holy grails are, by definition, difficult to obtain. The map doesn’t currently exist, and it’s not for lack of trying. 
Array Labs [ https://substack.com/redirect/40dec0ea-6455-4f3b-848c-69ec93150823?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] thinks that now is the time to build it. And its founder, Andrew Peterson, thinks he knows how. 
The main thing you need is Very High Resolution Imagery (VHR) of gigantic swaths of Earth, freshly collected daily, to start, and more frequently over time. There are a few ways, theoretically, you could collect the data. 
You could send out a fleet of LiDAR-equipped self-driving cars, with humans behind the wheel. That’s how Autonomous Vehicle (AV) companies do it today, one city at a time. But it’s too expensive and impractical to cover the globe. At $20 per mile, it would cost over $1 trillion to map the Earth’s surface, even assuming cars could drive everywhere. 
You might fly LiDAR-toting airplanes across the globe. When people want VHR of specific areas today, that’s what they do. At around $500 per square kilometer (apologies for the mixed units, but we’re going with industry standards), a single US collection would be $5 billion. A global collection would run you a cool quarter-trillion, assuming you can access all of the world’s airspace without getting shot down. Closer, but still not good enough. 
Let’s go even higher, from ground to planes to satellites. Satellites rarely get shot down. They scan the entire globe, airspace be damned. Once in orbit, they keep flying around and around and around at very high speeds. And they’re way cheaper: at current retail pricing of around $50/sq. km, it would only cost you $150 million to cover the US, or $7.7 billion to cover the whole Earth. 
We’re getting warmer, but there are still two main problems with this approach: 
Resolution. Today, the resolution from even the best 3D satellite collections is still 100x worse than airplanes. You couldn’t guide self-driving cars with these maps. 
Coverage Cost. Getting coverage by sending up enough high-resolution satellites to capture the whole Earth would be too expensive to pencil out.
For a number of reasons we’ll get into, you can’t simply scale up current earth observation satellites to larger and larger sizes. They get exponentially less efficient as you scale them, and assuming you worked all of that out, a satellite big enough to provide the resolution and coverage you’d need would be way, way too big to send up on a rocket. 
If you wanted to make the antenna really big – like 50 kilometers in diameter big – it would be impossible with anything close to our modern capabilities. Such an antenna would be 1,000x taller and 5,000x wider than SpaceX’s Starship. It would be 60x taller than the Burj Khalifa. It would have 5.82x the diameter of CERN’s Large Hadron Collider. 
I tried to make an image to scale but it doesn’t come close to fitting on the screen. So let’s try a metaphor. If Starship were the size of a soda can, this 50 km diameter satellite antenna would be the size of the island of Manhattan. 
But a diameter that size is useful, because it helps increase vertical resolution, a key piece if you want a true 3D map instead of a stack of high-resolution 2D pictures. 
But having something that behaves like an enormous imaging satellite, or even just a giant radar antenna, would be really useful... 
There’s a way to do that, but it’s kind of crazy. 
What if instead, you kept the radar imaging satellites very small, but sent dozens of them up there in a big ring? 
When you do that, what you end up with is something that behaves like an absolutely enormous antenna – an antenna 30 miles wide – that improves exponentially. 
Instead of a monolithic antenna that gets exponentially less efficient with scale, you end up with a distributed system that gets more and more efficient with every satellite you add. Each satellite has its own solar panels, providing plenty of power. Each one is small and stackable enough that the whole cluster fits on a single port on an ESPA ring, snuggling in amongst all of the other satellites on the next SpaceX rideshare mission. Pointing them at the target is as easy as adjusting a small cubesat, like directing a ballet with dozens of prima ballerinas. 
“Then, pretty soon,” Andrew explains, “You've got the most efficient image collection system that ever existed in the history of mankind.” 
That’s what Array Labs is building, the crazy way: the most efficient image collection system that ever existed in the history of mankind. Its mission is to create a daily-refreshed, high res 3D map of Earth. 
To be sure, Andrew’s idea for Array Labs is crazy in a lot of ways. 
For one, the Air Force Research Lab tried to use radar to make a 3D map of the Earth back in the early 2000s with a program called TechSat-21. Working with DARPA, they designed the system to demonstrate formation-flying of radar satellites that would work together and operate as a single “virtual satellite.” It was an idea ahead of its time, sadly, and the program was scrapped due to significant cost overruns. 
For another, earth observation isn’t necessarily the rising star of the space economy these days. There are already a bunch of EO satellites orbiting our Blue Marble. Incumbents and upstarts alike, companies like Maxar, Planet, and Blacksky, have a lot of capacity in orbit. A workable business model has been harder to come by. Planet and Blacksky are both trading near all-time lows after coming public via a SPAC in 2021. 
When Ryan Duffy and Mo Islam wrote a piece on The Space Economy [ https://substack.com/redirect/49aaed5e-630e-4f6b-bab3-10c4bacdb94c?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] for Not Boring last year, they weren’t particularly bullish on the EO market, which was why I was surprised when Duffy called me a couple of months ago to tell me about a company I absolutely had to meet … in EO. 
He’d gotten bullish – he was doing consulting work for them, and asked to take his pay in equity instead of cash – but after five years at media startups writing newsletters about emerging tech, he told me that he was planning on doing his own thing for the foreseeable future. So I was doubly surprised when, on our next call, Duffy told me that he was giving up the consulting life early to join Array Labs full-time as Head of Commercial BD. 
After he introduced me to Andrew, I understood why. 
Array Labs has many of the characteristics I love to see in a startup. It’s ambitious and just the right kind of crazy. It’s reanimating an idea that didn’t work before but might now thanks to exponential technology curves [ https://substack.com/redirect/7721aa88-41bd-4585-8e9c-809e3044ce9a?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ]. It’s turning something traditionally monolithic into something distributed. It’s using technological innovation to unlock business model innovation, and executing against a clear strategy [ https://substack.com/redirect/ab443a2f-2cca-43bb-894e-23b1ca5e9bd0?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ] while it’s still in its uncertainty period [ https://substack.com/redirect/1d02143a-cb3f-4e2f-ae31-a41d96b2bb84?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ]. And, if it works, it will enable new businesses to be built that aren’t possible today. 
In short, Array Labs both has its own powerful answer to the question, “Why now?” and the rare opportunity to serve as other companies’ answer. 
But taking advantage of a powerful “Why now?” means that it’s also very early. Array Labs plans to launch four demonstration satellites next year and two more orbital pathfinder missions in 2025, before sending up its first full cluster in 2026. Risks abound. 
That makes it a particularly fun time to write about the company. This essay is a time capsule from before Array Labs becomes obvious. It’s a Not Boring thesis paper of sorts, and the thesis is this: a company with a near-perfect why now (and the right team to capture it) and a strategy to match the moment can both disrupt and grow an established industry while enabling new ones. 
To lay it out, we’ll need to cover a lot of ground in one pass: 
Earth Observation: The 600km View
The Engineering Magic of SAR
How to Make the Most Efficient Image Collection System Ever
Intersecting Exponentials
Array Labs’ Strategy
Enabling New Markets
Risks
Mapping the Path to Mapping the World
Put on your spacesuit. Let’s launch into orbit to get a better view of the industry.
Earth Observation: The 600km View
A couple of weeks ago, I wrote [ https://substack.com/redirect/a60ead95-22cc-40cb-bb40-237957674691?j=eyJ1IjoiOXAwZ3QifQ.gb8J5T7GnA_ZlNuaMZjmlXXepKbqOsa8-6m8ExkRNpU ], “Any technology that is sufficiently valuable in its ideal state will eventually reach that ideal state.” 
The earth observation market is sufficiently valuable, even in its current state. In 2022, estimates put the market size around $7 billion and growing at roughly 10% annually. This is likely a fairly significant underestimate, as the US and other governments spend billions of dollars on highly classified programs. 
But the earth observation market isn’t close to its ideal state. In its ideal state, earth observation would produce real-time, high-resolution, global coverage, easily consumable by the naked eye or machine learning models, accessible to anyone for their specific needs. 
AV companies would ingest point clouds that turn into real-time maps, alerting cars of changes in traffic conditions, construction projects, or closed roads. 
The Department of Defense would have real-time visibility into the movement of enemy resources, no matter the weather or time of day. 
Environmental groups would be able to track planetary indicators by the minute. 
Augmented Reality (AR) companies would design experiences that interact with the real world in real-time. 
Foundation model companies, always hungry for more data to scale performance, could train their models on 3D and HD continental-level scans of the world. 
If the data was good and cheap enough, entrepreneurs would certainly dream up uses that I can’t. 
In its ideal state, earth observation will expand humanity’s ability to understand, respond to, and shape events on a global scale. 
And we’re getting closer. Over the past century, we’ve made significantly more progress towards that ideal state than we did in all of the millennia of human history before it. 
There’s much more where this came from. For history on mapmaking and earth observation, a SAR primer, a peek into how Array plans to build the most efficient image collection system in the history of mankind, the curves it’s riding, its strategy, some risks, and where it’s heading…
(Click the button or the title up top to head over to Not Boring)
Here’s a little teaser:
Thanks to Dan for editing, and to Andrew and Duffy for teaching me the ins and outs of SAR and letting me tell the Array Labs story!
That’s all for today. We’ll be back in your inbox with a Weekly Dose on Friday. Go get it this week.
Thanks for reading,
Packy

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubm90Ym9yaW5nLmNvL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3hOakk0TXpVME9Td2ljRzl6ZEY5cFpDSTZNVE0zTkRBd09ESTNMQ0pwWVhRaU9qRTJPVFUzTXpJNU9EVXNJbVY0Y0NJNk1UWTVPRE15TkRrNE5Td2lhWE56SWpvaWNIVmlMVEV3TURJMUlpd2ljM1ZpSWpvaVpHbHpZV0pzWlY5bGJXRnBiQ0o5LmRqa3pFUDVoUzdDbnhmU0dWV0tQaEY5bEtDU0VmV3BZdXZHRTk3aEoyM0kmZXhwaXJlcz0zNjVkIiwicCI6MTM3NDAwODI3LCJzIjoxMDAyNSwiZiI6dHJ1ZSwidSI6MTYyODM1NDksImlhdCI6MTY5NTczMjk4NSwiZXhwIjoxNjk4MzI0OTg1LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.bQ070FMKnGM8IJSyJg12HPENvKZFbve5wWV18mMKLNA?