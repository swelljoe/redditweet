#!/usr/bin/env python
# simple script to copy a reddit submission to a tweeter
# config.ini should contain your twitter API details and subreddit name

import praw
import json
import requests
import tweepy
import time
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def setup_connection_reddit(subreddit):
	print ("[bot] setting up connection with Reddit")
	r = praw.Reddit('Music Maker Deals twitter script monitoring $subreddit by /u/SwellJoe')
	subreddit = r.get_subreddit(subreddit)
	return subreddit

def strip_title(title):
    if len(title) < 110:
        return title
    else:
        return title[:110] + "..."

def add_id_to_file(id):
    with open('seen.txt', 'a') as file:
        print(str(id), file = file)

def duplicate_check(id):
    found = 0
    with open('seen.txt', 'r') as file:
        for line in file:
            if id in line:
                found = 1
    return found

def tweeter(subreddit):
    auth = tweepy.OAuthHandler(config['twitter']['consumer_key'], \
								config['twitter']['consumer_secret'])
    auth.set_access_token(config['twitter']['access_token'], \
							config['twitter']['access_token_secret'])
    api = tweepy.API(auth)
    for submission in subreddit.get_hot(limit=10):
        found = duplicate_check(submission.id)
        if found == 0:
            print ("[bot] Posting this link on twitter")
            print((submission.id +" "+strip_title(submission.title)+" "+submission.permalink))
            api.update_status(strip_title(submission.title)+" "+submission.permalink)
            add_id_to_file(submission.id)
            time.sleep(10)
        else:
            print ("[bot] Already posted")

def main():
	subreddit = setup_connection_reddit(config['reddit']['subreddit'])
	tweeter(subreddit)

if __name__ == '__main__':
    main()
