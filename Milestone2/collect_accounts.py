# collect_accounts.py
# Nov 12, 2019
# Author: Eni Mustafaraj

import tweepy, json

consumer_key = "i4aC355Yg88iuO5er7x8iWIz8"
consumer_secret = "5blIodguUoOz1nNI3vCu39xcDxxMr68kufymf1CuggBnKgnVUl"
access_token = "1196078327842430978-aIOT6vOorIpi1gkISxQimu4q9S4BbU"
access_token_secret = "HcHDrOm5kfPgXcoNDNHfLW6gEi087bwlQzvq8TlNNAvle"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_profiles(accntList):
    """Retrieve proviles for all accounts in list of accounts."""
    profiles = api.lookup_users(screen_names=accntList)
    profilesJSON = [user._json for user in profiles]
    return profilesJSON

def read_accounts(fname):
    """read accounts from file and clean them up"""
    with open(fname, 'r') as inFile:
        lines = inFile.readlines()
        accounts = [el[1:].strip() for el in lines]
        return accounts

def store_json(data, fname):
    """Store data into a JSON file."""
    fname = fname.split('.')[0] + "-profiles.json"
    with open(fname, 'w') as outFile:
        json.dump(data, outFile)

if __name__ == "__main__":
    import sys
    filename = sys.argv[1] # read file name from console
    accounts = read_accounts(filename)
    jsonProfiles = get_profiles(accounts)
    store_json(jsonProfiles, filename)
