#!/usr/bin/python


import re
import os
import sys
import math
import numpy

global CURRENT_CLUSTER

def get_points_from_line( line, oline=None ):
	
	try:
		points = [float(x) for x in line]
	except:
		points = [0.0,0.0,0.0,0.0,0.0,0.0]
		for x in line:
			i = int(x.split(":")[0].strip())
			points[i-1] = float(x.split(":")[1])			
	return points

def get_centroids( lines ):
	
	RESULTS = {}
	LINES = []
	
	exp = re.compile('c=\[.*]$')
	line_number = 0
	for line in lines:
		if "VL" in line:
			
			cluster_name =  line.split("{")[0]
			LINES.append( (cluster_name,line_number) )
			center = line.split("[")[1].split("]")[0].split(",")
			if len(center) == 6:
				RESULTS.setdefault(cluster_name,[0.0,0.0,0.0,0.0,0.0,0.0])
				RESULTS[cluster_name] = [float(x) for x in center]
			else:
				temp = [0.0,0.0,0.0,0.0,0.0,0.0]
				for x in center:
					i = int(x.split(":")[0].strip())
					temp[i-1] = float(x.split(":")[1])
				RESULTS[cluster_name] = temp
		line_number += 1
	return (RESULTS, LINES)
	
def euclidean_dist(x,y): return numpy.sqrt(numpy.sum((x-y)**2))
def cosine_distance(u, v): return numpy.dot(u, v) / (math.sqrt(numpy.dot(u, u)) * math.sqrt(numpy.dot(v, v)))

def parse( filepath ):
	
	lines = [ line.strip() for line in open(filepath).readlines() ]
	(centers, line_numbers) = get_centroids(lines)
		
	for line in lines:
		if "VL" in line:
			CURRENT_CLUSTER = line.split("{")[0]
			continue
		if "Weight" in line: 
			continue
		
		location =  line.split("[")[1].split("]")[0].split(",")
		center = numpy.array(centers[CURRENT_CLUSTER])
		product = numpy.array(get_points_from_line(location, line))
		distance = euclidean_dist(center,product)
		
		print "%s,%s,%s" % (line.split(" ")[1], CURRENT_CLUSTER, distance)
		
		
if __name__ == "__main__":
	if len(sys.argv) == 2:
		parse(sys.argv[1])
	else:
		print "usage ./parse_results.py <path-to-file>"
		sys.exit()