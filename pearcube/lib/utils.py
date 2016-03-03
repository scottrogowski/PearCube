import hashlib
import time
import os

def unique_id():
    # 1 / ~1 trillion chance of collision
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return hash.hexdigest()

def absolute_path(path_from_base):
    this_dir = os.path.dirname(__file__)
    base_dir = this_dir.rsplit('/', 1)[0]
    return base_dir + '/' + path_from_base

def force_ascii(uni):
    try:
        uni = unicode(uni)
    except:
        print "error forcing unicode"
        return uni
    try:
        return uni.encode('ascii', 'ignore')
    except:
        print "error forcing ascii"
        return uni

