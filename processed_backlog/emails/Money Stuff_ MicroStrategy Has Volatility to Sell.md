# Money Stuff: MicroStrategy Has Volatility to Sell

**From:** "Matt Levine" <noreply@news.bloomberg.com>
**Date:** Thu, 05 Dec 2024 19:06:22 +0000
**Source:** inputs/saved_emails/Money Stuff MicroStrategy Has Volatility to Sell_Thu,_05_Dec_2024_19-06-22_+0000_19398377fe84165c.eml
**Processed:** 2025-08-24T19:13:07.612150

Money Stuff
 Programming note: Money Stuff will be off tomorrow and early next week, back
Wednesday, Dec. 11.Here’s the basic idea of convertible arbitra



<https://www.bloomberg.com/opinion/authors/ARbTQlRLRjE/matthew-s-levine?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>

<https://sli.bloomberg.com/click?s=825881&stpe=default&li=11931332&m=21d6dea82d6b16615cf44233be620525&p=12052024>


Programming note: Money Stuff will be off tomorrow and early next week, back
Wednesday, Dec. 11.


MicroStrategy

Here’s the basic idea of convertible arbitrage. You buy a convertible bond
that will pay you back, in a year, either (1) $1,000 in cash or (2) 20 shares
of the company’s stock. (Or some other “conversion ratio”; 20 is an arbitrary
simple number.) If the stock today is at, say, $2 per share, then those 20
shares of stock are worth $40, and you will almost definitely want the $1,000
in a year. If the stock today is at $200 per share, then those 20 shares of
stock are worth $4,000, and you will almost definitely want the stock in a
year. At very high stock prices, the convertible bond is essentially equivalent
to stock; at very low stock prices, it is essentially equivalent to a $1,000
bond.

You, as a convertible arbitrageur, are in the business of hedging your
stock-price risk. You do this by selling the stock short. How much you sell
short depends on how much stock-price risk you have. If the stock price is very
high, then the convertible bond is essentially stock, and a $1 move in the
stock price should cause about a $20 move in the convertible price (because the
convertible represents 20 shares). So you sell short 20 shares of stock to
hedge your stock price risk. If the stock price is very low, then the
convertible has essentially no exposure to the stock, and a $1 move in the
stock price should cause about a $0 move in the convertible price. So you sell
short zero shares of stock to hedge your (non-existent) stock price risk. [1]
<>

And in between those extremes, the convertible has some medium amount of stock
exposure. If the stock today is at $40 per share, then the convertible might
have, say, a 70% exposure to the stock: A $1 move in the stock price should
cause about a $14 move in the convertible price ($1 times 20 shares times 70%).
So you’d sell short 14 shares of stock — 70% of the shares underlying the
convertible — to hedge your stock price risk. The actual number — the “hedge
ratio” or “delta” — varies smoothly between 0% and 100% and can be calculated
by reasonably well-understood methods. The point is that eventually, at
maturity, the convertible will be paid back in cash or stock, so eventually it
will be pure cash or pure stock; before that, the convertible has some varying
probability of being cash or stock.

What does it mean to hedge your stock-price risk? Well, literally, it means
that if the stock moves up (or down) by $1, you will make (or lose) some money
on your convertible bond, and you will lose (or make) some offsetting amount of
money on your stock position. [2]  <> The stock can go up or down, and you
don’t care; you’re hedged either way.

You can’t just set this and forget it, though. The higher the stock price is,
the more stock-like the convertible is: If the stock price is high, the
convertible is mostly stock, but if it is low, the convertible is mostly a
regular bond. So your correct hedge ratio will change as the stock moves up or
down. So if the stock goes up by $1, you will make some money on your
convertible and lose some offsetting amount of money on your stock hedge, but
then at the end of the day you willadjust your hedge by selling more stock,
because the convertible now has more stock exposure. On the other hand, if the
stock goes down by $1, the convertible will become less stock-like, so you will
have to adjust your hedge by buying back some of the stock you were short.

This is the more practical meaning of hedging your stock-price risk. It means
that every day the stock moves around and you rebalance your hedge. When the
stock goes up, you sell some stock at high prices. When the stock goes down,
you buy some stock at low prices. Hedging the convertible means buying stock
low and selling it high.

The thing to realize is that, the more you get to do this, the more money you
make. If the stock goes up one day and down the next, you sell stock on the up
day and buy it back on the down day and make a profit. If the stock just stays
flat or drifts up or down, you don’t make that much money adjusting your hedge;
if the stock bounces around wildly, you do.

