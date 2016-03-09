#!/usr/bin/env python

import re

from flask import Flask, request, render_template, redirect
from werkzeug.routing import BaseConverter
import premailer

from lib.utils import absolute_path, unique_id
from lib.options import options
from lib.email_handler import send_request_email, send_results_email
from lib.product_handler import render_product_page, sync_mongo_with_flatfile

app = Flask(__name__)
hash_version = unique_id()[:5]

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

# Use the RegexConverter function as a converter
# method for mapped urls
app.url_map.converters['regex'] = RegexConverter

@app.context_processor
def inject_globals():
    return {'debug': options.DEBUG,
            'port': options.PORT}

@app.template_filter('absolutify')
def absolutify_filter(path):
	if options.LIVE_EMAILING:
	    return "http://www.pearcube.com" + path
	else:
		return path

LINKIFY_RE = re.compile(r"\[(.*?)\]\((.*?)\)")
def link_repl(matchobj):
    return "<a class='link' href='%s'>%s</a>" % (matchobj.group(2), matchobj.group(1))

@app.template_filter('linkify')
def linkify_filter(string):
    return LINKIFY_RE.sub(link_repl, string)

@app.template_filter('format_price')
def format_price_filter(price_float):
    return "$%.2f" % price_float

@app.template_filter('dashes_to_spaces')
def remove_dash_filter(url):
    return url.replace('-', ' ')

@app.template_filter('versioned')
def versioned_static(url):
    return "/static/" + url + "?v=" + hash_version

# @app.route('/static/<regex("[a-f0-9]{5}"):hash_version>/<path:static_path>')
# def debug_redirect_static(hash_version, static_path):
#     print 'here'
#     return redirect('/static/' + static_path)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/<regex(A-Z"[A-Za-z0-9\-]+"):dest>')
def product_page(dest):
	return render_product_page(dest)

@app.route('/cs_request', methods=['POST'])
def cs_request():
    return send_request_email(request.form)

@app.route('/debug_email', methods=['GET'])
def debug_email():
	if options.DEBUG:
		html = render_template('email.html')
		# html = premailer.transform(html)
		return html

@app.route('/send_email', methods=['GET'])
def send_debug_email():
	if options.DEBUG:
		return send_results_email()

if __name__ == '__main__':
    options.parse_command_line()
    sync_mongo_with_flatfile()
    app.run(debug = options.DEBUG,
            host = options.HOST,
            port = options.PORT,
            extra_files = [absolute_path('data/db.json')])
