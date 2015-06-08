#READING
import ZODB, ZODB.FileStorage

db = ZODB.DB("db.fs")
connection = db.open()
root = connection.root

print root.Test
print root.Parties
print root.Counter
