#pip install poetry (Gerenciador de pacotes)
import requests

from dadosacesso import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BASE_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy

BRAZIL_WOE_ID= 23424768

auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
trends = api.get_place_trends(BRAZIL_WOE_ID)



for tweet in tweets:
    print(tweet)