So a convertible bond is a bet on volatility: The more the company’s stock
bounces around, the more money convertible arbitrageurs can make.

I used to be a convertible bond investment banker, and this was, often,
roughly the pitch to companies: “You have a valuable asset that you don’t even
know about: volatility. Your stock is volatile. You probably don’t think about
that much, and if you do, you think it’s bad. You don’t like your volatile
stock. But do you know who does? Convertible arbitrageurs. They will pay you a
lot of money for that volatility, in the form of cheap convertible bond
financing.”

You know who knows all about this? MicroStrategy. Bloomberg’s Yiqin Shen
reports
<https://www.bloomberg.com/news/articles/2024-12-05/convertible-bond-arbs-are-making-microstrategy-wall-street-s-hottest-trade?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
:

To sate his multibillion dollar rampant appetite for Bitcoin, Michael Saylor
has tapped demand from retail investors transfixed by MicroStrategy Inc.’s more
than 500% rally this year. He’s also benefited from hedge funds who care far
less where the stock trades.

Calamos Advisors LLC co-Chief Investment Officer Eli Pars has been among the
buyers for more than $6 billion of convertible notes sold by MicroStrategy this
year to finance the purchase of his ever-expanding cryptocurrency hoard. Like
many other managers, Pars uses the notes in market-neutral arbitrage bets that
exploit the surging volatility of the underlying asset.

“Convertibles are a way for issuers to monetize the volatility of their
stocks, and MicroStrategy is an extreme example,” said Pars, whose firm owns
more than $130 million of MicroStrategy notes in both long and arbitrage
strategies.

We have talked
<https://www.bloomberg.com/opinion/articles/2024-11-18/palantir-delivers-the-tendies?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 aboutMicroStrategy
<https://www.bloomberg.com/opinion/articles/2024-10-31/microstrategy-has-stock-to-sell?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 a lot, and I have said that it is roughly in the business of (1) owning a big
pot of Bitcoins, (2) selling stock at a large premium to the value of its pot
of Bitcoins and (3) reinvesting the money in more Bitcoins. This is a weird
enough business model.

But to be fair MicroStrategy is also in the business of selling billions of
dollars of convertible bonds to buy more Bitcoins, which is in many ways a much
nicer trade:

 * Bitcoin is, at least historically, a volatile asset, and there is a lot of
demand for options on Bitcoin. It has traditionally been hard for US
institutional investors to buy lots of options on Bitcoin in a convenient way.
MicroStrategy convertibles provide, in a very rough way, billions of dollars of
Bitcoin volatility bets in a nice institutional-friendly package.
 * But MicroStrategy is not just a pot of Bitcoins: It also trades at a large
premium to the value of its pot of Bitcoins. You could have various fundamental
views on that premium — “it is too high” is a normal view, but “it is too low”
also seems popular — but the point here is that there is no reason to think it
isstable. There’s no reason to think “ah yes MicroStrategy should naturally
trade at 2x the value of its Bitcoins forever,” or whatever. And so in fact
MicroStrategy’s stock price ismuch more volatile than Bitcoin is, so
MicroStrategy can sell its volatility at a huge (and deserved) premium to the
volatility of Bitcoin. [3]  <>
 * I have been talking about convertible bonds as mostly a stock volatility
bet, but they are also a credit bet: For convertible arbitrage to work as I
described, you need to be pretty confident that, if the stock price ends up
low, the company will pay you back the $1,000. My gut sense is that the
one-sentence intuitive credit analysis of MicroStrategy — “it has a huge pot of
Bitcoins, has borrowed significantly less than the market value of that pot in
the convertible market, and has like a $90 billion equity cushion” — isjust fine
for convertible investors in a way that it might not be for, like, ratings
agencies or traditional credit investors. [4]  <>
There’s one other really neat aspect of the trade. We have also talked about
another popular MicroStrategy derivative instrument, thelevered exchange-traded
funds
<https://www.bloomberg.com/opinion/articles/2024-12-02/texas-asks-if-index-funds-are-illegal?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 that own billions of dollars of its stock. The rough way to think about those
is:

 * They take in $100 of investor money and borrow $100 from banks to buy $200
of MicroStrategy stock.
 * If the stock goes up 5% one day, then they have $210 of MicroStrategy stock
