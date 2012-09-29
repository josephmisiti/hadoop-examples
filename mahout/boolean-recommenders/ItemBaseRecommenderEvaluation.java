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
import org.apache.mahout.cf.taste.recommender.Recommender;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import java.io.*;
import java.util.*;
import org.apache.mahout.common.RandomUtils;


/**
	* <p>
	*  This code evaluates a boolean collaborative filtering algorithm. 
	* </p>
*/


class ItemBaseRecommenderEvaluation {

	private ItemBaseRecommenderEvaluation() {}
	
	public static void main(String[] args) throws Exception {

	DataModel model = new FileDataModel(new File("ua.base.boolean.csv"));

	RecommenderBuilder builder = new RecommenderBuilder() {
	  @Override
	  public Recommender buildRecommender(DataModel model) throws TasteException {
			return new GenericBooleanPrefItemBasedRecommender(model, new LogLikelihoodSimilarity(model));
	  }
	};

    RecommenderIRStatsEvaluator evaluator = new GenericRecommenderIRStatsEvaluator();
    IRStatistics stats = evaluator.evaluate(builder, 
											null, 
											model, 
											null, 
											1, 
											GenericRecommenderIRStatsEvaluator.CHOOSE_THRESHOLD, 
											1);

	// on average, about P % of recommendations are good
	System.out.println("PRECISION: On Avarege, about " + stats.getPrecision()*100.0 + "% of recommendations are good" );
	
	// %R of good recommenations are amont those recommended
	System.out.println("RECALL: " + stats.getRecall()*100.0 + "% of good recommenations are among those recommended");

	}


}
