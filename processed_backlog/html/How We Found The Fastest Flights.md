# How We Found The Fastest Flights

**Source:** inputs/New Docs/reader/fivethirtyeight.com_features_how-we-found-the-fastest-flights.html
**Processed:** 2025-08-24T19:14:20.253223

Our analysis of the fastest flights has two goals. First, it serves as a quick way to help you find the fastest airline on any particular route. Flying from Atlanta (ATL) to Houston (IAH)? The interactive tells you that Delta took an average of 2 hours and 22 minutes to complete the flight last year; United took 20 minutes longer.  
  
The second goal is to find the best- and worst-performing airlines and airports. Our method apportions blame for delays between them: For instance, it recognizes that all carriers perform worse flying out of Chicago O’Hare (ORD) than flying out of Honolulu (HNL). Accounting for this helps us compare airlines on a level playing field — something the government’s on-time statistics do not do.  
  
Creating that level playing field requires thinking about air travel a little differently. In particular, we’re concerned with which airlines are fastest relative to the distance they travel and the airports they fly into and out of, rather than as compared to the schedules they publish.  
  
We’d encourage you to explore the interactive, and read our article about the fastest airports and airlines. What follows are a series of answers to questions you may have about our methodology.  
  
What data are you using?  
  
This data comes from the Bureau of Transportation Statistics (BTS), which publishes very large files each month that contain delay data on every flight flown by a major airline within the U.S. They cover about 500,000 flights per month, or about 6 million over the course of the past year. Our analysis of the fastest flights is based on the most recent 12 months of available data. As of the launch of the interactive, this covers the period from January to December 2014.  
  
What do you mean by “fastest” flights? I’m used to hearing about delayed or on-time flights.  
  
Yeah, we know. So let me give you a proposition. Airline A says it will fly you from Seattle to Portland, Oregon, in 45 minutes, but actually takes 60 minutes. Airline B says it will fly the same route in 75 minutes, and actually takes 70 minutes. Which flight would you rather take?  
  
That seems easy. Airline A!  
  
I agree: Airline A saves you 10 minutes relative to Airline B. It’s the “faster” flight — the flight with the quickest average travel time, accounting for delays, cancellations and diversions.  
  
But according to the way the government keeps track of delays, Airline A’s flight is “late” because it comes in at least 15 minutes after its scheduled arrival time. Airline B’s flight is “on time” (a few minutes early, in fact). That seems backward to us.  
  
The problem is that airlines are responsible for setting their own schedules, and they often pad them. On average, United schedules about 8 minutes longer to fly the same routes as Frontier, for example.  
  
We think it’s best to compare airlines against a neutral baseline and not one they set themselves. So that requires us to introduce some new language.  
  
There are more terms I’m not familiar with. For instance, “target time,” “typical time” and “time added.” What does all of that mean?  
  
Let’s define those terms with an example. Here’s how the four airlines that regularly fly from San Francisco (SFO) to Los Angeles (LAX) compared on that route in 2014:  
  
Average flight time is just what it sounds like: how long the airline took to complete the route, on average, over the past 12 months of available data. It includes a way of accounting for canceled and diverted flights in addition to delays (more about that later).  
  
Target flight time is an estimate of how long the flight “should” take based on the distance and direction of travel. It assumes flights travel at about 500 mph, adds a buffer of about 45 minutes for taxi-in and taxi-out time, and adjusts for whether the flight is eastbound or westbound (eastbound flights fly faster because of the jet stream). Note that because target time is based on only the origin and destination airports, it’s the same for each airline on a particular route. On the flight from SFO to LAX, for instance, the target time is 1 hour, 19 minutes. (For a more precise description of how target time is calculated, see the footnotes. )  
  
But target time is based on somewhat ideal conditions — it assumes flights land exactly on time. In fact, the average flight lands about 14 minutes late, by our accounting. Some of this has to do with the airlines, but a lot of it also involves the airports.  
  
That’s what typical time is about. It reflects the target time plus the typical delays associated with the origin and departure airports. Departing out of San Francisco adds 10 minutes to the typical flight. Arriving at LAX adds 5 minutes. So the typical time on this route is 1 hour, 34 minutes, or 15 minutes longer than the target time.  
  
