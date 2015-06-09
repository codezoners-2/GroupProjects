import ZODB, ZODB.FileStorage, transaction, persistent #import everything

class Counter(persistent.Persistent): #create persistent class
    def __init__(self):
        self.count = 0 #set initial value
    
    def increment(self):
        self.count += 1 #incrementing function

db = ZODB.DB("twitterElection.fs") #create db with specified name
connection = db.open() #open db
root = connection.root() #connect to root
root.Parties = {} #create parties dict then add entries
root.Parties["Conservatives"] = Counter()
root.Parties["Labour"] = Counter()
root.Parties["Lib Dems"] = Counter()
root.Parties["Green"] = Counter()
root.Parties["UKIP"] = Counter()
root.Parties["SNP"] = Counter()
transaction.commit() #commit to db (like Git)

#must be run when server isnt running
#run once