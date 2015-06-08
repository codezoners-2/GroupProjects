import ZODB, ZODB.FileStorage, transaction, persistent

class Counter(persistent.Persistent):
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
def update(root):
    #IF TWEET CONTAINS *PARTY*
        #INCREMENT PARTY
    root.Parties["Conservatives"].increment()
    transaction.commit()
    print root.Parties["Conservatives"].count

db = ZODB.DB("twitterElection.fs") #create db with specified name
connection = db.open() #open db
root = connection.root() #connect to root

update(root)