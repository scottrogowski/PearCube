# -*- coding: utf-8 -*-
import json

from flask import render_template, abort

from orm import get_db
from utils import memoized

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
