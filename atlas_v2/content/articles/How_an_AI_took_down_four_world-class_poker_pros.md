# How an AI took down four world-class poker pros

**Source**: https://www.engadget.com/2017/02/10/libratus-ai-poker-winner/
**Type**: article
**Created**: 2025-08-13T17:33:36.587534

---

title: How an AI took down four world-class poker pros
source: https://www.engadget.com/2017/02/10/libratus-ai-poker-winner/
date: 2025-08-13T17:33:34.710296
tags: []
---
"That was anticlimactic," Jason Les said with a smirk, getting up from his
seat. Unlike nearly everyone else in Pittsburgh's Rivers Casino, Les had just
played his last few hands against an artificially intelligent opponent on a
computer screen. After his fellow players -- Daniel McAulay next to him and
Jimmy Chou and Dong Kim in an office upstairs -- eventually did the same, they
started to commiserate. The consensus: That AI was one hell of a player.

The four of them had spent the last 20 days playing 120,000 hands of heads-up,
no-limit Texas Hold'em against an artificial intelligence called Libratus
created by researchers at Carnegie Mellon University. At stake: a total pot of
$200,000 and, on some level, the pride of the human race. A similar scene had
unfolded two years prior when Les, Kim and two other players decisively laid
the smackdown on another AI called Claudico. The players hoped to put on a
repeat performance, finish up the event January 30th, and ride the rush of
endorphins until they got home and resumed their usual games of online poker.

