# Money Stuff: JPMorgan Undercharged for a Trade

**From:** "Matt Levine" <noreply@news.bloomberg.com>
**Date:** Mon, 04 Nov 2024 19:58:00 +0000
**Source:** inputs/saved_emails/Money Stuff JPMorgan Undercharged for a Trade_Mon,_04_Nov_2024_19-58-00_+0000_192f8c191debd4af.eml
**Processed:** 2025-08-24T19:13:10.236033

Money Stuff
 I wrote last week that, “if you are a big bank, somebody somewhere in your
organization is pretty much always doing something that looks a b



<https://www.bloomberg.com/opinion/authors/ARbTQlRLRjE/matthew-s-levine?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>

<https://sli.bloomberg.com/click?s=825881&stpe=default&li=11592634&m=21d6dea82d6b16615cf44233be620525&p=11042024>



JPMorgan miscellany: MMLF

I wrote last week
<https://www.bloomberg.com/opinion/articles/2024-10-30/florida-banned-some-banks?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
 that, “if you are a big bank, somebody somewhere in your organization is
pretty much always doing something that looks a bit like securities fraud, and
periodically the SEC will add it all up and send you an invoice for a big
fine.” The next day the US Securities and Exchange Commission sent JPMorgan
Chase & Co. an invoice for $151 million for assorted securities misdeeds over
the last few years. I’m not sure it’s even fair to say that the SEC sent an
invoice. These days it’s more like a tax return: JPMorgan downloads a form that
is like “what securities laws did you violate this year,” and it fills out the
form and attaches the relevant receipts and sends it all in to the SEC with a
check. Fromthe SEC’s announcement
<https://www.sec.gov/newsroom/press-releases/2024-178>:

“JP Morgan’s conduct across multiple business lines violated various laws
designed to protect investors from the risks of self-dealing and conflicts of
interest,” said Sanjay Wadhwa, Acting Director of the SEC’s Division of
Enforcement. “With today’s settlements, which include multiple self-reports and
large voluntary payments to harmed investors, JP Morgan is being held
accountable for its regulatory failures.”

The violations are very miscellaneous; there’s one about
<https://www.sec.gov/files/litigation/admin/2024/34-101493.pdf> putting clients
into higher-fee mutual funds rather than lower-fee but otherwise identical
exchange-traded funds, andanother one
<https://www.sec.gov/files/litigation/admin/2024/33-11324.pdf> about waiting
too long after initial public offerings to sell stocks for clients. But here’s
a good one about amoney market fund regulatory arbitrage
<https://www.sec.gov/files/litigation/admin/2024/ic-35373.pdf>.

In March 2020, the Federal Reserve created a “Money Market Mutual Fund
Liquidity Facility <https://www.federalreserve.gov/monetarypolicy/mmlf.htm>,”
or MMLF, to help bail out money market funds. Investors had parked their cash
in money market funds, but they were nervous about Covid and withdrew a lot of
cash. Meeting those withdrawals would require the money market funds to sell
assets, but the markets were nervous enough that there might not be any buyers.
This is a pretty clear case for Fed intervention: When depositors want their
money back, and banks have good assets that they temporarily can’t sell to meet
those withdrawals, the central bank is supposed tostep in to lend
<https://www.federalreserve.gov/newsevents/speech/madigan20090821a.htm> against
those assets and prevent a run on the bank. So it did.

Of course money market funds are not technically banks and the Fed is not
technically supposed to be a lender of last resort to them, but those feel like
quaint technicalities and the Fed was not too troubled by them. As a concession
to these technicalities, though, the Fed didnot lend money to money market
funds: Instead, it “made loans available to eligible financial institutions
secured by high-quality assets purchased by the financial institution from
money market mutual funds.” The money market funds had to sell their assets to
a bank or broker, which would then get the (non-recourse) loan, but the promise
of the Fed loan made it easier for the funds to sell without dislocating
markets.

Because the Fed was looking to support US money market funds, it made only US
funds eligible for the MMLF.

J.P. Morgan Investment Management runs US money market funds and also a
foreign money market fund that was not eligible for the MMLF. In March 2020,
its US and foreign money market funds faced redemption requests. The US funds
raised money from MMLF as intended, but the foreign fund couldn’t. JPMorgan
sensibly thought “well these are money market funds, it’s all short-term
low-risk stuff, surely there is a trade here.” The trade is extremely simple:

 * The foreign fund sells assets to the US fund.
 * The US fund sells assets to a bank or broker eligible for the MMLF.
 * The broker brings the assets to the Fed for an MMLF loan.
