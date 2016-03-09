import hashlib
import time
import os
import collections
import functools

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

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)
