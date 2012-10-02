#!/bin/sh

# perform k-means on csv data (which has been converted to mahout format),
# dump the results to friendly txt format, and then view them :)

mahout kmeans   -i /user/rdw/kmeans_input \
                -o /user/rdw/kmeans_results \
                --maxIter 20 \
                --clustering \
                --distanceMeasure org.apache.mahout.common.distance.CosineDistanceMeasure \
                --method mapreduce \
                --convergenceDelta .0001 \
                --maxIter 30 \
                -k 50 \
                --overwrite \
                --clusters /user/rdw/clusters


wait

mahout clusterdump  --seqFileDir  /user/rdw/kmeans_results/clusters-1 \
                    --pointsDir /user/rdw/kmeans_results/clusteredPoints \
                    --output /hadoop/joem/clustering/results.txt


wait

cat /hadoop/joem/clustering/results.txt | head -n 100
