#!/usr/bin/env python
#encoding: utf-8
 
import tweepy #https://github.com/tweepy/tweepy
import csv
import time

#Twitter API credentials
consumer_key = "cp2HpHsZOtWK6cXKxzmFgI2bC"
consumer_secret = "WXvj6eKXP26gsHtdcAjH71JNNfvUHo2ilUiU6SzgWKLtfikJGz"
access_key = "3245138284-bNfY3h3WTZyUwpnLi4gPzYBkmImqr1a2e03DhI8"
access_secret = "NaeVMi8W0qByjg0qav2Z9MltTKUTRokhZNOOozrx39ULT"
 
 
def get_all_tweets(screen_name):

	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
        
		break
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	return outtweets

def get_num_of_refs(tweets, last_date, a_word):
    counter = 0
    #a_word = unicode(a_word)
    #convertedLastDate = time.strptime(last_date[:-4],"%a, %d %b %Y %H:%M:%S")
    for t in tweets:
        #convertedDate = time.strptime(t[1][:-4],"%a, %d %b %Y %H:%M:%S")
        print a_word, t[2]
        if a_word.lower() in t[2].decode('utf-8').lower() and t[1]>last_date:
            counter = counter + 1
    #return "hello"
    return {'lastDate': tweets[0][1], 'occurrences': counter, 'keyword': a_word}


if __name__ == '__main__':
    d = {key: get_all_tweets(key) for key in ["BBCNews","HarisSeoudy"]}
    print d
   