# redditweet

Tweet hot submissions from a given subreddit using the Twitter and reddit APIs

# Usage

Configure your twitter API authentication details in config.ini in the twitter
section, and the name of the subreddit in the reddit section. See
config.ini-example for all of the available configuration options.

    $ redditweet.py

redditweet.py accepts no arguments or environment variables. It produces a text
file called seen.txt, which contains a list of reddit IDs for the submissions
that have already been posted.
