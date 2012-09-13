#!/bin/sh

MAHOUT_PATH='/Users/josephmisiti/Downloads/trunk'

javac -d bin -cp $MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:$MAHOUT_PATH/core/target/mahout-core-0.8-SNAPSHOT.jar EvaluatorIntro.java
java -cp "$MAHOUT_PATH/integration/target/dependency/*:$MAHOUT_PATH/math/target/mahout-math-0.8-SNAPSHOT.jar:bin:/Users/josephmisiti/Downloads/trunk/core/target/mahout-core-0.8-SNAPSHOT.jar" mia.recommender.ch02.EvaluatorIntro
