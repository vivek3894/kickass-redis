__author__ = 'dvirsky'


import redis
from kickass_redis.patterns.lua import LuaCall, LuaScriptError

#A lua script that multiplies two numbers and stores the result in a key

lua_str = '''
            local val = ARGV[1]*ARGV[2]
            redis.call('set', KEYS[1], val)
            return redis.call('get', KEYS[1])
            '''
conn = redis.Redis()
#Define the call
mult = LuaCall(lua_str, conn)

#Call it once:
print "Result: %s" % mult(keys = ('foor',), args = (3,10))

print "Result: %s" % mult(keys = ('foor2',), args = (5,20))
