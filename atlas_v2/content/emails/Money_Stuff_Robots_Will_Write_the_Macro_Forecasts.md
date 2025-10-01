# Money Stuff: Robots Will Write the Macro Forecasts

**Source**: inputs/saved_emails/Money Stuff Robots Will Write the Macro Forecasts_Wed,_26_Feb_2025_19-06-14_+0000_19543a744bf87115.eml
**Type**: email
**Created**: 2025-08-25T02:54:09.840927

---

Money Stuff 
 There are two basic ways to use artificial intelligence to predict stock 
prices: You build a deep learning model to predict stock prices: Yo 


 <> 
 
<https://sli.bloomberg.com/click?s=825881&stpe=default&li=12737188&m=21d6dea82d6b16615cf44233be620525&p=02262025>



LLM forecasters

There are two basic ways to use artificial intelligence to predict stock 
prices:

 * You build a deep learning model to predict stock prices: You set up a deep 
neural net, you feed it tons of historical data about stocks, and you train it 
to figure out how that data predicts stock price returns. Then you run the 
model on current data, it predicts future returns, and you buy the stocks that 
it thinks will go up. 
 * You take some deep learning model that someone else built, a large language 
model, one that is good at predictingtext. It is trained on a huge corpus of 
human language, and it is good at answering questions like “write a poem about 
a frog in the style of W.B. Yeats.” Andyou ask it questions like “write a 
report about whether I should buy Nvidia Corp. stock in the style of Warren 
Buffett.” And then it trains on the writing style of Warren Buffett, which 
reflects his thinking style, and its answer to your question — you hope — 
actually reflects what Buffett might say, or what he might say if he was a 
computer with a lot of time to think about the question. And because Warren 
Buffett is good at picking stocks, this synthetic version of him is useful to 
you. You read the report, and if robot Warren Buffett says “buy” you buy. 
The first approach makes obvious intuitive sense and roughly describes what 
various quantitative investment firms actually get up to: There might be 
patterns in financial data that predict future returns, and deep learning is a 
statistical technique for finding them.

The second approach seems … sort of insane and wasteful and indirect? Yet also 
funny and charming? It is an approach to solving the problem by first solving a 
much harder and more general problem: Instead of “go through a ton of data to 
see what signals predict whether a stock goes up,” it’s “construct a robot that 
convincingly mimics human consciousness, and then train that robot to mimic the 
consciousness of a particular human who is good at picking stocks, and then 
give the robot some basic data about a stock, and then ask the robot to predict 
whether the human would predict that the stock will go up.”

My impression is that there are people using the first approach with 
significant success — this is roughly, like Renaissance Technologies — and the 
second approach is mostly me making a joke. But notentirely. The second 
approach has some critical advantages:

 * Somebody else — OpenAI or xAI or DeepSeek or whoever — already built the 
large language model for you, at great expense. If you are on the cutting edge 
of machine learning and can afford to pay for huge quantities of data and 
researchers and computing capacity, go ahead and build a stock-predicting 
model, but if you are just, say,an academic, using someone else’s model is 
probably easier. The large language model companies release their models pretty 
widely. The stock model companies do not. You can’t, like, pay $20 a month for 
Rennaissance’s stock price model. 
 * Because the large language model’s output is prose, its reasoning is 
explainablein a way that the stock model is not. The stock model is like “I 
have looked at every possible combination of 100,000 data time series and 
constructed a signal that is a nonlinear combination of 37,314 of them, and the 
signal says Nvidia will go up,” and if you ask why, the model will say “well, 
the 37,314 data sets.” You just have to trust it. Whereas robot Warren Buffett 
will write you a nice little report, withreasons you should buy Nvidia. The 
reasons might be entirely hallucinated, but you can go check. Iwrote once <>: 
“One criticism that you sometimes see of artificial intelligence in finance is 
that the computer is a black box that picks stocks for reasons its human users 
can’t understand: The computer’s reasoning process is opaque, and so you can’t 
be confident that it is picking stocks for good reasons or due to spurious 
correlations. Making the computer write you an investment memo solves that 
problem!” 
 * I do think that the aesthetic and social appeal of typing in a little box 
