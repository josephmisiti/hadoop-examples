#!/usr/bin/python

import os,sys
from recommendations import *

def get_data_dict(name='ratings_300.csv'):
	results = {}
	lines = [line.strip() for line in open(name).readlines()]
	for line in lines:
		user 	= line.split(",")[0]
		item 	= line.split(",")[1]
		rating 	= line.split(",")[2]
		results.setdefault(user,{})
		results[user][item] = float(rating)
	return results
		
if __name__ == "__main__":
	
	if len(sys.argv) == 1:
		print "usage: python itemrecommendations.py <user> <item>"
		sys.exit()
	else:
		prefs =  get_data_dict()
		#results  = getRecommendations( prefs, sys.argv[1], pearsons_correlation_score)
		results  = getRecommendations( prefs, sys.argv[1], euclidean_distance)
		
		pprint.pprint(getRecommendedItems(prefs, calculateSimilarItems(prefs),'1'))
		
		
		# print "------------------------------------"
		# print "user %s rated the following items" % sys.argv[1]
		# for item,rating in prefs[sys.argv[1]].items():
		# 	print "item: %s rating %2.2f" % (item,rating)
		# print "------------------------------------"
		# 		
		# for rating, item in results:
		# 	if len(sys.argv) == 3:
		# 		if item == sys.argv[2]:
		# 			print "item: %s rating %2.2f" % (item,rating)
		# 	else:
		# 		print "item: %s rating %2.2f" % (item,rating)