and $100 of borrowing, so there’s $110 of investor equity.
 * But they need to give investors 2x exposure every day, which means that
they need to go out and borrow $10 more to buy more stock so they have $220 of
stock.
 * On the other hand, if the stock instead goes down 5%, they have $190 of
stock and $90 of equity, and need to sell $10 of stock to repay borrowing to
maintain their 2x exposure.
That is: The ETFs are forced to buy high and sell low, the opposite of
convertible investors.

Leveraged single-stock ETFs are, in an approximate sense, a bet against
volatility: The more volatile the underlying stock is,the worse the leveraged
ETF does
<https://www.bloomberg.com/opinion/articles/2024-09-03/triple-etfs-triple-your-fun?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 at tracking its returns. (This is called “volatility drag
<https://davenadig.substack.com/p/why-your-leveraged-mstr-etf-is-sloppy>.”)
They are notsold as bets against volatility — they are sold as extra-volatile
bets on the stock — but that is roughly what they are. And they are
volatility-reinforcing:The more money there is in leveraged MicroStrategy ETFs,
the more volatile MicroStrategy’s stock will be, because those ETFs have to buy
more stock whenever it goes up and sell stock whenever it goes down. The more
it bounces around, the morethey bounce it around.

MicroStrategy’s convertibles are the opposite: They are a bet on
MicroStrategy’s volatility, and they are volatility-dampening. Convertible
arbitrageurs buy stock when it goes down and sell it when it goes up, which
reduces the volatility of the stock.

Ordinarily this suggests some limit on a company’s ability to sell
convertibles: Convertibles are worth more if your stock is more volatile, but
the more convertibles you sell, the less volatile your stock will be, because
convertible arbitrageurs will smooth out the moves in your stock by buying when
it goes down and selling when it goes up. MicroStrategy has, weirdly, found a
solution: It sells volatility to convertible arbitrageurs, andbuys volatility
from retail ETF investors, so there’s always plenty of volatility to go around.


<https://sli.bloomberg.com/click?s=868432&stpe=default&li=11931332&m=21d6dea82d6b16615cf44233be620525&p=12052024>


<https://sli.bloomberg.com/click?s=868432&stpe=default&li=11931332&m=21d6dea82d6b16615cf44233be620525&p=12052024>

Pharma financing

I guess a thing that happens sometimes at microcap biotech companies is:

 * You develop some drug and do some preliminary testing.
 * That takes all of your money, and to continue developing the drug and
getting it approved, you will need more money.
 * You go out to investors to raise the money.
 * You have some preliminary results of your preliminary testing.
 * What do you tell the investors about those results?
I mean! If the results are good, probably you tell them the results? That will
make it a lot easier to raise money. If the results are bad … man, you should
definitely still tell them the results, because they will find out eventually,
and if they find outafter they give you the money, they will be very annoyed
and also you might have done fraud. But, uh, I can understand how you might be
inclined not to tell them about the bad results. What if they don’t give you
the money? You really want the money.

Here is a US Securities and Exchange Commission enforcement action
<https://www.sec.gov/newsroom/press-releases/2024-189> against a company called
Kiromic:

The Securities and Exchange Commission [Tuesday] filed settled charges against
Houston-based biotherapeutics company Kiromic BioPharma, Inc., its former CEO,
Maurizio Chiriva-Internati, and its former chief financial officer, Tony
Tontat, for failing to disclose material information about Kiromic’s two cancer
fighting drug candidates before, during, and after a July 2021 follow-on public
offering that raised $40 million. ...

According to the SEC’s order against Kiromic, the company raised $40 million
in a public offering on July 2, 2021, for the purpose of funding the
prospective clinical trials for its two cancer fighting drug candidates, the
ALEXIS-PRO-1 and the ALEXIS-ISO-1. However, the SEC’s order found that two
weeks before the public offering, the Food and Drug Administration (FDA)
notified Kiromic that it had placed the drug candidates on clinical hold—an FDA
order to delay the proposed clinical investigations. The SEC’s order also found
that Kiromic did not disclose the FDA clinical holds in its SEC filings,
investor roadshow calls, or during due diligence calls leading up to the
offering, despite the fact that Kiromic disclosed the hypothetical risk of a
clinical hold and the potential negative consequences on Kiromic’s business.

Here is the prospectus
<https://www.sec.gov/Archives/edgar/data/1792581/000110465921087657/tm2118321-9_424b4.htm>
 for that offering, which contains a risk factor about a possible clinical hold,
