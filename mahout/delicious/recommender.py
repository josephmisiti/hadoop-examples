

import os
import sys
import random
import pprint
import cPickle as pickle
from math import sqrt, log
from copy import deepcopy

def get_items_in_common(pref_dict, p1, p2):
	items_in_common = []
	for item,pref in pref_dict[p1].items():
		if item in pref_dict[p2]:
			items_in_common.append( item )	
	return items_in_common

def tanimoto_distance(pref_dict, person1, person2):
	"""
		http://en.wikipedia.org/wiki/Jaccard_index#Tanimoto_Similarity_and_Distance
	"""
	X = set(pref_dict[person1].keys())
	Y = set(pref_dict[person2].keys())
	score = len(X.intersection(Y)) / len(X.union(Y))
	return -1.0*log(score,2)
	
		
def euclidean_distance(pref_dict, p1, p2):
	"""
		Calculates the ED of two people
		http://en.wikipedia.org/wiki/Euclidean_distance
	"""
	items_in_common = get_items_in_common(pref_dict, p1, p2)
	preference_pairs = [ (pref_dict[p1][item],pref_dict[p2][item]) for item in items_in_common]
	distance = sqrt(sum([pow(pair[0]-pair[1],2) for pair in preference_pairs]))

	# the smaller the ED is between two people, the close they are, but we need a function
	# that returns larger numbers for people that are closer together. When two people are identical,
	# they return on, else ----> 0 as they become opposites
	return 1 / (1 + distance)
		
def pearsons_correlation_score(pref_dict, person1, person2):
	"""
		http://davidmlane.com/hyperstat/A51911.html
	"""
	items_in_common = get_items_in_common(pref_dict, person1, person2)
	
	X = pref_dict[person1]
	Y = pref_dict[person2]
	N = len(items_in_common)
	
	if N == 0: return 0.0
	
	sumX		= sum([ X[item] for item in items_in_common ])
	sumY		= sum([ Y[item] for item in items_in_common ])
	sumXsumY	= sum([ X[item]*Y[item] for item in items_in_common ])
	sumXSquared	= sum([ pow(X[item],2) for item in items_in_common ])
	sumYSquared	= sum([ pow(Y[item],2) for item in items_in_common ])
	
	num = (sumXsumY - ((sumX*sumY)/N))
	den = sqrt( (sumXSquared - (pow(sumX,2)/N)) * (sumYSquared - (pow(sumY,2)/N))) 
	
	return num/den


def topMatches( pref_dict, person, n, similarity ):
	"""
		Calculate similar people in dataset to 'person'
	"""
	pdict = deepcopy(pref_dict)
	if person in pdict:
		del pdict[person]
	
	ranking = [  (similarity(pref_dict, person, other),other) for other,prefs in pdict.items() ]
	ranking.sort()
	ranking.reverse()
	
	if len(ranking) > n:
		return ranking[:n]
	else:
		return ranking
		
def transformItemPrefs(prefs):
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			result[item][person] = prefs[person][item]
	return result
		
def getRecommendations( pref_dict, person, similarity, isBoolean=True ):
	
	rankings = {}
	totalSim = {}
	
	similarities = topMatches( pref_dict, person, 10, similarity )
	for sim in similarities:
		for item in pref_dict[sim[1]]:
			if item in pref_dict[person]: 
				if isBoolean:
					if pref_dict[person][item] > 0.0:
						continue
				else:
					continue
			
			rankings.setdefault(item,0)
			totalSim.setdefault(item,0)
			
			SIMILARITY = sim[0]
			USER_PREF  = pref_dict[sim[1]][item]
			rankings[item] += SIMILARITY*USER_PREF
			totalSim[item] += SIMILARITY
	
	results = [ (v/totalSim[k],k) for (k,v) in rankings.items()]
	results.sort()
	results.reverse()		
	return results


def transformItemPrefs(prefs):
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			result[item][person] = prefs[person][item]
	return result

def calculateSimilarityMatrix( prefs, n=10):
	RESULTS = {}
	tprefs = transformItemPrefs(prefs)
	for item, preferences in tprefs.items():
		RESULTS[item] = topMatches( tprefs, item, n, euclidean_distance )
	return RESULTS
	

def getRecommendedItems( prefs, itemMatch, user, isBoolean=False ):

	scores = {}
	totalSim = {}
	
	# go through all the users items
	for item,pref in prefs[user].items():
		# find similiar items
		for sim in itemMatch[item]:
			theitem = sim[1]
			thesimilarity = sim[0]
			
			# if the user already rated this, skip
			
			if theitem in prefs[user]: 
				if isBoolean:
					if pref_dict[person][item] > 0.0:
						continue
				else:
					continue
			
			scores.setdefault(theitem,0)
			totalSim.setdefault(theitem,0)
			
			# take the preference had for some item, and weight it
			# by the similarities of of similiar item
			scores[theitem] += thesimilarity*pref
			totalSim[theitem] += thesimilarity
			
	
	results = [ (v/totalSim[k],k) for (k,v) in scores.items()]
	results.sort()
	results.reverse()
	return results
				
if __name__ == "__main__":
	f = open('data_top_5.dat','rb')
	delusers =  pickle.load(f)
	user = delusers.keys()[ random.randint(0,len(delusers)-1) ]
	
	# if 0:
	# 	recommendations = getRecommendations( delusers, 'josephmisiti', euclidean_distance )[0:5]
	# else:
	# 	getRecommendations( delusers, 'josephmisiti', euclidean_distance )[0:5]
	
	