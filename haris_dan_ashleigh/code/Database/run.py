import threading
from flask import Flask, render_template, jsonify
import json
import os, random
import logic
import datetime
import time

#thread stuff
POOL_TIME = 10 #Seconds

#DB Stuff
start_date = datetime.datetime(1980, 11, 5, 11, 26, 15, 37496)
app = Flask(__name__)
tweets = {'data': []}
past_query_dates = {}
last_user_fetched = ""

@app.route('/')
def index():
    return render_template('index.html')

def fetch():
    for u in users:
            global tweets
            tweets['data'] = logic.get_all_tweets(u)
            #resp = jsonify({"data": logic.get_all_tweets(user)})
            resp = json.dumps({"data": 'hello'})
            global past_query_dates
            if u not in past_query_dates.keys(): past_query_dates[u] = start_date
            global last_user_fetched
            last_user_fetched = u
            print "updating DB entry for: {}".format(u)
    yourThread = threading.Timer(POOL_TIME, fetch, ())
    yourThread.start()

yourThread = threading.Thread(name='fetcher', target=fetch)
yourThread.start()

@app.route('/counter/<keyword>')
def getcounts(keyword):    
    global past_query_dates
    if past_query_dates.get(last_user_fetched, None): #if you have searched BBC
        date = past_query_dates[last_user_fetched].get(keyword, start_date) #get date for spec keywrd else set to start_date
    else: #if you have not searched BBC before
        past_query_dates[last_user_fetched] = {} #create an empty dictionary to store keywords: dates
        date = start_date # and set the date to start date
    
    results = logic.get_num_of_refs(tweets['data'], date, keyword)
    past_query_dates[last_user_fetched][keyword] = results["lastDate"]
    return jsonify(results)

app.run(host='0.0.0.0', port=8080, debug=True)