[5]  <> but which neglects to mention that it had already happened. The SEC
complaint <https://www.sec.gov/files/litigation/admin/2024/33-11332.pdf>
suggests that this might actually have been a misunderstanding:

Chiriva is not a native English speaker, and his messaging to the Board about
the FDA’s communications about the status of the ALEXIS INDs was imprecise.
Chiriva told the Board that: Kiromic had received communications from the FDA
about the ALEXIS INDs; the FDA had requested an additional 30 days to conduct a
secondary review; and the IND applications were on halt and administratively on
hold until Kiromic received further questions from the FDA. … Some attendees at
the meeting, including members of the Board, did not understand from Chiriva’s
update that the FDA had already imposed clinical holds on the ALEXIS INDs.

Still there were a lot of roadshow calls in which the hold was not mentioned.

Kiromic’s current market capitalization is about $1.7 million, so basically
all of the $40 million it raised in 2021 has disappeared. I am not sure that,
if it had disclosed “we got a clinical hold,” the investors would haveavoided
that mistake, but it’s not a good look.

Meanwhile today Byrne Hobart writes
<https://www.thediff.co/archive/are-vcs-incentivized-to-be-too-nice-for-venture-debt/?ref=the-diff-newsletter>
 about a small biotech company with the opposite problem:

A microcap biotech company, Senti, ended the September quarter with three or
four months of runway. Their options at that point were to wind down or to take
some external money, and they went with the external money in the form of a
convertible preferred and warrants, which collectively cover 54 million shares.
At the end of the prior quarter, they had 4.4m shares outstanding, so the vast
majority of the company belongs to the new buyers.

And those new buyers got themselves a pretty good deal: the deal was priced at
$2.25-$2.30/share, the prevailing price before it was announced, but the day
the deal was announced the stock popped to almost $17 and closed at $10,
because that announcement was concurrent with the announcement that a very
early-stage trial turned out well: exactly two thirds of patients recovered,
because there were three in total. ...

Companies can and do raise money from investors on the basis of material
information that isn't yet widely shared. ... But it does raise the question of
how to divide up the spoils. It's hard to disentangle the impact of the
business news from the impact of financing that gives the company more than a
year of cash burn, and apparently the company’s conclusion—thus far correct—was
that their investors would prefer 8% of something to 100% of nothing.

Obviously telling new investors “hey we got good trial results” helps with
raising money, but it didn’t helpthat much: The investors who kicked in the
money got 92% of the company in return. The company needed the cash more than
the investors needed the promising drug, apparently. It’s possible that
disclosing the results before doing the deal would have pushed up the stock
price and gotten a better deal for the company, but it’s also possible that it
wouldn’t have: Disclosing good results with no financing might not have moved
the market, and telling the new investors “hey you get to buy in based on
information that the market doesn’t know yet” is a good pitch.


Fake insider betting

Classically a popular way to do fraud is to trick people into thinking that
they are actually committing crimes with you. Youcould say “I have a clever
well-researched system to predict which stocks will go up, and if you give me
your money I will use it for you,” but it might work better to say “I have hot
illegal insider tips and if you give me your money I will use them for you,” or
“I run pump-and-dump scams and if you pay to sign up for my newsletter I will
give you early notice of the stocks I plan to pump,” or “I will front-run my
market-making clients and share the profits with you
<https://www.fraud-magazine.com/article.aspx?id=313>.” The advantages of this
are:

 * It tends to attract the people you want to attract. “You can’t cheat an
honest man,” etc.; the people who are looking to participate in a scam seem to
be the people who are most likely tofall for a scam.
 * If they find out that you’re scamming them, what are they going to do about
it? They were trying to do crimes, so it’s not like they can go to the police.
The second advantage is not legal advice and also not all that reliable. We
talked a few years ago
<https://www.bloomberg.com/opinion/articles/2021-03-22/fake-insider-trading-is-illegal-too?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 about a guy who got arrested for selling fake insider information about public
companies on the dark web. The problem, I suppose, is that if you go around
advertising “hey would you like to do crimes with me,” and then defraud whoever
replies, (1) your victims might not complain to the authorities but (2) the
authorities might have seen your ads themselves, and replied to them. If you
advertise “I have illegal inside information for stock trading” on the dark
web, and you get an email from someone saying “I would like to purchase your
inside information to do illegal insider trading,”probably that email is from
the FBI! Not legal advice!

