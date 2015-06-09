import mongoengine as db

dbname = "twitproject"
user = "main"
passwd = raw_input("pass: ")

c = db.connect(host=("mongodb://{user}:{passwd}@ds063779.mongolab.com:63779/{dbname}"
                     .format(user=user, passwd=passwd, dbname=dbname)))

class Tweet(db.EmbeddedDocument):
    twitid = db.StringField(required=True)
    date = db.DateTimeField(required=True)
    content = db.StringField(required=True)
    
class NewsSource(db.Document):
    name = db.StringField(required=True)
    tweets = db.ListField(db.EmbeddedDocumentField(Tweet))

#t = Tweet(timestamp="00000", date="Monday", content="This is a tweet")
#n.tweets = [t]

#n.save()
#n2.save()

for n in NewsSource.objects.all():
    for t in n.tweets:
        print t.content
        
def init():
    NewsSource.objects.all().delete()
    n = NewsSource(name="BBCNews")
    n2 = NewsSource(name="Guardian")
    n3 = NewsSource(name="thetimes")
    n4 = NewsSource(name="DailyMirror")
    n5 = NewsSource(name="MailOnline")
    n.save()
    n2.save()
    n3.save()
    n4.save()
    n5.save()
    
def update(screen_name,outtweets):
    db_tweets = []
    
    for t in outtweets:
        db_tweets.append(Tweet(twitid=t[0], date=t[1], content=t[2]))
        
    n = NewsSource.objects(name=screen_name)[0]
    n.tweets = db_tweets
    n.save()
    
    #t = Tweet(timestamp="00000", date="Monday", content="This is a tweet")
#n.tweets = [t]

#n.save()
#n2.save()
    
init()