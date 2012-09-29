#!/bin/sh
#
# This script is used to build the evaluators + recommenders .. 
#

source ./globals.sh

if [ $# -ne 1 ] || [ "$1" != "REC" ] && [ "$1" != "EVAL" ] && [ "$1" != "REC-USER" ]; then
  echo "Usage: $0 <REC or EVAL>\n"
  exit -1
fi

# recommeders are java apps that perform recommendations and returns
# recommendations to stdout or file

if [ "$1" == "REC" ]; then
	echo "Building Item-Based Recommender ... "
  	javac -d bin -cp $MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:$MAHOUT_PATH/core/target/mahout-core-0.8-SNAPSHOT.jar ItemBaseRecommender.java
  	echo "Complication Complete ...."
	exit
fi

if [ "$1" == "REC-USER" ]; then
	echo "Building User-Based Recommender ... "
  	javac -d bin -cp $MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:$MAHOUT_PATH/core/target/mahout-core-0.8-SNAPSHOT.jar UserBaseRecommender.java
  	echo "Complication Complete ...."
	exit
fi

# evaluators are used to evaluate the performance of the collaborative filters
# currently using precision, recall

if [ "$1" == "EVAL" ]; then
	echo "Building Evaluator ... "
  	javac -d bin -cp $MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:$MAHOUT_PATH/core/target/mahout-core-0.8-SNAPSHOT.jar ItemBaseRecommenderEvaluation.java
  	echo "Complication Complete ...."
	exit
fi

