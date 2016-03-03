# -*- coding: utf-8 -*-
import json

import pymongo 
from flask import render_template, abort

from orm import get_db

def load_flatfile():
    with open('data/db.json') as flatfile:
        return json.load(flatfile)

def sync_mongo_with_flatfile():
    # not very scalable but it will get the job done
    db = get_db()
    # db.products.remove( {} )
    flat_json = load_flatfile()
    for product_json in flat_json:
        try:
            db.products.update_one(
                {'page_url': product_json['page_url']},
                {'$set': product_json},
                upsert = True
                )
        except pymongo.errors.OperationFailure, e:
            print unicode(e)

def render_product_page(dest):
    print dest
    db = get_db()
    res = db.products.find_one({'page_url': dest})
    if res:
        return render_template('product_landing.html', **res)
    else:
        abort(404) # TODO http://flask.pocoo.org/docs/0.10/patterns/errorpages/
