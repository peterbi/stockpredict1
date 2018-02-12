import os
import sys
import tweepy
import requests
import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from textblob import TextBlob


# twitter
#redacted
#redacted
#redacted
#redacted
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
user = tweepy.API(auth)

FILE_NAME = 'historical.csv'


def stock_sentiment(quote, num_tweets):
    # Checks if the sentiment for our quote is
    # positive or negative, returns True if
    # majority of valid tweets have positive sentiment
    list_of_tweets = user.search(quote, count=num_tweets)
    positive, null = 0, 0

    for tweet in list_of_tweets:
	print tweet.text
        blob = TextBlob(tweet.text).sentiment
        if blob.subjectivity == 0:
            null += 1
            next
	print blob. polarity
        if blob.polarity > 0:
            positive += 1

    if positive > ((num_tweets - null)/2):
        return True

def stock_prediction(epo):

    # Collect data points from csv
    dataset = []
    data = pd.read_csv(FILE_NAME)
    dataset = data['close'].values

    # Create dataset matrix (X=t and Y=t+1)
    def create_dataset(dataset):
        dataX = [dataset[n+1] for n in range(len(dataset)-2)]
        return np.array(dataX), dataset[2:]
        
    trainX, trainY = create_dataset(dataset)

    # Create and fit Multilinear Perceptron model
    model = Sequential()
    model.add(Dense(8, input_dim=1, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=epo, batch_size=2, verbose=2)

    # Our prediction for tomorrow
    prediction = model.predict(np.array([dataset[0]]))
    result = 'The price will move from %s to %s' % (dataset[0], prediction[0][0])

    return result

    
#AAPL stock sentiment

print "Stock sentiment for AAPL"

print stock_sentiment("AAPL", num_tweets=100)
# Check if the stock sentiment is positve

# We have our file so we create the neural net and get the prediction
print stock_prediction(200)

# We are done so we delete the csv file
#os.remove(FILE_NAME)
