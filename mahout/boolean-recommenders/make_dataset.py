#!/usr/bin/python

"""
	generate random data
"""

import sys
import random

def make_dataset(num_users=25, num_items=50, num_ratings=250, boolean=True):
	DICT = {}
	for i in range(1,num_ratings+1):
		if boolean:
			DICT[ (random.randint(1,num_users), random.randint(1,num_items) ) ] = 1
		else:
			DICT[ (random.randint(1,num_users), random.randint(1,num_items))] = random.randint(1,5)

	if boolean:
		for key in DICT.keys():
			print "%d,%d" %( key[0], key[1]  )
	else:
		for key,value in DICT.items():
			print "%d,%d,%d" %( key[0], key[1], value )

if __name__ == "__main__":
	if len(sys.argv) > 1:
		boolean = sys.argv[5].lower() == 'true'
		make_dataset(num_users=int(sys.argv[2]), num_items=int(sys.argv[3]), num_ratings=int(sys.argv[4]), boolean=True)
	else:
		make_dataset(num_users=25, num_items=50, num_ratings=300, boolean=False)
	