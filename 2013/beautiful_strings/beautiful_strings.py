#! /usr/bin/env python
# Problem Question: Refer problems.txt file
import collections
import operator
import re
import sys

def beauty_val(beauty_string):
	#filter alphabets and convert to lowercase
	beauty_string = filter(str.isalpha, beauty_string).lower() 

	# Get count for each unique character
	counter = collections.Counter(beauty_string)
	counter_list = sorted(counter.values(), reverse=True)
	#multiples = range(0, len(counter_list)-1)
	return sum([x * (26 - n) for x,n in zip(counter_list, range(0,len(counter_list)))])

case_count = 1
with open('input.txt', 'r') as f:
	next(f)
	for line in f:
		line = line.rstrip('\n')
		print "Case #%d: %d" %(case_count, beauty_val(line))
		case_count += 1