All of the assets are pretty fungible, so “US money market funds can
(indirectly) sell their assets to the Fed” also means “foreign money market
funds can sell their assets to US funds who can sell them to the Fed.”
JPMorgan’s US funds are in the business of investing in short-term
cash-equivalent securities, and being in the middle of this trade is in fact a
low-risk short-term cash-equivalent sort of trade. The foreign fund goes to the
US fund and says “we’ll pay you a 1.3% annualized yield to hold this stuff for
us overnight and then hand it to the Fed in the morning,” and the US fund is
like “yeah 1.3% is a good rate for this safe trade” and does it. [1]  <>

Is it cheating? Was JPMorgan tricking the Fed into giving liquidity to foreign
funds? I mean, sure, I guess, maybe, but (1) it’s the mild loophole-based sort
of cheating that you’d expect from fixed-income traders and (2) JPMorgan didask
the Fed and the Fed was like “eh fine I guess”:

On March 23, 2020, in coordination with JP Morgan IM, personnel at J.P. Morgan
Securities LLC (“JP Morgan Securities”) emailed the Fed seeking guidance on
whether a hypothetical transaction would comply with the intent of the MMLF.
The hypothetical transaction posed to the Fed was similar to what later became
the Repack ABCP trades. In the following days, the Fed and JP Morgan Securities
engaged in further communications about the hypothetical transaction. The Fed
ultimately responded that it did not plan to issue any guidance that would
prevent the hypothetical transaction.

So JPMorgan did this to the tune of $4.3 billion of assets.

But last week the SEC objected to the prices of the trades. Everything
involved here is a short-term, highly rated cash substitute, so the price of
everything is more or less 100 cents on the dollar, but not quite. The foreign
funds’ assets had appreciated, [2]  <> so they had about $1.5 million of gains
on $4.3 billion of assets, or about 3 basis points. There were fees to be paid
to the broker that bought the assets from the foreign fund and sold them to the
US funds, [3]  <> and to the broker that bought them from the US funds to
deliver into the MMLF. And then the US funds needed to be paid for buying the
assets — but, again, they were buying safe low-risk assets for one night before
handing them over to the Fed, so they didn’t need to be paidmuch. Specifically
they needed to be paid a 1.3% annual yield on $4.3 billion for one day, or
about $150,000.

The SEC objects that (1) the US funds took on some risk (what if the Fed had
said no to taking these assets? It didn’t) and (2) they didn’t get paid enough:

The Domestic Funds earned only one-tenth of the investment gain that the
Foreign Fund made from the transactions. Because JP Morgan IM personnel were
involved in all aspects of the transactions, JP Morgan IM could have allocated
more of the investment proceeds from the transactions to the Domestic Funds by
increasing the annualized yield of the Repack ABCP but did not do so.

There was a conflict of interest here in that JPMorgan funds were on both
sides of the trade, and the SEC isn’t happy with how the conflict was managed.
Oh well. It is a good story of the traps of financial engineering. The US
government is like “we want to backstop US money market funds,” and you are
like “how can I use this to backstop my non-US money market fund,” and you come
up with the sensible answer “have my US funds backstop my foreign fund and then
have the Fed backstop the US ones,” and you call the Fed and say “does this
work,” and they sigh and say “we can’t stop you,” and then you get in trouble
with a different bit of the US government because you didn’t pay your US fund
enough of a commission.


<https://sli.bloomberg.com/click?s=868432&stpe=default&li=11592634&m=21d6dea82d6b16615cf44233be620525&p=11042024>


<https://sli.bloomberg.com/click?s=868432&stpe=default&li=11592634&m=21d6dea82d6b16615cf44233be620525&p=11042024>

JPMorgan miscellany: Portfolio managers

Two ways you can invest with JPMorgan Securities are:

 * Your JPMorgan financial adviser can park your money with some outside
portfolio manager, and you pay (1) that manager’s fee plus (2) a “wrap fee” to
JPMorgan, or
 * Your JPMorgan financial adviser can manage your money herself, and you pay
one fee to JPMorgan.
When I describe it like that presumably you immediately understand that:

 * Paying one fee to JPMorgan, instead of two fees to JPMorgan and the outside
manager, is cheaper for you.
 * But paying one fee to JPMorgan, instead of two fees to JPMorgan and the
