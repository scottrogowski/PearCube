import hashlib
import time

def unique_id():
    # 1 / ~1 trillion chance of collision
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return hash.hexdigest()
