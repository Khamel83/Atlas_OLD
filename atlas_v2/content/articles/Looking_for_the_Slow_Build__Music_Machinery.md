# Looking for the Slow Build | Music Machinery

**Source**: http://musicmachinery.com/2011/09/18/looking-for-the-slow-build/
**Type**: article
**Created**: 2025-08-13T20:30:53.623855

---

title: Looking for the Slow Build | Music Machinery
source: http://musicmachinery.com/2011/09/18/looking-for-the-slow-build/
date: 2025-08-13T20:30:46.365886
tags: []
---
_This is the second in a series
of[posts](http://web.archive.org/web/20250615204833/https://musicmachinery.com/tag/msd/)
exploring the [Million Song
Dataset](http://web.archive.org/web/20250615204833/http://labrosa.ee.columbia.edu/millionsong/)._

[![reddit post titled 'what is your favorite song that
builds'](http://web.archive.org/web/20250615204833im_/https://musicmachinery.com/wp-
content/uploads/2011/09/what-is-your-favorite-song-that-_builds_-_-
music.png?w=620&h=100)](http://web.archive.org/web/20250615204833/http://www.reddit.com/r/Music/comments/hnc3b/what_is_your_favorite_song_that_builds/)

Every few months you’ll see a query like this on Reddit – someone is looking
for songs that slowly build in intensity. It’s an interesting music query
since it is primarily focused on what the music sounds like. Since we’ve
analyzed the audio of millions and millions of tracks here at [The Echo
Nest](http://web.archive.org/web/20250615204833/http://echonest.com/ "The Echo
Nest") we should be able to automate this type of query. One would expect that
Slow Build songs will have a steady increase in volume over the course of a
song, so lets look at the loudness data for a few Slow Build songs to confirm
this intuition. First, here’s the canonical slow builder: Stairway to Heaven:

![Loudness plot of Stairway to
Heaven](http://web.archive.org/web/20250615204833im_/https://i0.wp.com/static.echonest.com/SlowBuild/plots/TRLNETB128F429215B.png)The
green line is the raw loudness data, the blue line is a smoothed version of
the data. Clearly we see a rise in the volume over the course of the song.
Let’s look at another classic Slow Build – [The Hall Of the Mountain
King](http://web.archive.org/web/20250615204833/http://open.spotify.com/track/2ChK8O6mUhNYyVHXR471hm)
– again our intuition is confirmed:

[![Loudness Plot for The Hall of the Mountain
King](http://web.archive.org/web/20250615204833im_/https://i0.wp.com/static.echonest.com/SlowBuild/plots/TRZUMYC128F428F491.png)](http://web.archive.org/web/20250615204833/http://open.spotify.com/track/2ChK8O6mUhNYyVHXR471hm)

Looking at a non-Slow Build song like Katy Perry’s California Gurls we see
that the loudness curve is quite flat by comparison:

![Loudness Plot for California Gurls by Katy
Perry](http://web.archive.org/web/20250615204833im_/https://i0.wp.com/static.echonest.com/SlowBuild/plots/TRTPBNW12E5AE4FD9C.png)

Of course there are other aspects beyond loudness that a musician may use to
build a song to a climax – tempo, timbre and harmony are all useful, but to
keep things simple I’m going to focus only on loudness.

Looking at these plots it is easy to see which songs have a Slow Build. To
algorithmically identify songs that have a slow build, we can use a technique
similar to the one I described in [The Stairway
Detector](http://web.archive.org/web/20250615204833/https://musicmachinery.com/2009/08/17/the-
stairway-detector/). It is a simple algorithm that compares the average
loudness of the first half of the song to the average loudness of the second
half of the song. Songs with the biggest increase in average loudness rank the
highest. For example, take a look at a loudness plot for Stairway to Heaven.
You can see that there is a distinct rise in scores from the first half to the
second half of the song (the horizontal dashed lines show the average loudness
for the first and second half of the song). Calculating the ramp factor we see
that Stairway to Heaven scores an 11.36 meaning that there is an increase in
average loudness of 11.36 decibels between the first and the second half of
the song.

This algorithm has some flaws – for instance it will give very high scores to
‘hidden track’ songs. Artists will sometimes ‘hide’ a track at the end of a CD
by padding the beginning of the track with a few minutes of silence. For
example, this
[track](http://web.archive.org/web/20250615204833/http://open.spotify.com/track/1sLNjx3d0Q8Ikn6Lg1WRb8)
by ‘Fudge Tunnel’ has about five minutes of silence before the band comes in.

[![Extra by Fudge
Tunnel](http://web.archive.org/web/20250615204833im_/https://i0.wp.com/static.echonest.com/SlowBuild/plots/TROXEPF12903CFA169.png)](http://web.archive.org/web/20250615204833/http://open.spotify.com/track/1sLNjx3d0Q8Ikn6Lg1WRb8)

Clearly this song isn’t a Slow Build, our simple algorithm is fooled. To fix
this we need to introduce a measure of how straight the ramp is. One way to
measure the straightness of a line is to calculate the[ Pearson
correlation](http://web.archive.org/web/20250615204833/http://en.wikipedia.org/wiki/Pearson_product-
moment_correlation_coefficient) for the loudness data as a function of time.
XY Data with correlation that approaches one (or negative one) is by
definition, linear. This nifty wikipedia visualization of the correlation of
different datasets shows the correlation for various datasets:

[![](http://web.archive.org/web/20250615204833im_/https://musicmachinery.com/wp-
content/uploads/2011/09/400px-
correlation_examples2.png?w=620)](http://web.archive.org/web/20250615204833/https://musicmachinery.com/wp-
content/uploads/2011/09/400px-correlation_examples2.png)We can combine the
correlation with our ramp factors to generate an overall score that takes into
account the ramp of the song as well as the straightness of the ramp. The
overall score serves as our Slow Build detector. Songs with a high score are
Slow Build songs. I suspect that there are better algorithms for this so if
you are a math-oriented reader who is cringing at my naivete please set me and
my algorithm straight.

Armed with our Slow Build Detector, I built a little web app that lets you
explore for Slow Build songs. The app –[ Looking For The Slow
Build](http://web.archive.org/web/20250615204833/http://labs.echonest.com/loud/)
– looks like this:

[![Screenshot of Looking for the slow build
app](http://web.archive.org/web/20250615204833im_/https://musicmachinery.com/wp-
content/uploads/2011/09/looking-for-the-slow-
build.png?w=620&h=542)](http://web.archive.org/web/20250615204833/http://labs.echonest.com/loud/)

The application lets you type in the name of your favorite song and will give
you a plot of the loudness over the course of the song, and calculates the
overall Slow Build score along with the ramp and correlation. If you find a
song with an exceptionally high Slow Build score it will be added to the
gallery. I challenge you to get at least one song in the gallery.

You may find that some songs that you think should get a high Slow Build score
don’t score as high as you would expect. For instance, take the song
[Hoppipolla by Sigur
Ros](http://web.archive.org/web/20250615204833/http://open.spotify.com/track/6eTGxxQxiTFE6LfZHC33Wm).
It seems to have a good build, but it scores low:

![Loudness plot for Hoppipolla by Sigur
Ros](http://web.archive.org/web/20250615204833im_/https://i0.wp.com/static.echonest.com/SlowBuild/plots/TRGEQZP12E5ACC33B5.png)

It has an early build but after a minute it has reached it’s zenith. The
ending is symmetrical with the beginning with a minute of fade. This explains
the low score.

Another song that builds but has a low score is [Weezer’s The Angel and the
One](http://web.archive.org/web/20250615204833/http://open.spotify.com/track/2SjZbnlu6xg90w0Tnf4TwQ).

[![Loudness plot for Weezer's the Angel and the
One](http://web.archive.org/web/20250615204833im_/https://i0.wp.com/static.echonest.com/SlowBuild/plots/TRWLEVK12E5AC92D94.png)](http://web.archive.org/web/20250615204833/http://open.spotify.com/track/2SjZbnlu6xg90w0Tnf4TwQ)

This song has a 4 minute power ballad build – but fails to qualify a a slow
build because the last 2 minutes of the song are nearly silent.

**Finding Slow Build songs in the Million Song Dataset**

Now that we have an algorithm that finds Slow Build songs, lets apply it to
the Million Song Dataset. I can create a simple MapReduce job in Python that
will go through all of the million tracks and calculate the Slow Build score
for each of them to help us find the songs with the biggest Slow Build. I’m
using the same framework that I described in the post “[How to Process a
Million Songs in 20
minutes](http://web.archive.org/web/20250615204833/https://musicmachinery.com/2011/09/04/how-
to-process-a-million-songs-in-20-minutes/)“. I use the S3 hosted version of
the Million Song Dataset and process it via Amazon’s Elastic MapReduce using
[mrjob](http://web.archive.org/web/20250615204833/https://github.com/Yelp/mrjob)
– a Python MapReduce library. Here’s the mapper that does almost all of the
work, the full code is on github in
[cramp.py](http://web.archive.org/web/20250615204833/https://github.com/echonest/msd-
examples/blob/master/cramp.py):

    
    
        def mapper(self, _, line):
            """ The mapper loads a track and yields its ramp factor """
            t = track.load_track(line)
            if t and t['duration'] > 60 and len(t['segments']) > 20:
                segments = t['segments']
                half_track = t['duration'] / 2
                first_half = 0
                second_half = 0
                first_count = 0
                second_count = 0
    
                xdata = []
                ydata = []
                for i in xrange(len(segments)):
                    seg = segments[i]
                    seg_loudness = seg['loudness_max'] * seg['duration']
    
                    if seg['start'] + seg['duration'] <= half_track:
                        seg_loudness = seg['loudness_max'] * seg['duration']
                        first_half += seg_loudness
                        first_count += 1
                    elif seg['start'] < half_track and seg['start'] + seg['duration'] > half_track:
                        # this is the nasty segment that spans the song midpoint.
                        # apportion the loudness appropriately
                        first_seg_loudness = seg['loudness_max'] * (half_track - seg['start'])
                        first_half += first_seg_loudness
                        first_count += 1
    
                        second_seg_loudness = seg['loudness_max'] * (seg['duration'] - (half_track - seg['start']))
                        second_half += second_seg_loudness
                        second_count += 1
                    else:
                        seg_loudness = seg['loudness_max'] * seg['duration']
                        second_half += seg_loudness
                        second_count += 1
    
                    xdata.append( seg['start'] )
                    ydata.append( seg['loudness_max'] )
    
                correlation = pearsonr(xdata, ydata)
                ramp_factor = second_half / half_track - first_half / half_track
                if YIELD_ALL or ramp_factor > 10 and correlation > .5:
                    yield (t['artist_name'], t['title'], t['track_id'], correlation), ramp_factor
    
    

This code takes less than a half hour to run on 50 small EC2 instances and
finds a bucketload of Slow Build songs. I’ve created a page of plots of the
top 500 or so Slow Build songs found by this job. There are all sorts of
hidden gems in there. Go check it out:

The page has 500 plots all linked to Spotify so you can listen to any song
that strikes your fancy. Here are some my favorite discoveries:

**Respighi’s The Pines of the Appian Way**

I remember playing this in the orchestra back in high school. It really is
sublime. Click the plot to listen in Spotify.

[![Pines of the Appian
Way](http://web.archive.org/web/20250615204833im_/https://i0.wp.com/static.echonest.com/SlowBuild/plots/TRZAUQH128F424A11B.png)](http://web.archive.org/web/20250615204833/http://open.spotify.com/track/0FTmGMNWL6jIokVhj5L15i)

**Maria Friedman’s Play The Song Again**

So very theatrical

[![Play the song
again](http://web.archive.org/web/20250615204833im_/https://i0.wp.com/static.echonest.com/SlowBuild/plots/TRXZDNM12903CC233C.png)](http://web.archive.org/web/20250615204833/http://open.spotify.com/track/7qTBwexxUa5Bvg6Cyy0jnQ)

**Mandy Patinkin’s Rock-A-Bye Your Baby With A Dixie Melody**

****Another song that seems to be right off of Broadway – it has an awesome
slow build.

There are thousands and thousands of slow build songs. I’ve created a table
with all the songs that have a score of above 10 on the Slow Build scale
(recall that Stairway to Heaven scores a 9, so this is a table of about 6K
songs that are bigger Slow Build songs than Stairway).

**Conclusion**

This just about wraps up the most complex blog post I’ve ever made with a web
app, a map-reduce program, and a jillion behind the scenes scripts to make
tables and nice looking plots – but in the end, I found new music that I like
so it was worth it all. Here’s a summary of all the resources associated with
this post:

Thanks to Spotify for making it so easy to find music with their meta-data API
and make links that play music. Apologies to all of the artists with accented
characters in their names, I was encoding-challenged this weekend, so my UTF
is all WTF.