outside manager, results in a bigger feefor JPMorgan. The one fee is bigger
than its share of the two fees. So JPMorgan, and in particular the JPMorgan
adviser who gets paid based on revenue, would prefer that you let her manage
your money rather than sending a lot of revenue away to a third-party manager.
And so your JPMorgan adviser will say “you can let me manage your money, or
you can use our third-party manager programs, but letting me do it is cheaper,”
and then she will probably go on to say how good she is at managing money and
how she won’t let you down etc. And, for a while, she would not then go on to
say “but I should warn you that I have a conflict of interest: I get paid more
for managing your money myself than if I find you an outside manager.” And this,
says the SEC <https://www.sec.gov/files/litigation/admin/2024/34-101494.pdf>,
was deceptive:

In part because clients do not pay a separate third-party fee when invested in
PM Program strategies [where a JPMorgan adviser manages the portfolio], JP
Morgan Securities and its financial advisors are able to charge a higher wrap
fee for the PM Program, while maintaining a lower overall fee for the client.
The opportunity to charge a higher wrap fee for PM Program strategies creates a
financial incentive for JP Morgan Securities and its financial advisors to
recommend the PM Program over the TPM Programs [where a third-party manager
runs the money]. …

The PM Program brochure disclosure used until August 2021 did not disclose the
conflicts of interest that PM Program financial advisors have when recommending
that clients invest through the PM Program over the TPM Programs, particularly
the fact that financial advisors most often negotiate a higher JP Morgan
Securities fee when clients participate in the PM Program, which has no
separate portfolio manager fee, instead of in TPM Programs where clients also
pay a separate portfolio manager fee.

Okay. It would be weird if the JPMorgan adviser got paid the same amount for
managing your money herself as she would for outsourcing it to a paid third
party? But I guess you have to be really clear.


BlackRock

My crude rule of thumb
<https://www.bloomberg.com/opinion/articles/2024-06-06/bill-ackman-wants-a-lot-of-your-money?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
 is that if you are a giant traditional asset manager you can charge fees of
roughly 10 basis points, so at 10x earnings you should be valued at roughly 1%
of assets under management. And if you are a big alternative asset manager you
can charge fees of roughly 100 basis points, so you should be valued at roughly
10% of assets under management. And then for some reasonPershing Square
<https://www.bloomberg.com/opinion/articles/2024-06-06/bill-ackman-wants-a-lot-of-your-money?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
 is worth 56% of its assets under management.

This suggests that if you are a giant traditional asset manager with trillions
of dollars under management, and you can rebrand yourself as also a little bit
of an alternative asset manager, there is a lot of valuation leverage there. If
you run $11 trillion and are valued at 1% of AUM, and then people start
thinking “well they’re kind of an alts manager so should be 10% of AUM,” then,
uh, that adds $1 trillion to your valuation? It doesn’t really work that way,
but the thought process is not entirely wrong.Here’s this
<https://www.wsj.com/finance/investing/why-11-trillion-in-assets-isnt-enough-for-blackrocks-larry-fink-8644ac17?mod=hp_lead_pos114>
:

BlackRock’s clients are pouring money into its core stock and bond offerings.
To keep the momentum going, chief Larry Fink wants to push the world’s largest
asset manager into the more lucrative world of private markets.

Managing more assets such as private equity, private credit, real estate and
infrastructure would allow BlackRock to compete with the biggest alternative
asset managers. It could also make BlackRock more valuable.

Firms such as Blackstone, Apollo Global Management and KKR manage just a
fraction of BlackRock’s $11.5 trillion in assets. Yet those rivals command
market values that are in the ballpark of BlackRock’s, which is around $150
billion.

The reason: Private-market funds can charge more than BlackRock gets for much
of its plain-vanilla, index-based funds. And the market rewards that. ...

Alternatives made up just 3% of BlackRock’s total assets in the third quarter,
but generated 11% of total revenue, highlighting how lucrative the fees are.

[Martin] Small, BlackRock’s finance chief, called out that opportunity, noting
that insurance companies have $700 billion of assets with BlackRock, and
flipping just 10% of that to private-credit strategies would be a huge boost to
alternative assets.

The way that I tend to think about private credit
<https://www.bloomberg.com/opinion/articles/2023-06-27/silicon-valley-is-on-drugs?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
 is that in the olden days insurance companies bought bonds and held them to
maturity, and then there was a long interlude where insurance companies
invested in actively managed bond strategies, and then private credit was
invented so that insurance companies could make loans and hold them to
maturity. You could tell that story with a slightly different emphasis:

 * In the olden days insurance companies bought bonds and held them to
