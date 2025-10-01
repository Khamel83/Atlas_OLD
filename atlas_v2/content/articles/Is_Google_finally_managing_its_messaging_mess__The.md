# Is Google finally managing its messaging mess? | The Verge

**Source**: https://www.theverge.com/2020/5/27/21271186/google-rcs-t-mobile-encryption-ccmi-universal-profile
**Type**: article
**Created**: 2025-08-13T15:56:22.093156

---

title: Is Google finally managing its messaging mess? | The Verge
source: https://www.theverge.com/2020/5/27/21271186/google-rcs-t-mobile-encryption-ccmi-universal-profile
date: 2025-08-13T15:56:11.864131
tags: []
---
Sadly, the time has come for me to write about Rich Communication Services
again. There have been a few pieces of news about it in the past week or so
and I find myself vaguely optimistic that by this time next year Google will
be offering properly encrypted messaging to Android users with a relatively
simple, seamless experience that’s well on its way to being universally
available.

Plus, Google is finally starting to transition users from Hangouts to Google
Chat in a real way [under new management that is motivated to finally get it
right](/web/20250722001148/https://www.theverge.com/2020/5/7/21250790/google-
android-messaging-duo-phone-g-suite-javier-soltero-hangouts-chat) because
everybody is paying way more attention during the pandemic.

