import tweepy
import re

consumer_key = "cp2HpHsZOtWK6cXKxzmFgI2bC"
consumer_secret = "WXvj6eKXP26gsHtdcAjH71JNNfvUHo2ilUiU6SzgWKLtfikJGz"
access_token = "3245138284-bNfY3h3WTZyUwpnLi4gPzYBkmImqr1a2e03DhI8"
access_token_secret = "NaeVMi8W0qByjg0qav2Z9MltTKUTRokhZNOOozrx39ULT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
keywords = ["General Election","GE2015","Election"]


#Search for keywords in tweets (up to week in past)
results = api.search(q=keywords)

for result in results:
    print result.text

    
##Search all followed users and return tweets
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text

