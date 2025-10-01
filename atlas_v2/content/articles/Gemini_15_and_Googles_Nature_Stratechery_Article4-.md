# Gemini 1.5 and Google's Nature (Stratechery Article 4-10-2024)

**Source**: inputs/old stuff/Docs/Gemini 15 and Googles Nature Stratechery Article4102024_041024.html
**Type**: article
**Created**: 2025-08-27T03:02:08.038855

---

# Gemini 1.5 and Google's Nature (Stratechery Article 4-10-2024)

Google Cloud Next 2024 was Google's most impressive assertion yet that it has the AI scale advantage and is determined to use it.

  
  
[View in browser](https://stratechery.com/2024/gemini-1-5-and-googles-nature/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI0L2dlbWluaS0xLTUtYW5kLWdvb2dsZXMtbmF0dXJlLyJdfSwiZXhwIjoxNzE1MzU0NDYzLCJpYXQiOjE3MTI3NjI0NjMsImlzcyI6Imh0dHBzOi8vYXBpLnBhc3Nwb3J0Lm9ubGluZS9vYXV0aCIsInNjb3BlIjoiZmVlZDpyZWFkIGFydGljbGU6cmVhZCBhc3NldDpyZWFkIGNhdGVnb3J5OnJlYWQgZW50aXRsZW1lbnRzIiwic3ViIjoiV1JDWFY3TjVWVnNaWnplbmJFZzdIRSIsInVzZSI6ImFjY2VzcyJ9.TQKJoSzXdyqvbUk9tFPnndj9atzJ8zolYDpJyerbGo8NtDT0hV6AviqpPBZ5USA4SuprUOSX1lsW5fX7BGPE9SMfKyCuDgoi-vZ1e_KWcOIW_cvokabuJwRU-b97GeiunGs-oyfvp2EtRqyxASSH0xL8GsUgD6xdaMvDAV0OH7d5AZq40m22kDssi4WqYQdGXaee7lYhP-OTrZbCiKDOShSBz4MAyFA-96j7ior52eVVtzoEwF6ShXyAzC1CcboAwzx6zbi4-ESpkF-KiNKIoU81mhpQ2gzOgGMLpMzrmMWz-M-4VH7ycwg-MZuGkk9BYQPGjQca0C7Q5UXcArVhaw)
[![](https://stratechery.com/wp-content/themes/stratechery-theme/images/header_large.png)](https://stratechery.com)


Wednesday, April 10, 2024

#### [Listen to this Update in your podcast player](https://stratechery.passport.online/member/podcast?url=https%3A%2F%2Frss.stratechery.passport.online%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH)

It was impossible to miss the leading message at [yesterday’s Google Cloud Next keynote](https://www.youtube.com/watch?v=V6DJYGn2SFk): Google has the best infrastructure for AI. This was CEO Sundar Pichai in his video greeting:

[![](https://assets.stratechery.passport.online/assets/vpress-3PbRb54u.png)](https://videopress.com/embed/3PbRb54u?hd=1&cover=1&loop=0&autoPlay=0&permalink=1&muted=0&controls=1&playsinline=0&useAverageColor=0&preloadContent=metadata)

I want to highlight just a few reasons Google Cloud is showing so much progress. One is our deep investments in AI. We’ve known for a while that AI would transform every industry and company, including our own. That’s why we’ve been building AI infrastructure for over a decade, including TPUs, now in their 5th generation. These advancements have helped customer train and serve cutting-edge language models. These investments put us in the forefront of the AI platform shift.

Google Cloud CEO Thomas Kurian made the priority clear as well:

[![](https://assets.stratechery.passport.online/assets/vpress-XvsaCANl.png)](https://videopress.com/embed/XvsaCANl?hd=1&cover=1&loop=0&autoPlay=0&permalink=1&muted=0&controls=1&playsinline=0&useAverageColor=0&preloadContent=metadata)

Today we’re going to focus on how Google is helping leading companies transform their operations and become digital and AI leaders, which is the new way to cloud. We have many important advances, starting with our infrastructure.

What was most interesting about the keynote, though, is what that infrastructure makes possible, and, by extension, what that says about Google’s ability to compete.

### Grounding

One of the most surprising things about large language models (LLMs) is how much they know; from the very beginning, though, hallucinations have been a concern. Hallucinations are, of course, part of what makes LLMs so impressive: a computer is actually being creative! It’s also a feature that isn’t particularly impressive to the enterprise customers that this keynote was directed at.

To that end, Kurian, shortly after going over Google’s infrastructure advantages, talked about “grounding”, both in terms of the company’s Gemini model broadly, and for enterprise use cases specifically in the context of Google’s Vertex AI model management service:

[![](https://assets.stratechery.passport.online/assets/vpress-dEFArgb3.png)](https://videopress.com/embed/dEFArgb3?hd=1&cover=1&loop=0&autoPlay=0&permalink=1&muted=0&controls=1&playsinline=0&useAverageColor=0&preloadContent=metadata)

To augment models, Vertex AI provides managed tooling to connect your model to enterprise applications and databases, using extensions and function-calling. Vertex also provides retrieval augmented generation (RAG) combining the strengths of retrieval and generative models to provide high quality personalized answers and recommendations. Vertex can augment models with up-to-date knowledge from the web and from your organization, combining generative AI with your enterprise truth.

Today we have a really important announcement: you can now ground with Google Search, perhaps the world’s most trusted source of factual information, with a deep understanding of the world’s knowledge. Grounding Gemini’s responses with Google Search improves response quality and significantly reduces hallucinations.

Second, we’re also making it easy to ground your models with data from your enterprise databases and applications, and any database anywhere. Once you’ve chosen the right model, tuned it, and connected it with your enterprise truth, Vertex’s MLOps can help you manage and monitor models.

A RAG implementation using Google Search is an obvious win, and mirrors ChatGPT’s integration with Bing (or Microsoft Copilot in Bing): the LLM provides answers when it can, and searches the web for things it doesn’t know, a particularly useful feature if you are looking for more recent information.

A more impressive demonstration of grounding, though, was in the context of integrating Gemini with Google’s [BigQuery data warehouse](https://cloud.google.com/bigquery) and [Looker business intelligence platform](https://cloud.google.com/looker):

[![](https://assets.stratechery.passport.online/assets/vpress-kfsaLM2P.png)](https://videopress.com/embed/kfsaLM2P?hd=1&cover=1&loop=0&autoPlay=0&permalink=1&muted=0&controls=1&playsinline=0&useAverageColor=0&preloadContent=metadata)

In this demo, the worker gets an alert that a particular product is selling out; using generative AI the worker can see sales trends, find similar models, and create a plan of action for dealing with declining inventory for delivery to her team.

What is notable is not the demo specifics (which is unapologetically made-up for [Cymbal, Google’s demo brand](https://console.cloud.google.com/marketplace/product/cymbal/cymbal)); rather, note the role of the LLM: it is not providing information or taking specific actions, but rather serving as a much more accessible natural language interface to surface and collect data that would otherwise take considerably more expertise and time. In other words, it is trustworthy because it is grounded through integration Google is promising with its other enterprise data services.

### Gemini 1.5

At the same time, that last section didn’t really follow on from the introduction: yes, those LLMs leveraging Google or BigQuery are running on Google’s infrastructure, but [other companies](https://learn.microsoft.com/en-us/fabric/get-started/copilot-fabric-overview) or [startups](https://count.co/) can build something similar. This is where the rest of Pichai’s introduction comes in:

[![](https://assets.stratechery.passport.online/assets/vpress-KcX1FQsC.png)](https://videopress.com/embed/KcX1FQsC?hd=1&cover=1&loop=0&autoPlay=0&permalink=1&muted=0&controls=1&playsinline=0&useAverageColor=0&preloadContent=metadata)

We also continue to build capable AI models to make products like search, Maps, and Android radically more helpful. In December, we took our next big step with Gemini, our largest and most capable model yet. We’ve been bringing it to our products and to enterprises and developers through our APIs. We’ve already introduced our next generation Gemini 1.5 Pro. It’s been in private preview in Vertex AI. 1.5 Pro shows dramatically enhanced performance and includes a breakthrough in long context understanding. That means it can run 1 million tokens of information consistently, opening up new possibilities for enterprises to create, discover, and build using AI. There’s also Gemini’s multi-modal capabilities, which can process audio, video, text, code and more. With these two advances, enterprises can do things today that just weren’t possible with AI before.

Google hasn’t said how Gemini 1.5 was made, but clearly the company has overcome the key limitation of traditional transformers: memory requirements increase quadratically with context length. One promising approach is [Ring Attention with Blockwise Transformers](https://arxiv.org/abs/2310.01889), which breaks long contexts into pieces to be computed individually even as the various devices computing those pieces simultaneously communicate to make sense of the context as a whole; in this case memory requirements scale linearly with context length, and can be extended by simply adding more devices to the ring topology.

This is where Google’s infrastructure comes in: the company not only has a massive fleet of TPUs, but has also been developing those TPUs to run in parallel at every level of the stack, from chip to cluster to even data centers (this latter requirement is more pertinent for training than inference); if there is a solution that calls for scale, Google is the best placed to provide it, and it seems the company has done just that with Gemini 1.5.

### Demos

To that end, and per Pichai’s closing line, almost all of the other demos in the keynote were implicitly leveraging Gemini 1.5’s context window.

In a Gemini for Workspaces demo, the worker evaluated two statements of work against each other, and against the company’s compliance document:

[![](https://assets.stratechery.passport.online/assets/vpress-ncFUFuer.png)](https://videopress.com/embed/ncFUFuer?hd=1&cover=1&loop=0&autoPlay=0&permalink=1&muted=0&controls=1&playsinline=0&useAverageColor=0&preloadContent=metadata)

Here are the key quotes:

Google Drive is ready without any additional AI pre-work…

Each of these documents is over 70 pages. It would have taken me hours to review these docs, but instead Gemini is going to help me find a clean answer to save me a ton of time…

Before I proceed with this vendor, I need to ensure that no compliance issues exist, and I’m going to be honest, I have not memorized every rule in our compliance rulebook because it is over 100 pages. I would have to need to scour the 80 pages of this proposal and compare it manually with the 100 pages of the rulebook. So instead, in the side panel I ask, “Does this offer comply with the following” and I’m going to just @-mention our compliance rulebook, hit Enter, and see what Gemini has to say. So interesting: Gemini has found an issue, because the supplier has not listed their security certifications.

Because Gemini is grounded in my company’s data, with source citations to specific files, I can trust this response and start to troubleshoot before selecting a vendor.

The key distinction between this demo and the last one is that quote at the beginning: a large context window *just works* in a far greater number of use cases, without any fiddly RAG implementations or special connections to external data stores; just upload the files you need to analyze, and you’re off.

In a Creative Agent with Imagen demo, the worker was seeking to create marketing images and storyboards for an outdoor product:

[![](https://assets.stratechery.passport.online/assets/vpress-owUPmlMz.png)](https://videopress.com/embed/owUPmlMz?hd=1&cover=1&loop=0&autoPlay=0&permalink=1&muted=0&controls=1&playsinline=0&useAverageColor=0&preloadContent=metadata)

Here is the key quote:

The creative agent can analyze our previous campaigns to understand our unique brand style and apply it to new ideas. In this case, the creative agent has analyzed over 3,000 brand images, descriptions, videos, and documents of other products that we have in our catalog, contained within Google Drive, to create this summary…The creative agent was able to use Gemini Pro’s 1 million token context window and it’s ability to reason across text, images, and video to generate this summary.

This was, to be fair, one of the weaker demos: the brand summary and marketing campaign weren’t *that* impressive, and the idea of creating a podcast with synthetic voices is technically impressive and also something that will never be listened to. That, though, is impressive in its own right: as I noted in [an Update when Gemini 1.5 was first announced](https://stratechery.com/2024/groq-costs-gemini-pro-1-5-googles-timidity/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI0L2dyb3EtY29zdHMtZ2VtaW5pLXByby0xLTUtZ29vZ2xlcy10aW1pZGl0eS8iXX0sImV4cCI6MTcxNTM1NDQ2MywiaWF0IjoxNzEyNzYyNDYzLCJpc3MiOiJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvb2F1dGgiLCJzY29wZSI6ImZlZWQ6cmVhZCBhcnRpY2xlOnJlYWQgYXNzZXQ6cmVhZCBjYXRlZ29yeTpyZWFkIGVudGl0bGVtZW50cyIsInN1YiI6IldSQ1hWN041VlZzWlp6ZW5iRWc3SEUiLCJ1c2UiOiJhY2Nlc3MifQ.iWwVJbJ2mrcisGQqEPERpuubNJ6vLVlb6H9bUx41EL00148xkhYacvILZG1bfVjgqcZw9cMZEa1xpDlTups30P1SDDXxMhcbucApsBFyg-YG85MZWpphNzp8rmnk1VKKTCttQCJ1S_RF1PVWqBj7hSfLI7W0jg6fTIOu5MvjvWtEmWnwNkBoxHnt7WkMeRyD0qDIBNWSxw0dolyCm2NMFBIFkvKt2Mn7OTd0D4jl5-0UofTyosICBj41rYd5_tkvXm8QP2ZBolBMLzjuc_c04PjsyzI29k1V_JgFxKGxL6-Nbds_oZKdKgmETbgb4RRuhmXfFP_Q8ApdgMibWwgodw), “a massively larger context window makes it possible to do silly stuff”, and silly stuff often turns into serious capabilities.

In a Gemini Code Assistant Demo (formerly Duet AI for Developers), a developer new to a job (and the codebase) was tasked with making a change to a site’s homepage:

[![](https://assets.stratechery.passport.online/assets/vpress-Kd0kqaXg.png)](https://videopress.com/embed/Kd0kqaXg?hd=1&cover=1&loop=0&autoPlay=0&permalink=1&muted=0&controls=1&playsinline=0&useAverageColor=0&preloadContent=metadata)

Here is the key quote:

For the developers out there, you know that this means we’re going to need to add padding in the homepage, modify some views, make sure the configs are changed for our microservices, and typically, it would take me a week or two to even just get familiarized with our company’s code base which has over 100,000 lines of code over 11 services. But now, with Gemini Code Assist, as a new engineer on the team, I can be more productive than ever and can accomplish all of this work in just a matter of minutes. This is because Gemini’s code transformations with full codebase awareness allows us to easily reason through our entire codebase, and in comparison, other models out there can’t handle anything beyond 12,000 to 15,000 lines of code. Gemini with Code Assist is so intelligent that we can just give it our business requirements, including the visual design…Gemini Code Assist doesn’t just suggest code edits; it provides clear recommendations, and makes sure that all of these recommendations align with [the company’s] security and compliance requirements…

And the conclusion:

Let’s recap: behind the scenes Gemini has analyzed my entire codebase in GitLab; it has implemented a new feature; and has ensured that all of the code generated is compatible with my company’s standards and requirements.

Again, leave aside the implausibility of this demo: the key takeaway is the capabilities unlocked when the model is able to have all of the context around a problem while working; this is only possible with — and here the name is appropriate — a long *context* window, and that is ultimately enabled by Google’s infrastructure.

### Google’s Nature

In case it isn’t clear, I think that this keynote was by far the most impressive presentation Google has made in the AI era, not least because the company knows exactly what its advantages are. Several years ago I wrote an Article called [Microsoft’s Monopoly Hangover](https://stratechery.com/2017/microsofts-monopoly-hangover/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDE3L21pY3Jvc29mdHMtbW9ub3BvbHktaGFuZ292ZXIvIl19LCJleHAiOjE3MTUzNTQ0NjMsImlhdCI6MTcxMjc2MjQ2MywiaXNzIjoiaHR0cHM6Ly9hcGkucGFzc3BvcnQub25saW5lL29hdXRoIiwic2NvcGUiOiJmZWVkOnJlYWQgYXJ0aWNsZTpyZWFkIGFzc2V0OnJlYWQgY2F0ZWdvcnk6cmVhZCBlbnRpdGxlbWVudHMiLCJzdWIiOiJXUkNYVjdONVZWc1paemVuYkVnN0hFIiwidXNlIjoiYWNjZXNzIn0.bYmcEXCaOBz51S11SyXss104tIf-UWxtiXROMxOXnqI_-xITO5MXOlepIBot7D_aP4yi8sZwrgR_SLZdgnpJsUoMEuRxaEFCJBpmMb1PMkIY98cWqS3V3DadqvYA1vICOj8DDNpkJ2VCViznXXhdHsLvUr5w2YLZHvbaAapBcEAzyVdqTU1ToqQGqXm6TQQdoOLF7mCXasR_4GX5tjvd5Y0irL8KsJ2IfIsnNs3QJ-Ko6ZbwTCNnTkzQufyj4941AYZbPq6II-4NbpkNcvdSFB36175tPW-a_qrj5rzTGd6BBcSYkPFtyMrulaDdZdcFSMQQusLzOK3M7diKa_c90A) that discussed the company’s then-ongoing transition away from Windows as the center of its strategy; the central conceit was a comparison to Lou Gerstner’s 1990’s transformation of IBM.

The great thing about a monopoly is that a company can do anything, because there is no competition; the bad thing is that when the monopoly is finished the company is still capable of doing anything at a mediocre level, but nothing at a high one because it has become fat and lazy. To put it another way, for a former monopoly “big” is the only truly differentiated asset.

My argument was that business models could be changed: IBM did it, and Microsoft was in the process of doing so when I wrote that. Moreover, Gerstner had shown that culture could be changed as well, and [Nadella did just that at Microsoft](https://stratechery.com/2018/the-end-of-windows/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDE4L3RoZS1lbmQtb2Ytd2luZG93cy8iXX0sImV4cCI6MTcxNTM1NDQ2MywiaWF0IjoxNzEyNzYyNDYzLCJpc3MiOiJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvb2F1dGgiLCJzY29wZSI6ImZlZWQ6cmVhZCBhcnRpY2xlOnJlYWQgYXNzZXQ6cmVhZCBjYXRlZ29yeTpyZWFkIGVudGl0bGVtZW50cyIsInN1YiI6IldSQ1hWN041VlZzWlp6ZW5iRWc3SEUiLCJ1c2UiOiJhY2Nlc3MifQ.GmcnyPem_dP2nIcbUS3jmL0nZuN57s7AlRDT4YftOizYK5cpU-RGpq74acJU43rw2KTDkD8Zqko6v3cwvEc2eILG8MtdmgIR61zdaKJZtIj-dNpay2rVxY-RUhis-BWVUspjaD4eAc9V20vvNuGKPHy4eBhn62xdPfsKEx4n_ChCeVAzMfSZ5E4ANLiWmz6HNbrWs87r972uhg02mNAUQrs-ZFTE1KN3o5WVbKWC28zi3seFo-zWVHiz3JcCCpb2AnL1-lRwWU34eHWlqolwGKh8oqON85gHsuCMVuVtcFW7eM_fsYX19i-MYQovh7lmOxmJoyu0LzpsNsM3ueBp0A). What couldn’t be changed was nature: IBM was a company predicated on breadth, not specialization; that’s why Gerstner was right to not break apart the company but to instead deliver Internet solutions to enterprises. Similarly, Microsoft was a company predicated on integration around Windows; the company’s shift to services centered on [Teams as Microsoft’s operating system in the cloud](https://stratechery.com/2020/the-slack-social-network/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDIwL3RoZS1zbGFjay1zb2NpYWwtbmV0d29yay8iXX0sImV4cCI6MTcxNTM1NDQ2MywiaWF0IjoxNzEyNzYyNDYzLCJpc3MiOiJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvb2F1dGgiLCJzY29wZSI6ImZlZWQ6cmVhZCBhcnRpY2xlOnJlYWQgYXNzZXQ6cmVhZCBjYXRlZ29yeTpyZWFkIGVudGl0bGVtZW50cyIsInN1YiI6IldSQ1hWN041VlZzWlp6ZW5iRWc3SEUiLCJ1c2UiOiJhY2Nlc3MifQ.InelnoDDD27KKLKTLjCqXmD1axQX9_lWThlDIWfeCeA6FgvvEv51_peVwwEJXMy3F1UpQc3kOEergwehPA5Trj7OMPAp0VeL1wou-NdLtgZcHgLOyD1n0AVH3OLI3ruLLIEdMULzcitSsrXanl5XLU7RIpYGaXjfIQcqI-kIym59QqojcgeY3QiKOeTPEA4PIcv3JU9tkoamcjNgehIU9Q1yieHOamM_c3cgj2oT3aoL0ycGK78edD-HUYv7t3J0f93lNG0mz48gMda40iLzuj-gAio4zfbj635LDGiNwGpv8NtlAHdim0f0Ke8jq8dt6t69Lmtb8VySaZM4gvcL2w) was also true to the company’s nature.

Google is facing many of the same challenges after its decades long dominance of the open web: all of the products shown yesterday rely on a different business model than advertising, and to properly execute and deliver on them will require a cultural shift to supporting customers instead of tolerating them. What hasn’t changed — because it is the company’s nature, and thus cannot — is the reliance on scale and an overwhelming infrastructure advantage. That, more than anything, is what defines Google, and it was encouraging to see that so explicitly put forward as an advantage.

#### Listen to this update and other Stratechery Plus content in your podcast player: [Stratechery](https://stratechery.passport.online/member/podcast?url=https%3A%2F%2Frss.stratechery.passport.online%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH) | [Sharp Tech](https://sharptech.fm/member/podcast?url=https%3A%2F%2Fsharptech.fm%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH) | [Dithering](https://dithering.passport.online/member/podcast?url=https%3A%2F%2Frss.dithering.passport.online%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH) | [Sharp China](https://sharpchina.fm/member/podcast?url=https%3A%2F%2Fsharpchina.fm%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH) | [Greatest Of All Talk](https://goat.passport.online/member/podcast?url=https%3A%2F%2Fgoat.passport.online%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH)

  

Subscription Information  
  

Member: Omar Zoheri  
Email: [stratechery@khamel.com](mailto:stratechery@khamel.com)  
Plan type: Free  
  
  
You are receiving this email because you are subscribed to [Stratechery](https://www.stratechery.com).  
  
[Click here](https://stratechery.passport.online/member/login?email=stratechery%40khamel.com) to view your account and manage your subscriptions.  
[Click here](https://stratechery.passport.online/member/unsubscribe?unsub=https%3A%2F%2Fapi.passport.online%2Fapi%2F1.0.0%2Fusers%2FWRCXV7N5VVsZZzenbEg7HE%2FchannelOptOut%3Faccess_token%3DeyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvYXBpLzEuMC4wL3VzZXJzL1dSQ1hWN041VlZzWlp6ZW5iRWc3SEUvY2hhbm5lbE9wdE91dD9jaGFubmVsPWVtYWlsXHUwMDI2cmVkaXJlY3RfdXJpPWh0dHBzJTNBJTJGJTJGc3RyYXRlY2hlcnkucGFzc3BvcnQub25saW5lJTJGbWVtYmVyJTJGdW5zdWJzY3JpYmUiXX0sImV4cCI6MTcxNTM1NDQ2MywiaWF0IjoxNzEyNzYyNDYzLCJpc3MiOiJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvb2F1dGgiLCJzY29wZSI6Im1lbWJlcjp3cml0ZSIsInN1YiI6IldSQ1hWN041VlZzWlp6ZW5iRWc3SEUiLCJ1c2UiOiJhY2Nlc3MifQ.ur2mptQiLP1f1OrA1lYsSb-Q3is5J8KK40M_vSbPHnSUBC8FzKND6KN4tQCBAqtAYOVgWrKtvZE9S2FwxIlQrojzWykYtZKFA5r7vmacl0vVPOrImClqQlUUNZQNrJctBqVipkFznrry5I5PTZ4DVNhH5UFHA1clNyMl5xZnJ97Mj3yWIMZEWPSElb0MJ449mg7q3piequEjVkXn6B97qFXOjjSIwbyWJjaRANBiORBc-i4HNkBsUz3ujBNVtTjZnNCu1kyxJFgTaSFw4v75V87BN-0tX_0Jd5Mw2h4vy7qvs_LPvq6BcMtojdFYLL_is6RuxUjWcMKcpEGR-mwtgQ%26channel%3Demail%26redirect_uri%3Dhttps%253A%252F%252Fstratechery.passport.online%252Fmember%252Funsubscribe) to unsubscribe.  

  
*© 2024
[Stratechery LLC](https://www.stratechery.com),
2093 Philadelphia Pike #9930, Claymont DE 19703*