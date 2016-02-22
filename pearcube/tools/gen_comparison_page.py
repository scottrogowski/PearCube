#!/usr/bin/env python

from __future__ import unicode_literals
import io
from pybars import Compiler
import os
from time import sleep

handlebars_compiler = Compiler()

def watch_file(fname, context, debug):
    last_mod_time = 0
    while True:
        mod_time = os.stat(fname).st_mtime
        if mod_time == last_mod_time:
            sleep(.1)
            continue
        last_mod_time = mod_time

        gen_template(fname, context, debug)


def gen_template(fname, context, debug):
    with io.open(fname, encoding='utf8') as f:
        comparison_template = f.read()
        template = handlebars_compiler.compile(comparison_template)
        print template(context)
        #TODO if debug use absolute paths

if __name__ == "__main__":
    context = {
        "hello": "hello world"
    }

    if '--debug' in sys.argv:
        watch_file('email.html', context, True)
    else:
        gen_template('email.html', context, False)
