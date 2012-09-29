#!/bin/sh

source ./globals.sh

if [ "$1" != "REC" ] && [ "$1" != "EVAL" ] && [ "$1" != "REC-USER" ]; then
  echo "Usage: $0 <REC or EVAL>\n"
  exit -1
fi


if [ "$1" == "REC" ]; then
	java -cp "$MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:bin:/Users/josephmisiti/Downloads/trunk/core/target/mahout-core-0.8-SNAPSHOT.jar" mia.recommender.ch02.ItemBaseRecommender $2
	exit
fi

if [ "$1" == "EVAL" ]; then
	java -cp "$MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:bin:/Users/josephmisiti/Downloads/trunk/core/target/mahout-core-0.8-SNAPSHOT.jar" mia.recommender.ch02.ItemBaseRecommender $2
	exit
fi

