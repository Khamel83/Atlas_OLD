# Inside Twitter's ambitious plan to kill the password

**Source**: inputs/New Docs/reader/www.theverge.com_2014_10_22_7034113_inside-twitters-ambitious-plan-to-kill-the-password-on-mobile-devices.html
**Type**: article
**Created**: 2025-08-25T02:53:56.040442

---

As he traveled the world last year as part of a user research project, Michael Ducker noticed a problem. Ducker, a senior product manager at Twitter, was part of a team that visited Brazil, India, and Indonesia to learn about how people use mobile devices around the world. Twitter is courting new users aggressively, and like most tech companies it signs them up with a combination of an email address and password. The problems with passwords are well known: they can be hard for us to keep track of, easy for hackers to figure out, and never anything but tedious to type out on your mobile device’s tiny keyboard.  
  
But in his travels, Ducker and his team began to understand the other half of the problem in signing up new users: the farther he traveled from America, the less likely it was that anyone he met had an email address. In developing countries, people are more likely to identify themselves via their mobile devices. Instead of email addresses, they have cell phones — and no way to easily sign up for Twitter or other services. But that’s all about to change: if Twitter has its way — and developers decide they can trust it again — phone numbers will become the primary way we log into our mobile applications, and we’ll all have fewer passwords to remember.  
  
The further you travel from America, the less likely anyone is to have an email address  
  
Today at Flight, its first developer conference in four years, Twitter is unveiling a suite of developer tools aimed at re-making mobile applications. And while many of the details are of interest only to developers, Twitter is positioning the tool set — called Fabric — as a new start. "Fabric is actually the next evolution of Twitter itself," says Kevin Weil, vice president of product for revenue at the company. "After Fabric, as the platform grows, you won’t think about Twitter as just the consumer app. You’ll think about Twitter as a broader mobile services company. So Fabric is a really big step in that direction for us."  
  
Introducing Digits  
  
For most people, the most visible part of the new Twitter will be Digits, the company’s password replacement effort. Starting soon, developers will be able to use Digits to sign up users to their apps. The process has three steps: a login screen with an option to sign up via mobile device; a screen to enter your phone number, and a screen to enter the confirmation code Twitter sends you via SMS. (The process will look familiar to anyone who has signed up for WhatsApp or, more recently, Yo.) The confirmation code expires after you use it once, so the next time you need to log in to the app, you’ll be sent a fresh code.  
  
Like Vine, Twitter’s video-sharing app, Digits will operate as a brand unto itself. It has a home at Digits.com, where you can manage other apps’ access to your phone number, or delete your account. For developers, it’s a more secure way to bring on users around the world. And for Twitter, it’s a way to help eliminate passwords. Most people use the same passwords repeatedly, and use passwords that are relatively easy to guess. And many buzzy new apps aren’t backed by strong security practices. Twitter says it is bringing everything it has learned about security since its founding to Digits. "Passwords just suck," Ducker says. "I go to dinner parties and people say, 'Oh, you work in tech? Can you get rid of the password?' And we’re finally getting rid of the password, for the vast majority of use cases."  
  
Phone numbers aren’t perfectly secure; it is possible, though not easy, to clone a phone number. But for most people, logging in with a phone number is probably more secure than using an email address and a password. And because the login codes created through Digits expire after a single use, there’s less danger in hackers obtaining a cache of login information and using it maliciously, as seems to happen every other week. Eventually, Digits will support two-factor authentication for apps, sending users a secondary PIN code to use in combination with the expiring codes.  
  
A way to diversify Twitter  
  
Much of Twitter Fabric was first reported last month by The Information. But contrary to that report, registering a number with Digits does not create a "shadow" Twitter account. Twitter says there is almost no connection between Fabric and the consumer app whatsoever. Fabric is not primarily a way to attract more users to Twitter, they say — it’s a way to diversify Twitter, growing its nascent business of selling tools to mobile developers from a company that was born on cellphones. (It’s not the only social network to have this idea; Facebook started doing something similar last year after acquiring the developer service Parse.)  
  
In addition to Digits, Twitter will also announce new features for MoPub, Twitter’s lucrative advertising platform, and Crashlytics, which offers developers free services for beta testing and crash reporting. Crashlytics will offer a native development kit for Android, let developers troubleshoot problems at the system level; and a tool for distributing beta versions of software to testers via an emailed link. And Digits is part of a larger module called TwitterKit, a new set of APIs for Twitter that, among other features, enables the same system-level sign on for Android that Twitter already has on iOS. Log in to your Android device with Twitter and you’ll be able to sign into any other app that has enabled Twitter logins.  
  
Twitter still pays for all those SMS messages  
  
Everything Twitter is announcing today will be free to developers, raising the question of how the company benefits. (The company will pay carriers for every SMS it sends through Digits.) The basic idea is that if a critical mass of developers adopts Twitter’s tools, the company will eventually be able to sell them services to complement the free ones. "If you do that, you’re providing a very powerful platform for developers, and there’s lot of benefits that come down the road from that," Weil says.  
  
Can Twitter be trusted?  
  
First, though, Twitter has to convince developers to embrace it. The company’s relationships with the developers who build on its platform has been strained since 2012, when it unveiled new "rules of the road" whose primary effect has been to discourage the development of third-party Twitter clients. A handful remain, but they seem perpetually at risk of disappearing. The developer Marco Arment, writing this week, said he would never trust Twitter again: "We’re just innocent bystanders getting hit whenever this fundamentally insecure, jealous, unstable company changes direction, which happens every few years," wrote Arment, who most recently developed Overcast, an app for listening to podcasts. "Twitter will never, and should never, have any credibility with developers again."  
  
"Our API was so open that we allowed people to compete with us."  
  
Twitter, for its part, says what happened in 2012 has little bearing on its platform strategy today. "The two situations are completely different — so different, in fact, that it doesn’t even really make sense to conflate them, honestly," Weil says. He named a few companies that have made millions of dollars developing on Twitter’s platform, including TweetDeck, Hootsuite, and the social-media monitoring company Radian6, which sold to Salesforce for $340 million. The changes in 2012 were intended only to ensure Twitter had control over its core service, he says. "Our API was so open that we allowed people to compete with us, and so there were changes we had to make."