Anyway here’s this guy
<https://www.espn.com/espn/betting/story/_/id/42776872/poker-pro-cory-zeidman-pleads-guilty-bettor-fraud-scheme>
:

A professional poker player pleaded guilty Wednesday to defrauding bettors in
New York and Florida by falsely claiming to have inside information on sporting
events.

Cory Zeidman of Boca Raton, Florida, pleaded guilty to conspiracy to commit
mail and wire fraud in connection with a sports betting scheme that lasted for
years, according to a news release from United States Attorney's Office for the
Eastern District of New York.

Federal authorities alleged that Zeidman and his partners misled customers to
pay the organization for betting advice by claiming to have knowledge of
nonpublic injury information, "dirty" referees and fixed games, according to
court documents. The scheme lasted from 2006 to 2020.

"Sports bettors sought Cory Zeidman's advice before gambling their money --
but it was Zeidman himself who was scoring big through his deceptive practices,
outright lies, and high-pressure tactics that exploited unsuspecting clients,"
special agent Charles Walker of Homeland Security in New York said in the
release.

We talked about Zeidman
<https://www.bloomberg.com/opinion/articles/2022-05-26/elon-called-off-his-margin-loan?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 back when he was charged. Here isthe news release
<https://www.justice.gov/usao-edny/pr/former-long-island-resident-pleads-guilty-massive-fraud-scheme-involving-sports>
:

As alleged in court documents, Zeidman helped run an organization that placed
national radio advertisements to lure prospective bettors to retain the
organization for sports betting advice. Using fake names and high-pressure
sales tactics, Zeidman and his partners falsely led the bettors to believe that
their organization had access to non-public information—bettors were often
told, for example, that Zeidman’s organization had access to non-public player
injury information, “dirty” referees, or that professional sporting events were
“fixed” and that media executives’ shares predetermined outcomes with Zeidman’s
organization. This information, the bettors were told, made gambling on
sporting events a low or no-risk proposition. Victims were required to pay
exorbitant fees to obtain this supposedly privileged information which,
unbeknownst to them, was fictitious or based on the conspirators’ open-source
internet research. Over the course of several years, Zeidman and his partners
reaped millions in fees from victims.

On the one hand, if you are a victim, why would you think “oh yes this
organization that has fixed professional sports games isadvertising on the radio
for people to make no-lose bets on their fixed games”? On the other had, if you
areadvertising on the radio that you will help people make illegal sports bets
[6]  <> using inside information, surely like 10% of your potential customer
inquiries are going to come from the FBI?


A certain amount of bribery

If you run a large multinational commodity trading firm, how much bribery
should you do? “Zero,” of course, feels like the right answer. If you get to
decide on an amount of bribery to do, decide on zero. But it’s not always that
straightforward. You have a lot of people running their own budgets in
far-flung corners of the world where a little bribery might help them win
business, and you can’t supervise them all constantly. It ispossible that the
right answer is:

 * There is a real trade-off between letting people do business, on the one
hand, and preventing them from doing bribery, on the other hand, and you have
to strike some balance in which you have lots of policies and supervision to
prevent bribery, and you try to inculcate a culture of not doing bribery, but
you understand that those policies and supervision and culture cannot be
perfect, because the only perfect way to prevent bribery is to not do any
business.
 * But you should never say that; you should always say “we have a zero
tolerance policy for bribery,” because regulators get really mad when you say
“well obviously there’s going to be a certain amount of bribery.”
The optimal amount of bribery to allow is slightly more than zero, but the
amount of bribery that you shouldsay you allow is exactly zero. Not legal
advice! Anyway there’s a trial in Switzerland about allegations that Trafigura
Group paid some bribes in Angola, and Trafigura’s chief financial officer
managed to say this
<https://www.ft.com/content/bfa4c689-fa2a-4fe7-835b-266544c53b5d> — “we say we
allow zero bribes but we can’t actually do that” — with unusual clarity:

He said: “Claude [Dauphin, former head of Trafigura] clearly indicated that
[compliance] was a zero tolerance issue . . . it was important for the company
that the people in the most important sectors of the company spent time on
these subjects and showed and indicated that this was a completely real
programme whose aim was to limit risk”.

There was nevertheless always a “balance” to strike, he added.

“There are many risks in our businesses and compliance is just one of
them . . . there is always a balance to be struck between risk management and
the ability to operate, because if you want the perfect system, everything
stops. Crossing the road is a risk.”