to have a chat with your friend Robot Warren is different from the black box 
just giving you a list of stocks to buy. This probably doesn’t matter too much 
to rigorous quantitative hedge funds, but it must matter to someone. Wetalked 
last year <> about a startup that was launching “a chatbot that offers 
stock-picking advice” to retail brokerage customers, and it seemed like the 
goal of the project was not “the chatbot will always tell you stocks that will 
go up” but rather “the chatbot will offer a convincing simulacrum of talking to 
a human broker,” who also will not always tell you stocks that will go up. You 
call the broker anyway. Now you can text the chatbot instead. 
And so we also talked last year <> about an exchange-traded-fund firm that 
would use large language models to simulate human experts — ones with 
characteristics of particular humans, like Buffett — to make stock picks. Why 
use LLMs rather than build a model to directly predict stock prices? Well, 
because the LLM is already there, and the data is already there, and the 
schtick is a little more human than “here’s our black box.”

Anyway here’s a paper on “Simulating the Survey of Professional Forecasters <>
,” by Anne Lundgaard Hansen, John Horton, Sophia Kazinnik, Daniela Puzzello and 
Ali Zarifhonarvar:

We simulate economic forecasts of professional forecasters using large 
language models (LLMs). We construct synthetic forecaster personas using a 
unique hand-gathered dataset of participant characteristics from the Survey of 
Professional Forecasters. These personas are then provided with real-time 
macroeconomic data to generate simulated responses to the SPF survey. Our 
results show that LLM-generated predictions are similar to human forecasts, but 
often achieve superior accuracy, particularly at medium- and long-term 
horizons. We argue that this advantage arises from LLMs' ability to extract 
latent information encoded in past human forecasts while avoiding systematic 
biases and noise. Our framework offers a cost-effective, high-frequency 
alternative that complements traditional survey methods by leveraging both 
human expertise and AI precision.

See you could imagine predicting future macroeconomic data by feeding a ton of 
current macroeconomic data into a deep learning model and trying to get it to 
make predictions. This has the advantage of directly answering the question, 
but it has important disadvantages like “you need a lot of data” and “you have 
to build the model.”

Or you could predict future macroeconomic data by prompting a commercial large 
language model with some current data and asking it to pretend to be a human 
forecaster. This has the advantage that the model already exists and you just 
have to type in a good prompt, probably one with a lot less data than a large 
macro model would want. Also there is “latent information encoded in past human 
forecasts.” From the paper:

Consider the problem of forecasting a vector of economic variables H periods 
ahead, denoted byyt+H. We assume that the true forecasting process is governed 
by a functionf that depends on two types of information available at time t: 
observable dataxt and unobservable factors zt, plus an unpredictable zero-mean 
errorε. …

The unobservable factors zt represent any additional information that can help 
predictyt+H but is not captured by xt. This may include private insights, tacit 
domain knowledge, internalized heuristics, and intuition.

Humans can access both observable and unobservable information. However, they 
process this information imperfectly, which introduces an error term. …

Algorithms, by contrast, can only access xt, but they process xt efficiently. 
… This represents traditional algorithmic forecasting using machine learning 
techniques. We, however, employ LLMs, which form expectations in a 
nondeterministic manner.

That is: Humans can bring some secret sauce to macroeconomic forecasts, some 
extra source of insight — “tacit domain knowledge,” etc. — that is not captured 
in the data used by machine learning algorithms to make forecasts. But if you 
train a machine-learning algorithmon humans, it has access to that 
human-specific secret sauce, and can make better predictions.

 
<https://sli.bloomberg.com/click?s=868432&stpe=default&li=12737188&m=21d6dea82d6b16615cf44233be620525&p=02262025>

 
<https://sli.bloomberg.com/click?s=868432&stpe=default&li=12737188&m=21d6dea82d6b16615cf44233be620525&p=02262025>

BlackRock DEI loans

