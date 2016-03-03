import os

import pymongo

from options import options
# from secrets import MLAB_USERNAME, MLAB_PASSWORD

db = None

def connect_to_mongo():
    global db
    try:
        if options.DEBUG:
            client = pymongo.MongoClient()
            db = client.dev_db
            print "Connected successfully to mongo debug"
        else:
            uri = os.environ['MONGOLAB_URI']
            client = pymongo.MongoClient(uri)
            db = client.get_default_database()
            print "Connected successfully to mongo prod"
    except pymongo.errors.ConnectionFailure, e:
       print "Could not connect to mongo: %s" % e 
       exit(1)

def get_db():
    if not db:
        connect_to_mongo()
    return db
