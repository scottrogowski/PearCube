# -*- coding: utf-8 -*-
import json

from flask import render_template, abort

from orm import db

def load_flatfile():
    with open('data/db.json') as flatfile:
        return json.load(flatfile)

def sync_mongo_with_flatfile():
    # not very scalable but it will get the job done
    db.products.drop()
    flat_json = load_flatfile()
    for product_json in flat_json:
        db.products.insert_one(
            product_json
            )

sync_mongo_with_flatfile()

def render_product_page(dest):
    print dest
    res = db.products.find_one({'page_url': dest})
    if res:
        return render_template('product_landing.html', **res)
    else:
        abort(404) # TODO http://flask.pocoo.org/docs/0.10/patterns/errorpages/