Seven hundred years ago, in 2021, BlackRock Inc. struck a deal <> to borrow 
some money from a group of banks led by Wells Fargo & Co. [1]  <> As part of 
the agreement, BlackRock and the banks agreed to three sets of “sustainability 
targets” for BlackRock’s business: It would aim to employ more Black and 
Hispanic employees, have more women in leadership roles, and manage more assets 
with sustainable-investing mandates. [2]  <> If it hit enough of these targets, 
its commitment fee for the credit facility — the amount it paid the banks every 
year even if it didn’t actually draw any money — would go down by 0.01% from 
the baseline agreed fee, and its interest rate — the amount it paid if itdid 
actually take any money — would go down by 0.05%. If it missed enough of the 
targets badly enough, its commitment fee and rate would goup by 0.01% and 
0.05%. So if BlackRock was very diverse, it would pay 0.02% less per year (in 
commitment fees) than if it was very not diverse. (As far as I can tell it has 
not drawn on the credit facility, so I focus on the commitment fee.)

You could try to analyze this provision in a normal credit-y way. Many credit 
agreements contain some sort of rate adjustment for things that make the loan 
riskier or safer. You could have a credit agreement where the rate is linked to 
credit ratings or net income or leverage ratios: If the company’s credit gets 
riskier, it has to pay its banks more; if it gets safer, it can pay them less. 
You can tell a story like this here. “These sustainability targets do in fact 
improve the long-term sustainability of the firm — thus the name — so the more 
diverse BlackRock’s leadership is, the more stable it will be, and the safer 
its debt will be. Therefore the banks should be willing to accept 0.02% less 
interest in states of the world where BlackRock is more diverse than in states 
where it is less diverse, because the more-diverse states are better for the 
credit, and the banks want to incentivize BlackRock to make decisions that are 
good for the credit.”

I do not think this is the right analysis? [3]  <> Or rather, I do not think 
it is what the banks or BlackRock were thinking. I have various reasons for 
this belief, but a simple one is: 0.02% is not very much. A bank making 
decisions about credit risk is probably thinking things like “if this company’s 
income goes down a lot, its credit will be a lot riskier, and we should charge 
a lot more,” or at least a medium amount; credit decisions rarely come as 
fine-tuned as 0.02%. It’s possible that a more diverse BlackRock really would 
be 0.02% less risky than a less diverse one, and that fee difference is 
correct, but if that’s true it’s sort of a lucky accident.

A more realistic analysis might be:

 * The banks, in 2021, liked being able to say <> that they were doing some 
large volume of loans that were sustainable, sustainability-linked, ESG 
(environmental, social and governance investing), etc. Adding a — small — 
diversity incentive transformed this loan into a “sustainability-linked” loan, 
and the banks could put in their reports that they were doing a lot of 
sustainable lending. 
 * BlackRock, in 2021, was also very into that sort of thing <>, and taking 
out the sustainability-linked loan was good press for it. 
Anyway, right, that was 700 years ago. Here’s the Wall Street Journal today <>:

BlackRock cut references to its diversity, equity and inclusion strategy in 
its latest annual report, joining the list of Wall Street firms and corporate 
employers distancing themselves from DEI.

It is a particularly notable turnaround for BlackRock, where Chief Executive 
Larry Fink once embraced DEI and environmental, social and governance investing.

“Just as we ask of other companies, we have a long-term strategy aimed at 
improving diversity, equity and inclusion at BlackRock,” Fink wrote in a 2021 
letter to shareholders. “To truly drive change, we must embed DEI into 
everything we do.”

In BlackRock’s annual report filed Tuesday, the world’s largest asset manager 
deleted statements it included in past reports about a diverse and inclusive 
workforce being “a commercial imperative and indispensable.”

BlackRock removed references to its “three pillar DEI strategy.” Gone also was 
a statement that “BlackRock views transparency and measurement as critical to 
its strategy,” and a breakdown of its U.S. employees by gender and 
self-disclosed ethnicity.

And — perhaps — more substantively:

A subtle footnote in the annual filing showed BlackRock backing away from DEI 
in another way. In 2021, the company struck a financing deal with a group of 
banks that linked the lending costs for a $4.4 billion credit facility to its 
ability to achieve certain goals, such as meeting targets for women in senior 
leadership and Black and Latino employees in its workforce.

BlackRock said the ESG-linked credit facility, a novel arrangement at the 
time, would enhance its accountability.

