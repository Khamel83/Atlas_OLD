# OpenAI's New Model, How o1 Works, Scaling Inference (Stratechery Update 9-16-2024)

**From:** Ben Thompson <email@stratechery.com>
**Date:** Mon, 16 Sep 2024 14:39:29 +0000
**Source:** inputs/saved_emails/OpenAI's New Model, How o1 Works, Scaling Inference (Stratechery Update 9-16-2024)_Mon,_16_Sep_2024_14-39-29_+0000_191fb466cdbb073c.eml
**Processed:** 2025-08-24T19:13:10.819963

OpenAI's has a new model called o1; it's a new approach that solves some of the key limitations of current LLMs — and it solves crossword puzzles.

View in browser ( https://stratechery.com/2024/openais-new-model-how-o1-works-scaling-inference/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI0L29wZW5haXMtbmV3LW1vZGVsLWhvdy1vMS13b3Jrcy1zY2FsaW5nLWluZmVyZW5jZS8iXX0sImV4cCI6MTcyOTA4OTU2OCwiaWF0IjoxNzI2NDk3NTY4LCJpc3MiOiJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvb2F1dGgiLCJzY29wZSI6ImZlZWQ6cmVhZCBhcnRpY2xlOnJlYWQgYXNzZXQ6cmVhZCBjYXRlZ29yeTpyZWFkIGVudGl0bGVtZW50cyIsInN1YiI6IlJzZXVZRThqZ0hlUHBXSmYxZkFiNEMiLCJ1c2UiOiJhY2Nlc3MifQ.kcDil8PRzwZ9Dwd-_zPl4xsZRUyVbvkqzv-CZw0UMPMKWQpi3rCu6E-64BFZcOs3DjI6JOu8LPDX98ufw1MdPupB0vAnsZNFxm2eiMpItDS5CWttRvc1idrW97Di9c5LCzA_-WGEIzz2vVVJ0OPltTpx4VV0NxXlLGv_f5o5vKaeqRp2WMKW6ZAtY-RwM7ttROwzesiMYo8w9aFUmaFhqlh6Rf6b2z_w_HCwSC8t-qwdWNZGBg0EmJSJcqkB7rDvmOlwhJfbrf4NelRab5hCRQhEOalO5p4EJqmj5MV3WbYty42i3x1datujwKTN9U_6obIdnrb72QJfJenFHYRAhg )

( https://stratechery.com )

***************************************************
OpenAI's New Model, How o1 Works, Scaling Inference
***************************************************

( https://stratechery.com/2024/openais-new-model-how-o1-works-scaling-inference/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI0L29wZW5haXMtbmV3LW1vZGVsLWhvdy1vMS13b3Jrcy1zY2FsaW5nLWluZmVyZW5jZS8iXX0sImV4cCI6MTcyOTA4OTU2OCwiaWF0IjoxNzI2NDk3NTY4LCJpc3MiOiJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvb2F1dGgiLCJzY29wZSI6ImZlZWQ6cmVhZCBhcnRpY2xlOnJlYWQgYXNzZXQ6cmVhZCBjYXRlZ29yeTpyZWFkIGVudGl0bGVtZW50cyIsInN1YiI6IlJzZXVZRThqZ0hlUHBXSmYxZkFiNEMiLCJ1c2UiOiJhY2Nlc3MifQ.kcDil8PRzwZ9Dwd-_zPl4xsZRUyVbvkqzv-CZw0UMPMKWQpi3rCu6E-64BFZcOs3DjI6JOu8LPDX98ufw1MdPupB0vAnsZNFxm2eiMpItDS5CWttRvc1idrW97Di9c5LCzA_-WGEIzz2vVVJ0OPltTpx4VV0NxXlLGv_f5o5vKaeqRp2WMKW6ZAtY-RwM7ttROwzesiMYo8w9aFUmaFhqlh6Rf6b2z_w_HCwSC8t-qwdWNZGBg0EmJSJcqkB7rDvmOlwhJfbrf4NelRab5hCRQhEOalO5p4EJqmj5MV3WbYty42i3x1datujwKTN9U_6obIdnrb72QJfJenFHYRAhg ) Monday, September 16, 2024

Listen to this Update in your podcast player ( https://stratechery.passport.online/member/podcast?url=https%3A%2F%2Frss.stratechery.passport.online%2Ffeed%2Fpodcast%2F6EynvegSpNaDpnt4DJsHzD )

Good morning,

Last Thursday’s episode of Sharp Tech ( https://sharptech.fm/member/episode/the-strategic-logic-of-the-i-phone-16-services-upside-and-downside-steve-jobs-and-modern-apple ) was about Apple’s recent iPhone event; I thought this was a good one, particularly the last 20 minutes about that age-old question, “Does Apple miss Steve Jobs?” We got into the same topic on Friday’s Dithering ( https://daringfireball.net/linked/2024/09/14/dithering-apple-event ).

On to the Update:

OpenAI’s New Model
------------------

From Bloomberg ( https://www.bloomberg.com/news/articles/2024-09-12/openai-releases-o1-model-with-reasoning-capabilities ) :

OpenAI is releasing a new artificial intelligence model known internally as “Strawberry” that can perform some human-like reasoning tasks, as it looks to stay at the top of a crowded market of rivals. The new model, called o1 , is designed to spend more time computing the answer before responding to user queries, the company said in a blog post ( https://openai.com/index/introducing-openai-o1-preview/ ) Thursday. With the model, OpenAI’s tools should be able to solve multi-step problems, including complicated math and coding questions.

“As an early model, it doesn’t yet have many of the features that make ChatGPT useful, like browsing the web for information and uploading files and images,” the company said. “But for complex reasoning tasks this is a significant advancement and represents a new level of AI capability. Given this, we are resetting the counter back to 1 and naming this series OpenAI o1.”

I think this model is really interesting, and definitely a breakthrough; there are also a lot of unknowns as to exactly how it works, both in terms of the model and in terms of the operational infrastructure necessary to support it. With that in mind, consider this Update as my initial draft on how I am thinking about this model and what it means; I expect to update my thinking as we get more understanding on how exactly it works.

For now, though, I thought the following example (inspired by Ethan Mollick ( https://www.oneusefulthing.org/p/something-new-on-openais-strawberry ) ) is a great example of what this model is capable of: solving the New York Times Daily Mini crossword. Specifically, I chose last Saturday’s crossword ( https://www.nytimes.com/crosswords/game/mini/2024/09/14 ) , which is a 7×7 puzzle (the rest of the week is 5×5). I’ll get to why I chose Saturday in a moment, but here is the puzzle:

The Saturday, September 14, NYT mini crossword ( https://www.nytimes.com/crosswords/game/mini/2024/09/14 )

o1 is text-only, so I needed to describe the puzzle; here was my prompt:

Solve this 7×7 crossword puzzle

Row 1 has three blanks in columns 1 through 3
Row 2 has one blank in column 1
Row 3 has one blank in column 1
Row 4 has one blank in column 4
Row 5 has one blank in column 7
Row 6 has one blank in column 7
Row 7 has three blanks in columns 5 through 7

1-across: Shortens, as a skirt
5-across: What each word in “My Very Educated Mother Just Served Us Noodles” is a stand-in for
7-across: Puzzling question
8-across: Nonhuman “child”
9-across: “You reap what you ___”
10-across: Agrees to receive promotional emails, say
12-across: Feats for gymnasts or bowlers
13-across: What some teachers claim to have in the backs of their heads
1-down: “I’ve ___ it up to here with you!”
2-down: Calls off the relationship
3-down: Cantaloupes and the like
4-down: Hearty soup
5-down: Like polo shirts and varsity jackets
6-down: Minuscule
8-down: Cat or cow, in yoga
11-down: Feminine family nickname

I ran this prompt through Claude Sonnet and Opus and ChatGPT 4o and o1 , and here were the results (links have spoilers!):

Time Correct Output Claude Sonnet 14 seconds No link ( https://claude.site/artifacts/6e8227b8-cb38-44d3-906b-d4bba12fe0a3 ) Claude Opus 20 seconds No N/A ChatGPT 4o 12 seconds No link ( https://chatgpt.com/share/66e8172f-9858-8011-83b0-2c82bcd9258f ) ChatGPT o1 124 seconds Yes link ( https://chatgpt.com/share/66e818e4-113c-8011-89f2-43e3f26ab244 ) Ben 64 seconds Yes N/A

The reason I used a Saturday is because Claude Sonnet in particular kept getting the 5×5 puzzles right, including a couple of tricky puzzles with clues that referenced other clues; 7×7 had sufficient complexity though that only o1 could figure it out.

The big challenge for traditional LLMs is that they are path-dependent; while they can consider the puzzle as a whole, as soon as they commit to a particular guess they are locked in, and doomed to failure. This is a fundamental weakness of what are known as “auto-regressive large language models”, which to date, is all of them.

To grossly simplify, a large language model generates a token (usually a word, or part of a word) based on all of the tokens that preceded the token being generated; the specific token is the most statistically likely next possible token derived from the model’s training (this also gets complicated, as the “temperature” of the output determines what level of randomness goes into choosing from the best possible options; a low temperature chooses the most likely next token, while a higher temperature is more “creative”). The key thing to understand, though, is that this is a serial process: once a token is generated it influences what token is generated next.

The problem with this approach is that it is possible that, in the context of something like a crossword puzzle, the token that is generated is wrong; if that token is wrong, it makes it more likely that the next token is wrong too. And, of course, even if the first token is right, the second token could be wrong anyways, influencing the third token, etc. Ever larger models can reduce the likelihood that a particular token is wrong, but the possibility always exists, which is to say that auto-regressive LLMs inevitably trend towards not just errors but compounding ones.

Note that these problems exist even with specialized prompting like insisting that the LLM “go step-by-step” or “break this problem down into component pieces”; they are still serial output machines that, once they get something wrong, are doomed to deliver an incorrect answer. At the same time, this is also fine for a lot of applications, like writing; where the problem manifests itself is with anything requiring logic or iterative reasoning. In this case, a sufficiently complex crossword puzzle suffices.

How o1 Works
------------

So how does o1 work? Well, we don’t know exactly — OpenAI is being pretty vague, and isn’t revealing the underlying “reasoning tokens” that undergird o1 — but I thought this post from Mike Knoop ( https://arcprize.org/blog/openai-o1-results-arc-prize ) of the ARC Prize ( https://arcprize.org/ ) , which seeks to be a test of intelligence, not just skill (which can be memorized), is pretty compelling:

o1 fully realizes the “let’s think step by step” chain-of-thought (CoT) paradigm by applying it at both training time and test time inference.

o1 scales with both training and inference compute ( https://openai.com/index/learning-to-reason-with-llms/ )

I’ll come back to this image in a moment; it’s super important.

In practice, o1 is significantly less likely to make mistakes when performing tasks where the sequence of intermediate steps is well-represented in the synthetic CoT training data. At training time, OpenAI says they’ve built a new reinforcement learning (RL) algorithm and a highly data-efficient process that leverages CoT. The implication is that the foundational source of o1 training is still a fixed set of pre-training data. But OpenAI is also able to generate tons of synthetic CoTs that emulate human reasoning to further train the model via RL. An unanswered question is how OpenAI selects which generated CoTs to train on?…

o1 isn’t just trained on facts; it’s explicitly trained on the logic used to arrive at those facts. To that end, note this article in Semafor from January 2023 ( https://www.semafor.com/article/01/27/2023/openai-has-hired-an-army-of-contractors-to-make-basic-coding-obsolete ) :

OpenAI, the company behind the chatbot ChatGPT, has ramped up its hiring around the world, bringing on roughly 1,000 remote contractors over the past six months in regions like Latin America and Eastern Europe, according to people familiar with the matter…

Previously, OpenAI trained its models on code scraped from GitHub, a repository site owned by its largest investor, Microsoft, which last week confirmed multi billion dollars in new funding first reported by Semafor. But in this case, OpenAI appears to be building a dataset that includes not just lines of code, but also the human explanations behind them written in natural language.

A software developer in South America who completed a five-hour unpaid coding test for OpenAI told Semafor he was asked to tackle a series of two-part assignments. First, he was given a coding problem and asked to explain in written English how he would approach it. Then, the developer was asked to provide a solution. If he found a bug, OpenAI told him to detail what the problem was and how it should be corrected, instead of simply fixing it.

“They most likely want to feed this model with a very specific kind of training data, where the human provides a step-by-step layout of their thought-process,” said the developer, who asked to remain anonymous to avoid jeopardizing future work opportunities. He has not yet been hired or rejected by OpenAI.

I don’t know whether or not this bit of news is specifically about o1 , but it certainly fits the distinction between previous LLMs and o1 : while the former attempt to give you the answer, o1 is about understanding and leveraging the reasoning used to arrive at an answer. This technique was described by one Ilya Sutskever (who I believe was the key inventor behind o1 ) in a May 2023 paper entitled Let’s Verify Step by Step ( https://arxiv.org/pdf/2305.20050 ) :

To collect process supervision data, we present human data-labelers with stepby-step solutions to MATH problems sampled by the large-scale generator. Their task is to assign each step in the solution a label of positive, negative, or neutral, as shown in Figure 1.

Creating training data for step-by-step reasoning ( https://arxiv.org/pdf/2305.20050 )

A positive label indicates that the step is correct and reasonable. A negative label indicates that the step is either incorrect or unreasonable. A neutral label indicates ambiguity. In practice, a step may be labelled neutral if it is subtly misleading, or if it is a poor suggestion that is technically still valid. We permit neutral labels since this allows us to defer the decision about how to handle ambiguity: at test time, we can treat neutral labels as either positive or negative.

The goal was to build a “Process-supervised Reward Model (PRM)”:

We train PRMs to predict the correctness of each step after the last token in each step. This prediction takes the form of a single token, and we maximize the log-likelihood of these target tokens during training. The PRM can therefore be trained in a standard language model pipeline without any special accommodations.

Back to Knoop’s post:

We believe iterated CoT genuinely unlocks greater generalization. Automatic iterative re-prompting enables the model to better adapt to novelty, in a way similar to test-time fine-tuning leveraged by the MindsAI team.

If we only do a single inference, we are limited to reapplying memorized programs. But by generating intermediate output CoTs, or programs, for each task, we unlock the ability to compose learned program components, achieving adaptation. This technique is one way to surmount the #1 issue of large language model generalization: the ability to adapt to novelty. Though like test-time fine-tuning it does ultimately remain limited.

When AI systems are allowed a variable amount of test-time compute (e.g., the amount of reasoning tokens or the time to search), there is no objective way to report a single benchmark score because it’s relative to the allowed compute. That is what this chart shows. More compute means more accuracy.

In summary, there are two important things happening: first, o1 is explicitly trained on how to solve problems, and second, o1 is designed to generate multiple problem-solving streams at inference time, choose the best one, and iterate through each step in the process when it realizes it made a mistake. That’s why it got the crossword puzzle right — it just took a really long time.

Scaling Inference
-----------------

I do have to come clean: it actually took o1 two tries to complete the crossword puzzle; this was the outcome of the first attempt:

o1's initial failed attempt to solve the crossword ( https://chatgpt.com/share/66e83242-ce18-8011-86e9-85a84df0f45c )

That’s a really big image, but the important parts are at the very top and the very bottom. At the top notice that it took o1 195 seconds to “think”; that’s a very long time! Then, at the bottom, there was an “Error in message stream.” I don’t know for sure, but my guess is that the model simply ran out of tokens. Remember, OpenAI isn’t revealing the intervening “reasoning tokens” where all of this iteration and testing is taking place, but they do exist; the API docs ( https://platform.openai.com/docs/guides/reasoning ) state that o1-preview has a maximum number of 32,768 output tokens, including reasoning tokens. My suspicion is that I hit this limit the first time; the second run (in a fresh session) only “thought” for 111 seconds (if you compare the summary of the thinking of the successful run ( https://chatgpt.com/share/66e818e4-113c-8011-89f2-43e3f26ab244 ) to the failed run ( https://chatgpt.com/share/66e83242-ce18-8011-86e9-85a84df0f45c ) you will notice that the former arrived at the correct answer to a few key clues more quickly than the latter, speaking to the importance of path dependence).

This is a limit that I presume can be expanded over time, which brings me back to the image above (which comes from OpenAI’s announcement page ( https://openai.com/index/learning-to-reason-with-llms/ ) ):

o1 scales with both training and inference compute ( https://openai.com/index/learning-to-reason-with-llms/ )

There has been a lot of talk about the importance of scale in terms of LLM performance; for auto-regressive LLMs that has meant training scale. The more parameters you have, the larger the infrastructure you need, but the payoff is greater accuracy because the model is incorporating that much more information. That certainly still applies to o1 , as the chart on the left indicates.

It’s the chart on the right that is the bigger deal: o1 gets more accurate the more time it spends on compute at inference time. This makes sense intuitively given what I laid out above: the more time spent on compute the more time o1 can spend spinning up multiple chains-of-thought, checking its answers, and iterating through different approaches and solutions.

It’s also a big departure from how we have thought about LLMs to date: one of the “benefits” of auto-regressive LLMs is that you’re only generating one answer in a serial manner. Yes, you can get that answer faster with beefier hardware, but that is another way of saying that the pay-off from more inference compute is getting the answer faster; the accuracy of the answer is a function of the underlying model, not the amount of compute brought to bear. Another way to think about it is that the more important question for inference is how much memory is available; the more memory there is, the larger the model, and therefore, the greater amount of accuracy.

In this o1 represents a new inference paradigm: yes, you need memory to load the model, but given the same model, answer quality does improve with more compute. The way that I am thinking about it is that more compute is kind of like having more branch predictors, which mean more registers, which require more cache, etc.; this isn’t a perfect analogy, but it is interesting to think about inference compute as being a sort of dynamic memory architecture for LLMs that lets them explore latent space for the best answer.

To that end, it’s hardly a surprise that o1 API pricing is dramatically more expensive than 4o:

1M input tokens 1M output tokens GPT-4o $5.00 $15.00 GPT-4o mini $0.15 $0.60 o1-preview $15.00 $60.00 o1-mini $3.00 $12.00

This pricing probably understates the delta, given that o1 is going to use more tokens to generate an answer. Moreover, 4o remains the better choice for a lot of use cases that don’t require logic, above-and-beyond being a lot cheaper.

There’s another way in which this pricing is symbolic, though: auto-regressive LLMs already make a lot of sense as an assistant (“help me write this letter”); the promise of something like o1 is that it actually can function as an agent, with the ability to do work — work that has been done before, to be clear — without the in-depth level of supervision required by LLMs. That’s worth a lot more money!

One more thing that is notable about o1 : while OpenAI isn’t saying how big o1-mini is, they emphasized that it is “particularly adept at coding, math, and science tasks where extensive general knowledge isn’t required”. This model is arguably the most interesting release; to quote one more line from Knoop’s article:

o1 represents a paradigm shift from “memorize the answers” to “memorize the reasoning” but is not a departure from the broader paradigm of fitting a curve to a distribution in order to boost performance by making everything in-distribution.

o1-mini is just the reasoning; that, though, is the most interesting part. To that end, my big question is how small a reasoning model might get: could there be one that runs locally? Imagine a model on your computer or even your phone that knows how to solve problems, and which can always reach out to the cloud for world knowledge. That seems quite compelling and a much clearer path to local agents than simply shrinking down large language models to be dumb enough (i.e. small enough) to fit into memory.

This Update will be available as a podcast later today. To receive it in your podcast player, visit Stratechery ( https://stratechery.passport.online/member ).

The Stratechery Update is intended for a single recipient, but occasional forwarding is totally fine! If you would like to order multiple subscriptions for your team with a group discount (minimum 5), please contact me directly.

Thanks for being a subscriber, and have a great day!

Listen to this update and other Stratechery Plus content in your podcast player: Stratechery ( https://stratechery.passport.online/member/podcast?url=https%3A%2F%2Frss.stratechery.passport.online%2Ffeed%2Fpodcast%2F6EynvegSpNaDpnt4DJsHzD ) | Sharp Tech ( https://sharptech.fm/member/podcast?url=https%3A%2F%2Fsharptech.fm%2Ffeed%2Fpodcast%2F6EynvegSpNaDpnt4DJsHzD ) | Dithering ( https://dithering.passport.online/member/podcast?url=https%3A%2F%2Frss.dithering.passport.online%2Ffeed%2Fpodcast%2F6EynvegSpNaDpnt4DJsHzD ) | Sharp China ( https://sharpchina.fm/member/podcast?url=https%3A%2F%2Fsharpchina.fm%2Ffeed%2Fpodcast%2F6EynvegSpNaDpnt4DJsHzD ) | Greatest Of All Talk ( https://goat.passport.online/member/podcast?url=https%3A%2F%2Fgoat.passport.online%2Ffeed%2Fpodcast%2F6EynvegSpNaDpnt4DJsHzD )

Subscription Information

Member: Omar Zoheri
Email: stratecheryUSC@khamel.com
Member since: April 23, 2022
Your subscription renews every year
Renewal date: December 8, 2024

You are receiving this email because you are subscribed to Stratechery ( https://www.stratechery.com ).

Click here ( https://stratechery.passport.online/member/login?email=stratecheryUSC%40khamel.com ) to view your account and manage your subscriptions.
Click here ( https://stratechery.passport.online/member/unsubscribe?unsub=https%3A%2F%2Fapi.passport.online%2Fapi%2F1.0.0%2Fusers%2FRseuYE8jgHePpWJf1fAb4C%2FchannelOptOut%3Faccess_token%3DeyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvYXBpLzEuMC4wL3VzZXJzL1JzZXVZRThqZ0hlUHBXSmYxZkFiNEMvY2hhbm5lbE9wdE91dD9jaGFubmVsPWVtYWlsXHUwMDI2cmVkaXJlY3RfdXJpPWh0dHBzJTNBJTJGJTJGc3RyYXRlY2hlcnkucGFzc3BvcnQub25saW5lJTJGbWVtYmVyJTJGdW5zdWJzY3JpYmUiXX0sImV4cCI6MTcyOTA4OTU2OCwiaWF0IjoxNzI2NDk3NTY4LCJpc3MiOiJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvb2F1dGgiLCJzY29wZSI6Im1lbWJlcjp3cml0ZSIsInN1YiI6IlJzZXVZRThqZ0hlUHBXSmYxZkFiNEMiLCJ1c2UiOiJhY2Nlc3MifQ.CzlvT8nnHq77PPcLnSit8rAm9BOAEtrbqAEao04p_KRueQNL9BAdArIGQO2P_UwwI-qT-n-VInq17-5OO6-8b8B_BMjOe9gqz7Ad5SLhoQSNA9KEJlPtfHseovtb6cMSiI3iFeNua3MW9WRUA22Uj5QD_dFCFDSfQ8TpTpULAftYVIBCZTnEFG6ASOgsUg4cVxTagoSstr7k-gpmkGn1NTNmd-giuZd7OuSAYvRvEhcdZRdAsZxSWjH7ECawAyWkpi7sOLg6MhHlTN5J9vQFUZbGCcNSNyzGduqfmaIb23D0RkXYkrcq-xgoPMFKWOaL-tIAXwLV0vPTz3iZw1km0g%26channel%3Demail%26redirect_uri%3Dhttps%253A%252F%252Fstratechery.passport.online%252Fmember%252Funsubscribe ) to unsubscribe.

© 2024 Stratechery LLC ( https://www.stratechery.com ) , 2093 Philadelphia Pike #9930, Claymont DE 19703