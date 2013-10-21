# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import

import os
import sys

import tweepy

import lx300


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


def get_tweets(api, username):
    user = api.get_user(username)
    return user.timeline()


if __name__ == '__main__':
    # Get twitter username
    username = sys.argv[1]

    # Twitter stuff
    api = do_auth()
    tweets = get_tweets(api, username)
    
    # Initialize printer
    printer = lx300.LX300()

    # Print!!1!
    printer.write("                        _                       \n")
    printer.write("  ___ ___  _ __ ___  __| |_   _ _ __ ___  _ __  \n")
    printer.write(" / __/ _ \| '__/ _ \/ _` | | | | '_ ` _ \| '_ \ \n")
    printer.write("| (_| (_) | | |  __/ (_| | |_| | | | | | | |_) |\n")
    printer.write(" \___\___/|_|  \___|\__,_|\__,_|_| |_| |_| .__/ \n")
    printer.write("                                         |_|    \n")
    printer.write('\n')
    printer.write('Tweets:\n\n')
    for tweet in tweets:
        printer.write(tweet.text.encode('ascii', 'replace'))
        printer.write('\n---------------\n\n')
