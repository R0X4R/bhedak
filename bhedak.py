#!/usr/bin/env python3
'''
Author: R0X4R (Eshan Singh)
Version: 2.0.0
'''
import re
import urllib.parse as ul
from sys import stdin, stdout, argv, exit

#@> TAKE INPUT FROM USER AS "sys.argv[1]"", ELSE IT WILL USE "FUZZ" AS THE VALUE
try:
    encoded = ul.quote(str(argv[1]), safe='')
except IndexError:
    encoded = ul.quote("FUZZ", safe='')

#@> READ URLs AS STDIN AND USE REGEX TO FILTER AND REPLACE
try:
    for url in stdin.readlines():
        domain = str(url.strip())
        stdout.write(re.sub(r"=[^?\|&]*", '=' + str(encoded), str(domain)) + '\n')
except KeyboardInterrupt:
    exit(0)
except:
    exit(127)