# -*- coding: utf-8 -*-
import json

import pymongo
from flask import render_template, abort

from orm import get_db
from utils import absolute_path, force_ascii, memoized

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

@memoized
def get_product_by_id(int_id):
    db = get_db()
    return db.products.find_one({'int_id': int_id})

@memoized
def get_product_by_dest(dest):
    db = get_db()
    res = db.products.find_one({'page_url': dest})
    if 'see_also' in res:
        res['see_also'] = {text: '/' + get_product_by_id(int_id)['page_url'] for text, int_id in res['see_also'].iteritems()}
    return res

def render_product_page(dest):
    res = get_product_by_dest(dest)
    if res:
        return render_template('product_landing.html', **res)
    else:
        abort(404) # TODO http://flask.pocoo.org/docs/0.10/patterns/errorpages/