maturity.
 * Asset managers realized they could charge insurance companies higher fees
for actively managing their bond portfolios.
 * Over time, competition heated up and those fees compressed.
 * Asset managers realized they could charge insurance companies higher fees
for private credit.
It does seem like a waste for BlackRock to charge a few basis points for bond
beta when it could charge a few percentage points for “the beta of alts
<https://www.bloomberg.com/news/articles/2024-10-30/apollo-founder-harris-says-big-pe-firms-have-left-alpha-behind?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
.”


Who owns farmland?

It is roughly true that Chinese law prohibits foreign investors from owning
certain Chinese technology companies. A lot of those companies want to go
public offshore (in the US, UK, etc.), raise money from foreign investors and
have stocks that trade freely in global markets. (Or, rather, they wanted to:
This was a popular thing for Chinese companies to do for a while, but itmore or
less stopped in 2021
<https://www.reuters.com/markets/deals/china-publishes-offshore-listing-rules-2023-02-17/>
.) How can you have stock that trades freely among foreigners, if you can’t be
owned by foreigners? Well! There is a solution. The solution is:

 * You’ve got a Chinese company owned by Chinese people.
 * You set up another company (in the Cayman Islands or wherever) that can
sell stock to anyone, and it goes public in London or New York.
 * The Chinese company and the Caymans company sign a series of contracts
saying things like “the Chinese company will give the Caymans company its
profits” and “the Caymans company can appoint the executives of the Chinese
company,” but in vaguer ways. (“[Caymans Company] or its designated parties
have the exclusive right to provide [Chinese Company] with comprehensive
technical support, consulting services and other services, and [Chinese
Company] agrees to pay services fees, the amount of which is determined by
[Caymans Company] on the basis of the work performed and commercial value of
the services” is a good way to say “the Chinese company will pay dividends to
the Caymans company,” without using those words. [4]  <>)
This is called a “variable interest entity”; we talked about it once
<https://www.bloomberg.com/opinion/articles/2021-07-07/owning-chinese-companies-is-complicated?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
 when DiDi Global Inc. went public in New York with a VIE. So the Caymans
company (which is owned by global shareholders) doesn’town the Chinese company,
in the standard legal sense of share ownership, but it has something more or
less economically equivalent to ownership of the Chinese company. It quasi-owns
the Chinese company: It owns the Chinese companyenough to make shareholders
willing to invest, but not so much that the Chinese authorities crack down.

Again, this was the state of the art in 2021, but then both Chinese and US
authoritiesdid crack down
<https://www.sec.gov/Archives/edgar/data/1764757/000104746921001227/a2243300z424b4.htm#dk10201_corporate_history_and_structure>
, so, uh, never mind. Still the broad idea is correct. The broad idea is that
if you live in Country X and you want to own Asset Y in Country Z, and Country
Z prohibits residents of Country X from owning Asset Y, you enter into some
sort of agreement with someone in Country Z that gives you ownership-like
rights over Asset Y without actually owning it. The concept of “ownership” is
broad and fuzzy, and you can probably find something that is enough like
ownership for you but not so much like ownership that the Country Z authorities
will object.

Though a big chunk of the job of Country Z’s regulators is writing the rules
in a way that covers all the sorts of quasi-ownership that, if they thought
about it, they would object to. Still it’s probably easier for you to find
loopholes than for them to close them.

Anyway here’s a story about US farmland and Chinese investors
<https://www.wsj.com/us-news/chinese-owned-farmland-us-national-security-election-2024-5082faa6?mod=hp_lead_pos11>
:

Walton Global has been identified by the U.S. government as a Chinese owner of
U.S. farmland for a decade. The private land-banking company has opened four
new offices in China since 2018 and last year was named by the U.S. Department
of Agriculture as one of the top five Chinese owners of American farmland.

But last month, the company successfully petitioned the agency to reclassify
much of its land as owned by investors from other countries, after The Wall
Street Journal inquired about its holdings. It said the agency had made a
mistake in saying so much of its land was held by Chinese investors. …

Few agree on what even counts as owned by China or which aspect of that
ownership is bad for the U.S., even when that land is close to military
installations. …

“We do business in China. We’re proud to do business in China,” the company’s
chief executive, Bill Doherty, said in an interview. But he said, “The company
is owned by me and my family. And I’m most definitely not Chinese.”

The company has touted its proximity to military installations, along with
other local attractions, in some of its marketing materials in China. …

