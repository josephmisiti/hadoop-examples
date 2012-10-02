#!/bin/sh
#
# This script is used to build the evaluators + recommenders .. 
#

source ./globals.sh

if [ "$1" != "CSV2VECTOR" ]; then
  echo "Usage: $0 <REC or EVAL>\n"
  exit -1
fi

if [ "$1" == "CSV2VECTOR" ]; then
	echo "Building CSV TO VECTOR ... "
  	javac -d bin -cp $MAHOUT_LIBS CSVToMahout.java
  	echo "Complication Complete ...."
	exit
fi

