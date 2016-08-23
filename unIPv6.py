#!/usr/bin/env python3
import sys
import re

ipv6Pat = re.compile(r'(?:[a-z0-9]{4}:){6}([a-z0-9]{4}):([a-z0-9]{4})')

while True:
    s = sys.stdin.readline()
    if s == '':
        break
    try:
        match = ipv6Pat.search(s)
        
        if match:
            a = int(match.group(1)[0:2], 16)
            b = int(match.group(1)[2:4], 16)
            c = int(match.group(2)[0:2], 16)
            d = int(match.group(2)[2:4], 16)
        
            newIP = "{}.{}.{}.{}".format(a, b, c, d)
        
            s = s.replace(match.group(0), newIP)
            sys.stdout.write(s)
            sys.stdout.flush()
        else:
            sys.stdout.write(s)
            sys.stdout.flush()
    except:
        pass