Walton said it has investors from around the world who can take brief tours of
their land holdings, but don’t otherwise have access to the land, which the
company then aims to sell to developers.

I don’t know enough about the ownership structures here to really comment, but
“few agree on what even counts as owned by China” does seem like a pretty
standard problem in these sorts of regulatory regimes.


Trade secrets

One thing you can do is:

 * Take a job at a quantitative asset manager.
 * Email yourself all of the company’s models and secret sauce.
 * Use it to set up your own quantitative hedge fund.
Compared to painstakingly building the models and discovering useful signals
yourself, this is a pretty convenient shortcut. There are disadvantages:

 * Painstakingly doing it yourself might make you better at it: Your
employer’s signals probably won’t be that good for that long, and if you just
downloaded them you probably won’t understand them well enough to keep
improving the models and finding new trades.
 * If you copy your employer’s models, you’ll also end up copying their
trades, which might get crowded and lose their edge.
 * You’ll get, like, extremely sued? And arrested? Not legal advice, but this
is very much not allowed, and peopledo get arrested for it
<https://www.vanityfair.com/news/2013/09/michael-lewis-goldman-sachs-programmer?srsltid=AfmBOop54QJXUvRZ0XpKCvbyLwXhX-mq23lsZEma3f4SlmDLKN1EyVNm>
.
Here is a potential solution to Problems 2 and 3:

 * Be a citizen of the People’s Republic of China.
 * Come to the US and take a job at a US quantitative asset manager.
 * Go to China and log into your work computer remotely.
 * (Use a virtual private network, because your work computer doesn’t actually
allow logins from China.)
 * Download all the models and secret sauce.
 * Use them to set up your own quantitative hedge fund in China, trading
Chinese stocks.
 * Get charged with a crime in the US, but don’t get extradited.
I guess? Not legal advice or anything but here’s this
<https://www.bloomberg.com/news/articles/2024-11-04/chinese-hedge-fund-manager-indicted-by-us-in-trade-secrets-case?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
:

A co-founder of high-flying Chinese quantitative hedge fund Pinestone Asset
Management Co. has been indicted in the US for alleged theft of trade secrets,
according to people with knowledge of the matter.

Xiao Zhang, a 33-year-old Chinese citizen from Shanghai, was indicted by a
federal grand jury in Boston for allegedly stealing secrets from an
unidentified global investment management firm while he was working for it in
2021, according to a statement dated Oct. 31 from the US Attorney’s Office in
Massachusetts.

Here are the Justice Department press release
<https://www.justice.gov/usao-ma/pr/citizen-peoples-republic-china-indicted-theft-trade-secrets>
 and theindictment
<https://assets.bwbx.io/documents/users/iqjWHBFdfxIU/rYhVFePk6Ugk/v0>:

According to the indictment, in 2021, Zhang allegedly utilized a virtual
private network (VPN) to access his employer’s network from the PRC, which
enabled him to circumvent the company’s controls. Zhang then allegedly made
copies of his employer’s code, projects and research, and sent the copies
through a PRC-based file-sharing application, enabling him to again evade his
employer’s controls. It is alleged that Zhang then utilized the stolen items
with the intent of establishing his own investment firm in the PRC.

I will say it seems hard
<https://www.bloomberg.com/news/articles/2024-09-27/quant-hedge-funds-trapped-in-short-squeeze-after-china-glitch?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
 to run a quant fund in China, and the intuitions that you develop from long
experience with finding useful equity signals in the US might not be all that
valuable when applied to China. But maybe the models still are.


Things happen

People are worried about the basis trade
<https://www.bloomberg.com/news/articles/2024-11-04/hedge-fund-basis-trade-faces-scrutiny-as-regulators-mull-probe?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
. Wall Street frenzy creates$11bn debt market
<https://www.ft.com/content/41bfacb8-4d1e-4f25-bc60-75bf557f1f21> for AI groups
buying Nvidia chips. Nvidia Set to Replace Intel in theDow Jones Industrial
Average
<https://www.bloomberg.com/news/articles/2024-11-01/nvidia-set-to-replace-intel-in-the-dow-jones-industrial-average?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
. B. Riley Chairman Is ‘Personally Sick’ asFRG
<https://www.bloomberg.com/news/articles/2024-11-04/b-riley-chairman-feels-personally-sick-as-frg-goes-bankrupt?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
 Goes Bankrupt.TGI Fridays
