# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

import os, sys
from math import sqrt
import pprint

def tanimoto_distance(prefs, person1, person2):
	"""
	
	"""
	pass

def euclidean_distance(prefs, person1, person2):
	items_in_common = []
	for item in prefs[person1]:
		if item in prefs[person2]:
			items_in_common.append(item)
	
	if len(items_in_common) == 0: return 0
	sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item],2) for item in items_in_common])
	
	return 1/(1+sqrt(sum_of_squares))
	#return 1/(1+ sum_of_squares ) 


def pearsons_correlation_score(prefs, person1, person2):
	items_in_common = []
	for item in prefs[person1]:
		if item in prefs[person2]:
			items_in_common.append(item)	
	
	n = len(items_in_common)
	if n == 0: return 0.0
	
	# sum all preferences
	sum1 = sum([ prefs[person1][item] for item in items_in_common ])
	sum2 = sum([ prefs[person2][item] for item in items_in_common ])

	# sum the squares
	sum1sqrd = sum([ pow(prefs[person1][item],2) for item in items_in_common ])
	sum2sqrd = sum([ pow(prefs[person2][item],2) for item in items_in_common ])	
	
	pSum = sum([ prefs[person1][item]*prefs[person2][item] for item in items_in_common ])	

	num = pSum-(sum1*sum2/n)
	den = sqrt((sum1sqrd-pow(sum1,2)/n)*(sum2sqrd-pow(sum2,2)/n))
	
	print num
	print den
	
	
	if den == 0: return 0
	
	return num/den

def topMatches( prefs, person, n, similarity, debug=True ):
	"""
		Returns a list of length n of movie critics most similar to 'person'
	"""
	scores = []
	for other_person in prefs:
		if person != other_person:
			scores.append( (similarity(prefs,person,other_person),other_person) )
	scores.sort()
	scores.reverse()
	scores = scores[0:n]
	
	if debug:
		print("%s is most similar to:")
		for score in scores:
			print "%s %2.2f" % (score[1], score[0])
	
	return scores

def getRecommendations( prefs, person, similarity):
	'''
		get recommendations for a person
	'''
	totals = {}
	simSum = {}
	for other_person in prefs:
		if other_person == person: continue
		
		# similar are these two people .. 
		sim = similarity( prefs, person, other_person)
		if sim <= 0.0: continue
		
		# now go through each items
		for item in prefs[other_person]:
			if item not in prefs[person] or prefs[person][item] == 0:
				totals.setdefault(item,0)
				totals[item] += prefs[other_person][item]* sim
		
				simSum.setdefault(item,0)
				simSum[item] += sim
		
	rankings = [ (totals[item]/simSum[item],item) for item in totals]
	rankings.sort()
	rankings.reverse()
	return rankings

def getRecommendedItems(prefs, itemMatch, user):
	
	scores = {}
	totalSim = {}
	
	userRatings = prefs[user]
	for (item,rating) in userRatings.items():
		for (similarity, item2) in itemMatch[item]:
			if item2 in userRatings: continue
			scores.setdefault(item2,0)
			scores[item2] += rating*similarity
			
			totalSim.setdefault(item2,0)
			totalSim[item2] += similarity
	
	rankings = [ (scores[item]/totalSim[item],item) for item in totalSim]
	rankings.sort()
	rankings.reverse()
	
	return rankings		
			
			
def transformItemPrefs(prefs):
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			result[item][person] = prefs[person][item]
	return result

def calculateSimilarItems( prefs, n=10):
	results = {}
	itemPrefs = transformItemPrefs( prefs )
	for item in itemPrefs:
		scores = topMatches( itemPrefs, item,n=n, similarity=euclidean_distance, debug=False)
		results[item] = scores
	return results	
	
	
if __name__ == "__main__":
	person1 = 'Lisa Rose'
	person2 = 'Gene Seymour'	
	print pearsons_correlation_score( critics, person1, person2 )
	