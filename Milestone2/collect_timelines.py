# collect_timelines.py
# Nov 12, 2019
# Author: Eni Mustafaraj

import tweepy, json

consumer_key = "i4aC355Yg88iuO5er7x8iWIz8"
consumer_secret = "5blIodguUoOz1nNI3vCu39xcDxxMr68kufymf1CuggBnKgnVUl"
access_token = "1196078327842430978-aIOT6vOorIpi1gkISxQimu4q9S4BbU"
access_token_secret = "HcHDrOm5kfPgXcoNDNHfLW6gEi087bwlQzvq8TlNNAvle"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_timeline(user):
    """Get all most recent 3200 tweets of a user."""
    # statuses are organized in pages, 20 statuses per page
    allPages = []

    for page in tweepy.Cursor(api.user_timeline, id=user).pages():

        allPages.append(page)

    # store tweets in a single list
    allTweets = []
    for page in allPages:
        tweets = [tweet._json for tweet in page]
        allTweets.extend(tweets)
    return allTweets


def read_accounts(fname):
    """read accounts from file and clean them up"""
    with open(fname, 'r') as inFile:
        lines = inFile.readlines()
        accounts = [el[1:].strip() for el in lines]
        return accounts

def store_json(data, fname):
    """Store data into a JSON file."""
    fname = fname + "-timeline.json"
    with open(fname, 'w') as outFile:
        json.dump(data, outFile)

if __name__ == "__main__":
    import sys, time
    filename = sys.argv[1] # read file name from console
    accounts = read_accounts(filename)
    for account in accounts:
        try:
            timeline = get_timeline(account)
        except tweepy.RateLimitError:
            time.sleep(15 * 60) # sleep for 15 minutes
            timeline = get_timeline(account)

        store_json(timeline, account)
