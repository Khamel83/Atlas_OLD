# Epic 'Frinkiac' Search Engine Matches Any Simpsons Quote With Its Still | WIRED

**Source**: http://www.wired.com/2016/02/ultimate-simpsons-search-engine-pairs-quotes-with-stills/
**Type**: article
**Created**: 2025-08-13T18:26:27.861393

---

title: Epic 'Frinkiac' Search Engine Matches Any Simpsons Quote With Its Still | WIRED
source: http://www.wired.com/2016/02/ultimate-simpsons-search-engine-pairs-quotes-with-stills/
date: 2025-08-13T18:26:20.994582
tags: []
---
One site. Fifteen seasons. _Three million_ searchable screengrabs. This is the
wonder that is
[Frinkiac](http://web.archive.org/web/20250223141705/https://frinkiac.com/), a
compendium of _Simpsons_ moments frozen in time, and the latest, best, most
perfectly cromulent way to waste time on the Internet.

_Update, May 12th: Frinkiac now offers GIFs in addition to screengrabs.
Everything else is the same; you search a term, brings back frames, you can
add text to "meme" them. Now, though, you can also create a GIF of up to four
seconds, which adds up to about 19 Frinkiac frames. They take just a few
seconds to process, after which there are easy-share buttons for Facebook,
Twitter, and Reddit. Please use this power responsibly!_

Frinkiac, named after Springfield’s favorite eccentric scientist, Professor
Frink, landed on the Internet yesterday with all the subtlety of a Lard Lad
Donuts mascot. It collects every quote from the first 15 seasons of _The
Simpsons_ , the most quotable show of the last two decades, and pairs them
with screenshots from the exact moment they happened.

"We had the idea several years ago when we were quoting _The Simpsons_ at each
other all day long, and it was surprisingly difficult to find an image of the
scenes we were quoting on Google," says Sean Schulte, who created Frinkiac
with Paul Kehrer and Allie Young. Though they kicked the idea around for
awhile, they didn't decide until six months or so ago to actually build it.

The work went surprisingly quickly. "The majority of the code was written in
about a week, to parse the video files and upload them to the server and index
them and search them," says Schulte. From there, Young spent a few weeks
developing and tweaking the UI. And so Frinkiac was born.

In a [post
describing](http://web.archive.org/web/20250223141705/https://langui.sh/2016/02/02/frinkiac-
the-simpsons-screenshot-search-engine/) what’s under the hood, Kehrer outlines
the process by which this brilliant bit of coding generates screen captures.
While he describes it as “fairly naive,” it’s also fairly brilliant. Frinkiac
cuts every scene into 100 parts, takes the average color of each part, and
compares its coloration to the most recently saved image. If they’re different
enough, _voila!_ , new screenshot, with minimal redundancy through the
hundreds of hours of video being parsed.

To match the resulting screenshots with the right quote, Frinkiac parses
subtitle files as well, and lines up time codes between words and images.
Kehrer notes that season 11 has “a significant time skew problem,” making it
hard to track down the precise moment Professor Frink mutters “for glaven out
loud” at Lucy Lawless. A loss, but not an irredeemable one.

"For the last several months it's been complete," says Kehrer, "but we've just
used it with coworkers and friends."

Thank goodness they made it public. The demise of Frank Grimes? Frinkiac's got
it. Beer as the cause of and solution to all of life’s problems? You bet. I
bent my Wookie? Darn right I did. For each of these searches, Frinkiac doesn’t
return just a single, representative shot. It offers a range from which to
choose. Ralph Wiggums’ “Wookie” moment spits back 10 frames from that scene
alone, along with several partial matches from other episodes.
