#!/bin/sh

MAHOUT_PATH='/Users/josephmisiti/Downloads/trunk'

if [ $# -ne 1 ] || [ "$1" != "REC" ] && [ "$1" != "EVAL" ]; then
  echo "Usage: $0 <REC or EVAL>\n"
  exit -1
fi

if [ "$1" == "REC" ]; then
	echo "Building Recommender ... "
  	javac -d bin -cp $MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:$MAHOUT_PATH/core/target/mahout-core-0.8-SNAPSHOT.jar ItemBaseRecommender.java
  	echo "Complication Complete ...."
	exit
fi

if [ "$1" == "EVAL" ]; then
	echo "Building Evaluator ... "
  	javac -d bin -cp $MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:$MAHOUT_PATH/core/target/mahout-core-0.8-SNAPSHOT.jar ItemBaseRecommenderEvaluation.java
  	echo "Complication Complete ...."
	exit
fi

