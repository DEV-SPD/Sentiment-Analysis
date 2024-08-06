# PRODUCT REVIEW SENTIMENT ANALYSIS
The Product Review Sentiment Analysis project aims to evaluate and categorize customer sentiments from product reviews on e-commerce platforms like Amazon. Utilizing a dataset of 4000 customer reviews, the project employs natural language processing (NLP) techniques and machine learning algorithms to classify the sentiment of each review as positive, negative, or neutral. Achieving an impressive 97.01% accuracy on test data, the model effectively balances bias and variance, ensuring reliable sentiment analysis. This tool is instrumental for businesses to understand customer feedback, improve products, and enhance customer satisfaction.

# RESULTS 
## Model Performance Results
Logistic Regression:
   1. Train Accuracy: 94.71%
   2. Test Accuracy: 93.50%
   3. Cross-Validation Score: 93.04%
Support Vector Classifier (SVC)
   1. Train Accuracy: 97.35%
   2. Test Accuracy: 97.02%
   3. Cross-Validation Score: 96.82%
Decision Tree Classifier
  1. Train Accuracy: 97.40%
  2. Test Accuracy: 92.82%
  3. Cross-Validation Score: 93.46%
Random Forest Classifier
  1. Train Accuracy: 97.40%
  2. Test Accuracy: 95.93%
  3. Cross-Validation Score: 95.38%
AdaBoost Classifier (n_estimators=1000)
  1. Train Accuracy: 97.40%
  2. Test Accuracy: 95.19%
  3. Cross-Validation Score: 94.83%
Bagging Classifier (Base Estimator: DecisionTreeClassifier, n_estimators=1000)
  1. Train Accuracy: 97.40%
  2. Test Accuracy: 93.83%
  3. Cross-Validation Score: 93.62%
Gradient Boosting Classifier (n_estimators=1000)
  1. Train Accuracy: 97.40%
  2. Test Accuracy: 94.44%
  3. Cross-Validation Score: 94.39%
Multinomial Naive Bayes (MultinomialNB)
  1. Train Accuracy: 91.88%
  2. Test Accuracy: 90.24%
  3. Cross-Validation Score: 90.05%

These results demonstrate the performance of various models on the sentiment analysis dataset. The Support Vector Classifier (SVC) performed the best overall with high accuracy on both training and testing data, and a strong cross-validation score