The fight [wasn't even close](https://www.engadget.com/2017-01-31-libratus-
the-poker-playing-ai-destroyed-its-four-human-rivals.html). All told, Libratus
won by more than 1.7 million (virtual) dollars, and — just like that — the
second [Brains vs. AI
competition](https://www.riverscasino.com/pittsburgh/BrainsVsAI/) came to a
close. To understand what these players were up against and what makes
Libratus work, let's go back to a time before all hope of victory was lost.

### Men vs. machine

For the four men playing against Libratus, victory didn't always seem
impossible. The AI was in the lead from the get-go, building an impressive
streak of wins for the first three days. Then came the counter-attack. Day
four saw the gap narrow $40,000, and a string of successes on day six brought
the humans to within $50,000 of the lead.

_Jason Les and Daniel McAulay in the final stretch of the competition._

"In the start here, we lost the first day," Les explained. "Whatever -- not a
big deal. And then we were losing, but then we fought back up to nearly equal.
We were feeling really confident! We know how to play, we're going to be able
to win."

On the night after the sixth day of competition, the humans did what they did
every other night: sift through the Libratus hand data provided to them by CMU
in hopes of devising a winning strategy. With spirits high after a big day,
they decided on a seemingly crazy strategy: three-betting on every hand that
came along.

Three-betting, for the uninitiated, is poker slang for reraising on a hand.
When you decide to play a hand in a situation like this, paying the blinds is
the first bet. If you're confident in your cards, you raise — that's the
second bet. Generally, when you reraise — the third bet — you're pretty sure
you've got the exchange in the bag. Based on their understanding of Libratus'
play style, the humans thought they could knock if off balance by playing this
aggressively for a while. It backfired.

"We applied this crazy strategy we would never do online," Kim explained.
"Basically, we reraised all of our hands. All of us went in, like, 'Let's just
try this, let's go crazy.'"

"We had a reason to believe that specific size-three-bet was going to work
well against the AI," Les added. "We just fired off all day doing that."

Les and Kim concede that they just got unlucky, too, but either way: Libratus
was unfazed by their plan and started demolishing them. "It just kept
improving every single day, and we started going backwards and backwards," Les
said. In fairness, the humans weren't playing with their usual setups. The
four competitors are almost exclusively online poker pros, and when duking it
out at virtual tables at home, they always have their HUDs handy. These heads-
up displays are filled with stats and probabilities that help online players
make the best moves. Their absence here in Pittsburgh was noticeable.

"Without the HUD, without the numbers, you don't know if you're being paranoid
or not," Daniel McAulay said, leaning back in his chair after winning a hand.
"Is it folding less? We were never sure. We would always say the same thing to
each other: 'Just play it out until we get home and we'd see the sample of
hands and then we'll change the plan. But that cost us a lot of money. A lot
of money."

Those losses would only continue to mount.

### Building the beast

One of the men responsible for the players' anguish can usually be found in
his ninth-floor office, overlooking Carnegie Mellon University's snow-flecked
quad. Professor [Tuomas Sandholm](http://www.cs.cmu.edu/~sandholm/) might live
a second life as a startup entrepreneur, but he has spent years trying to
perfect the algorithms that make Libratus such a potent player. It wasn't out
of any particular love for the game -- Sandholm admits he's no poker pro --
but he was fascinated by the thought of complex computer systems that make
decisions better than we can. That fixation led him to co-create Claudico (the
earlier AI that the humans trounced) with pHD student [Noam
Brown](http://www.cs.cmu.edu/~noamb/), and it led the two of them to try again
with Libratus.

To think of Libratus as just a poker-playing champ is to sorely underestimate
it. Instead, Sandholm says, it's a more general set of algorithms meant to
tackle any information-imperfect situation. Confused? Don't be. Broadly
speaking, the term just describes any situation in which two or more parties
don't have the same information. Something unlike, say, chess, where the
entirety of the game's world is splayed out on the board in front of players.
Those players can figure out exactly what's going on and, assuming they have
decent memories, draw on their understanding of the events that led them
there. This is a perfect information game.

No-limit Texas Hold'em is different. You don't know which cards your opponent
has, your opponent doesn't know which cards you have, and those minutes
playing a hand to its conclusion are spent trying to make the smartest moves
possible with a shortage of intel. And unlike the limit variant, where there's
a cap on how big your bets can be, no-limit gives you the freedom to bet
whatever you want. There's so much information a person — or an AI — can infer
about an opponent's strategy based on their bets that it's no wonder
researchers have been trying to crack the game.

"Heads-up, no-limit Texas Hold'em poker has emerged as the leading benchmark
for measuring the quality of these general purpose algorithms in the AI
community," Sandholm told me.

With that in mind, Sandholm and Brown jointly built Libratus from three major
components. The first is an algorithm that devises overall strategies based on
Nash equilibria. In other words, Libratus spent a total of 15 million
computing hours chewing on the rules of the game before the competition,
finding rational ways to act when both players are making the best possible
moves with the information available. Thanks to a new logic model developed by
the two researchers to minimize Libratus' "regret," the AI could solve larger
abstractions of the game faster and with higher accuracy than before.

The second is what Sandholm calls the end-game solver. This is the part that
players actually faced during their 20 days of combat. Unsurprisingly, too,
this is where Sandholm says most innovative breakthroughs have happened.
Essentially, this allowed Libratus to cook up an approach based on the first
two cards it was dealt, and modify that approach based on its opponent's
actions and the river and flop that are dealt. Sandholm says Libratus was also
designed to keep tabs on how safe its options are. Let's say a human player
screws up and loses $372. That money is viewed as a gift of sorts, so the AI
can freely lose up to $372 and still remain ahead.

"That gives us more flexibility for optimizing our strategies while still
being safe," Sandholm explained.

We'll get to the last key component a little later. In any case, the sheer
number of complex calculations meant Libratus couldn't run on the desktop in
Sandholm's office. If nothing else, the human players can take solace in the
fact that it took a supercomputer and millions of computing hours to beat
them. If you thought _Go_ was tough to wrap your head around, consider the
complexity of no-limit Texas Hold'em: When you're dealt into a game, the hands
you're dealt and the communal cards that appear are one possibility of 10^160.

"That's one followed by 160 zeroes," said Sandholm. "That's more than the
number of atoms in the universe. You cannot just brute-force your way through
it." Still, it takes some degree of brute force to build as close to optimal a
strategy as possible. That's where "Bridges" comes in.

If Libratus is the brain of the operation, Bridges -- a supercomputer made of
hundreds of nodes in the basement of the [Pittsburgh Supercomputing
Center](https://www.psc.edu/) \-- is most definitely the brawn.

"Libratus is running on about 600 nodes at Bridges, out of 846 total compute
nodes," said [Nick Nystrom](https://www.psc.edu/), senior director of research
at the Pittsburgh Supercomputing Center. Most of those 800+ nodes have two
CPUs, each with 28 computing cores and 128GB of RAM. Forty-eight of those
nodes have two state-of-the-art GPUs, and still others were loaded with even
more power: NVIDIA's Tesla-series K80 and P100 GPUs.

There's more: 42 of those nodes have 3TB of RAM each, and a very special four
nodes have a whopping 12TB of RAM. That's some serious firepower, but all
those nodes were ingeniously woven together to maximize data bandwidth and
minimize latency. It's just as well, considering the amount of data involved:
Libratus was using up to 2.6 petabytes of storage during the competition.

When not being used to best humans at card games, Bridges was being used for
around 650 projects by more than 2,500 people. Think of Bridges as a
supercomputer for hire: Researchers from around the country are using it to
gain insight into arcane subjects like genomics, genome-sequence assemblies
and other kinds of machine-learning.

The beauty of Bridges, according to Nystrom, is that those researchers don't
need to be supercomputer buffs. "It's a very cloud-like model letting people
who are not programmers, not computer scientists, not supercomputer users make
use of a supercomputer without necessarily even knowing it." That's what
happened with Libratus, and everything seemed to be working perfectly.

### Game theory

After the humans' gutsy attack plan failed, Libratus spent the rest of the
competition inflating its virtual winnings. When the game lurched into its
third week, the AI was up by a cool $750,000. Victory was assured, but the
humans were feeling worn out. When I chatted with Kim and Les in their hotel
bar after the penultimate day's play, the mood was understandably somber.

"Yesterday, I think, I played really bad," Kim said, rubbing his eyes. "I was
pretty upset, and I made a lot of big mistakes. I was pretty frustrated.
Today, I cut that deficit in half, but it's still probably unlike for me to
win." At this point, with so little time left and such a large gap to close,
their plan was to blitz through the remaining hands and complete the task in
front of them.

For these world-class players, beating Libratus had gone from being a real
possibility to a pipe dream in just a matter of days. It was obvious that the
AI was getting better at the game over time, sometimes by leaps and bounds
that left Les, Kim, McAulay and Chou flummoxed. It wasn't long before the pet
theories began to surface. Some thought Libratus might have been playing
completely differently against each of them, and others suspected the AI was
adapting to their play styles while they were playing. They were wrong.

As it turned out, they weren't the only ones looking back at the past day's
events to concoct a game plan for the days to come. Every night, after the
players had retreated to their hotel rooms to strategize, the basement of the
Supercomputing Center continued to thrum. Libratus was busy. Many of us
watching the events unfold assumed the AI was spending its compute cycles
figuring out ways to counter the players' individual play styles and fight
back, but Professor Sandholm was quick to rebut that idea. Libratus isn't
designed to find better ways to attack its opponents; it's designed to
constantly fortify its defenses. Remember those major Libratus components I
mentioned? This is the last, and perhaps most important, one.

"All the time in the background, the algorithm looks at what holes the
opponents have found in our strategy and how often they have played those,"
Sandholm told me. "It will prioritize the holes and then compute better
strategies for those parts, and we have a way of automatically gluing those
fixes into the base strategy."

If the humans leaned on a particular strategy -- like their constant three-
bets -- Libratus could theoretically take some big losses. The reason those
attacks never ended in sustained victory is because Libratus was quietly
patching those holes by using the supercomputer in the background. The Great
Wall of Libratus was only one reason the AI managed to pull so far ahead.
Sandholm refers to Libratus as a "balanced" player that uses randomized
actions to remain inscrutable to human competitors. More interesting, though,
is how good Libratus was at finding rare edge cases in which seemingly bad
moves were actually excellent ones.

"It plays these weird bet sizes that are typically considered really bad
moves," Sandholm explained. These include tiny underbets, like 10 percent of
the pot, or huge overbets, like 20 times the pot. Donk betting, limping -- all
sorts of strategies that are, according to the poker books and folk wisdom,
bad strategies." To the players' shock and dismay, those "bad strategies"
worked all too well.

### Poker and beyond

On the afternoon of January 30th, Libratus officially won the second Brains vs
AI competition. The final margin of victory: $1,766,250. Each of the players
divvied up their $200,000 spoils (Dong Kim lost the least amount of money to
Libratus, earning about $75,000 for his efforts), fielded questions from
reporters and eventually left to decompress. Not much had gone their way over
the past 20 days, but they just might have contributed to a more thoughtful,
AI-driven future without even realizing it.

Through Libratus, Sandholm had proved algorithms could make better, more-
nuanced decisions than humans in one specific realm. But remember: Libratus
and systems like it are general-purpose intelligences, and Sandholm sees
plenty of potential applications. As an entrepreneur and negotiation buff,
he's enthusiastic about algorithms like Libratus being used for bargaining and
auctions.

"When the FCC auctions spectrum licenses, they sell tens of billions of
dollars of spectrum per auction, yet nobody knows even one rational way of
bidding," he said. "Wouldn't it be nice if you had some AI support?"

But there are bigger problems to tackle — ones that could affect all of us
more directly. Sandholm pointed to developments in cybersecurity, military
settings and finance. And, of course, there's medicine.

"In a new project, we're steering evolution and biological adaptation to
battle viral and bacterial infections," he said. "Think of the infection as
the opponent and you're taking sequential actions and measurements just like
in a game." Sandholm also pointed out that such algorithms could even be used
to more helpfully manage diseases like cancer, both by optimizing the use of
existing treatment methods and maybe even developing new ones.

Jason, Dong, Daniel and Jimmy might have lost this prolonged poker showdown,
but what Sandholm, Brown and their contemporaries have learned in the process
could lead to some big wins for humanity.
