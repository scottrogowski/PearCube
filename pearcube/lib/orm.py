import os
import json

import pymongo

from options import options
from utils import absolute_path, force_ascii

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

def load_flatfile():
    absolute = absolute_path('data/db.json')
    with open(absolute) as flatfile:
        return json.load(flatfile)

def sync_mongo_with_flatfile():
    # not very scalable but it will get the job done
    # TODO. Let's not introduce mongo until we need it.
    # Let's get rid of this.
    db = get_db()
    db.products.drop()
    print "dropped %s" % db.name
    flat_json = load_flatfile()
    for product_json in flat_json:
        try:
            db.products.update(
                {'page_url': product_json['page_url']},
                {'$set': product_json},
                upsert = True
                )
        except pymongo.errors.OperationFailure, e:
            print "mongo update failure"
            print e.code
            print force_ascii(e.details)
