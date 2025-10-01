# The Super-Aggregators and the Russians - Stratechery by Ben Thompson

**Source**: https://stratechery.com/2017/the-super-aggregators-and-the-russians/
**Type**: article
**Created**: 2025-08-13T17:00:44.484030

---

title: The Super-Aggregators and the Russians - Stratechery by Ben Thompson
source: https://stratechery.com/2017/the-super-aggregators-and-the-russians/
date: 2025-08-13T17:00:43.078862
tags: []
---
In August 2011, just a day or two into my career at Microsoft, I sat in on a
monthly review meeting for Hotmail (now known as Outlook.com); the product
manager running the meeting was going through the various geographies and
their relevant metrics — new users, churn, revenue, etc. — and it was, well,
pretty boring. It was only later that I realized just how astounding “boring”
was; a small group of people in a conference room going over numbers that
represented hundreds of millions of people and dollars in revenue, and most of
us cared far more about what was on the menu for lunch.

I’ve [reflected on that meeting
often](https://twitter.com/benthompson/status/854381355026702336) over the
years, particularly when it comes to Facebook and controversies like
[censoring too much](https://stratechery.com/2016/facebook-versus-the-media/),
[censoring too little](https://stratechery.com/2017/facebook-content-
guidelines-facebook-video-amazon-prime-video-on-apple-tv/), or [“fake
news”](https://stratechery.com/2016/fake-news/), and I was reminded of it
again with [this
tweet](https://twitter.com/markwarner/status/908431496737935361):

Mark Warner, the senior Senator from Virginia, is referring to a Russian
company, thought to be linked to the Kremlin’s propaganda efforts, having
bought $100,000 worth of political ads on Facebook, some number of which
directly mentioned 2016 presidential candidates Donald Trump and Hillary
Clinton. Facebook has [released limited details about the
ads](https://newsroom.fb.com/news/2017/09/information-operations-update/),
likely due to its [2012 consent decree with the
FTC](https://www.ftc.gov/sites/default/files/documents/cases/2012/08/120810facebookdo.pdf),
which bars the company from unilaterally making private information public, as
well as the problematic precedent of releasing information without a clear
order compelling said release. To that end, it was reported over the weekend
that special counsel Robert Mueller received [a much more comprehensive set of
data](https://www.wsj.com/articles/facebook-gave-special-counsel-robert-
mueller-more-details-on-russian-ad-buys-than-
congress-1505514552?mg=prod/accounts-wsj) from Facebook [after obtaining a
search warrant](http://money.cnn.com/2017/09/15/media/facebook-mueller-
ads/index.html).

Even with all that context, though, I found Senator Warner’s tweet puzzling:
how else would the propaganda group have paid? Facebook’s self-service ad
portal lets you buy ads in 55 different currencies, including the Russian
Ruble:1

[![](https://i0.wp.com/stratechery.com/wp-content/uploads/2017/09/Screen-
Shot-2017-09-18-at-5.09.22-PM-1.png?resize=923%2C428&ssl=1)](https://i0.wp.com/stratechery.com/wp-
content/uploads/2017/09/Screen-Shot-2017-09-18-at-5.09.22-PM-1.png?ssl=1)

That, though, brought me back to that Hotmail meeting: that I, and probably
many more in the tech industry, find the idea of Facebook selling ads in
rubles to strangers to be utterly unremarkable, even as thousands find it
equally outrageous and damning, is a reminder of just how unprecedented and
misunderstood aggregators like Facebook continue to be, and what a challenge
it will be to regulate them.

#### The Cellular Network Company

Senator Warner, it should be noted, is considered one of the most
technologically literate people in the entire Senate — and [the
richest](https://en.wikipedia.org/wiki/List_of_current_members_of_the_United_States_Congress_by_wealth).
Warner originally made his fortune by [facilitating the sale of cellular phone
licenses](https://www.theatlantic.com/magazine/archive/2006/05/the-man-with-
the-golden-phone/304777/); he then co-founded [Columbia
Capital](https://www.crunchbase.com/organization/columbia-capital), a venture
capital firm which specialized in cellular businesses: the firm’s early
investments included Nextel, BroadSoft, and MetroPCS.

A cellular network company is certainly a new kind of business that is similar
to today’s tech giants in many respects:

  * At a fundamental level, cellular network companies are about the movement of information — voice and text, in Warner’s era — not physical goods. Moreover, because this information is digital, there are no marginal distribution costs in its transfer. This is the same characteristic of companies like Google and Facebook.
  * A cellular network company has massive fixed costs and minimal marginal costs; one more minute of talk time costs practically nothing to provide, unless the network is saturated, at which point significant capital investment is necessary. Today’s internet services are similar: marginal usage is effectively free, although significant capital investments in data centers are necessary (as well as significant ongoing bandwidth costs, which are effectively zero to serve any one individual but huge in aggregate).
  * A cellular network company is, quite obviously, a network. That means the value of the service increases as the number of customers increases. This produces a powerful virtuous cycle in which new customers increase the value of the network such that it becomes attractive to new marginal customers, further increasing the value of the network for the next set of marginal customers; this “network effect” is the most common driver of the sort of “scalable advantage in customer acquisition costs” that I discussed [in the case of Uber](https://stratechery.com/2017/ubers-new-ceo/), and is a hallmark of Facebook in particular (but also Google and all of the aggregators).
  * Cellular network companies have direct relationships with their customers.

These four characteristics may seem familiar: they are all parts of
[Aggregation Theory](https://stratechery.com/2015/aggregation-theory/), and
I’ve written about each of those components in the two years since I first
wrote about the theory.2 There is one more piece, though, that I have only
mentioned in passing: zero transaction costs. This is the piece that
apparently sets Facebook beyond Senator Warner’s understanding,3 and it is
perhaps the key reason why Facebook and other aggregators are unlike any other
company we have seen before; oh, and it explains this Russian ad buy.

#### Transaction Costs

Go back to the generic cellular network company I discussed above, and think
about what is entailed in adding a new customer (and leaving aside the
marketing expenditure to make them aware of and desirous of the service in the
first place):

  * Talk with the customer on the phone or in person
  * Collect identifying details and run a credit check
  * Provision a SIM card and/or a phone
  * Receive payment
  * Manage contract renewals and cancellations and other customer service

While some of these activities could be automated, the reality is that the
cost of customer management had a linear curve: more customers meant more
costs. Moreover, these costs accumulated, limiting the natural size of any
company; at some point the complexity of managing some finite number of
customers across some finite number of geographic areas cost more than the
marginal profit of adding one more customer, and that limited how big a
company could grow (which, to be clear, could be very large indeed!).

What makes aggregators unique, though, is that thanks to the Internet they
have zero transaction costs: for Google, or Airbnb, or Uber, or Netflix, or
Amazon, or the online travel agents, adding one more customer is as simple as
adding one more row in a database. Everything else is automated, from sign-up
to billing to the delivery of the service in question. This is why all of
these companies are global, often from day one, and, as I explained in [Beyond
Disruption](https://stratechery.com/2015/beyond-disruption/), why they start
at the high end of a market and work their way down.

Note that aggregators can deal with the physical world and still have zero
transaction costs, at least on the consumer side: Airbnb deals with rooms, but
bears no transaction costs when it comes to signing up new customers; Amazon
and Uber are similar with regards to e-commerce and transportation,
respectively. Netflix doesn’t deal in physical goods (beyond its old DVD
business), although it does bear significant transaction costs when it comes
to sourcing content (in addition to actually paying for the content), but when
it comes to customers there are no marginal costs at all.

Facebook and Google, though are a special case: they are (and yes, I know this
is the least imaginative term ever) super-aggregators.

#### Super-Aggregators

What makes Facebook and Google unique is that not only do they have zero
transaction costs when it comes to serving end users, they also have zero
transaction costs when it comes to both suppliers and advertisers.

Start with supply: not only is the vast majority of online content accessible
to Google’s search engine (unsurprisingly, the biggest exception is Facebook),
but in fact that content _wants_ to be discovered by Google. Nearly every site
on the web has a sitemap that is intended not for humans but for web crawlers,
Google’s in particularly, and there is an entire industry dedicated to search
engine optimization (SEO). Netflix is on the opposite side of the spectrum
here (unlike YouTube, it should be noted): the company has to actively source
content and pay for it. Uber and Airbnb and Amazon are in the middle:
theoretically there is an open platform for suppliers but there are costs
involved in bringing them online.

Facebook takes this to another level: its users are its most important content
providers, and they do it for free. Professional content providers aren’t far
behind, not only linking to all of their content but increasingly putting said
content on Facebook directly (to the extent Facebook is paying for content it
is to juice this cycle of self-interested content production on Facebook).

That said, there are a few more companies that have a similar content model:
Twitter, Snapchat, LinkedIn, Yelp, etc. All run on user-generated content
augmented by professional content placing links or original material on their
services. However, there is still one more thing that separates Facebook and
Google from the rest: advertisers.

Super-aggregators not only have zero transaction costs when it comes to users
and content, but also when it comes to making money. This is at the very core
of why Google and Facebook are so much more powerful than any of the other
purely information-centric networks. The vast majority of advertisers on both
networks never deal with a human (and if they do, it’s in customer support
functionality, not sales and account management): they simply use the self-
serve ad products like the one pictured above (or a more comprehensive tool
built on the companies’ self-serve API).

This is the level that the other social networks have not reached: Twitter
grew revenue, but primarily through its sales team, which meant that [costs
increased inline with revenue](https://stratechery.com/2016/googles-earnings-
the-problem-with-alphabet-twitter-earnings-layoffs-vine/); the company never
gained the leverage that comes from having a self-serve ad platform
(specifically, the self-serve platform costs are fixed but the revenue is
marginal).

[![](https://i0.wp.com/stratechery.com/wp-content/uploads/2016/11/Screen-
Shot-2016-11-02-at-7.41.16-PM.png?resize=640%2C381&ssl=1)](https://stratechery.com/2016/googles-
earnings-the-problem-with-alphabet-twitter-earnings-layoffs-vine/)

Snap is following in Twitter’s footsteps: to date the vast majority of the
company’s revenue has come from its sales team; the company has a perfunctory
API for self-serve ads, but most of the volume springs from the aforementioned
deals made by its sales team. Similar stories can be told about [LinkedIn,
Yelp, and other advertising-based
businesses](https://stratechery.com/2016/the-reality-of-missing-out/).

This, then, is a super-aggregator: zero transaction costs not just in terms of
user acquisition, but also supply acquisition, and most importantly, revenue
acquisition, and Google and Facebook are the ultimate examples.

#### Facebook and the Russians

This is why I was confused that Senator Warner made a big deal out of the fact
Facebook was paid in Russian Rubles: the entire premise of the company’s
revenue model is that anyone can run an ad without having to talk to another
human, and obviously a key component of such a model is supporting multiple
currencies.

Again, though, this is the first such model in economic history: it seems I am
the one who was blinded by my having experienced the meaning of scale. In that
Hotmail meeting everyone and everything was reduced to a number on a
spreadsheet: the United States, Japan, Brazil, Russia, all were simply another
row. So I naturally assume it is in the case of Facebook ads: that some
advertisers buy in dollars, some in Yen, some in Real, others in Rubles is
unremarkable to me, and, I suspect, many of the folks working at these
companies.

And yet, it is not at all unrealistic that this be very remarkable to everyone
else, even someone with the technical and business background of Senator
Warner. It would immediately be eyebrow-raising should any of the companies he
managed or was invested in suddenly started transacting in Russian Rubles! For
a super-aggregator, though, it is not only unremarkable, it is the system
working as designed.

This applies to the content of those ads, too: last week, when [ProPublica
reported that Facebook enabled anti-Semitic
targeting](https://www.propublica.org/article/facebook-enabled-advertisers-to-
reach-jew-haters), I told a friend that a similar story would come out about
Google within a week; [it only took one
day](https://www.buzzfeed.com/alexkantrowitz/google-allowed-advertisers-to-
target-jewish-parasite-black). When you make something
[frictionless](https://stratechery.com/2013/friction/) — which is another way
of describing zero transaction costs — it becomes easier to do _everything_ ,
both good and evil.

#### Regulating the Super-Aggregators

This should probably be another article — indeed, it’s an article I’ve been
working towards for a long time now — but this appreciation of what Super-
Aggreagators are, and how it is a Russian propaganda outfit could buy Facebook
ads that likely [broke the
law](https://www.law.cornell.edu/uscode/text/52/30121), gives insight into a
number of principles that should guide people like Senator Warner as they
consider potential regulation:

  * **Don’t Force the Super-Aggregators to Make Editorial Decisions:** It has been distressing to see how quickly some folks have resorted to insisting that Google and Facebook start having a point-of-view on content on their platforms. The problem is not that they might be effective, but rather that it is inevitable that they will be. I wrote in [Manifestos and Monopolies](https://stratechery.com/2017/manifestos-and-monopolies/):  

> My deep-rooted suspicion of Zuckerberg’s manifesto has nothing to do with
> Facebook or Zuckerberg; I suspect that we agree on more political goals than
> not. Rather, my discomfort arises from my strong belief that centralized
> power is both inefficient and dangerous: no one person, or company, can
> figure out optimal solutions for everyone on their own, and history is
> riddled with examples of central planners ostensibly acting with the best of
> intentions — at least in their own minds — resulting in the most horrific of
> consequences; those consequences sometimes take the form of overt costs,
> both economic and humanitarian, and sometimes those costs are foregone
> opportunities and innovations. Usually it’s both.

The best solution in my estimation is enforced neutrality; to the extent
limitations are put in place they should be enforced by another entity with
far more accountability to the people than either of these Super-Aggregators.
That probably means the government (with the obvious caveat that authoritarian
governments would certainly prefer to use Facebook for their own ends).

  * **Focus on Transparency:** The personalization afforded by Super-Aggregators means their advertising is simply not comparable to anything that has come before: television commercials, radio jingles, newspaper ads, all are publicly disseminated and thus can be tracked (the one possible exception is direct mail, which, unsurprisingly, has been the home of the foulest sort of political advertising in particular). Digital ads, on the other hand, can be shown to a designated audience without anyone else knowing. It is worth debating whether this level of secrecy should be allowed in general; it seems without question, [in my mind](https://stratechery.com/2017/amazons-second-headquarters-amazons-internal-primitives-facebook-and-political-ads/), that it should not be allowed for political ads. Of course, that begs the question of what is a political ad, which again points towards regulation (which, per point one, is preferable to the unaccountable Google and Facebook deciding).

  * **Remember the Benefits of Zero Transaction Costs:** The biggest beneficiaries of zero transaction costs on the super-aggregators are not traditional advertisers, whether that be companies like CPG conglomerates or presidential campaigns. Both have the resources to advertise anywhere and everywhere, and indeed, often find that the fine-tooth targeting on super-aggregators isn’t worth the effort required. The folks that do benefit, though, are those that wouldn’t have a voice otherwise: startups and niche offerings, both in terms of business and politics. Google and Facebook have opened the field to far more entrants, and while that means there are more folks with bad intentions, there are also a whole lot more folks with ideas that were shut out by the significant transaction costs inherent in pre-Internet platforms.

There’s one final consideration that should apply to regulation, broadly:
given that Google and Facebook are already well-established with businesses
that serve users, suppliers, and advertisers in a virtuous cycle, it is
unlikely that regulation of any kind will have meaningful effects on their
bottom lines. Indeed, I expect Google and Facebook to be mostly cooperative
with whatever regulation comes from these recent revelations.

Rather, the companies that will be hurt are those seeking to knock Google and
Facebook off their perch; given that they are not yet super-aggregators, they
will not have the feedback loops in place to overcome overly prescriptive
regulation such that they can seriously challenge Google and Facebook.

For example, consider the much-touted [General Data Protection Regulation
(GDPR)](http://www.opentext.com/campaigns/99challenges/comply-with-
regulations-
wp?utm_source=google&utm_medium=ppc&utm_campaign=99-gdpr&utm_content=ppc-99-gdpr-
text&elqcampaignid=27115&gclid=EAIaIQobChMIrrbT892u1gIVSgoqCh3zTweKEAAYASAAEgLaifD_BwE)
set to take effect in the European Union next year. There is lot of excitement
about how this regulation will limit Google and Facebook in particular, by,
for example, limiting the use of personal data and enforcing data portability
(and not just a PDF of your data — services will be required to build API
access for easy export).

The reality, though, is that given that Google and Facebook make most of their
money on their own sites, they will be hurt far less than competitive ad
networks that work across multiple sites; that means that even more digital
advertising money — which will continue to grow, regardless of regulation —
will flow to Google and Facebook. Similarly, given that the data portability
provisions explicitly exclude your social network — exporting your friends
requires explicit approval from your friends — it will be that much harder to
bootstrap a competitor.

This is the reality of regulation: as much as the largest incumbents may moan
and groan, they are, in nearly all cases, the biggest beneficiaries. To be
sure, that doesn’t mean regulation isn’t appropriate — it should be far more
obvious to everyone that Russians were purchasing election-related ads on
Facebook — but rather that it be expressly designed to limit the worst abuses
and enable meaningful competitors, even if they accept payment in Russian
Rubles.
