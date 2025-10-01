# Here's How Google Makes Sure It (Almost) Never Goes Down | WIRED

**Source**: http://www.wired.com/2016/04/google-ensures-services-almost-never-go/
**Type**: article
**Created**: 2025-08-13T18:14:16.540670

---

title: Here's How Google Makes Sure It (Almost) Never Goes Down | WIRED
source: http://www.wired.com/2016/04/google-ensures-services-almost-never-go/
date: 2025-08-13T18:14:07.996616
tags: []
---
When was the last time you needed to Google something and Google wasn't there?

Odds are, you don't remember that ever happening. Sure, there are times when
you can't reach Google because your internet connection is down. But Google's
primary online services, from its search engine to Gmail to Google Docs and
more, are nearly always accessible. The company's Google Apps suite, including
Gmail and Docs, was available about 99.97 percent of the time in 2015,
according to the company's own numbers. The world pretty much takes this for
granted, but it's a remarkable reality. The billions who use Google hardly
stop to consider how Google made something so impressive seem so mundane.

Google explains the feat in three words: Site Reliability Engineering. OK,
they aren't the best three words. But that's the rather unsexy name Google
gave to this seminal philosophy more than a decade ago. It's a rather nuanced
and expansive philosophy, but it really boils down to one central idea: _Don't
get IT people who specialize in running Internet services to run your Internet
services. Have software coders run them instead_. If you do this, the thinking
goes, the software coders will build tools that can help run the operation
_without the active involvement of real live people_.

"The result of our approach," writes Googler Ben Treynor Sloss in a new essay,
"is that we end up with a team of people who will quickly become bored by
performing tasks by hand and have the skill set necessary to write software to
replace their previously manual work."

For many in Silicon Valley, that may seem like a common idea. This kind of
thing is now practiced across the tech world, from Amazon to Box.com. People
call it DevOps---"development" plus "operations"---an effort to combine the
ways of the software coder with the aims of the systems administrator. But the
DevOps movement, embodied by tools like Chef and Puppet, [evolved separately
from and largely
after](http://web.archive.org/web/20250425132443/https://www.wired.com/2011/10/chef_and_puppet/)
the SRE philosophies that arose inside Google (and similar ideas that took
hold at Amazon). It's just that Google has kept largely quiet about this over
the last decade, as it [often did when the topic was the inner workings of its
enormously efficient online
operation](http://web.archive.org/web/20250425132443/https://www.wired.com/2012/08/google-
as-xerox-parc/).

But the company has entered a new period, one in which it's more willing to
discuss such things ([mainly because it wants to promote the cloud services
that allow outside business to run their own software atop its vast network of
data centers and
machines](http://web.archive.org/web/20250425132443/https://www.wired.com/2014/03/urs-
google-story/)). Google has even gone so far as to write a book about Site
Reliability Engineering.

The book is called, well, _Site Reliability Engineering_. It was just
[published by
O'Reilly](http://web.archive.org/web/20250425132443/http://shop.oreilly.com/product/0636920041528.do),
and the essay from Sloss serves as the first chapter. If you're into DevOps,
it's a must-read. And even if you're not, the opening of the book---the
preface, the introduction, and the first chapter--is a fascinating look at the
attitudes that drive the world's largest online empire.

For many in tech---and almost everyone outside of tech---system administration
(or operations or whatever you want to call it) is an afterthought, one of the
more boring aspects of computer technology. But Sloss, officially known as
Google's Vice President for 24/7 Operations, turns this notion upside down,
arguing that site reliability is "the most fundamental feature of any
product." After all: "A system isn't very useful if nobody can use it."

Ground Zero

Sloss is ground zero for the SRE movement. It began when Google hired him to
run its operations, and it was he who coined the term. "SRE is what happens
when you ask a software engineer to design an operations team," he says. "I
designed and managed the group the way I would want it to work if I worked as
an SRE myself."

For Todd Underwood, now an SRE director at Google, it's only natural that the
company would hire a coder like Sloss for the job. "When Google was in its
infancy, there were so many software engineers who had a better sense of how
things broke and a better sense of how engineering could be done well," he
tells WIRED. "But not one them wanted to do any of that by hand."
