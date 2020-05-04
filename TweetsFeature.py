import tweepy
from textblob import textblob

#Each twitter developer has his unique key's for certain projects.
 
consumer_key = 's6c1P5M7qldsdFs1K7ZOg3M78'
consumer_secret = 'yCHlDTE9tL0LxEIX2YvB34WerjPEisSCgJvbOYRTDsdJRdqf3o'

#Access token for the twitter API.

access_token = '1073198340156899328-0AMWleXahPLrpZPygoEiakrl35PZRL'
access_token_secret = '2sO7XnqFE4qDLI4QS9IwsEpnW7XLeqrnSl5V5NVrUBKez'

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)