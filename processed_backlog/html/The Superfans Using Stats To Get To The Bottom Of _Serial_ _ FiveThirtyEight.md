# The Superfans Using Stats To Get To The Bottom Of ‘Serial’ | FiveThirtyEight

**Source:** inputs/New Docs/html/fivethirtyeight.com_features_the-superfans-using-stats-to-get-to-the-bottom-of-serial.html
**Processed:** 2025-08-24T19:14:11.995622

![](https://fivethirtyeight.com/wp-content/uploads/2014/12/serial-podcast1.jpg?w=575)



Family photos are seen in the home of Adnan Syed’s mother, Shamim Syed.

Patrick Semansky / AP



Prison artwork created by Adnan Syed sits near family photos in the home of his mother, Shamim Syed.

Patrick Semansky / AP

“[Serial](http://serialpodcast.org/)” is over, but the podcast’s fans aren’t done debating who committed the 1999 murder of Baltimore County high school student Hae Min Lee. And statisticians have ideas about how to make the debate smarter.

“Serial” attracted a broad audience over its 12 episodes; it [got 5 million downloads and streams](http://www.theverge.com/2014/11/18/7241715/serial-breaks-itunes-record-for-fastest-podcast-to-reach-5-million) on iTunes faster than any other podcast in history, according to Apple. Among the first season’s audience were many [lawyers](https://www.themarshallproject.org/2014/12/10/our-jury-is-in-on-serial) and [journalists](http://www.slate.com/blogs/browbeat/2014/12/18/serial_podcast_last_episode_what_we_know_was_a_worthy_finale_slate_discuses.html).1 That isn’t a surprise; the show is about justice and journalism. But it’s also about stats.

Enter the “Serial” statistician superfans. These fans ask questions like: What is the probability that then-17-year-old Adnan Syed2 killed Lee, his ex-girlfriend, in a Best Buy parking lot? What is the probability that Jay3, his friend-turned-accuser, was telling the truth about Syed’s guilt? If Syed is innocent, how likely is it that several pieces of evidence point to his guilt? And how likely is it for someone who is convicted of murder to be innocent?

[Bayesian statistical thinking](https://fivethirtyeight.com/features/how-statisticians-could-help-find-flight-370/) can’t solve the podcast’s central mysteries, but it can provide tools to make analysis of the case more systematic and less speculative. Each listener who became obsessed with host Sarah Koenig’s narrative started out with some personal estimate of the likelihood of Syed’s guilt, then updated that probability based on evidence. Doing that quantitatively is a Bayesian process.

Following the case as a Bayesian is “a roller coaster” of updating probabilities, said statistician Kristian Lum, who spoke to me by phone along with her husband, James Johndrow, a doctoral student in statistics at Duke University.4 Lum started our conversation by saying she was a 9 out of 10 in obsessiveness about “Serial.” By the time she was quoting Reddit threads, she’d upgraded herself to 9.5.

That roller coaster starts at a different position depending on who is riding it. In a criminal trial, jurors are supposed to presume the accused is innocent. In Bayesian terms, that means “the court system instructs the jury to start with the assumption of prior probability of guilt close to zero and only convict if the evidence moves that belief all the way from near 0 percent to near 100 percent certainty of guilt,” said Ander Wilson, a postdoctoral research fellow in biostatistics at Harvard’s public health school.

Listeners aren’t jurors. Yet statistical thinking still can help guide fans of the show in their thinking about Syed.

Take, for instance, the argument of producer Dana Chivvis, which she outlined in the finale Thursday. Chivvis said that if Syed is innocent, then he’d have to have been awfully unlucky to have the following series of facts all make him look guilty:

* He asked the victim for a ride;
* He lent his car and cellphone to Jay, the man who accused him of the murder5;
* His phone had a record of a call to Syed’s friend who didn’t know Jay (that suggests Syed had the phone when he said it was with Jay);
* And his cellphone records can seem to corroborate the prosecution witness’s account during the time Syed couldn’t say exactly where he was on the day the victim disappeared.6

Chivvis said this argument points to Syed’s guilt. But Bayesians say that’s not quite right. The probability of this evidence given Syed’s innocence could be low, yet so could the probability of his guilt given this evidence. Other factors, such as one’s prior belief of his innocence, affect the calculation.

Syed’s bad luck looks more plausible when we take into account the [multiple-testing problem](http://www.stat.berkeley.edu/~mgoldman/Section0402.pdf). That’s one name for the problem researchers face when they test their hypothesis in too many different ways. They risk reaching a false conclusion because they’ve looked too hard for it. They’ve raised their chance of finding what looks like something too unlikely to be a coincidence, unless you correct for all the different ways they’ve looked for it. The call to Syed’s friend, Nisha, raises this problem. “The Nisha call” would have looked just as suspicious if it had gone to any of Syed’s contacts whom Jay didn’t know, Joe Guinness, an assistant professor of statistics at North Carolina State University, points out. Accidentally calling any particular one of them — a pocket dial, Syed’s explanation for the call — was unlikely. Calling any of them, rather than someone Jay knew, was the most likely outcome of an accidental dial.

Also in Syed’s case, there is lots of evidence that doesn’t look bad for him. For instance, there’s the claim of a classmate, never raised at trial, that she saw Syed at a library at a time prosecutors said he was committing murder. Depending on how many different pieces of evidence prosecutors and Koenig examined, we might expect them to find as many pieces of evidence that look bad for Syed as Chivvis outlined, even if he were innocent. Focusing only on the evidence that implicates him artificially elevates the probability he’s guilty — which, according to “Serial,” is the sort of selective narrative that got the prosecution its conviction.

“There is a very low probability that a similar string of events would happen to you or me tomorrow,” Guinness said. “However, there is a much higher probability that a randomly selected person convicted of murder had some unfortunate events occur that made him look guilty when he was innocent.”7

This could apply to any criminal case, but Syed’s case wasn’t randomly chosen for “Serial.” Koenig probably selected it in part because of her connection to Baltimore (she was a former reporter in the city) and to Syed’s attorney, whose career [Koenig had covered](http://articles.baltimoresun.com/2001-06-02/news/0106020237_1_lawyer-gutierrez-clients). That helped, but by itself it wouldn’t have prompted a year of work and millions of streams. Syed’s case could carry the podcast because it has two seemingly contradictory traits: It resulted in a conviction, yet the predicament of the man convicted is strong enough to inspire his friend to advocate on his behalf for 15 years, to bring the case before a journalist, and to persuade the journalist to devote a year of her life and the time and resources of her colleagues to a show that wouldn’t work without a strong chance he’s innocent. That sort of selection bias could produce a case that is more likely than the average case to feature an innocent defendant with evidence that makes him look guilty.

“Adnan’s case was not randomly selected — it was pursued specifically because of the lack of physical evidence leading to his conviction and his incessant claims of innocence,” Guinness said.

Without hard data, statistical principles won’t get us all the way to a probability of Syed’s guilt. Guinness tries to work out some of the numbers — for instance, the prior probability Syed is guilty based on his status as a recent intimate partner of the victim, and stats showing [many women are killed by intimate partners](http://www.bjs.gov/content/pub/press/ipv.pr). It remains a matter of subjective judgment, though, to assign conditional probabilities to things like Jay accusing Syed, if Syed is innocent; and a pocket dial, when there is a disputed phone record.

“These days we’re so used to saying, ‘Oh, I can just download the data and answer really quickly,’ ” said Johndrow, the Duke doctoral student. “But in this case, we can’t really do that.”

People’s different prior beliefs about the case — based, for instance, on how much stock they put in a conviction — and different weighing of the evidence drive very different conclusions, Geoffrey Colin Peterson and Christopher Krut, stats doctoral students at N.C. State, point out.

“There’s a lot of wiggle room based on subjective probabilities you’re plugging in in your head,” Lum said.

Even so, there is value in using Bayes’ Theorem to process all these subjective probabilities, Johndrow said. Without training, [people generally can’t intuit](http://www.significancemagazine.org/details/review/1392103/Thinking-Fast-and-Slow-by-Daniel-Kahneman.html) their way to statistical thinking. “It’s often very dangerous to try to do it in your head,” Johndrow said. “You kind of need to do each piece by itself, give that a number, and see what pops out.”

Enthusiasts of the show have been digging into the evidence, looking for clues to solve the case. Johndrow thinks more statisticians will start applying their trade to Lee’s murder. “This is a really interesting statistical problem here,” Johndrow said. “Maybe it will stimulate them to think more about it.”