Those metrics will no longer be enforced. BlackRock disclosed Tuesday that it 
amended the credit facility to “update the sustainability-linked pricing 
mechanics to remove existing metrics.”

Here is the annual report <>; apparently the sustainability-linked metrics 
were removed in May 2024 and “new metrics, if any” might be set later. [4]  <> 
I would love to have been at those negotiations. Do you think they got heated?

BlackRock: We will need to stop doing the thing where we pay you an extra 
0.01% if we’re not diverse enough, and we pay you 0.01% less if we’re very 
diverse.

Banks: What? Those metrics were crucial to our credit analysis, and we are not 
comfortable just deleting them. You promised us that you would work to meet 
diversity targets, and if you can’t do that then we will have to reevaluate our 
entire lending relationship.

BlackRock: ...

Banks: …

BlackRock: Lol.

Banks: Ahahaha we had you going for a minute there. No it’s fine just delete 
it, who cares, we’re not reporting our diversity-linked lending anymore either.

There is something a little annoying about this. A loan agreement is mostly 
negotiated between lenders who want one thing and a borrower who wants another 
thing. Generally speaking, if the loan agreement says the borrower has to pay 
more in some circumstances, it’s because the lenders are worried about those 
circumstances and have insisted on some protections and incentives. If the 
borrower comes to the lenders and says “can we just forget about that,” the 
lenders will say things like “no” or “what” or “are you in trouble?”

And so, in 2021, when BlackRock signed this agreement, it was meant to signal 
some sort of costly commitment: If we fail to hit our diversity targets, it 
will cost us, because there are economically motivated banks on the other side 
who will hold us to those targets. But there weren’t! It was all pretty much 
fake. There was no real commitment, and when it became inconvenient for 
BlackRock, it became similarly inconvenient for the banks, and they could just 
forget about it.


Related parties

Classically, if you are the chief executive officer of a public company, and 
you are also a big shareholder in adifferent company, and your public company 
does a deal with the other company that you own, that is a conflict of 
interest. The board of directors of your public company should set up a special 
committee of independent directors to review the transaction and make sure it’s 
fair, and you should recuse yourself from the negotiations, and when the deal 
happens your public company will have to disclose it extensively so 
shareholders understand what you’re getting up to.

So Elon Musk is the chief executive officer of Tesla Inc., and he was also a 
big shareholder in a company called SolarCity Corp. In 2016, SolarCity was not 
in great shape, and Musk decided — sorry sorry sorry, Tesla’s and SolarCity’s 
boards of directors decided — that Tesla should buy SolarCity. It did, Tesla 
shareholders sued, and there was a drawn-out legal fight about the obvious 
conflicts of interest involved in one of Musk’s companies bailing out another 
one. EventuallyMusk won <>, with a judge concluding that the deal and how it 
was approved were not perfect, but were good enough.

Since then Musk has moved on to bigger things, and at the Wall Street Journal 
todayJonathan Weil asks questions like <>: Does Elon Musk own the US 
government? And: If so, what does that do to Tesla’s disclosure obligations?

Here is the question at hand: Are Tesla and the government “related parties” 
for purposes of generally accepted accounting principles? The answer would 
appear to be yes, as wild as that might seem. ...

The related-party designation would mean Tesla, in its disclosures to 
investors, could have to start reporting transactions it has with the 
government if they are significant. It also would underscore how powerful Musk 
has become. U.S. accounting standards say the reason for requiring such 
disclosures is that “transactions involving related parties cannot be presumed 
to be carried out on an arm’s-length basis, as the requisite conditions of 
competitive, free-market dealings may not exist.”

Other public companies have named the U.S. government as a related party 
before in their disclosures, including American International Group, General 
Motors, Fannie Mae and Freddie Mac. But that was because the government had 
bailed them out and taken large ownership stakes during the 2008 financial 
crisis. If Tesla were to start identifying the government as a related party in 
its reports to investors, it would be because of the amount of control Musk 
wields over the government, not the other way around.

Under U.S. accounting standards, Tesla and the government would be considered 
related parties if one of them “can significantly influence the management or 
operating policies of the other to an extent that one of the transacting 
parties might be prevented from fully pursuing its own separate interests.”

