import pymongo

# Connection to Mongo DB
try:
    client = pymongo.MongoClient()
    print "Connected successfully to mongo"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 
   exit(1)

db = client.db
