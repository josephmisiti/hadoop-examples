package mia.recommender.ch02;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.eval.RecommenderBuilder;
import org.apache.mahout.cf.taste.eval.*;
import org.apache.mahout.cf.taste.impl.eval.*;
import org.apache.mahout.cf.taste.impl.neighborhood.*;
import org.apache.mahout.cf.taste.impl.recommender.*;
import org.apache.mahout.cf.taste.impl.similarity.*;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.*;
import org.apache.mahout.cf.taste.similarity.*;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import java.io.*;
import java.util.*;
import org.apache.mahout.common.RandomUtils;
import org.apache.mahout.cf.taste.impl.common.LongPrimitiveIterator;


/**
	* <p>
	*  This code implements a boolean collaborative filtering algorithm. 
	* </p>
*/

class ItemBaseRecommender {

	private ItemBaseRecommender() {}

	public static final int NUM_OF_RECOMMENDATIONS_RETURNED = 10;
  	public static boolean USE_LOG_LIKELIHOOD = true;
  	public static boolean WRITE_TO_FILE = true;
  	public static boolean KILL_EARLY = true;


	public static void main(String[] args) throws Exception 
	{
		
		
	
		String INPUT_FILE = "ua.base.boolean-large.csv";
		String OUTPUT_FILE = "recommendations.txt";
		if( args.length < 2){
			System.out.println("Usage: ./run.sh <INPUT-FILE> <OUTPUT-FILE>");
			System.exit(0);
		}
		else {
			INPUT_FILE = args[0];
			OUTPUT_FILE = args[1];
		}
	
		ItemSimilarity similarity;
		DataModel model = new FileDataModel(new File(INPUT_FILE));
		BufferedWriter out = new BufferedWriter(new FileWriter(OUTPUT_FILE));

	
	
		if( USE_LOG_LIKELIHOOD ){
			similarity =  new LogLikelihoodSimilarity(model);
		}
		else {
			similarity =  new TanimotoCoefficientSimilarity(model);
		}

		Recommender recommender = new GenericBooleanPrefItemBasedRecommender(model, similarity);
		
		int counter = 0;
		LongPrimitiveIterator users = model.getUserIDs();
		while (users.hasNext()) {
			long userID = users.nextLong();
			List<RecommendedItem> recommendations = recommender.recommend(userID, NUM_OF_RECOMMENDATIONS_RETURNED);
			for (RecommendedItem recommendation : recommendations) {
				
				if( WRITE_TO_FILE ){
					out.write(String.format("%d,%d,%2.2f\n", userID, recommendation.getItemID(), recommendation.getValue()));
				}
				else {
					System.out.format("%d,%d,%2.2f\n", userID, recommendation.getItemID(), recommendation.getValue() );
				}
				
				if (counter == 100 && KILL_EARLY){
					out.close();
					System.exit(0);
				}
				counter++;
			}		
		}
		
		out.close();
	}
}
