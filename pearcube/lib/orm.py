import os

import pymongo

from options import options
# from secrets import MLAB_USERNAME, MLAB_PASSWORD

db = None

def connect_to_mongo():
    try:
        if options.DEBUG:
            client = pymongo.MongoClient()
            print "Connected successfully to mongo debug"
        else:
            # uri = "mongodb://%s:%s@ds019658.mlab.com:19658/heroku_2wzxbwzm" % (MLAB_USERNAME, MLAB_PASSWORD)
            uri = "mongodb://who:slapchop123@ds019698.mlab.com:19698/heroku_gcxjklhr"
            # uri = os.environ['MONGOLAB_URI']
            client = pymongo.MongoClient(uri)
            print "Connected successfully to mongo prod"
    except pymongo.errors.ConnectionFailure, e:
       print "Could not connect to mongo: %s" % e 
       exit(1)
    global db
    db = client.db

def get_db():
    if not db:
        connect_to_mongo()
    return db
