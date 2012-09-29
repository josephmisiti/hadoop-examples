#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
import pprint
from recommender import euclidean_distance, pearsons_correlation_score, tanimoto_distance 

class RecommendationEngineTests(unittest.TestCase):

	def setUp(self):
		self.critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
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

	def tearDown(self):
		pass

	def test_euclidean_distance(self):		
		person1 = 'Lisa Rose'
		person2 = 'Gene Seymour'
		self.assertTrue( abs(0.2942 - euclidean_distance( self.critics, person1, person2 )) < .0001 )
	
	def test_pearsons_cc(self):
		person1 = 'Lisa Rose'
		person2 = 'Gene Seymour'
		self.assertTrue(  abs(0.396 - pearsons_correlation_score( self.critics, person1, person2 )) < .001 )		
		
	def test_tanimoto_distance(self):
		person1 = 'Lisa Rose'
		person2 = 'Gene Seymour'
		print tanimoto_distance( self.critics, person1, person2 )
		#self.assertTrue(  abs(0.396 - pearsons_correlation_score( self.critics, person1, person2 )) < .001 )		
		
	def test_top_matches(self):
		from recommender import topMatches
		results =  topMatches( self.critics, 'Toby', 5, euclidean_distance )
	
		self.assertEqual( results[0][1], 'Mick LaSalle' )
		self.assertTrue( 0.4 - results[0][0] < .0001 )

		self.assertEqual( results[1][1], 'Michael Phillips' )
		self.assertTrue( 0.387 - results[1][0] < .0001 )
		
		self.assertEqual( results[2][1], 'Claudia Puig' )
		self.assertTrue( 0.35 - results[2][0] < .0001 )
		
		self.assertEqual( results[3][1], 'Lisa Rose' )
		self.assertTrue( 0.34 - results[3][0] < .0001 )

	def test_recommend_items(self):
		from recommender import  transformItemPrefs,calculateSimilarityMatrix, getRecommendedItems
		
		#calulate item similirity matrix one
		ISM = calculateSimilarityMatrix( self.critics, n=10)
		results = getRecommendedItems( self.critics, ISM, 'Toby' )

		self.assertEqual( results[0][1], 'The Night Listener' )
		self.assertTrue( 3.1 - results[0][0] < .0001 )

		self.assertEqual( results[1][1], 'Just My Luck' )
		self.assertTrue( 2.9 - results[1][0] < .0001 )
		
		self.assertEqual( results[2][1], 'Lady in the Water') 
		self.assertTrue( 2.8 - results[2][0] < .0001 )

	def test_get_recommendations(self):
		from recommender import  getRecommendations
		results =  getRecommendations( self.critics, 'Toby', euclidean_distance )
				
		self.assertEqual( results[0][1], 'The Night Listener' )
		self.assertTrue( 3.4 - results[0][0] < .0001 )

		self.assertEqual( results[1][1], 'Lady in the Water' )
		self.assertTrue( 2.4 - results[1][0] < .0001 )
		
		self.assertEqual( results[2][1], 'Just My Luck') 
		self.assertTrue( 2.4 - results[2][0] < .0001 )		
		
if __name__ == '__main__':
	unittest.main()