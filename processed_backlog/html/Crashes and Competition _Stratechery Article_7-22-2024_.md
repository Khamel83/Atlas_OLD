# Crashes and Competition (Stratechery Article 7-22-2024)

**Source:** inputs/old stuff/Docs/Crashes and Competition Stratechery Article7222024_072224.html
**Processed:** 2025-08-24T19:49:20.362092

# Crashes and Competition (Stratechery Article 7-22-2024)

[View in browser](https://stratechery.com/2024/crashes-and-competition/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI0L2NyYXNoZXMtYW5kLWNvbXBldGl0aW9uLyJdfSwiZXhwIjoxNzI0MjM1MTIwLCJpYXQiOjE3MjE2NDMxMjAsImlzcyI6Imh0dHBzOi8vYXBpLnBhc3Nwb3J0Lm9ubGluZS9vYXV0aCIsInNjb3BlIjoiZmVlZDpyZWFkIGFydGljbGU6cmVhZCBhc3NldDpyZWFkIGNhdGVnb3J5OnJlYWQgZW50aXRsZW1lbnRzIiwic3ViIjoiV1JDWFY3TjVWVnNaWnplbmJFZzdIRSIsInVzZSI6ImFjY2VzcyJ9.pcwdc9ThQr5oe5syvBEWoPYYJe-3uXhSp6R5OEqIg9YQHyfTYmGJO2wmrk7PzY9IjGwHL0jQeF66qGwvO3emG0wCFlMxqEwpfOkIDkHpt9f3qL-RlOShkSJ2XHhENAliPlP8lomNxXjq2PXrQrJAZgEqgNyLRvpCv0G0vTCBpgRCA1y2h9_W12nUu9Ujsyq7nyWcj_lJtGQFu-SUP46uSypgytO6dSDml_YlIlaEt1TwZt80YnBiEWUHIIIPHMgNJ_Ufahh2UcyCZ8HMEfLZ1A2x4wDhbpvM2A7YOb3xqbF5qawiLTVamFU1zgaRtBS-GjRZ7QA70PkIOluxI5e-hw)
[![](https://stratechery.com/wp-content/themes/stratechery-theme/images/header_large.png)](https://stratechery.com)


Monday, July 22, 2024

#### [Listen to this Update in your podcast player](https://stratechery.passport.online/member/podcast?url=https%3A%2F%2Frss.stratechery.passport.online%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH)

I’ve long maintained that if the powers-that-be understood [what the Internet’s impact would be](https://stratechery.com/2019/the-internet-and-the-third-estate/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDE5L3RoZS1pbnRlcm5ldC1hbmQtdGhlLXRoaXJkLWVzdGF0ZS8iXX0sImV4cCI6MTcyNDIzNTEyMCwiaWF0IjoxNzIxNjQzMTIwLCJpc3MiOiJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvb2F1dGgiLCJzY29wZSI6ImZlZWQ6cmVhZCBhcnRpY2xlOnJlYWQgYXNzZXQ6cmVhZCBjYXRlZ29yeTpyZWFkIGVudGl0bGVtZW50cyIsInN1YiI6IldSQ1hWN041VlZzWlp6ZW5iRWc3SEUiLCJ1c2UiOiJhY2Nlc3MifQ.Vay3v6mQAmURH1aMxIhTxyEVu-TEvWEwbc-3E8Xr4DUE3Gwi_YJgTHm2UQtE905BO3pzCKVvOgv1iS-V9CD0g8GwXBdpUVPRZ0H-axApSj42AuZynNmBpK6opOX70X2ov0wufgdY2uVDXOy3P62ddk6hGvfGCkeD2i4iQxuksqqOHf0XGkzaUvBLPYsUcCPLaB6u9BmOk3dkjUOkoHMpHoyHLutt20HJrHRzFYBw_KTnTQ0qvFUOjUOjor8AQOblLb3CFQEnkGvvZKsZ5hNoXhGBhD4sh-HJhI3lv9KrnQoOfIH9lpXtz6VGBQclgufaYnACMWu8DR6O5j-TPJp0pw), they would have never allowed it to be created. It’s hard to accuse said shadowy figures of negligence, however, given how clueless technologists were as well; look no further than an operating system like Windows.

Windows was, from the beginning, well and truly open: 3rd-party developers could do anything, including “patching the kernel”; to briefly summarize:

* The “kernel” of an operating system is the core of the operating system, the function of which is to manage the actual hardware of a computer. All software running in the kernel is fully privileged, which is to say it operates without any restrictions. If software crashes in the kernel, the entire computer crashes.
* Everything else on a computer runs in “user space”; user space effectively sits on top of the kernel, and is dependent on APIs provided by the operating system maker to compel software in kernel space to actually interface with the hardware. If software crashes in user space the rest of the computer is fine.

This is a drastically simplified explanation; in some operating systems there are levels of access between kernel space and user space for things like drivers (which need direct hardware access to the hardware they are controlling, but not necessarily hardware access to the entire computer), and on the other side of things significant limitations on software in user space (apps, for example, might be “sandboxed” and unable to access other information on the computer, even if it is in user space).

The key point for purposes of this Article, though, is that Windows allowed access to both kernel space and user space; yes, the company certainly preferred that developers only operated in user space, and the company never officially supported applications that patched the kernel, but the reality is that operating in kernel space is far more powerful and so a lot of developers would do just that.

### Security Companies and Kernel Access

An example of developers with a legitimate argument for access to kernel space are security companies: Windows’ openness extended beyond easy access to kernel space; the reason why sandboxing became a core security feature of newer operating systems like iOS is that not all developers were good actors: virus and malware makers on Windows in particular would leverage easy access to other programs to infiltrate computers and make them nigh on unusable at best, and exfiltrate data or use computers they took over to attack others at worse.

The goal of security software like antivirus programs or malware scanners was to catch these bad actors and eliminate them; the best way to do so was to patch the kernel and so operate at the lowest, most powerful layer of Windows, with full visibility and access to every other program running on the computer. And, to be clear, in the 2000s, when viruses and malware were at their peak, this was very much necessary — and necessary is another way of saying this was a clear business opportunity.

Two of the companies seizing this opportunity in the 2000s were Symantec and McAfee; both reacted with outrage in 2005 and 2006 when Microsoft, in the run-up to the release of Windows Vista, introduced [PatchGuard](https://en.wikipedia.org/wiki/Kernel_Patch_Protection). PatchGuard was aptly named: it guarded the kernel from being patched by 3rd-parties, with the goal of increasing security. This, though, was a threat to Symantec and McAfee; George Amenuk, CEO of the latter, released [an open letter](https://news.softpedia.com/news/Microsoft-Increasing-Security-Risk-with-Vista-37014.shtml) that stated:

Over the years, the most reliable defenders against the many, many vulnerabilities in the Microsoft operating systems have been the independent security companies such as McAfee. Yet, if Microsoft succeeds in its latest effort to hamstring these competitors, computers everywhere could be less secure. Computers are more secure today, thanks to relentless innovations by the security providers. Microsoft also has helped by allowing these companies’ products full access to system resources-this has enabled the security products to better “see” threats and deploy defenses against viruses and other attacks.

With its upcoming Vista operating system, Microsoft is embracing the flawed logic that computers will be more secure if it stops cooperating with the independent security firms. For the first time, Microsoft shut off security providers’ access to the core of its operating system – what is known as the “kernel”.

At the same time, Microsoft has firmly embedded in Vista its own Windows Security Center-a product that cannot be disabled even when the user purchases an alternative security solution. This approach results in confusion for customers and prevents genuine freedom of choice. Microsoft seems to envision a world in which one giant company not only controls the systems that drive most computers around the world but also the security that protects those computers from viruses and other online threats. Only one approach protecting us all: when it fails, it fails for 97% of the world’s desktops.

Symantec, meanwhile, went [straight to E.U. regulators](https://arstechnica.com/information-technology/2006/09/7851/), making the case that Microsoft, already in trouble over its inclusion of Internet Explorer in the 90s, and Windows Media Player in the early 2000s, was unfairly limiting competition for security offerings. [The E.U. agreed](https://web.archive.org/web/20061115202549/http://software.silicon.com/os/0%2C39024651%2C39163274%2C00.htm) and Microsoft soon backed down; from [Silicon.com](https://web.archive.org/web/20061023112233/http://software.silicon.com/security/0,39024655,39163277,00.htm) in 2006:

Microsoft has announced it will give security software makers technology to access the kernel of 64-bit versions of Vista for security-monitoring purposes. But its security rivals remain as yet unconvinced. Redmond also said it will make it possible for security companies to disable certain parts of the Windows Security Center in Vista when a third-party security console is installed. Microsoft made both changes in response to antitrust concerns from the European Commission. Led by Symantec, the world’s largest antivirus software maker, security companies had publicly criticised Microsoft over both Vista features and also talked to European competition officials about their gripes.

Fast forward nearly two decades, and while Symantec and McAfee are still around, there is a new wave of cloud-based security companies that dominate the space, including CrowdStrike; Windows is much more secure than it used to be, but after the disastrous 2000s, a wave of regulations were imposed on companies requiring them to adhere to a host of requirements that are best met by subscribing to an all-in-one solution that checks all of the relevant boxes, and CrowdStrike fits the bill. What is the same is kernel-level access, and that brings us to last week’s disaster.

### The CrowdStrike Crash

On Friday, from [The Verge](https://www.theverge.com/2024/7/19/24201717/windows-bsod-crowdstrike-outage-issue):

Thousands of Windows machines are experiencing a Blue Screen of Death (BSOD) issue at boot today, impacting banks, airlines, TV broadcasters, supermarkets, and many more businesses worldwide. A faulty update from cybersecurity provider CrowdStrike is knocking affected PCs and servers offline, forcing them into a recovery boot loop so machines can’t start properly. The issue is not being caused by Microsoft but by third-party CrowdStrike software that’s widely used by many businesses worldwide for managing the security of Windows PCs and servers.

On Saturday, from the [CrowdStrike blog](https://www.crowdstrike.com/blog/falcon-update-for-windows-hosts-technical-details/):

On July 19, 2024 at 04:09 UTC, as part of ongoing operations, CrowdStrike released a sensor configuration update to Windows systems. Sensor configuration updates are an ongoing part of the protection mechanisms of the Falcon platform. This configuration update triggered a logic error resulting in a system crash and blue screen (BSOD) on impacted systems. The sensor configuration update that caused the system crash was remediated on Friday, July 19, 2024 05:27 UTC. This issue is not the result of or related to a cyberattack.

In any massive failure there are a host of smaller errors that compound; in this case, CrowdStrike created a faulty file, failed to test it properly, and deployed it to its entire customer base in one shot, instead of rolling it out in batches. Doing something different at each one of these steps would have prevented the widespread failures that are still roiling the world (and will for some time to come, given that the fix requires individual action on every affected computer, since the computer can’t stay running long enough to run a remotely delivered fix).

The real issue, though, is more fundamental: erroneous configuration files in userspace crash a program, but they don’t crash the computer; CrowdStrike, though, doesn’t run in userspace: it runs in kernel space, which means its bugs crash the entire computer — 8 million of them, [according to Microsoft](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). Apple and Linux were not impacted, for a very obvious reason: both have long since locked out 3rd-party software from kernel space.

Microsoft, though, despite having tried to do just that in the 2000s, has its hands tied; from the [Wall Street Journal](https://www.wsj.com/tech/cybersecurity/microsoft-tech-outage-role-crowdstrike-50917b90):

A Microsoft spokesman said it cannot legally wall off its operating system in the same way Apple does because of an understanding it reached with the European Commission following a complaint. In 2009, Microsoft agreed it would give makers of security software the same level of access to Windows that Microsoft gets.

I wasn’t able to find the specifics around the agreement Microsoft made with the European Commission; the company did agree to implement [a browser choice screen in December 2009](https://ec.europa.eu/commission/presscorner/detail/en/IP_09_1941), along with [a commitment to interoperability](https://news.microsoft.com/2009/12/16/microsoft-statement-on-european-commission-decision/) for its “high-share software products” including Windows. What I do know is that a complaint about kernel level access was filed by Symantec, that Microsoft was under widespread antitrust pressure by regulators, and, well, that a mistake by CrowdStrike rendered millions of computers inoperable because CrowdStrike has kernel access.

### Microsoft’s Handicap

On Friday afternoon, FTC Chair Lina Khan [tweeted](https://x.com/linakhanftc/status/1814395610788929649):

[![](https://assets.stratechery.passport.online/assets/tweet-1814395610788929649.png)](https://twitter.com/linakhanFTC/status/1814395610788929649?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1814395610788929649%7Ctwgr%5E7c2719ecc590a8f61602c6d9a190dcdb02602844%7Ctwcon%5Es1_&ref_url=http%3A%2F%2Fchrome-headless.local%3A9222%2Fatomic)

This is wrong on a couple of levels, but the ways in which it is wrong are worth examining because of what they mean for security specifically and tech regulation broadly.

First, this outage was the system working as regulators intended: 99% of Windows computers were not affected, just those secured by CrowdStrike; to go back to that 2006 open letter from the McAfee CEO:

We think customers large and small are right to rely on the innovation arising from the intense competition between diverse and independent security companies. Companies like McAfee have none of the conflicts of interest deriving from ownership of the operating system. We focus purely on security. Independent security developers have proven to be the most powerful weapon in the struggle against those who prey on weak computers. Computer users around the globe recognize that the most serious threats to security exist because of inherent weaknesses in the Microsoft operating system. We believe they should demand better of Microsoft.

For starters, customers should recognize that Microsoft is being completely unrealistic if, by locking security companies out of the kernel, it thinks hackers won’t crack Vista’s kernel. In fact, they already have. What’s more, few threats actually target the kernel – they target programs or applications. Yet the unfettered access previously enjoyed by security providers has been a key part of keeping those programs and applications safe from hackers and malicious software. Total access for developers has meant better protection for customers.

That argument may be correct; the question this episode raises, though, is what is the appropriate level of abstraction to evaluate risk? The McAfee CEO’s argument is that most threats are targeting userspace, which is why security developers deserve access to kernel space to root them out; again, I think this argument is probably correct in a narrow sense — it was definitely correct in the malware-infested 2000s — but what is a bigger systemic problem, malware and viruses on functioning computers, or computers that can’t even turn on?

Second, while Khan’s tweets didn’t mention Microsoft specifically, it seems obvious that is the company she was referring to; after all, CrowdStrike, who was actually to blame, is apparently only on 1% of Windows PCs, which even by the FTC’s standards surely doesn’t count as “concentration.” In this Khan was hardly alone: the company that is taking the biggest public relations hit is Microsoft, and how could they not:

[![](https://assets.stratechery.passport.online/assets/tweet-1814415179725107502.png)](https://twitter.com/benthompson/status/1814415179725107502?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1814415179725107502%7Ctwgr%5E7c2719ecc590a8f61602c6d9a190dcdb02602844%7Ctwcon%5Es1_&ref_url=http%3A%2F%2Fchrome-headless.local%3A9222%2Fatomic)

Everyone around the world encountered these images everywhere, both in person and on social media:

[![](https://assets.stratechery.passport.online/assets/tweet-1814387942401654874.png)](https://twitter.com/wilplatypus/status/1814387942401654874?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1814387942401654874%7Ctwgr%5E7c2719ecc590a8f61602c6d9a190dcdb02602844%7Ctwcon%5Es1_&ref_url=http%3A%2F%2Fchrome-headless.local%3A9222%2Fatomic)

This tweet was a joke, but from Microsoft’s position, apt: if prison is the restriction of freedom by the authorities, well, then that is exactly how this happened, as regulators restricted Microsoft’s long-sought freedom to lock down kernel space.

To be clear, restricting access to kernel space would not have made an issue like this impossible: after all, Microsoft, by definition, will always have access to kernel space, and they could very well issue an update that crashes not just 1% of the world’s Windows computers, but all of them. This, though, raises the question of incentives: is there any company both more motivated and better equipped than Microsoft to *not* make this sort of mistake, given the price they are paying today for a mistake that wasn’t even their fault?

### Regulating Progress

Cloudflare CEO Matthew Prince already anticipated the potential solution I am driving at, and wrote a retort [on X](https://x.com/eastdakota/status/1814544614638166442):

Here’s the scary thing that’s likely to happen based on the facts of the day if we don’t pay attention. Microsoft, who competes with @CrowdStrike, will argue that they should lock all third-party security vendors out of their OS. “It’s the only way we can be safe,” they’ll testify before Congress.

But lest we forget, Microsoft themselves had their own eternal screw up where they potentially let a foreign actor read every customer’s email because they failed to adequately secure their session signing keys. We still have no idea how bad the implications of #EternalBlue are.

So pick your poison. Today CrowdStrike messed up and some systems got locked out. That sucks a measurable amount. On the other hand, if Microsoft runs the app and security then they mess up and you’ll probably still be able to check your email — because their incentive is to fail open — but you’ll never know who else could too. Not to mention your docs, apps, files, and everything else.

Today sucked, but better security isn’t consolidated security. It isn’t your application provider picking who your security vendor must be. It’s open competition across many providers. Because CrowdStrike had a bad day, but the solution isn’t to standardize on Microsoft.

And, if we do, then when they have a bad day it’ll make today look like a walk in the park.

Prince’s argument is ultimately an updated version of that made by the McAfee CEO, and while I agree in theory, in this specific instance I disagree in practice: Windows gave kernel access because the company didn’t know any better, but just because the company won in its market doesn’t mean decisions made decades ago must then be the norm forever.

This is a mistake that I think that regulators make regularly, particularly in Europe. [Last week I wrote](https://stratechery.com/2024/tech-ceos-on-trump-x-and-the-e-u-apple-settles-with-e-u-over-nfc/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI0L3RlY2gtY2Vvcy1vbi10cnVtcC14LWFuZC10aGUtZS11LWFwcGxlLXNldHRsZXMtd2l0aC1lLXUtb3Zlci1uZmMvIl19LCJleHAiOjE3MjQyMzUxMjAsImlhdCI6MTcyMTY0MzEyMCwiaXNzIjoiaHR0cHM6Ly9hcGkucGFzc3BvcnQub25saW5lL29hdXRoIiwic2NvcGUiOiJmZWVkOnJlYWQgYXJ0aWNsZTpyZWFkIGFzc2V0OnJlYWQgY2F0ZWdvcnk6cmVhZCBlbnRpdGxlbWVudHMiLCJzdWIiOiJXUkNYVjdONVZWc1paemVuYkVnN0hFIiwidXNlIjoiYWNjZXNzIn0.H8194FHn2Ke5MdkkTFa6H6xSFWLATrid3IWeUCW4uwuDgc5VMHwFyw-AFh1xHEHgDVQaDif54DuzRAz44g94ntZGdGtm4CHolidWirN8iluHDnYkWj6QXARRugKqTWR-wYTOTmhCPddg9aIgt0Jp1hboP37qt25GBYhMlZh7ETDfoBq4JS0NPG17qWE6MHd9uoK36sIcMn24bqd1NpZ8CdyR_RdER17yx3DhzQ7nHN8db7jPYBMrW98cq3Wsdicokc6oh6xJSgrDNGN9NYU8_nEjn1dke2XYIMfMoj-zahQPe4jNWqy-_VlheGAWFcjkLj9p-fZOyM5FieoMx4ylDA) in the context of the European Commission’s investigation of X and blue checkmarks:

One of the the critiques of European economies is how difficult it is to fire people; while the first-order intentions are obviously understandable, the critique is that companies underinvest in growth because there is so much risk attached to hiring: if you get the wrong person, or if expected growth doesn’t materialize, you are stuck. What is notable is how Europe seems to have decided on the same approach to product development: Google is expected to have 10 blue links forever, Microsoft can’t include a browser or shift the center of gravity of its business to Teams, Apple can’t use user data for Apple Intelligence, and, in this case, X is forever bound to the European Commission’s interpretation of what a blue check meant under previous ownership. Everything, once successful, must be forever frozen in time; ultimately, though, the E.U. only governs a portion of Europe, and the only ones stuck in the rapidly receding past — for better or worse! — will be the E.U.’s own citizens.

In this case, people all over the world suffered because Microsoft was never allowed to implement a shift in security that it knew was necessary two decades ago.

More broadly, regulators need to understand that everything is a trade-off. Apple is under fire for its App Store policies — which I too have been relentlessly critical of — but as I wrote in [The E.U. Goes Too Far](https://stratechery.com/2024/the-e-u-goes-too-far/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI0L3RoZS1lLXUtZ29lcy10b28tZmFyLyJdfSwiZXhwIjoxNzI0MjM1MTIwLCJpYXQiOjE3MjE2NDMxMjAsImlzcyI6Imh0dHBzOi8vYXBpLnBhc3Nwb3J0Lm9ubGluZS9vYXV0aCIsInNjb3BlIjoiZmVlZDpyZWFkIGFydGljbGU6cmVhZCBhc3NldDpyZWFkIGNhdGVnb3J5OnJlYWQgZW50aXRsZW1lbnRzIiwic3ViIjoiV1JDWFY3TjVWVnNaWnplbmJFZzdIRSIsInVzZSI6ImFjY2VzcyJ9.IY7IAA3WtDtkAVFuRMeLw8jEVNu4GPq5Zn3uEt09P_IRmC0jEG584xrlIc4rAjY3MgR4mQOxXIrREi9u_75ltASlffMZF3hc_NM9hePhd6e99PXctAWi_VQYvHDWqvY73h5FHMy_c7-zq6Jfh_7j3_nFZ1N6rYP_aP9DSYt85scbT8bemh9C2K6HQ3oZVdWpWc8Y-ZXKPm_pgBNCPqZvBBTZ-Hd3mWtvQH3FkXkY3m4lnObb-Zx7akE7bel59l7rtPcGLFv4WOdSCFLkdQgr4pedBhMTWkiBDb1cJ4dAPi-AYg2hsmMMqBNmA8s1k98s0pe0cwgZ4aW4rBi1bKD7Kg) earlier this month:

Apple didn’t just create the iPhone, they also created the App Store, which, after the malware and virus muddled mess of the 2000s, rebuilt user confidence and willingness to download 3rd-party apps. This was a massive boon to developers, and shouldn’t be forgotten; more broadly, the App Store specifically and Apple’s iOS security model generally really do address real threats that can not only hurt users but, by extension, chill the market for 3rd-party developers.

I went on to explain how Apple has gone too far with this model, particularly with its policy choices in the App Store that seem to be motivated more by protecting App Store revenue than security (and why [the European Commission was right to go after anti-steering policies](https://stratechery.com/2024/apple-fined-by-european-commission-apples-spotify-press-release-apple-revokes-epics-developer-account-again/?access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL3N0cmF0ZWNoZXJ5LmNvbS8yMDI0L2FwcGxlLWZpbmVkLWJ5LWV1cm9wZWFuLWNvbW1pc3Npb24tYXBwbGVzLXNwb3RpZnktcHJlc3MtcmVsZWFzZS1hcHBsZS1yZXZva2VzLWVwaWNzLWRldmVsb3Blci1hY2NvdW50LWFnYWluLyJdfSwiZXhwIjoxNzI0MjM1MTIwLCJpYXQiOjE3MjE2NDMxMjAsImlzcyI6Imh0dHBzOi8vYXBpLnBhc3Nwb3J0Lm9ubGluZS9vYXV0aCIsInNjb3BlIjoiZmVlZDpyZWFkIGFydGljbGU6cmVhZCBhc3NldDpyZWFkIGNhdGVnb3J5OnJlYWQgZW50aXRsZW1lbnRzIiwic3ViIjoiV1JDWFY3TjVWVnNaWnplbmJFZzdIRSIsInVzZSI6ImFjY2VzcyJ9.BI7JK2skhDZgUgGba_t_SXjnKnxabTEctlGqsyYP3IWzVfT-55ok4mPibp1BrZv7sQEmWhSq2lnTJecY92udrBnsLz1VOHn-w3EuhOD6CcglIebOrTYOzVV48o4qNkeuN6Cau9xNVVwniUFymvylulubI5iNqI_-P9fX9y8fvVYrUi3WQWD05zslCDoAL7b_2-c35p8gAfKa_fM00aITNB7HbLSZyoLBRDNaukHOEkZw5d6utjtBc-NVfmt99eaHuQRMWyZKGkzav6YIOOS0KQhG241EaPDGDp6d1qDqcXPxfG-gQvQ-MvBgI41DFRP9RMJEUekHyU-pOyLFHdbCCg) in particular), but I included the excerpted paragraph as a reminder that these are hard questions.

What does seem clear to me is that the way to answer hard questions is to not seek to freeze technology in time but rather to consider how many regulatory obsessions — including Windows dominance — are ultimately addressed by technology getting better, not by regulators treating mistaken assumptions (like operating system openness being an unalloyed good) as unchangeable grounds for competition.

#### Listen to this update and other Stratechery Plus content in your podcast player: [Stratechery](https://stratechery.passport.online/member/podcast?url=https%3A%2F%2Frss.stratechery.passport.online%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH) | [Sharp Tech](https://sharptech.fm/member/podcast?url=https%3A%2F%2Fsharptech.fm%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH) | [Dithering](https://dithering.passport.online/member/podcast?url=https%3A%2F%2Frss.dithering.passport.online%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH) | [Sharp China](https://sharpchina.fm/member/podcast?url=https%3A%2F%2Fsharpchina.fm%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH) | [Greatest Of All Talk](https://goat.passport.online/member/podcast?url=https%3A%2F%2Fgoat.passport.online%2Ffeed%2Fpodcast%2FAjAuUytxGNaa8WMvLCMHhH)



Subscription Information


Member: Omar Zoheri
Email: [stratechery@khamel.com](mailto:stratechery@khamel.com)
Plan type: Free


You are receiving this email because you are subscribed to [Stratechery](https://www.stratechery.com).

[Click here](https://stratechery.passport.online/member/login?email=stratechery%40khamel.com) to view your account and manage your subscriptions.
[Click here](https://stratechery.passport.online/member/unsubscribe?unsub=https%3A%2F%2Fapi.passport.online%2Fapi%2F1.0.0%2Fusers%2FWRCXV7N5VVsZZzenbEg7HE%2FchannelOptOut%3Faccess_token%3DeyJhbGciOiJSUzI1NiIsImtpZCI6InN0cmF0ZWNoZXJ5LnBhc3Nwb3J0Lm9ubGluZSIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzdHJhdGVjaGVyeS5wYXNzcG9ydC5vbmxpbmUiLCJhenAiOiJIS0xjUzREd1Nod1AyWURLYmZQV00xIiwiZW50Ijp7InVyaSI6WyJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvYXBpLzEuMC4wL3VzZXJzL1dSQ1hWN041VlZzWlp6ZW5iRWc3SEUvY2hhbm5lbE9wdE91dD9jaGFubmVsPWVtYWlsXHUwMDI2cmVkaXJlY3RfdXJpPWh0dHBzJTNBJTJGJTJGc3RyYXRlY2hlcnkucGFzc3BvcnQub25saW5lJTJGbWVtYmVyJTJGdW5zdWJzY3JpYmUiXX0sImV4cCI6MTcyNDIzNTEyMCwiaWF0IjoxNzIxNjQzMTIwLCJpc3MiOiJodHRwczovL2FwaS5wYXNzcG9ydC5vbmxpbmUvb2F1dGgiLCJzY29wZSI6Im1lbWJlcjp3cml0ZSIsInN1YiI6IldSQ1hWN041VlZzWlp6ZW5iRWc3SEUiLCJ1c2UiOiJhY2Nlc3MifQ.p-4Ernw9zKLCmmUvHHPOJl8oWjLjGkaIb5z6Tu5GcpKWmaNBw1x5tWsssK9SUtQlgqom8N7-CeY906nCuCaa_7HHNUJNoq19axrIghOrczY_QxdZ33ASOQf3Sj2gaFA9gi_JCJRvotbNggV5l_GF-o4jhsdGlpsS7ozzXXQZcwZxJDPxpzeghrn-lRBQ5bAbFhleBmqYZJSkzY4HfE3M3r-zU57rdBImtBlvzFKNvY6Ro27L3-Mcu8hyq7aCNZWI58wOJUmouiuREYqOKIUXg1CHLmELIn5dYo6Kj460UPj-qkDTIuGMliHtSZKv0GhJ752TYRC7b3m9NdSWLKE7Wg%26channel%3Demail%26redirect_uri%3Dhttps%253A%252F%252Fstratechery.passport.online%252Fmember%252Funsubscribe) to unsubscribe.


*© 2024
[Stratechery LLC](https://www.stratechery.com),
2093 Philadelphia Pike #9930, Claymont DE 19703*