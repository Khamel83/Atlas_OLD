# Go Corporate or Go Home

**Source**: http://www.ribbonfarm.com/2016/03/17/go-corporate-or-go-home/
**Type**: article
**Created**: 2025-08-13T18:19:30.318853

---

title: Go Corporate or Go Home
source: http://www.ribbonfarm.com/2016/03/17/go-corporate-or-go-home/
date: 2025-08-13T18:19:26.051225
tags: []
---
If you’re in Silicon Valley, you might have missed the trend, but the
percentage of American workers working for big companies has been increasing,
even as corporate bureaucracy is getting more stifling. Strangely, this has
been happening even as the companies issue press releases about being more
flexible and adaptive, to compete with startups, as Paul Graham argues in his
recent controversial essay on
[_Refragmentation_](http://www.paulgraham.com/re.html) _._ But flexible seems
to mean layoffs and reorgs into ever more complex and, yes, fragmented
corporate structures. They aren’t slimming down into flexible startups.

Worse, startups scale into big companies, and transform into bureaucracies
when they do. Harvard Business Review just came out with [some advice on how
to stop being a startup](https://hbr.org/2016/03/start-ups-that-last). Even
_startups_ can’t stay startups. Github, the catalyst for distributed software
companies everywhere, is itself restructuring. As the author of [this
post](http://www.businessinsider.com/github-the-full-inside-story-2016-2) on
Github’s restructuring puts it, “Out with flat org structure based purely on
meritocracy, in with supervisors and middle managers.” But why?

My basic argument is this: the
[legibility](https://www.ribbonfarm.com/2010/07/26/a-big-little-idea-called-
legibility/) that lets companies scale is at odds with the flexible way
typical startups operate. I see two extremes, with flexibility and legibility
on opposite sides — but transitions only happens in one direction. Small
companies give up flexibility and illegibility in exchange for growth. Large
companies with legible structure and inflexibility, on the other hand, are not
typically interested in giving up size and profitability. Meritocracy, a
rallying cry for the Silicon Valley startup mindset, only works when merit can
be seen and rewarded by management. Merit can only be obvious to everyone when
groups are small enough. Once Github passed [Dunbar’s
Number](https://en.wikipedia.org/wiki/Dunbar%27s_number), there was going to
be no way for people to work as one coherent culture — though they grew so
fast they reached double that number before the VCs put in someone to
bureaucratize and let them scale.

To understand why management does this, we need to see them how they see
themselves. And how does the management of an organization represent
structure? Org charts.

**Databases and org charts**

Management structure is its own little world — and the map of management
structure is the org chart. These charts used to be a big deal, but by the
’80s, they had shrunk to simple tree structures. Before I explain why these
are trees, specifically, I’ll try to explain why the organization is getting
simplified, and what the structure of the organization actually looks like.

[The pace of change is one
explanation](https://www.ribbonfarm.com/2015/05/28/the-amazing-shrinking-org-
chart/), but I think a simpler one suffices: databases now store org charts.
If you store the org chart in a database, the database _becomes_ the org
chart. And while databases can store arbitrary data like images, they store
graph relationships really easily — which means that the storage technology,
databases, actually dictates the structure of the company.

In other words, _the medium is the message!_

But the relationships stored in these databases need not only be relationships
between people. Big bureaucratic companies connect employees to managers in an
org chart, but also have big contracts with SAP, or other enterprise resource
planning (ERP) software vendors. The ERP databases do a lot more than just
store org charts, they map the entire system. Good supply chain managers have
maps representing each input, source, and vulnerability for their business
processes.

Maps are great at increasing legibility, but once they dictate the territory,
you have the [‘Authoritarian High-Modernist Recipe for
Failure.’](https://www.ribbonfarm.com/2010/07/26/a-big-little-idea-called-
legibility/) Unlike social systems, managing a business is a case where
imposing structure is probably a good idea. If managers don’t dictate
structure, they are trying to manage a system that they haven’t made legible,
even to themselves!

It’s much easier to manage this map with ERP systems, which store both HR
data, and connect products to business lines, workers to the products they
make and sell, and so on. These SQL databases, with their structured indexes
and ids, allow managers to generate the reports they need — on profit per
vendor, revenue per employee, or almost any other metric they might use.

When companies need to change, there are predefined stored procedures in the
database for hiring, firing, or even reorganizing — as long as the database
structure itself doesn’t change too much. It is true that the pace of change
makes the exact details of the chart less stable, but, like [the beautiful org
charts of old](https://ribbonfarm.wpenginepowered.com/wp-
content/uploads/2015/01/orgchart-full.jpg), these structures are legible —
they can lend insight to management, because the structure of the database is
clear. Sure, switching from simple management to region-based matrix
management to job-type matrix management requires some heavy lifting, but
still fits within the structure — [SAP has you
covered](http://help.sap.com/saphelp_erp60_sp/helpdata/en/bb/bdbe65575911d189240000e8323d3a/content.htm).
And that’s what matters — a system legible enough to let your ERP optimize
your business process. Walmart need to be really efficient at doing its single
job, selling products that it buys cheaply, at scale. Adapting might be hard,
but the efficiency of having clear reports and being able to optimize revenue
per employee is worth it.

Some “Big Data” startups offer services extracting insight from other
companies’ data, but odds are good they don’t collect their own. The big
companies have legible, normalized datasets. And the legible data needs
analysis once it gets larger than a person can fit inside their[ tiny 7+/- 2
item](http://psychclassics.yorku.ca/Miller/) brains.

What about the startups, though? [With apologies to Paul
Simon](http://www.paulsimon.com/track/kodachrome-7/);

> When I think back  
>  on all the crap I learned in B-School,  
>  it’s a wonder  
>  I run startups at all.  
>  And the lack of legibility  
>  hasn’t hurt me none,  
>  ’cause I scribble diagrams on the wall.

Startups can’t afford contracts with ERP vendors. That’s good! They _need_ to
be much less structured. Rigid structure doesn’t allow for rapid pivoting, but
scribbling on the wall does. The pivoting that startups go through lets them
find a niche and build a culture that demands investment into new, risky, and
possibly profitable ideas. They thrive on the flexibility that illegible
structures permit.

So how do they manage to manage? I suppose startups could use agile NoSQL data
stores, which can fit their arbitrary changes pretty easily, but to be honest,
only an old-school MBA would want them to write down their org chart at all.
If data describing the organization is small enough, it doesn’t need to be
legible to be understood — and companies start tiny. Github is big and
impressive. [Logical Awesome](http://logicalawesome.com/) was tiny and quirky.
The founders probably sat in the same garage. Want three managers for your
first employee, and none for the second? Not a problem! Silicon Valley is fine
with polygamanagement, to coin a [malamanteau](https://xkcd.com/739/). But at
some point, [they stop pivoting](https://github.com/blog/589-new-year-new-
company). The “flat org structure based purely on meritocracy” at github
wasn’t just a design, it was also a default. It’s a natural default, well-
suited to startups, because the flexibility of illegibility is fantastic.

Flexible meritocracy is easy when you can shift people around as soon as you
see they are ready without needing to rely on metrics identifying top
performers, or wait for yearly performance reviews and promotion cycles. But
this changes as a company grows — probably around the time that management
notices it doesn’t know who everyone is. This is inevitable [even when they
say they are “acting like a startup”](http://qz.com/618451/to-be-like-
american-airlines-ceo-think-like-a-startup-and-avoid-business-dinners/). If
all an employee needs to do in a “large and complex organization” to be
recognized is “ show up and do your job,” as the CEO of American Airlines
claims, then management is admitting they value legibility over flexibility.

It is possible to have illegible relationships throughout large companies, but
then the companies are harder to manage, no more flexible, and impossible to
optimize. Big businesses can’t be unstructured. If they try, they end up
neither legible nor flexible. How do you store the org chart data if the
relationships are unclear? NoSQL is excellent if you’re a graph theorist
working with large datasets, grateful for a structure you can work with — but
a manager at a big firm would recoil in horror if they were told that there
was no way to find billed-hours-to-product-sales for their division. They need
that legibility to decide which division to lay off, so they can be more
flexible!

**Culture and Social Graphs**

So far, I’ve been explaining organizational structure as if though all that
matters is that it is the territory of management. In fact, the true structure
of a large company exists on three intertwined but conceptually distinct
levels, and all of them matter.

First, and most legible, are official _chains of command_ , which are the
territories corresponding to org charts (well, they would be if the latter
were kept updated), and are what we’ve been implicitly discussing so far.
These exist in legible databases with clear, 1-to-many manager-to-employee
relationships, allowing no ambiguity or complexity. They are trees, and if you
keep them pruned and streamlined, they slowly grow and bear reliable crops, in
the form of steady ROE.

Second are the _business processes_ , which rely on less formal networks.
These can also be stored in a database as business process diagrams. Even if
codified, they are much less legible, simply because the processes that exist
in a business are not always linear, and most people are part of various
different processes. If we have the process structure in a database, even if
it’s up to date, it wouldn’t be obvious how to normalize it cleanly. Still,
these maps can be captured, and probably shift only at clearly defined times.
It’s a messy graph at best — not a tree but a rapidly growing thicket full of
independent vines, bushes, and weeds. On the other hand, [this thicket is
where the real work gets done,
organically](http://www.jstor.org/stable/1930168). If the work isn’t easily
defined, these networks need to be more flexible than the org chart. That
means that, outside of a few slowly changing sectors, like insurance,
shipping, or retail, companies won’t even be able to follow [the advice to
manage along these rapidly shifting, illegible
lines](https://hbr.org/2010/06/the-decision-driven-organization).

Third is the _culture_ , built of personal relationships, reflecting the
social graph connecting employees themselves. Unlike the first two, it is not
an imposed structure, or a response to business needs, but an emergent
network, and a loosely defined culture — and this is much less legible, and
definitely isn’t captured anywhere. It’s dynamic, messy, and doesn’t allow for
clear structure. While the chain of command reflects patterns of
responsibility, and informal networks reflect processes, social graphs reflect
moods and chance encounters. They also include [weak
ties,](https://sociology.stanford.edu/sites/default/files/publications/the_strength_of_weak_ties_and_exch_w-
gans.pdf) which means that the structure of the social graph can shift over
time in unpredictable ways.

No one other than a researcher would even consider trying to represent the
constantly shifting culture — and even researchers would be better off
extracting it from employees’ texting and social media relationships than
asking the company about it. Instead of passively illegible like a business
process, personal relationships can be actively cryptic — specifically not
public, or weak enough [to fail under the stress of
definition](https://xkcd.com/355/).

Despite their impermanence and illegibility, cultures matter. Good ones make
companies more resilient, more sociable, and increase retention and
satisfaction. If the gods of “Company Culture” are appeased with the right mix
of bonuses and flextime, they may even magically help with things shareholders
care about, like worker productivity and profits. But this happens only
because the first two levels exist as well, providing a habitat. Culture is
co-extensive with the ecosystem created by the first two levels of the
organization structure — the chain of command and business processes. But
rather than being part of the structure of the ecosystem, it is better
understood as the activity within it.

Iain M. Banks’ “Culture” series, in part, explores a society without the first
two levels. There is no central anything, and everyone does whatever they
want. But in such a culture work is voluntary, and rare.

The smaller a company is, the less they need to formalize anything, and the
less the three levels — chain of command, business process, and culture —
differ. At small scale, you don’t want to formalize. Founders hold the whole
thing in their head, and manage everything. If hierarchy exists at all, clear
lines of reporting are secondary to the business process. The cryptic social
network is obvious to everyone involved, since everyone is already well
connected. When a startup is still exploring how it will make money, it can
(and must) pivot occasionally, changing the business completely. The loose
structure allows it to do so without reorganizing any explicit structures, and
the illegible social graph adapts without noticing. Flat unstructured
meritocracy works!

Unfortunately, as I noted earlier, this doesn’t scale. If we tried, it would
look, at best, like a high school’s social scene. You’d see cliques,
relationships that form and dissolve rapidly, and little if any productive
work being done, at least by the majority of the students. Startups can hobble
along for a while, growing increasingly illegible and messy, especially if
given the prospect of a huge payout. You just have to hope that the chaotic
emergent social patterns are stable enough so the cheerleaders can keep the
football team away from the basketball team long enough for each to play their
big games this weekend.

To extend the brief digression into what a startup would look like if we
scaled it without adding structure, let’s explore the high school metaphor a
bit more deeply.

#### **High Schools, Sex, and Database Design**

As noted earlier, only a researcher would try to map a social graph.

A research team interested in the spread of STDs went around a high school and
managed to interview 83% of the students, then graphed all the admitted sexual
partners that the 573 sexually active students (confidentially) claimed to
have with other students (40% of the total number of claimed sexual
relationships) over 18 months. They published [a paper
](http://www.soc.duke.edu/~jmoody77/chains.pdf)with the observed social
network graphs; .

The graphs show a single aspect of the messy social network of adolescents. As
with all attempts to map our dynamic third level, it’s incomplete. For
example, I’m guessing not everyone was honest. And other than two seemingly
bisexual girls, (can you find them on the chart?) no one at the school is
admitting to a homosexual relationship — and that’s probably something you’d
care about when studying AIDS. The territory is very different than the map as
initially imagined, or even than the one discovered by this study. And the map
was supposed to be used for modeling and predicting the spread of STDs.

Epidemiologists like the simplicity of [compartmental
models](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology) —
they are fantastic as long as the populations modeled are homogenous in the
right ways. But the dynamics of STDs among homosexuals, sex workers, and the
social graph of these high school students didn’t simplify the way that models
assume. (For epidemiology geeks and graph theorists, the mixing graph is
probably closer to
[Barabási–Albert](https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model)
than[
Erdős–Rényi](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model).)
But why was their mental model wrong? As a first guess, they were used to
legible patterns that they and their peers form, not the incoherent and
unstable ones that emerge from, say, letting adolescents loose in a high
school.

I’ll use database structures to illustrate what assumptions went wrong, and
then we can try to use the insight to improve our understanding of social and
corporate structure — though the example is much more widely interesting, as
well.

Most people, I suspect, have an implicit, mental model that considers a
relationship an attribute of a person; Person A has attributes height, weight,
interests, job, salary, gender, partner status, etc. This model is sufficient
for some purposes, but not for representing relationships. Here, I’ll use the
insight of someone much more skilled at building database structure, stealing
/ adapting the well-constructed example that
[www.twitter.com/qntm](http://www.twitter.com/qntm) wrote about [how a
database administrator (DBA) reconstructs a database to include gay
marriage](http://www.qntm.org/gay) — brilliantly labeled the Y2Gay problem.
This will refactor the mental map of the territory indirectly, by looking at
how to [refactor the database
structure](https://en.wikipedia.org/wiki/Database_refactoring) used to store
the map.

To start, we have separate tables to store men and women, with links to the
corresponding entry in the other table to represent relationships. This means
the “partner” entry is restricted to referencing someone of the opposite
gender. (“Gender” obviously used to be considered a binary variable, too — but
that’s not our point here.) the partner entry might be flagged as either
“dating” or “married.” Sometime, probably in the mid-20th century, people
shifted mental models. They kept everyone in a single table, with both men and
women listed, and a gender.

Relationships are no longer a link between two different tables, with
different categories of humans — it’s just a link by each person to another.
If we want to preserve “traditional marriage,” (as _The Mythical Man Month_
[explains](https://twitter.com/qntm/status/699955110026350592),) it requires
having male people marry female people. How do we do that? Instead of
requiring a “partner” entry in the opposite gender table, it requires the
partner from the people table be restricted to the opposite gender. When gay
marriage began to be discussed, the model could simply remove the restriction
that the partner needs to be of the opposite gender. At first, they required a
flag for “civil union” instead of “married,” but it’s a crude hack, and people
moved on. Voilà, we have gay marriage! (Interestingly, in many ways, accepting
more fluid gender identities, and gay marriage, is partly a consequence of
changing mental models to treat women as people.)

Our change so far is a minor refactoring. Sure, it tells us that marriage can
be conceptualized as between two people, instead of a man and a wife. It even
helps clarifying that women are people too. (Yes, they can even have
attributes like those men have, like jobs, or ambition!) This is a more or
less acceptable database structure for representing most people, and most long
term relationships — because they are pretty legible already. It’s still not
enough to help our epidemiologists, or enough to explain the problems with
startups scaling. High schoolers, like those in our study, are more
complicated. Obviously we need a more flexible, less legible structure to let
us represent and understand their relationships.

For a simple example of why our current structure is incomplete, how do we
represent ex-partners? Obviously, it matters for a high schooler — sleeping
with your friend’s ex is creating an ex-friend. Who you used to sleep with is
an even more critical part of the picture for an STD epidemiologist. To track
this, do we need a column for relationship 1..n, each of which has a partner,
and a start/end date? A DBA will quickly notice that this doesn’t scale well,
and keeping these entries updated and consistent is a nightmare; you could
have unconsummated marriages, or accidental polygamy, where, because of a
badly performed marriage registry update, multiple people are married to the
same person. (And how to we decide who pays child support?)

Instead, we can be more radical in refactoring our mental model, and the
equivalent, better [normalized
database](https://en.wikipedia.org/wiki/Database_normalization) model: we can
treat a relationship as independent of the people, and use a new table with
attributes that include which people are in it. The new table has two entries
for each relationship, one for each participant, as well as a start date, an
end date, and a type — so we can include fiancés, marriages, and even one-
night flings using the same structure. We now only enforce a simple rule to
limit people to one relationship at a time.

But why stop there? Now that we replaced the 1–1 relationship of males <->
females with a decently normalized table structure, why wouldn’t we go all the
way to letting relationships have arbitrary structures? If you’re interested
in STD transmission, you need to be able to represent what happens; a still-
limited database structure is hardly a reason to object. How do we fix it?

We remove the requirement that each relationship be exclusive, or limited to
two people. The new, more expansive model works well for showing the high
school network, easier to use and keep updated, and much better than the
planar graphs of a small slice of time that the researchers created. As the
original Y2Gay essay concludes, the new model extends all the way to graph-
theory, with arbitrarily complex directed nodes. [Any graph, in the
mathematical
sense](https://en.wikipedia.org/wiki/Graph_%28discrete_mathematics%29), can be
represented. This allows a much better model of how people actually have
cohabited, and not just in high schools; [group
marriages](https://en.wikipedia.org/wiki/Oneida_Community), [Heinlein-esque
line
marriages](https://en.wikipedia.org/wiki/The_Moon_Is_a_Harsh_Mistress#Politics_and_society),
and the vast
[panoply](http://onlinelibrary.wiley.com/doi/10.1525/aa.1907.9.4.02a00080/abstract)
of [similar structures](https://en.wikipedia.org/wiki/Cicisbeo) from
[history](https://en.wikipedia.org/wiki/Bloomsbury_Group#Rejection_of_bourgeois_habits).

Putting all these changes together, we can specify a legible database — but we
end up able to represent illegible social networks. It can represent any type
of actual relationship, but it can represent arbitrarily complex, implausible
structures just as easily. I’m sure there’s someone in the polyamory
subculture of Silicon Valley with a PhD in network theory who’s mapping out
cool untried graphical structures, since the number of graphs explodes pretty
quickly, but the central question isn’t about the graph — it’s what people
want, or do, and how adaptive these structures are. What I’ll call [pivot
culture](https://en.wikipedia.org/wiki/Hookup_culture), which exists in high
schools and colleges, doesn’t want or need legibility. But if you’re a lawyer,
you need to know who inherits, who pays child support, and who gets hospital
visitation rights. Tradeoffs exist between legibility and the freedom of
arbitrary structure — so it’s a good thing for lawyers that as people grow up,
they decide on more legible relationships.

As an aside, a question that initially bothered me about polyamory was: why
isn’t polyamory more widespread, especially among people who aren’t religious
or traditional? Yes, there are some scale limits. At the very least, there is
a tradeoff between the frequency you can see someone and the number of people
involved, but I’m sure there are people who would be happy to juggle 5 or 10
partners. Why isn’t it more common? Why don’t adults keep pivoting, and why is
polygamy now relatively rare? Traditional marriage was a good tradeoff for
social designers who wanted legible structures, but it’s less obvious why it’s
useful for the people. Given that, it’s confusing why so many people nowadays
think there is a single “correct” family structure.

I’ll leave that as a question for now, because it should answer itself later,
once we figure out why companies don’t stay agile as they scale. The parallel
to companies, though, is clear; what social structures work, for what
purposes, and why? In order to answer this question, we can refactor companies
the way we refactored relationships. Seeing where this works, or doesn’t work,
will finally address the question of why org charts are trees instead of some
other structure, and answer the original question of why startups need to go
corporate or go home.

#### **Legibility happens**

Startups typically find a useful business model by starting with an idea,
raising cash, then pivoting until they succeed, or fail. If a startup is
successful, it starts generating some free cash flow, then gathers enough
profit or bamboozles a high enough valuation to buy Time Warner — or get
bought by them. Either way, it forms a small part of the Silicon Valley circle
of life. I’d call it the standard Silicon Valley model — but as you’re
anticipating, it’s a bit self-defeating; once you succeed, you no longer need
to pivot.

Observers will notice that any company successful enough to buy or be bought
either has gone corporate, or starts tripping over its unmanageable structure,
and needs to fix it, or they might as well go home. For these less well-run,
less ambitious, or less lucky companies, they fizzle and stay small, or go
bankrupt, and the circle of life continues. In either direction, it leads a
bit further towards consolidation, not decentralization.

Flat meritocracies are awesome. Can’t an emergent startup culture, full of
collaboration and creativity, allow companies to succeed without turning into
corporate bureaucracies? To phrase this differently, Peter Pan has more fun,
and startups don’t want to grow up. Can’t kids stay kids, and be successful
too?

No. This is where the social graph becomes critical. The number of possible
social graphs explodes very quickly; 7 people have only 156 possible
configurations, 10 have over a quarter million, and by the time you get to 15
people, the [quadrillions of possible structures](https://oeis.org/A000088) is
clearly unmanageable. This means that decision makers can’t understand the
impacts of their decisions. Hiring people becomes a mess, since the only way
to scale anything is to disrupt this chaotic network. Firing people, or even
reassigning them, is worse — it may be removing a key piece of some process a
manager, or even the employee, doesn’t notice.

What is the alternative? Simple, legible org charts. (Preferably trees, which
are really simple — and I’ll explain why
[trees](https://en.wikipedia.org/wiki/Tree_%28data_structure%29) are so simple
soon.) Simple structures means that decision makers understand the impacts of
their decisions.

#### **Refactoring Bureaucracy**

We now have laid out some extremes, and pointed out why startup companies
inevitably move towards illegibility when they stay organic. If they succeed,
it’s because they manage to move from less legible, organic towards corporate.
On the other hand, they can fail in many ways; they can fail to become legible
when they try to go corporate, and wreck the business doing so, or they can
stay organic by failing to impose enough order to enable growth.

Successful startups generally move from organic and legible towards organic an
illegible as they grow, but if they don’t halt the process and impose
legibility, they fail. How is this done? The [recent piece at
HBR](https://hbr.org/2016/03/start-ups-that-last) that I mentioned at the
outset does a great job outlining some strategies. If you’re only interested
in scaling a startup, the article is a great place to start, but we can think
a bit more about the theory, and how this occurs. There is some more theory I
think we can expose here, and I will finally explain why org charts need to be
trees.

#### **Graph Theory and Org Charts**

The company types in our earlier 2×2 correspond to certain types of org charts
— or, in the mathematical sense, graphs. To consider the theoretical
possibilities for structuring a company, we can look at what graph structures
are possible, and what they correspond to in terms of companies. Here’s a
picture to get us started, which uses different, albeit related, axes:

If you don’t know the terminology, don’t worry. The things we care about are
mostly visible in the chart, or are about size. The only other thing that
matters for us is sparsity, which is just a fancy way of saying a graph has
relatively few links between nodes.

We can put many of the types of graphs from the zoo into an analogue of our
2×2, then step through and explain which are useful for companies.

In the top-right quadrant, we start with very small graphs. These are somewhat
legible no matter what the structure is — as we mentioned above, early stage
startups don’t have structural constraints. Sparse, [scale-free
networks](https://en.wikipedia.org/wiki/Scale-free_network) are also organic
and legible even at a somewhat larger size. A healthy startup turns into one
as it begins to grow, on the way to getting larger and less sparse. This
continues to work at a larger size, up to around Dunbar’s Number, when the
company’s organization is sparse — employees don’t need to communicate much
across areas. Making org structures less sparse helps with communication as
size increase, but it overloads people with too much communication and
management responsibility.

Next, in the bottom-right quadrant, we have larger scale-free networks. (“SF-
like” in the earlier image). These have legible structure but are organic
instead of imposed. I suspect this is the structure of many open source
projects. We already mentioned that communication overload makes this stop
working if not sparse. If they are sparse enough to allow people to work, they
would be interesting as organizational structures, but not as management
structures, because they don’t allow central control. This failing makes them
anti-corporate, and also probably makes them hard to optimize when you need
profitability.

Moving to the bottom-left quadrant, other types of large sparse graphs, ones
that are connected artificially, like modular [ER-
Graphs](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model),
are unhelpful for all the previously applicable reasons: communication is
hard, there is no coherent leadership, and optimization isn’t possible — you’d
only consider them if you care more about network resiliency than efficiency.
They might be useful for[ terrorist
cells](http://www.tandfonline.com/doi/abs/10.1080/09700160408450119), but
that’s about it.

In the top-left quadrant, before we arrive at trees, we do have another
legible, imposed structure. Fully connected graphs are fantastic for
communication — everyone talks to everyone else. Unfortunately they are not
sparse enough for sanity; everyone needs to be aware of everything else. We
already mentioned that it can’t scale as a management paradigm, due to
cognitive overload on the part of managers, and Dunbar’s number. (Modern
communications allows us to get some of the benefits of connection without the
overload, at the social network level. Nowadays, anyone can email the CEO, and
it probably isn’t even filtered by their secretary. Despite this, we don’t
expect management to happen this way, even if it does make the social graph
potentially well connected.)

As we stated earlier, most big companies use tree structures. Now we can
suggest a first reason why — most alternatives are unappealing. Slight
variations on the theme, however, might be a bit more helpful. We’ll mention
them, after a more mathematical detour that further explains why trees are so
great.

#### **Computational Complexity of Organizations**

This gets even more technical, and you can skip this section, but if you have
some familiarity with computational complexity theory…

What’s the [computational
complexity](https://en.wikipedia.org/wiki/Computational_complexity_theory) of
most operations on a tree? In computer science terms, it’s O(Log n) — or in
lay terms, ‘not too bad’. Your system still gets slower with scale, but it’s
logarithmic, so it can grow without grinding to a halt. Other structures (like
lists) might be faster for insertion and deletion, but searching is slower,
and we need to do communicate a lot more than we need to change the org
structure. Communication can be loglinear with the size of a system, at least
as long as your network is a tree.

Why? Legibility is related to ease of communication: if something is legible,
you can see where to go and what to do. Every time you need to ask about item
X for product Y, you need to find the person in charge of it. But on an
arbitrary graph, that’s O(n) or worse. When you need to look at incidence
matrices, to know who works with the person you need, since, say, they are out
of the office, it’s really bad, O(n · v) — so the less legible the
organization is, the harder it is to be resilient. And if you need to
optimize, forget it — it’s tree-searches versus traveling salesman problems.

#### **Legibility for Large Structures**

We know large bureaucracies are almost always essentially tree-like. They can
alter their structure slightly, but not radically simplify. Given this, we
would still like to know which variations of treelike structures are useful.
Using the theory developed, I’ll describe two of them, and note the graphs
that describe them. Of course, both of these are relatively legible and
treelike primary structures, and they are never going to allow for unlimited
flexibility — they only change the trade-off between robustness and ease of
optimization.

First, matrix management lays a slightly less legible layer higher up in the
tree. The trade-off allows a bit more flexibility at the top, at the cost of a
bit of legibility there. This moves a bit closer to a hierarchical modular
structure at the top, trading legibility for those lower down for more
connected structure, so that the organization is more fully connected at the
upper levels. This means senior managers can all work together as a team, even
while those lower down are still stovepiped.

Second, they can create modularity ([which is found in social
systems](http://www.pnas.org/content/99/12/7821.short)) throughout the tree,
making it more connected within each area. This trade-off allows a bit more
robustness in exchange for a loss in legibility for senior managers. This
allows some flexibility in the internal management structures lower down, even
if it decreases legibility, making it harder for other parts of the business
to work with them.

#### **Legibility for Growth**

OK, big organizations will be more efficient if they are tree-like. This
limits the endpoints, but there are still many possibilities for getting
there. It’s worthwhile to explain how scaling might happen well or badly, and
review the process we’ve been discussing from the beginning using the new
terminology.

Startups are illegible, with essentially random graphs. This is good for
flexibility, and allows meritocracy. The nodes will not be interchangeable,
but they are dictated by contingent needs, not structure. You can’t fire the
receptionist, he’s the only one who knows how to keep the email server
running. Also, no-one else knows how payroll works. The company is flexible,
but not scalable. Then the company grows anyways, and that is good for
investors, but it is bad for management, which starts imposing structure, or
losing control.

As a company scales up a bit, if it wants to be efficient, jobs and
responsibilities are shifted around and rationalized. Now the company is
partially structured by task or goal, but with a sparse, scale free graph with
a high degree of connection and interdependencies between business units.
These are not legible, but that’s not too big a deal until the company
continues growing. You need someone managing different parts of the company,
since it’s now too big to have a single omniscient CEO.

If growth continues without a full overhaul, managers will end up with unclear
areas of responsibility, and no way to evaluate or understand the tasks of
employees. And you can’t have a meritocracy if you can’t evaluate merit. The
company needs to increase legibility.

We’ve explained that a tree is a fairly unique structure for legibility at
scale, given our problem constraints. That’s why we see typical corporate
structures, instead of varieties, and why startups all face similar scaling
problems. Companies will find that other structures, say, for business
processes, face a different set of tradeoffs. Not using trees can make more
sense when legibility is less critical. That doesn’t mean trees are always
optimal even for organizational structure, but it’s at least a good default —
and defaults are always more legible, if only because of their familiarity.
(This also finally answers the questions about polyamory; typical structures
are comfortable, and the simplest structure that allows for a relationship is
a dyad.)

#### Variations on a Theme

Growing startups probably would prefer to modify the emergent structure
instead of allowing it to grow unmanageably, or completely replacing it. There
are better and worse ways to do this.

A seemingly plausible but bad strategy is worth dismissing; simply actively
limiting connections between various areas of a business. This will succeed in
reducing connectivity, by leaving only small, emergent subgraphs that are
unstructured. This solves one problem, because the company stays sparsely
connected overall, and local legibility stays high by making each segment
small enough not to need much structure. That helps keep things a bit clearer
for management, and it’s known as stove-piping: it makes companies especially
inflexible, and everyone despises it.

What is the alternative to stovepiping? A switch to a typical bureaucratic
tree-building mode. And that’s what we saw with _Github._ As the earlier
article explained,_“_ Out with flat org structure based purely on meritocracy,
in with supervisors and middle managers.” And this is exactly what the HBR
article [advises](https://hbr.org/2016/03/start-ups-that-last); “firms must…
_add management structures_ to accommodate increased head count while
maintaining informal ties across the organization.”

#### **Conclusion**

So now I can repeat myself a bit more, and answer my original question
succinctly why don’t companies stay flexible? It’s a necessary result of
scaling up and the need for legibility to optimize large systems. We’d love to
have flexibility, but the cost is scale, integration, and profitability. For a
startup to succeed, it needs to get past the phase where it can be fluid. This
isn’t, of course, an iron law — but it’s a reason that we’re not seeing tech
visionaries extrapolations borne out in the wider economy. The math of
complexity isn’t changing, and humans have cognitive limits. That means we
need to accept that growth of companies post-startup phase will not be
exponential, nor even linear, but logarithmic — scaling along with the
legibility of a tree.
