import pymongo

from options import options
from secrets import MLAB_USERNAME, MLAB_PASSWORD

# Connection to Mongo DB
try:
    if options.DEBUG:
        client = pymongo.MongoClient()
        print "Connected successfully to mongo debug"
    else:
        uri = "mongodb://%s:%s@ds019658.mlab.com:19658/heroku_2wzxbwzm" % (MLAB_USERNAME, MLAB_PASSWORD)
        client = pymongo.MongoClient(uri)
        print "Connected successfully to mongo prod"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to mongo: %s" % e 
   exit(1)

db = client.db
