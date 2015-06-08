#WRITING
import ZODB, ZODB.FileStorage, transaction

db = ZODB.DB("db.fs") #Create or attach to file (if already exists)
connection = db.open()
root = connection.root

root.Parties = {} #attach string to field called Test in Root
root.Counter = 0

transaction.commit() #commit to db (like Git)