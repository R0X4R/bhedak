#!/usr/bin/env python3
'''
Author: R0X4R (Eshan Singh)
Version: 2.0.0
'''
import re
import urllib.parse as ul
from sys import stdin, stdout, argv, exit

encoded = ul.quote(str(argv[1]), safe='')
try:
    for url in stdin.readlines():
        domain = str(url.strip())
        stdout.write(re.sub(r"=[^?\|&]*", '=' + str(encoded), str(domain)) + '\n')
except KeyboardInterrupt:
    exit(0)
except IndexError:
     exit(127)
except:
    exit(127)
