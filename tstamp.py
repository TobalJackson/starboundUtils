#!/usr/bin/env python3
from datetime import datetime as dt
import sys

while True:
    line = sys.stdin.readline()
    if line == '':
        break
    try:
        sys.stdout.write("{} ".format(dt.strftime(dt.now(), "%Y-%m-%d %H:%M:%S")))
        sys.stdout.write(line)
        sys.stdout.flush()
    except:
        pass