I don’t know how much commercial dealing Tesla does with the government; this 
is probably more relevant for SpaceX, but SpaceX is private so there is less 
emphasis on its accounting. Still: sure. We are not at the point where Tesla 
would have toconsolidate the government into its accounting, which would be the 
much funnier outcome. Put $34 trillion of government debt on Tesla’s balance 
sheet just to mess with analysts.

Elsewhere Bloomberg’s Kara Carlson reports <>:

After Elon Musk made gestures resembling a Nazi salute at an inauguration 
event for President Donald Trump last month, [Tesla owner Tae Helton] wants 
nothing to do with the brand.

“The pride and the good feeling I had driving in it is gone for me,” Helton 
said of the Model 3 he’s driven only around 2,500 miles. The politically 
moderate 49-year-old plans to pay off his car loan early and trade in the sedan 
before year-end.

Helton has company among Tesla customers and consumers. The EV maker’s sales 
fell 45% across Europe in January, following its first annual decline in global 
deliveries in over a decade. The company is showing particular signs of strain 
in places where its chief executive officer is inserting himself in politics in 
ways that run counter to Tesla’s stated mission and values. …

“Tesla’s biggest challenge in 2025 isn’t technology — it’s perception,” says 
Jacob Falkencrone, global head of investment strategy at Saxo, the Danish bank 
with more than €105 billion in client assets. “Elon Musk’s political baggage is 
now weighing on sales, brand loyalty and investor confidence.”

Readers periodically email me with questions along the lines of: “If Elon Musk 
keeps doing political stuff that alienates Tesla’s customers and pushes down it
sales and market value <>, is that a violation of his fiduciary duty to 
shareholders?” I suppose the answer is: I dunno, why don’t you sue him in
Texas’s new business courts <> and find out?

I think that, in general, lawsuits like this — involving not a conflicted 
transaction but rather a CEO who is making controversial decisions — are hard 
to win. But I also think that everything is securities fraud, and wetalked last 
year <> about a lawsuit against Target Corp. alleging that it angered customers 
by doing a Pride Month marketing event and that that was somehow securities 
fraud. That struck me as not a very strong case, but a federal judge in Florida 
let it go ahead, so who knows. I don’t love your chances of winning a lawsuit 
in Texas claiming that Elon Musk’s far-right provocations are a violation of 
his fiduciary duties to shareholders, but it would be a little funny to find 
out.


Junior banker resumes

Elsewhere in asking AI to mimic human consciousness <>:

For junior bankers using AI to help draft their resumes: Recruitment firms are 
on to you.

Words like “robust” and “meticulous” are telltale signs that banking hopefuls 
have enlisted AI to polish up their resumes, according to Wall Street executive 
search firms. Other giveaways are overused phrases like “ever-evolving,” or 
when candidates say they played “a significant role shaping” something, 
recruiters say.

Like many job applicants, young bankers are increasingly using AI tools like 
ChatGPT to draft their resumes. But it becomes an issue for recruiters when 
they don’t properly proofread their applications and errors creep in. This 
raises red flags for their potential investment banking employers who prize 
attention to detail, accuracy and seek applicants who don’t take short cuts.

“If this person didn’t bother to take the time to build a resume, why would I 
take the time reviewing it and interviewing them,” said Brianne Sterling, head 
of investment banking recruitment at Selby Jennings. “A lot of what these 
bankers are doing in their first jobs is putting together financial models and 
presentations for clients. It’s probably an immediate red flag for employers if 
they see a resume with errors in it or looks generic.”

What? I don’t believe this. First of all, the reason that the AI comes up with 
cliches is that it is trained on resumes, which are full of cliches. The AI 
tells people to call themselves “meticulous” on their resumes because, left to 
their own devices, people call themselves “meticulous” on their resumes.

Second: “It’s probably an immediate red flag” for an investment bank if they 
see a resume from ajunior applicant that “looks generic”? Do you hear yourself? 
Here I will write you a perfect resume for a junior banking job:

EDUCATION:

- Harvard University, AB, Applied Math
- GPA: 4.0
- Captain of lacrosse team
- President of investing club

WORK EXPERIENCE: 

