import json
import random

from flask import render_template

from orm import get_db
from utils import absolute_path, force_ascii, memoized

@memoized
def get_frontpage_products():
    db = get_db()
    products = list(db.products.find())
    random.shuffle(products)
    return products

def render_index_page():
    products = get_frontpage_products()
    print 'len(products)', len(products)
    return render_template('index.html', products=products)
