import re
import urllib.parse as ul
from sys import stdin, stdout, argv, exit

def bhedak():
    encoded = ul.quote(str(argv[1]), safe='')
    try:
        for url in stdin.readlines():
            domain = str(url.strip())
            stdout.write(re.sub(r"=[^?\|&]*", '=' + str(encoded), str(domain)) + '\n')
    except KeyboardInterrupt:
        exit(0)
    except:
        exit(127)