- Summer 2024 internship at Morgan Stanley (Financial Sponsors Group): Played 
significant role shaping ever-evolving coverage of financial sponsors. 
Meticulously built robust LBO models.
- Summer 2023 management internship at $100 billion market cap industrial 
conglomerate where my mom is the CEO and controlling shareholder.

There, done, you don’t need AI. “Generic”! Generic is good.


Things happen

Wall Street Gamblers Get Crushed as Leveraged ETF Losses <> Hit 40%. Nvidia’s 
AI Boom Brings Riches toPartners Like Dell <>, at a Cost. Hooters Bankruptc <>y 
Threatens Even Bonds Supposed to Be Bankruptcy-Proof. GMBoosts Investor Payout 
<> With New Buybacks, Dividend Hike. China to Inject at Least $55 Billion of 
Fresh Capital IntoSeveral Big Banks <>. FTX’s $950 Million Bankruptcy Fees <> 
Among Costliest Since Lehman. Private-Equity Firm Roark Nears $1 Billion Deal 
forDave’s Hot Chicken <>. People in industrialised societies sleep better <>, 
research finds. Woman pleads guilty of attempting to defraud Elvis Presley’s 
family ofGraceland <> estate. Apple Pledges to Fix Transcription Glitch <> That 
Replaces ‘Racist’ With ‘Trump.’

If you'd like to get Money Stuff in handy email form, right in your inbox, 
pleasesubscribe at this link <>. Or you can subscribe to Money Stuff and other 
great Bloomberg newslettershere <>. Thanks!

[1] This is a little loose; technically it amended an existing revolving 
credit agreement to increase its size and add terms including the diversity 
clause.

[2] The details are in Annex A and Annex B at the end of the amendment document
 <> that BlackRock filed with the US Securities and Exchange Commission. The 
actual targets are blank in the filing but you get the idea.

[3] An alternative analysis is: Some credit agreements offer a better rate if 
the borrowerdoes other business <> with the bank. This is in part a credit 
enhancement — if you keep a deposit at the bank, that’s sort of collateral for 
the loan — but it’s in part just a business decision; if the bank is making 
money from you elsewhere then it is happier to charge you less on the loan. 
There’s something like that going on here: The bank gets to tout its 
sustainability-linked lending program in a high-profile way, and that was 
desirable in 2021, so it was willing to take a bit less interest.

[4] The new metrics were going to be set following the closing of BlackRock’s 
Global Infrastructure Partners deal, whichhappened in October <>, shrug.


 <> 

Follow Us  <>  <>  <>  Get the newsletter  <> 


Like getting this newsletter?  Subscribe to Bloomberg.com <> for unlimited 
access to trusted, data-driven journalism and subscriber-only insights.

Before it’s here, it’s on the Bloomberg Terminal. Find out more about how the 
Terminal delivers information and analysis that financial professionals can’t 
find anywhere else.Learn more <>.

Want to sponsor this newsletter?  Get in touch here <>.

 You received this message because you are subscribed to Bloomberg's Money 
Stuff newsletter. 
Unsubscribe <> | Bloomberg.com <> | Contact Us <> 

 <>  |  <> 
Bloomberg L.P. 731 Lexington, New York, NY, 10022  
<https://links.message.bloomberg.com/s/eh/2u0dxLaAj9GuRDicLOXxNajfnkjQKnKgW82T2PYRC8F48--Xn2c9e3_32sf0aaTrFhJhPDgYjlI_XD90hSgAH2l8cucWunZUjHWbEQhqs_fdDO0tkgsMpRawQcPbjhSVj1lN3n6S0PxQOxDIFNE_gmrNQ_gggtfBiRR3JaD3rD7v81lhDBiLk4o76Hzs2hr1eZ58bDn7C7RfJQmXGmumUSab7wod1jA3DUqw9LfbR_KaOM48KYHS4JXZro10p57xhlMQ22EynGq3UCGG807FsAABYFdtK0DHFNx425kWx6NWIbGW7Nn8YJPCxo9DN_PNVxT3TtLPlq-ugj_GvEcaWw/Y6Hl-WV0uVlTj6mPwbcLcZgGbChtZXCG/6>