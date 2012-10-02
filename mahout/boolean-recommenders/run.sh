#!/bin/sh

source ./globals.sh

if [ "$1" != "REC" ] && [ "$1" != "EVAL" ] && [ "$1" != "REC-USER" ] && [ "$1" != "EVAL-USER" ] && [ "$1" != "CSV2VECTOR" ]; then
  echo "Usage: $0 <REC or EVAL>\n"
  exit -1
fi

if [ "$1" == "REC" ]; then
	java -cp $MAHOUT_EXE_CP mia.recommender.ch02.ItemBaseRecommender $2 $3
	exit
fi

if [ "$1" == "REC-USER" ]; then
	java -cp $MAHOUT_EXE_CP mia.recommender.ch02.UserBaseRecommender $2 $3
	exit
fi

if [ "$1" == "EVAL" ]; then
	java -cp $MAHOUT_EXE_CP mia.recommender.ch02.ItemBaseRecommenderEvaluation $2
	exit
fi

if [ "$1" == "EVAL-USER" ]; then
	java -cp $MAHOUT_EXE_CP mia.recommender.ch02.UserBaseRecommenderEvaluation $2
	exit
fi

if [ "$1" == "CSV2VECTOR" ]; then
	java -cp $MAHOUT_EXE_CP mia.recommender.ch02.CSVToMahout
	exit
fi