Our measure of an airline’s performance is whether its average flight time beats the typical time on a particular route. We call the difference time added. Negative scores are good — they mean the airline saves you time.  
  
You forgot about “scheduled time.” What does that mean?  
  
It means just what you think it means — how much time the airline scheduled for that route. But the airlines’ schedules aren’t a big point of emphasis in our method.  
  
The SFO-LAX route provides a good illustration of why. Virgin America’s average time is almost half an hour faster than Southwest’s. But Southwest’s scheduled time is the same as Virgin’s and is lower than United’s and American’s, even though its average time is higher.  
  
So you’re giving credit to flights for arriving early?  
  
As if that’s a bad thing? But I know the circumstance you’re worried about. Your flight lands 10 minutes ahead of schedule, only to sit on the tarmac for 30 minutes because there isn’t a gate open yet. You come out behind instead of ahead.  
  
But the government still considers those 30 minutes on the tarmac part of the flight — it only counts an arrival when the plane gets to the gate. So do our estimates of average flight time. Travel time is measured from the originally scheduled departure time — the one listed on your ticket when you book the flight — until the plane pulls up at the gate at the destination airport.  
  
OK, I got the terminology, but are these predictions of which flights will arrive soonest?  
  
Not really. Our calculations are based on historical data over the past 12 months of performance. With that said, we’ve found airline performance to be fairly consistent from year to year and month to month.  
  
I just flew a route yesterday, and I can’t find it in the interactive. What gives?  
  
It could be a new route, or one that’s flown too infrequently; in the interactive, we only list routes if they had at least 100 scheduled flights over the past 12 months.  
  
But the most likely explanation is that it was flown by a carrier that’s too small to meet the government’s reporting standards. BTS only requires an airline to report its on-time statistics if it accounts for at least 1 percent of domestic passenger revenues. Spirit Airlines met that threshold for the first time last year, for example, so it will begin reporting its data soon, but it didn’t in 2014. Sun Country Airlines still doesn’t account for 1 percent of passenger revenues so its data isn’t listed at all.  
  
But I flew Delta! In fact, I flew the Delta Shuttle from New York to Washington, D.C. That’s one of the more famous routes in the country. It flies about a dozen times per day. And I still can’t find it.  
  
Technically speaking, you didn’t fly Delta. You flew Shuttle America, which operates the flight on behalf of Delta.  
  
That seems awfully confusing. It said Delta when I booked my ticket. I checked in at the Delta counter. The plane was painted in Delta colors.  
  
We agree. If we had our druthers, this would be listed as a Delta flight in the government’s data. Unfortunately, it isn’t. In fact, it isn’t listed at all because Shuttle America is too small to meet the government’s reporting requirements.  
  
About half the flights in the United States are flown on this basis: a regional carrier or a smaller subsidiary operating on behalf of a major airline.  
  
But here’s the good news. Three regional carriers — Envoy Air, ExpressJet Airlines and SkyWest Airlines — are large enough to report their data. Together, they account for about 2 million flights each year. We’ve taken those flights and classified them under the major airlines on whose behalf they’re flown.  
  
How do you assign flights flown by regional carriers to the major airlines?  
  
For Envoy Air, this is simple. Envoy was formerly known as American Eagle and operates all its flights on behalf of American under its American Eagle brand. (In fact, Envoy is a subsidiary of American Airlines.) So all Envoy flights are treated as American flights.  
  
ExpressJet and SkyWest, however, operate on behalf of several major airlines. Fortunately, we were able to infer which flights are flown for which airlines based on the flight numbers. (Our inferences are based on looking at published schedules and the routes flown. For instance, SkyWest operates its Denver to Little Rock, Arkansas, flight only on behalf of United.) You can find which flight numbers our program assigns to which airlines in the footnotes.  
  
I noticed that you’re still listing American Airlines and US Airways as separate airlines. Don’t you know that they’ve merged?  
  
American Airlines and US Airways are, indeed, in the process of merging. But airline mergers are big, complicated things that can take several years to fully complete. For the time being, the government continues to list these airlines’ delay statistics separately and so we do, too. US Airways is one of our highest-ranked airlines while American is among the lowest, so it will be interesting so see which culture prevails.  
  
How about Southwest Airlines and AirTran?  
  
Their merger is complete. The government continued to list a few AirTran flights in 2014, but no longer does so. We classify all remaining AirTran flights as Southwest flights.  
  
