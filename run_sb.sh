#!/usr/bin/env bash
cd /home/sb/sb/linux/
./starbound_server | tee /dev/tty | /usr/local/bin/tstamp | /usr/local/bin/unIPv6 > ../storage/sb_f2b.log
