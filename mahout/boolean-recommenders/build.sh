#!/bin/sh
#
# This script is used to build the evaluators + recommenders .. 
#

source ./globals.sh

if [ $# -ne 1 ] || [ "$1" != "REC" ] && [ "$1" != "EVAL" ] && [ "$1" != "REC-USER" ] && [ "$1" != "EVAL-USER" ] && [ "$1" != "CSV2VECTOR" ]; then
  echo "Usage: $0 <REC or EVAL>\n"
  exit -1
fi

# recommeders are java apps that perform recommendations and returns
# recommendations to stdout or file

if [ "$1" == "REC" ]; then
	echo "Building Item-Based Recommender ... "
  	javac -d bin -cp $MAHOUT_LIBS ItemBaseRecommender.java
  	echo "Complication Complete ...."
	exit
fi

if [ "$1" == "REC-USER" ]; then
	echo "Building User-Based Recommender ... "
  	javac -d bin -cp $MAHOUT_LIBS UserBaseRecommender.java
  	echo "Complication Complete ...."
	exit
fi

if [ "$1" == "CSV2VECTOR" ]; then
	echo "Building CSV TO VECTOR ... "
  	javac -d bin -cp $MAHOUT_LIBS CSVToMahout.java
  	echo "Complication Complete ...."
	exit
fi

# evaluators are used to evaluate the performance of the collaborative filters
# currently using precision, recall

if [ "$1" == "EVAL" ]; then
	echo "Building Evaluator ... "
  	javac -d bin -cp $MAHOUT_LIBS ItemBaseRecommenderEvaluation.java
  	echo "Complication Complete ...."
	exit
fi

if [ "$1" == "EVAL-USER" ]; then
	echo "Building Evaluator ... "
  	javac -d bin -cp $MAHOUT_LIBS UserBaseRecommenderEvaluation.java
  	echo "Complication Complete ...."
	exit
fi