How do you compare canceled flights to delayed flights?  
  
We’re glad you saved this question since it’s one of the more complicated ones.  
  
A quick-and-dirty answer is that canceled flights are associated with a delay of four or five hours, on average. However, the calculation varies based on the particular circumstances of each flight. If your flight is canceled, the airline will usually put you on its next flight with an available seat. Our program simulates the process the passenger would have gone through at the time of the cancellation.  
  
In particular, our method assumes it takes three additional flights to accommodate passengers from a canceled one (equivalent to a load factor of 75 percent). So the program looks for the next three available flights that were flown by the same airline on the same route and assigns the passengers from canceled flights to them.  
  
“Available” is a key term because delays can accumulate. If all an airline’s Tuesday flights are full because they’re carrying passengers from a Monday morning cancellation, passengers from Monday afternoon’s flight will have to wait until Wednesday if their flight is canceled as well. Just like in the real world, it can sometimes take days to accommodate everyone.  
  
So let’s say you originally planned to fly on Saturday, but your flight was canceled and you didn’t get out until Tuesday. Should that count as a 48-hour delay?  
  
In my view, that assumption is too harsh. Instead, the added time associated with a cancellation is capped at four hours (240 minutes), plus whatever additional problems the passenger encounters on her new flight. (The reasoning behind this is explained in the footnotes. )  
  
For instance, say that the passenger’s original flight is canceled and there’s nothing available within the next four hours. She gets the maximum 240-minute penalty. But her replacement flight is also canceled (another 240-minute penalty). The third flight she’s assigned eventually takes off but arrives 90 minutes late. This counts as a 570-minute (240+240+90) delay. Cases like these are not uncommon since delays and cancellations can pile up.  
  
Our program also assumes passengers will drive to their destination if it estimates driving to be faster than waiting out the cancellation and arriving on a new flight. It calculates driving times from Google Maps, adding a 10 percent penalty for traffic, plus a one-hour penalty for the passenger to arrange for the car. For instance, Google estimates the drive time from JFK Airport to Boston Logan Airport as 203 minutes (3:23) without traffic; accounting for traffic and the time to procure the car brings it up to 283 minutes (4:43). After a cancellation, the program compares this time against how long it expects the journey to take by air, accounting for the delay until the new flight plus the scheduled flying time of the new flight, plus a “fudge factor” of one hour to account for the possibility that the new flight will also be delayed or canceled.  
  
What about diverted flights?  
  
A diverted flight is one that first lands at some airport other than its scheduled destination. Here are three examples drawn from my recent experiences:  
  
A flight from New York to Los Angeles encounters significant headwinds, so the pilot is diverted to Las Vegas to refuel before continuing on to LAX. The refueling stop is planned well in advance and is more or less directly en route. It doesn’t add much time to the journey.  
  
A flight from Miami to New York tries to land at LaGuardia in a thunderstorm, then aborts the landing because of strong winds, eventually landing in Boston instead. After sitting on the ground for an hour or two, it takes off for LaGuardia again, this time landing successfully.  
  
A flight from Charlotte to New York gets most of the way to LaGuardia when the New York airport imposes a ground stop because of wintry conditions. The plane turns back around and lands in Charlotte. Passengers are told the flight has been canceled and they must find a new one.  
  
Most diverted flights eventually land at their scheduled destinations, as in the first two examples. In these cases, calculating the travel time is straightforward. We just compare the actual arrival time at the final destination against the scheduled one, as in the case of a delay. On average, these flights take an extra 3 hours, 15 minutes to reach their destinations, according to the BTS data.  
  
But about 20 percent of diverted flights never reach their scheduled destinations, as in the Charlotte example. This is often even worse than a cancellation since you’ve already spent a lot of time in transit but still need to make a new plan to get to where you’re going. When this happens, our program assumes passengers would either have completed the journey to the original destination by car, or driven back to the origin airport and caught a new flight, whichever was faster.  
  
This yields some massive delay times: on average, almost nine hours. Fortunately, these cases are rare — only 1 in every 2,500 flights winds up in this category — so how our model treats them matters little to the bottom line.  
  
I have another question!  
  
Great — just shoot us a note or leave a comment. We’ll be updating this FAQ and the interactive periodically.