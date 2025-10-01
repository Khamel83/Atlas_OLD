# Vulnerabilities, Philosophies, and Ad-Blockers; Intel's Response; The Advantage of ServerlessÂ (Stratechery Daily Update 2018-01-09)

**Source**: http://mailchi.mp/stratechery/vulnerabilities-philosophies-and-ad-blockers-intels-response-the-advantage-of-serverless?e=ef6eeda78d
**Type**: article
**Created**: 2025-08-13T16:47:12.765042

---

title: Vulnerabilities, Philosophies, and Ad-Blockers; Intel's Response; The Advantage of ServerlessÂ (Stratechery Daily Update 2018-01-09)
source: http://mailchi.mp/stratechery/vulnerabilities-philosophies-and-ad-blockers-intels-response-the-advantage-of-serverless?e=ef6eeda78d
date: 2025-08-13T16:47:11.065721
tags: []
---
|  |  |   
---  
|  |  | The Daily Stratechery email, including exclusive content for members of [Stratechery.com](http://stratechery.com/)  
---  
  
|  |  |  |  | 

# Vulnerabilities, Philosophies, and Ad-Blockers; Intel's Response; The
Advantage of Serverless  
  
Tuesday, January 9, 2018

[blog post](https://stratechery.com/2018/vulnerabilities-philosophies-and-ad-
blockers-intels-response-the-advantage-of-serverless/) / [forum
thread](https://forum.stratechery.com/t/vulnerabilities-philosophies-and-ad-
blockers-intels-response-the-advantage-of-serverless/1446)  
---  
Happy New Year! I am happy to report — both for your sake and for mine! — that
by the second week of my time off I was ready to start writing again. I have
to say, in the four-and-a-half years I have been doing this (three-and-a-half
years full-time) this was the most I ever needed a vacation; it was a relief
to get that itch to come back. On to the update:  
---  
Vulnerabilities, Philosophies, and Ad-Blockers  
---  
[Yesterday’s Weekly Article](https://stratechery.com/2018/meltdown-spectre-
and-the-state-of-technology/) ended up being more explanatory than
philosophical; hopefully it was useful. I remain, though, more intrigued by
the latter. Everything about this bug, from speculative execution to the [Von
Neumann architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture),
is rooted in decisions made years — in some cases, _decades_ — ago. In nearly
every case the choice was made to prioritize speed over security, until we
arrive at today where practically every computer on earth is theoretically
vulnerable. It is easy to shake our heads and criticize those who made those
decisions: how could they have been so reckless? And yet, precisely because
they were, we have such incredible advances. In this too the analogy I made to
Internet companies holds: everyone knows that the initial research that led to
the Internet was funded by the government, but that only emphasizes just how
unexpected everything about the Internet has been. It is impossible that
anyone in a position of power would, had they understood just how deeply the
Internet would disrupt all aspects of life, authorized its creation. No one
saw any of this coming. And, at the same time, those who were in a position to
see the dangers — whether they be from processors or aggregators — were deeply
incentivized to ignore them. There simply was too much to be gained from being
blind. That, though, is why this is the vulnerability of our time: the scales
on everyone’s eyes are falling off, whether we want them to or not. Note,
though, that seeing dangers are not enough: what is done is done, which means
it is just as necessary to see the possibilities as well. For now there is one
topic on which I have completely changed my mind: ad-blocking. Back in 2015 I
upset a whole bunch of folks with [this Daily
Update](https://stratechery.com/2015/carriers-to-implement-ad-blocking-mad-
men-and-optimism-spotify-and-starbucks/):  
---  
|  |  |   
---  
Let’s get one thing straight up front: I believe that Carthy and his [ad-
blocking] company, and the mobile operators that use Shine’s software, are
wrong in a moral sense. And, frankly — and I know this will upset many of you
— I believe that those using ad-blockers are wrong as well. The appropriate
way to avoid advertisements is to not visit the sites that host them. True,
the effect on the publisher is the same — one less ad impression — but the
only way to properly evaluate business is to consider not only losses but also
money not made, and I simply cannot understand any sort of justification for
taking something while depriving publishers of that income: if you don’t want
to pay, then don’t play.  
Even then I found the most compelling argument for ad-blockers to be the fact
that ads were one of the best vectors for delivering malware (complaints about
aesthetics or performance were much less compelling). Spectre has pushed me
over the line: it is completely unreasonable that following a link could
potential lead to my most sensitive data being compromised, yet the nature of
Javascript and its just-in-time compilation is that that is a legitimate
attack vector. Here’s the thing though: to be for ad-blocking — or at least
not an opponent — is, for all intents and purposes, to be for Facebook and
Google. As I have [argued regularly](https://stratechery.com/2015/tim-cooks-
unfair-and-unrealistic-privacy-speech-strategy-credits-the-privacy-priority-
problem/) Facebook and Google are, by a significant margin, the most
responsible guardians of the sort of personal data that is used in digital
advertising; they are also the least impacted by ad blocking because they
serve their own ads, not third-parties. And this, indirectly, gets back to my
broader point: it is one thing to imagine a world where processors can be
trusted and the web remains decentralized; realistic approaches to the future
have to start with today’s reality where Google and Facebook are arguably the
most reliable entities there are. _While I’m here, I made a mistake in
the[last Daily Update of 2017](https://stratechery.com/2017/facebook-and-age-
discrimination-apple-slows-down-iphones-2017-when-tech-grew-up/). I said that
Facebook planned to only make political ads visible; in fact, according to
[this blog post](https://newsroom.fb.com/news/2017/10/update-on-our-
advertising-transparency-and-authenticity-efforts/), all ads will be visible.
I would push further, that they be searchable, but I regret the error._  
---  
I hinted at this yesterday, but Intel’s response to these vulnerabilities was,
to put it generously, underwhelming. From the company’s [press
release](https://newsroom.intel.com/news/intel-responds-to-security-research-
findings/):  
---  
|  |  |   
---  
Intel and other technology companies have been made aware of new security
research describing software analysis methods that, when used for malicious
purposes, have the potential to improperly gather sensitive data from
computing devices that are operating as designed. Intel believes these
exploits do not have the potential to corrupt, modify or delete data.  
This is the red flag in this press release: the issue with Meltdown and
Spectre is not that they “corrupt, modify or delete data”; it’s that they
steal data. Intel is purposely obfuscating the vulnerability from the first
paragraph on.  
---  
|  |  |   
---  
Recent reports that these exploits are caused by a “bug” or a “flaw” and are
unique to Intel products are incorrect. Based on the analysis to date, many
types of computing devices — with many different vendors’ processors and
operating systems — are susceptible to these exploits.  
This where the distinction I laid out yesterday between Meltdown and Spectre
is critical: Spectre is indeed broadly exploitable; Meltdown, on the other
hand, appears to be much closer to a bug. On Intel processors attackers can
effectively invoke a [race
condition](https://en.wikipedia.org/wiki/Race_condition) to steal data;
Spectre, which utilizes the fundamental nature of modern processors, is much
more intricate and harder to exploit. Intel, you will note, is eager to
conflate the two.  
---  
|  |  |   
---  
Intel is committed to product and customer security and is working closely
with many other technology companies, including AMD, ARM Holdings and several
operating system vendors, to develop an industry-wide approach to resolve this
issue promptly and constructively.  
It’s not “this issue”. It’s “these issues”, and one of them is mostly about
Intel, not AMD or ARM. What is worth noting, though, is that the Meltdown
vulnerability dates back to Intel’s Core architecture, which was a direct
response to AMD having taken the performance crown with Athlon. Intel had run
into a dead-end with its NetBurst architecture that prioritized clock-speed,
and instead started to focus on parallelism, an approach that benefits the
exact sort of speculative execution implication in these vulnerabilities. Who
knows if Meltdown is the result of a choice made back then, but it is much
more of a bug than is Spectre, and it is striking how carefully Intel is
trying to escape all blame.  
---  
The Advantage of Serverless  
---  
There is one more interesting takeaway from this episode. Version 1 of the
public cloud was what I illustrated yesterday; virtualized servers that, from
a developer perspective, were little different from something on-premises:  
---  
The payoff from being on AWS came from scaling everything surrounding the
server itself: hardware upgrades, networking, cooling, administration, etc.
The workflow, though, was largely the same: developers maintained an operating
system in the cloud, kept it up-to-date, ran their applications, etc.
Serverless offerings, like [AWS’s
Lambda](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html), are
different: there is no operating system, there is no app, there is simply an
API call to accomplish some sort of function; everything else is abstracted
away. These vulnerabilities have proven the worth of serverless services like
Lambda in two ways:  
---  
| • |  | First, applications relying on serverless services don’t have to do anything to account for these vulnerabilities. All updates are handled by Amazon (or Microsoft or Google) and, at least in the short term, all of the costs of the performance penalties incurred by the fixes are handled by the cloud provider as well.  
---|---|---  
| • |  | Second, and perhaps more importantly, it seems likely that serverless environments are more secure generally. Offering up specific functionality is a much higher level of abstraction than offering a virtual server where absolutely anything can be run; that layer of abstraction is itself a form of security.  
---|---|---  
This second point gets at one other root cause of not just this vulnerability
but also its impact: these processors are rooted in fundamental design choices
that assumed that only one user was using a computer — and thus a processor.
The concept of side attacks on cache is not new, but computer security has
long presumed that having physical access to a machine is such a security
nightmare that it doesn’t much matter. Cloud computing changed all of this; it
used to be that servers were built on specialized processors from IBM or SUN;
the triumph of Intel’s x86 processor in the server space is its own disruption
story. That disruption, though, of the high volume consumer processor winning
through scale, brought with it consumer assumptions, including the idea there
would only be a single user. To be sure, Intel processors added on all kinds
of protections to allow for multi-user use, but it wasn’t a controlling
constraint from the beginning, and everyone is now paying the price.  
---  
I apologize for the formatting issues in yesterday’s article. It appears my
template breaks with images in quotes. I’ll fix it. The Daily Update is
intended for a single recipient, but occasional forwarding is totally fine! If
you would like to order multiple subscriptions for your team with a group
discount (minimum 5), please contact me directly. Thanks for being a
supporter, and have a great day!  
---