<https://www.wsj.com/finance/tgi-fridays-files-for-bankruptcy-following-years-of-diners-declining-interest-1345b148?mod=itp_wsj>
 Files for Bankruptcy Following Years of Diners’ Declining Interest. China
piles pressure on rich people and companies tocough up taxes
<https://www.ft.com/content/1570747c-313d-49e9-afb0-2567e003438e>. State Street
Asks SEC for Blessing to FitETFs into 401(k) Plans
<https://www.bloomberg.com/news/articles/2024-11-01/state-street-asks-sec-for-blessing-to-fit-etfs-into-401-k-plans?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
. TheSALT Deduction Fight
<https://www.wsj.com/politics/policy/the-salt-deduction-fight-is-coming-backwhoever-wins-the-election-956d0513?mod=hp_lead_pos510>
 Is Coming Back—Whoever Wins the Election. “Doctors arelike any other employee
<https://www.wsj.com/lifestyle/careers/young-doctors-want-work-life-balance-older-doctors-say-thats-not-the-job-6cb37d48?mod=itp_wsj>
, and that’s how the new generation is behaving.” Even Some High-Income
AmericansCan’t Afford New Cars
<https://www.bloomberg.com/news/articles/2024-11-04/soaring-2024-new-car-prices-turn-more-buyers-toward-used-vehicles?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
 Anymore. “When he reached the finish line 12 minutes later, ‘you could tellthe
dogs were really happy and excited
<https://www.seattletimes.com/nation-world/he-walked-38-dogs-at-once-my-arms-felt-like-they-were-on-fire/>
 at the accomplishment.’” Instagram Plans toUse AI to Catch Teens Lying About
Age
<https://www.bloomberg.com/news/articles/2024-11-04/instagram-plans-to-use-ai-to-catch-teens-lying-about-age?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
. Meta’s plan fornuclear-powered AI data centre thwarted by rare bees
<https://www.ft.com/content/ed602e09-6c40-4979-aff9-7453ee28406a>.

If you'd like to get Money Stuff in handy email form, right in your inbox,
pleasesubscribe at this link
<http://link.mail.bloombergbusiness.com/join/4wm/moneystuff-signup&hash=54223001ca3ffcf40f2629c25acea67a>
. Or you can subscribe to Money Stuff and other great Bloomberg newslettershere
<https://login.bloomberg.com/newsletters>. Thanks!


 <https://link.chtbl.com/Money-Stuff-Podcast-Newsletter>


[1] The US Secured Overnight Financing Rate was about 0.01% at the time —
crushed by Covid — so 1.3% was a fine rate.

[2] It’s all short-term assets, but short-term rates had collapsed in the
couple of weeks leading up to these trades, so these assets were up a bit.

[3] Because it’s more or less illegal for a JPMorgan fund to sell assets
directly to another JPMorgan fund, so it’s all done through outside brokers.

[4] This is an approximate quotation
<https://www.bloomberg.com/opinion/articles/2021-07-07/owning-chinese-companies-is-complicated?cmpid=BBD110424_MONEYSTUFF&utm_medium=email&utm_source=newsletter&utm_term=241104&utm_campaign=moneystuff>
 from DiDi Global Inc.’sprospectus
<https://www.sec.gov/Archives/edgar/data/1764757/000104746921001227/a2243300z424b4.htm#dk10201_corporate_history_and_structure>
. There are other agreements; my favorite is that there are agreements with the
spouses of the somewhat nominal Chinese shareholders of the underlying Chinese
company, in which they “agreed not to assert any rights over the equity
interest in Xiaoju Technology held by the respective shareholder.” You would
not want the nominal shareholders’ spouses to take the business away from the
US-listed Caymans company.


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
<https://links.message.bloomberg.com/e/eh?_t=f574328d4d0c4c359b90d8e49b10e21d&_m=d1e5aff5e9014ca28a97384e102ff6c7&_e=kv8OjQPsjO2Z7K1yaQrwSX-pIJkXe0AGfAGp7GhAMDA-xgoztcDae9y6jGumSbCmRzfhdMDL2UeRNu0GMINVOq5s9nI1rsJ7ajhRjEp1se3RBJLvtlnXW9ou3KcZC_5htg5IdWOImBf-e2zVl4iktos6abDAcOu_zigazlmAks0Kt1SUyq1an-_d_n6eDf2Q79p_IQyogKgPOSrXg3S8Yilka68TYd4wIj8GLG0euctQ6n60JN1_Dwm9Rsiy2qvt2vPLvTYabZcuLVJ862ySSQ%3D%3D>