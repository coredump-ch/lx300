# -*- coding: utf-8 -*-
"""
LX300 Twitterstream printer.

Usage:
    twitter.py [--noloop]

Options:
    -h --help  Show this screen.
    --version  Show version.
    --noloop   Don't loop, only print tweets once.

"""
from __future__ import print_function, division, absolute_import

import os
import sys
import time

import tweepy
from docopt import docopt

import lx300


INITIAL_TWEETS = 3
LOOP_SLEEP = 120  # Note: Only 15 Twitter API requests per 15 minute window are allowed!


def do_auth():
    """Do authentication, return API object."""
    consumer_token = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']

    access_key = os.environ.get('ACCESS_KEY')
    access_secret = os.environ.get('ACCESS_SECRET')

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

    if access_key or access_secret:
        auth.set_access_token(access_key, access_secret)
    else:
        try:
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            print('Error! Failed to get request token.')
            sys.exit(1)

        print(redirect_url)
        verifier = raw_input('Verifier: ')

        try:
            auth.get_access_token(verifier)
        except tweepy.TweepError:
            print('Error! Failed to get access token.')
            sys.exit(1)

        print('ACCESS_KEY: {}'.format(auth.access_token.key))
        print('ACCESS_SECRET: {}'.format(auth.access_token.secret))

    api = tweepy.API(auth)
    return api


def get_tweets(api, count=5, since_id=None):
    """Fetch tweets.

    Args:
        api:
            The tweepy API instance.
        count:
            Number of tweets to return.
        since_id:
            Only fetch tweets since the specified tweet ID.

    Returns:
        List of tweets, sorted by date (oldest first).

    """
    # Handle "since_id" argument
    kwargs = {}
    if since_id:
        kwargs['since_id'] = since_id

    # Fetch tweets
    tweets = []
    tweets += api.user_timeline(count=count, **kwargs)
    tweets += api.mentions_timeline(count=count, **kwargs)

    # Sort tweets by date
    tweets = sorted(tweets, key=lambda x: x.created_at)

    return tweets[-count:]


def print_tweets(printer, tweets, header=False):
    if header:
        printer.write("                        _                       \n")
        printer.write("  ___ ___  _ __ ___  __| |_   _ _ __ ___  _ __  \n")
        printer.write(" / __/ _ \| '__/ _ \/ _` | | | | '_ ` _ \| '_ \ \n")
        printer.write("| (_| (_) | | |  __/ (_| | |_| | | | | | | |_) |\n")
        printer.write(" \___\___/|_|  \___|\__,_|\__,_|_| |_| |_| .__/ \n")
        printer.write("                                         |_|    \n")
        printer.write('\n')
        printer.write('Tweets & Mentions:\n\n')
        printer.write('---------------\n')
    for tweet in tweets:
        printer.write(tweet.text)
        meta = {
            'user_name': tweet.author.name,
            'screen_name': tweet.author.screen_name,
            'post_date': tweet.created_at.strftime('%d.%m.%Y %H:%M:%S'),
        }
        printer.write('\nTweeted by {user_name} (@{screen_name}) on {post_date}\n'.format(**meta))
        printer.write('---------------\n')


if __name__ == '__main__':
    # Parse arguments
    arguments = docopt(__doc__, version='v0.1.0')

    # Initialize API and printer
    api = do_auth()
    printer = lx300.LX300()

    # Loop & look for new tweets
    latest_id = None
    while True:
        print('Fetching tweets...')
        tweets = get_tweets(api, count=INITIAL_TWEETS, since_id=latest_id)
        print('Found {0} new tweets.'.format(len(tweets)))
        print_tweets(printer, tweets, header=(latest_id is None))
        if arguments['--noloop']:
            break
        if tweets:
            latest_id = tweets[-1].id
        time.sleep(LOOP_SLEEP)
