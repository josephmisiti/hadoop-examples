#!/bin/sh

source ./globals.sh

if [ "$1" != "CSV2VECTOR" ]; then
  echo "Usage: $0 <REC or EVAL>\n"
  exit -1
fi

if [ "$1" == "CSV2VECTOR" ]; then
	java -cp $MAHOUT_EXE_CP mia.recommender.ch02.CSVToMahout
	exit
fi