But let’s stick with RCS for the moment. Google has me at the spot where
[Charlie Brown is at his most tragically hopeful and
Sisyphean](http://web.archive.org/web/20250722001148/https://www.youtube.com/watch?v=RieABEtmpUg):
right before he resolves to run at the football and _really kick it this time_
despite knowing in his heart Lucy will pull it away again. Except the football
in this case is the easy answer I’d like to give to Android users about how
text messaging works on their phones.

By subscribing, you are agreeing to receive a daily newsletter from _The
Verge_ that highlights top stories of the day, as well as occasional messages
from sponsors and / or partners of _The Verge_.

Instead, the answer is as it ever was. (Deep breath.) [RCS is the more
advanced replacement for
SMS](/web/20250722001148/https://www.theverge.com/2018/4/19/17252486/google-
android-messages-chat-rcs-anil-sabharwal-imessage-texting) and if the carriers
and phones of all texters in a thread support it then you’ll get chat-like
features like typing indicators and bigger attachments. But there’s no real
way to know whether or not you’ll be getting RCS or plain old SMS until you
open up a chat window with one or several people and then wait to see what you
get.

If your carrier doesn’t support RCS, you can still [get it via Android
Messages and let Google handle RCS for
you](/web/20250722001148/https://www.theverge.com/2019/11/14/20964477/googles-
rcs-chat-android-rollout-us-ccmi-texting-sms), but it will still fall back
gracefully to SMS or MMS. In any case, none of these solutions offer truly
end-to-end encryption and there’s no indication Apple is even faintly
interested in supporting it on the iPhone.

And yet, I’m going to take a run at that football. Because while I don’t think
there’s going to be a _simple_ answer, I do see signs that Google is making
tangible progress towards _better_ answers.

The most recent news is that T-Mobile will finally begin supporting proper
[cross-carrier RCS
messaging](/web/20250722001148/https://www.theverge.com/2020/5/26/21270386/tmobile-
rcs-cross-carrier-universal-profile-google-messages) via the “Universal
Profile.” Until now, T-Mobile could technically say it supported RCS but in
reality it only worked between certain T-Mobile phones.

If you’re reading this and are an Android user, chances you think this whole
thing is moot because Google is already providing [RCS services to anybody who
wants them via its Android Messages
app](/web/20250722001148/https://www.theverge.com/2019/11/14/20964477/googles-
rcs-chat-android-rollout-us-ccmi-texting-sms). But the most common Android
phones are Samsung phones and Samsung ships its own texting app by default.
And most people just use the default.

So T-Mobile figuring out how to get its RCS to talk to Google’s RCS via the
globally accepted default is meaningful progress. That doesn’t mean we don’t
have more confusion in store. Last year [the major US carriers signed on to a
joint agreement called the Cross Carrier Messaging
Initiative](/web/20250722001148/https://www.theverge.com/2019/10/24/20931202/us-
carriers-rcs-cross-carrier-messaging-initiative-ccmi-att-tmobile-sprint-
verizon) that was designed to do the thing Google had been asking them to do
all along: support RCS Universal Profile. What does T-Mobile’s announcement
mean for the CCMI? Stay tuned I guess!

All of this RCS interconnect confusion and politicking would just be a morbid
fascination of mine if it weren’t for the fact that it all has direct and
tangible effects on Android users’ real lived experiences with text messaging.

So while I apologize for belaboring the minutiae, I am doing so to make a
point: even though you’re paying a monthly bill, your needs are not the
priority for your mobile carrier. It’s much more important in the boardrooms
of these carriers to make sure they’re not accidentally giving up anything to
another major tech company than it is to move more quickly towards the correct
solution.

“RCS is where we are like United Nations. We try to herd a bunch of people.”

That’s not to absolve Google, but as its [CEO Sundar Pichai told me in our
interview earlier this
month](/web/20250722001148/https://www.theverge.com/2020/5/19/21262934/google-
alphabet-ceo-sundar-pichai-interview-pandemic-coronavirus), “RCS is where we
are like United Nations. We try to herd a bunch of people.” Google is
committed to keeping Android at least somewhat neutral in the tug of war
between carriers and Google itself. That’s why progress is so slow.

But all of this is just a new version of the SMS status quo, honestly, because
RCS by default is not end-to-end encrypted. Unlike iMessage and Signal, your
texts are not as private as they could be.

Apparently that might change, as an [internal dogfooding build of Android
messages](http://web.archive.org/web/20250722001148/https://9to5google.com/2020/05/26/google-
messages-end-to-end-encryption-rcs/) has a bunch of strings and settings for
end-to-end encryption. As [it promised last
July](/web/20250722001148/https://www.theverge.com/2019/6/17/18681573/google-
rcs-chat-android-texting-carriers-imessage-encryption), Google is clearly
working on some kind of solution.

What will that solution look like? We’re still a little too early to say, but
if I had to guess I’d say it will be something that’s available for people who
use Google’s Android Messages app, but if anybody in the texting chain doesn’t
it’ll fall back to regular RCS or even SMS.

See, the way RCS works is your app sends a ping to the other phones to ask
whether it too can do RCS in a process called “capability exchange.” If both
apps support RCS, then you’re off to the races. There’s no technical reason
that capability exchange couldn’t also include a “hey do you support end-to-
end encryption?” message, too.

Maybe it will be more broad-based than that and become part of the official
GSMA Universal Profile spec, such that apps like Samsung Messages will also
work with it. But if I had to guess, I’d say Google’s going with the minimum
viable product. Or maybe that’s just what I _hope_ Google is doing, because
the fastest way to create pressure is to show real consumer demand.

Right now, iMessage users have the option for secure, end-to-end encrypted
messages when they text other iPhone users, built right into the default
experience. If Google comes through with encrypted messaging in Android
Messages, it’ll have the same option for Android users when they text other
Android Message users — again, built right into the default.

It would be nice if I didn’t need to add so many provisos to those sentences.
It would be really nice if, as they have done with exposure tracing, Apple and
Google could work together to create a system that protects user privacy in
messaging as well.

If Google actually enables end-to-end encryption, who will be holding the
secure messaging football? Google? The carriers? Apple? All I know is I’m
standing here under a leafless tree, a determined glint in my eye, getting
ready to take another run at it again. Knowing full well that one of them is
definitely going to yank it away.

* * *

Normally $250, the Apple AirPods Pro wireless earbuds [are down to
$220](http://web.archive.org/web/20250722001148/https://amzn.to/3aRkTYl) at
Amazon. Compared to the standard AirPods, these feature better sound quality
and noise cancellation. We’ve seen these drop a bit lower in price before, but
that’s a pretty rare occurrence.

__Vox Media has affiliate partnerships. These do not influence editorial
content, though Vox Media may earn commissions for products purchased via
affiliate links. For more information, see__[ __our ethics
policy__](http://web.archive.org/web/20250722001148/https://verge.cmail20.com/t/d-l-
mdkydlk-ykilzhrf-o/) __. Prices displayed are based on the MSRP at time of
posting.__

## SpaceX’s first crewed launch

> The Crew Dragon is designed to require minimal input from its passengers,
> but since this is a test, Hurley and Behnken will do some manual flying
> before they reach the space station. “It’s obviously something that we want
> to make sure we understand completely for future crews in case they ever
> have to fly the vehicle manually,” Hurley said during a press conference.
> The plan is for Hurley to take control right after Crew Dragon reaches orbit
> as well as when they approach the space station.

**┏**[**Sony’s Xperia 1 II ships in the US on July 24th for
$1,199**](/web/20250722001148/https://www.theverge.com/2020/5/24/21268097/sonys-
xperia-1-ii-ships-july-24th-1199-us-united-states)**.** For that price, those
cameras better finally deliver. Sony’s rap for years has been that it makes
the best sensors but somehow whiffs on its own smartphone cameras. Twelve
hundred bucks is definitely put up or shut up money.

I will say that as a Sony camera user, I’m weirdly excited for the pro camera
options here because Sony is using the same interface I’m already used to for
it.

**┏**[**Lenovo made two new tablets with detachable Bluetooth
keyboards**](/web/20250722001148/https://www.theverge.com/circuitbreaker/2020/5/26/21270506/lenovo-
tablets-yoga-duet-7i-ideapad-duet-3i-features-specs-price)**.** Putting
Bluetooth in the keyboard on a Surface clone (which is not a knock, just the
easiest way to describe this form factor) is maybe clever. Honestly, is there
a Windows computer Lenovo wouldn’t try out?

> The most interesting thing about the Oppo Watch software is its selection of
> built-in apps, which are accessible through a scrolling grid that’s halfway
> between the Apple Watch’s weird honeycomb and list views. There are the
> usual apps for phone calls, fitness tracking, timers, and weather, as well
> as an on-watch app store and China-specific services like Alipay. It’s a
> pretty robust feature set, including things like sleep tracking that haven’t
> come to the Apple Watch yet.

**┏**[**Microsoft Surface Headphones 2 review: perfect for work-from-home
life**](/web/20250722001148/https://www.theverge.com/2020/5/22/21267032/microsoft-
surface-headphones-2-review-noise-canceling-specs-price)**.** Chris Welch says
they’re competent in lots of categories even if they’re not class-leading.
Sometimes nailing the basics is exactly what you want.

> As you may have realized by now, the Surface Headphones 2 don’t best Sony
> and Bose in every category. But since Microsoft decided on a much smarter,
> more affordable price this time around, they don’t necessarily have to.

> I just spent a week riding Carqon’s first production bicycle here in
> Amsterdam. It’s an 88-pound (40 kg) electric cargo bike designed to
> transport an adult and up to four kids a distance of up 75 miles (120 km)
> before needing a recharge. I came away a believer in the transformative
> power of the electric cargo bike to replace both diesel-gulping delivery
> vans and family cars in the world’s cities.

**┏**[**The human cost of Instacart’s grocery
delivery**](/web/20250722001148/https://www.theverge.com/21267669/instacart-
shoppers-sick-extended-pay-quarantine-leave-coronavirus)**.** Russell Brandom
talked to eight Instacart workers who got sick, yet despite promises from the
company only three of them got sick pay. Just incredibly terrible treatment of
workers here.

> Under the circumstances, it was inevitable that customers would get
> frustrated. The app made it seem as though shoppers had access to a special
> warehouse where all of the goods were kept, like Amazon. Why would the app
> list a product for sale if you couldn’t actually buy it? Instacart would
> recoup the cost of a particular grocery order if buyers refused to pay, but
> there were lots of other ways angry customers could make life hard for
> shoppers, like clawing back tips or leaving a zero-star rating. And most of
> the time, customers didn’t get mad at stores; they got mad at shoppers.
> Instacart had arbitraged customer anger onto the most vulnerable people in
> the system.

**┏**[**Emergency COVID-19 vaccines will have to convince a skeptical
public**](/web/20250722001148/https://www.theverge.com/2020/5/26/21266591/covid-19-coronavirus-
vaccine-fda-authorize-emergency-experimental)**.** You’ve already learned a
lot of medical terminology in the past couple months. As Nicole Wetsman
writes, you’re going to need to learn yet more:

> The challenge is, Quinn’s research shows that most people don’t have a good
> sense of the difference between drug approval and emergency authorization.
> She found that Americans have a limited understanding of FDA terminology
> around experimental products. “People don’t understand that kind of
> language,” she says. In one survey, she found people were unfamiliar with
> terms like “emergency use authorization,” “off-label” (which is when a drug
> is used for different disease than the one it was approved for), and
> “investigational new drug” (a drug that’s being tested in clinical trials).

**┏**[**HBO Max is full of potential, but its biggest hurdle remains AT &T;’s
messy
execution**](/web/20250722001148/https://www.theverge.com/2020/5/26/21268490/hbo-
max-launch-price-warnermedia-att-dc-harry-potter-friends-disney-netflix-
peacock)**.** It’s launching today. Julia Alexander on all the ways AT&T; is
own-goaling itself on this launch strategy:

> In the middle of it all is a confusing, nearly comedic branding struggle
> that has HBO diehards concerned and WarnerMedia executives on the defense.
> (I cover this industry daily, and even I scratch my head over the
> differences between HBO Go, HBO Now, and HBO Max.) That’s the question at
> the heart of HBO Max’s launch: what is it? Leveraging prestigious
> programming from HBO, tentpole franchise movies from the DC and Harry Potter
> universes, kids content in the form of Sesame Street, and new original
> programming, HBO Max wants to give anyone and everyone something they can
> watch.

[](/web/20250722001148/https://www.theverge.com/2020/5/27/21271186/google-rcs-
t-mobile-encryption-ccmi-universal-profile#comments)
