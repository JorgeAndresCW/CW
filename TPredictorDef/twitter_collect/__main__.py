import tweepy

from Credentials2 import *
from tweet_collect_whole import*
from collect_candidate_actuality_tweets import get_retweets_of_candidate
from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

def get_tweets_from_candidates_search_queries(queries, twitter_api):
    try:
        listTweets=[]
        for querie in queries:
            tweets = twitter_api.search(querie)
            for tweet in tweets:
                listTweets.append(tweet.text)
        return listTweets

    except (tweepy.TweepError, tweepy.RateLimitError):
        print("There is a problem charging twitter")
        return

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

def collect_by_streaming(user_id):

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(follow=[user_id])


twitter_api=twitter_setup()
#num_candidate=input("Choose the number of the candidate")

list_queries=get_candidate_queries(1, 1)  #with the num of the candidate and the path for arriving to its hashtags and its keywords

list_queriestweets=get_tweets_from_candidates_search_queries(list_queries, twitter_api)

#list_retweets=get_retweets_of_candidate(num_candidate)

user_id=input("Ecris le id du candidate")

#list_reponses=get_replies_to_candidate(num_candidate)

#list_fix=list_queriestweets+list_retweets+list_reponses #We have to complete our function get reponse

list_streaming=[]

list_streaming=collect_by_streaming(user_id)

print(list_queriestweets)

print(list_streaming)


#as we need the id for the streaming function