You always indicate that compliance is a zero tolerance issue, but do you want
a perfect system? No, then you’d never do any business.


Things happen

Grief, Then Confusion: Questions of Motive
<https://www.bloomberg.com/news/articles/2024-12-04/unitedhealthcare-ceo-brian-thompson-killed-search-for-motive-emerges?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 Emerge in UnitedHealthcare CEO’s Killing.Murder at Dawn
<https://www.wsj.com/us-news/united-healthcare-ceo-killed-what-happened-33cf8452?mod=WSJ_home_mediumtopper_pos_1>
: A Top Executive’s Final Moments in Manhattan. Bitcoin Soars Past $100,000 on
Trump’sPro-Crypto Pick for SEC
<https://www.bloomberg.com/news/articles/2024-12-05/bitcoin-btc-nears-record-100-000-on-trump-s-pick-of-atkins-for-sec?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
.TD
<https://www.bloomberg.com/news/articles/2024-12-05/td-misses-on-weak-us-performance-suspends-its-growth-guidance?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 Suspends Growth Guidance in Wake of Historic US Settlement.HPS
<https://www.bloomberg.com/news/articles/2024-12-04/hps-offers-incentives-to-retain-staff-after-sale-to-blackrock?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 Offers Incentives to Retain Staff After Sale to BlackRock. Abu Dhabi’s
Mubadala Capital takes large stake in UScredit fund
<https://www.ft.com/content/4e2018cf-2343-4036-8356-4730ad223aa1>. EBRD
<https://www.bloomberg.com/news/articles/2024-12-05/ebrd-to-transfer-risk-tied-to-1-billion-of-private-sector-loans?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 to Transfer Risk Tied to $1 Billion of Private-Sector Loans. Ranks of401(k)
Millionaires
<https://www.bloomberg.com/news/articles/2024-12-05/there-are-more-401-k-millionaires-than-ever-before-fidelity-says?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 at Fidelity Surge to Fresh Record. BillionairesEmigrating More Frequently
<https://www.bloomberg.com/news/articles/2024-12-05/billionaires-emigrating-more-frequently-since-covid-ubs-says?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
 Since Covid, UBS Says.Chatbot Arena
<https://www.wsj.com/tech/ai/the-uc-berkeley-project-that-is-the-ai-industrys-obsession-bc68b3e3?mod=hp_featst_pos5>
. New‘anti-woke’ ETF
<https://www.ft.com/content/f19c34b2-2eb0-40f4-a799-f5221413e9b2> makes
Starbucks its first target.Money launderer for Russian spies
<https://www.ft.com/content/57a3fef0-64aa-4dd5-a1dd-6c31c1386de7> won deal to
help defend Ukraine power plant. TheNecktie
<https://www.wsj.com/lifestyle/workplace/the-necktie-is-making-an-office-comeback-e785e9f6?mod=hp_featst_pos4>
 Is Making an Office Comeback.

If you'd like to get Money Stuff in handy email form, right in your inbox,
pleasesubscribe at this link
<http://link.mail.bloombergbusiness.com/join/4wm/moneystuff-signup&hash=54223001ca3ffcf40f2629c25acea67a>
. Or you can subscribe to Money Stuff and other great Bloomberg newslettershere
<https://login.bloomberg.com/newsletters>. Thanks!


 <https://link.chtbl.com/Money-Stuff-Podcast-Newsletter>


[1] This is only loosely true, and in practice there is a rough notion that
very busted converts have negative gamma: Below some low stock price, as the
stock goes lower, you should short more stock to hedge the credit risk of the
bond. But I’m ignoring credit risk for now.

[2] This is also a bit loose, a $1 move is pretty big, and really you’d have
some convexity.

[3] A related argument here is that MicroStrategy is a *leveraged* pot of
BItcoins, so it should be more volatile than the underlying Bitcoins. I have
trouble thinking of MicroStrategy as a leveraged pot of Bitcoins because its
equity value is *higher*, not lower, than the value of its underlying Bitcoins,
but this is an argument that you hear sometimes.

