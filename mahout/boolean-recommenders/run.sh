#!/bin/sh

MAHOUT_PATH='/Users/josephmisiti/Downloads/trunk'

if [ $# -ne 1 ] || [ "$1" != "REC" ] && [ "$1" != "EVAL" ]; then
  echo "Usage: $0 <REC or EVAL>\n"
  exit -1
fi


if [ "$1" == "REC" ]; then
	java -cp "$MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:bin:/Users/josephmisiti/Downloads/trunk/core/target/mahout-core-0.8-SNAPSHOT.jar" mia.recommender.ch02.ItemBaseRecommender $1 
	exit
fi

if [ "$1" == "EVAL" ]; then
	java -cp "$MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:bin:/Users/josephmisiti/Downloads/trunk/core/target/mahout-core-0.8-SNAPSHOT.jar" mia.recommender.ch02.ItemBaseRecommender $1 
	exit
fi

