"""a simple Apache access log parser in Python
usage help = http://i.imgur.com/XBiX2kX.png
when required arguments are missing = http://i.imgur.com/P5L0GZV.png
when incorrect file path is passed = http://i.imgur.com/sJDc0om.png
successful sample output = http://i.imgur.com/iH89mwI.png
Found on github https://gist.github.com/sumeetpareek/9644255
log input /var/log/apache2/access.log 
"""

import re
import sys
import argparse
from collections import Counter

# Using argparse for reading arguments is pretty cool.
# We get defualt help, argument types, and a lot more done :-)
# Refer = http://docs.python.org/dev/library/argparse.html
parser = argparse.ArgumentParser(description='A very simple Apache access log parser')

# A readable log file is a required argument and the file is automagically read too.
parser.add_argument('log_file', metavar='LOG_FILE', type=argparse.FileType('r'),
                   help='Path to the Apache log file')


# Regex for the common Apache log format.
parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.*)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referrer>.*)"',              # referrer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

# Initiazlie required variables
args = parser.parse_args()
log_data = []

# Get components from each line of the log file into a structured dict
for line in args.log_file:
  log_data.append(pattern.match(line).groupdict())

# Using a counter to get stats on the status in log entries
# Refer = http://docs.python.org/2/library/collections.html#collections.Counter
status_counter = Counter(x['status'] for x in log_data)

# Printing the STATUS count sorted by highest to lowest count
print "Most common STATUSes in the Apache log file %s are:" % args.log_file.name
for x in status_counter.most_common():
  print "\t%s Status %d times" % x