[4] But Shen writes
<https://www.bloomberg.com/news/articles/2024-12-05/convertible-bond-arbs-are-making-microstrategy-wall-street-s-hottest-trade?cmpid=BBD120524_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241205&utm_campaign=moneystuff>
: “While the convertible arbitrage community is relatively shielded from the
wild price swings because their positions are hedged, a key risk to their trade
is the firm’s credit profile, which is tied to one of the riskiest asset
classes and Saylor’s unprecedented strategy. ‘If Bitcoin does correct and the
premium of MicroStrategy’s Bitcoin holdings to indebtedness compresses, it will
start to affect the credit of the converts,’ said David Clott, portfolio
manager at convertible bond specialist Wellesley Asset Management. ‘The trade
seems like a bit asymmetric on the downside now.’”

[5] “Further, a clinical trial may be suspended or terminated by us, the IRBs
for the institutions in which such trials are being conducted or by the FDA or
other regulatory authorities due to a number of factors, including failure to
conduct the clinical trial in accordance with regulatory requirements or our
clinical protocols, inspection of the clinical trial operations or trial site
by the FDA or other regulatory authorities resulting in the imposition of a
clinical hold, unforeseen safety issues or adverse side effects, failure to
demonstrate a benefit from using a product candidate, changes in governmental
regulations or administrative actions, lack of adequate funding to continue the
clinical trial, or based on a recommendation by the Data Safety Monitoring
Committee. The FDA’s review of our data of our ongoing clinical trials may,
depending on the data, also result in the delay, suspension or termination of
one or more clinical trials, which would also delay or prevent the initiation
of our other planned clinical trials. If we experience termination of, or
delays in the completion of, any clinical trial of our product candidates, the
commercial prospects for our product candidates will be harmed, and our ability
to generate product revenue will be delayed. In addition, any delays in
completing our clinical trials will increase our costs, slow down our product
development and approval process and jeopardize our ability to commence product
sales and generate revenue.”

[6] Sports betting was mostly illegal in much of the US before about 2018, and
this scheme ran from 2006 to 2020.


Follow Us  <https://www.facebook.com/bloombergopinion>
<https://www.instagram.com/bloombergopinion/>  <https://twitter.com/bopinion>
Get the newsletter
<https://www.bloomberg.com/account/newsletters/money-stuff?source=NLshare>


Like getting this newsletter?  Subscribe to Bloomberg.com
<https://www.bloomberg.com/subscriptions?utm_medium=email&utm_source=newsletter&utm_campaign=moneystuff&utm_content=tout-money-stuff&utm_term=>
 for unlimited access to trusted, data-driven journalism and subscriber-only
insights.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the
Terminal delivers information and analysis that financial professionals can’t
find anywhere else.Learn more
<https://link.mail.bloombergbusiness.com/click/15638356.78421/aHR0cHM6Ly93d3cuYmxvb21iZXJnLmNvbS9wcm9mZXNzaW9uYWwvc29sdXRpb24vYmxvb21iZXJnLXRlcm1pbmFsLw/55088ec43b35d034698d38aeBe3d4e6ab>
.

Want to sponsor this newsletter?  Get in touch here
<https://www.bloombergmedia.com/contact/?utm_medium=email&utm_source=newsletter&utm_campaign=moneystuff>
.

 You received this message because you are subscribed to Bloomberg's Money
Stuff newsletter.
Unsubscribe
<https://login.bloomberg.com/newsletters?source=newsletter_unsub&email=bloomberg@khamel.com&hash=3878bee49d8b2b98e3953b8420dc7f54053a9a7e>
 |Bloomberg.com <http://bloomberg.com> | Contact Us
<http://www.bloomberg.com/feedback?alcmpid=mostpop>

 <https://www.liveintent.com/powered-by>  |
<https://www.liveintent.com/ad-choices>
Bloomberg L.P. 731 Lexington, New York, NY, 10022
<https://links.message.bloomberg.com/e/eh?_t=f574328d4d0c4c359b90d8e49b10e21d&_m=3b64de4c1de04b4ca93d6dc0bae19d74&_e=QDdZM_DY1o6C6X_ndale4WSUIVCJArfEQX3iA2jbZjnTeBhlIFgM2_IEp_BH7CfhEJSj43wv5qGMr3nD46_uz7wUN0kjkBfLN366K1KVOGQE-FldwgQJxGP4uZRfmBOynb-hBVS-JeNZyOfBtIK-bEe3Tern8VVVnBwWRw2UYGwiZEjX2CT466HLvVza3VuKVoYOg-y7o7_8np87ZF46P3v90Zt9aV0sXCMUJ5l09Ma1aHeLEt2mWL9sHd1x7eKnm6RM7wCBu8KMGJpWq68TRw%3D%3D>