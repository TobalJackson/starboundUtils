# starboundUtils
some scripts and configurations for administering a dedicated starbound server with Fail2ban

## Why:
I wanted to run a server on linux but avoid the eventual hammering from the interwebs on my Starbound port. Therefore I sought to employ Fail2Ban to achieve this, however some things were lacking from the starbound logging facility, namely (date)-time-stamping, as well as IPv4 addresses as opposed to IPv6-encoded IPv4 Addresses.

###run_sb.sh
This file should be placed wherever you'd like to invoke it from, and the path to the `starbound_server` executable should be specified on line 2 where the `cd` directive is.

###tstamp.py
This python script simply reads from STDIN, prepends the date + time to each line read in, and outputs each prefixed line to STDOUT.  You can put this script in the right place with a symlink:
```sudo ln -s $(pwd)/tstamp.py /usr/local/bin/tstamp```
or just copy/move it to /usr/local/bin:
```sudo mv ./tstamp.py /usr/local/bin/tstamp```

###unIPv6.py
This python script simply reads from STDIN, and translates the last 8 "bytes" of the IPv6 address into an IPv4 address.  Perform the same steps above to move it into the right location for `run_sb.sh`.  An alternative to copying/symlinking/moving these two utilities anywhere would be to rewrite the 3rd line of the `run_sb.sh` script to point to a different/relative location.

###jail.local
This is an example fail2ban jail configuration which has the starbound stanza/definition.  Be sure to change the port to match the port of your starbound install [default == 21025].

###sb-signin.conf
Filter file for fail2ban's log matcher.  Copy this file to /etc/fail2ban/filter.d/ so that the jail file can access the filter rule.
