#!/bin/sh

# 
# This script will exceute the word-count example using Hadoop + Python Streaming
#
hadoop jar /usr/local/Cellar/hadoop/1.0.3/libexec/contrib/streaming/hadoop-*streaming*.jar \
			-file /Users/josephmisiti/mathandpencil/projects/hadoop/wordcount/mapper.py \
			-mapper /Users/josephmisiti/mathandpencil/projects/hadoop/wordcount/mapper.py \
			-file /Users/josephmisiti/mathandpencil/projects/hadoop/wordcount/reducer.py \
			-reducer /Users/josephmisiti/mathandpencil/projects/hadoop/wordcount/reducer.py \
			-input /user/hduser/gutenberg/* \
			-output /user/hduser/gutenberg-output
