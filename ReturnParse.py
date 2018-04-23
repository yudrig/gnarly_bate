#python ParseForPix.py /var/log/apache2/access.log
#[EMAIL]_[USER]
#http://compsci.adelphi.edu/~thomasrhatigan/pix_101_100.png
#http://compsci.adelphi.edu/~jasonmassimino/?ID=100_500&png

import re
import sys
import argparse
from collections import Counter

def findNumsURL(line):
	match = re.search('GET ([^ ]+) HTTP/1',line)
	if match is None:
		return "";
	else:
		x=match.group(1)
		print x;
		nummatch = re.search('ID=([_0-9]+)', x)
		if nummatch is None:
			return "";
		else:
			return nummatch.group(1)

def findNumsPIX(line):
	match = re.search('GET ([^ ]+) HTTP/1',line)
	if match is None:
		return "";
	else:
		x=match.group(1)
		print x;
		nummatch = re.search('pix_([_0-9]+)', x)
		if nummatch is None:
			return "";
		else:
			return nummatch.group(1)
			
#Returns Array of [a,b] a is Email ID, b is User ID
#Uses getPixelTrack	
def getPixelTrack():
	parser = argparse.ArgumentParser(description='A very simple Apache access log parser')
	# A readable log file is a required argument and the file is automagically read too.
	parser.add_argument('log_file', metavar='LOG_FILE', type=argparse.FileType('r'), help='Path to the Apache log file');
	args = parser.parse_args();

	pix=[];
	
	for line in args.log_file:
		if "~thomasrhatigan" in line and "pix_" in line:
			#
			#print "A";
			nums = findNumsPIX(line);
			#print line;
			if nums is not "":
				#[EMAIL]_[USER];
				a,b = nums.split("_");
				c = [a,b];
				pix.append(c);

	return pix;
	
#Returns Array of [a,b] a is Email ID, b is User ID
#Uses getURLTrack
def getURLTrack():
	parser = argparse.ArgumentParser(description='A very simple Apache access log parser')
	# A readable log file is a required argument and the file is automagically read too.
	parser.add_argument('log_file', metavar='LOG_FILE', type=argparse.FileType('r'), help='Path to the Apache log file');
	args = parser.parse_args();

	url=[];
	
	if "~jasonmassimino" in line and "?ID" in line:
		#
		#print line;
		nums = findNumsURL(line);
		if nums is not "":
			a,b = nums.split("_");
			c = [a,b];
			url.append(c);
	
	return url;
