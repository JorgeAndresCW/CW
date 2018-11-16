import tweepy
# We import our access keys:
from Credentials2 import *

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
twitter_setup()

def collect():
    connexion = twitter_setup()
    tweets = connexion.search("Boom: Jeff Flake says",count=43)

    for tweet in tweets:
        print(tweet.text)
        print(tweet.created_at)
    print(len(tweets))

def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 30)
    for status in statuses:
        print(status)
        print(status.id)
    print(len(statuses))
    return statuses

collect_by_user("@AlexandreDubou3")

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




def collect_by_streaming():

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(follow=["25073877"])
   # stream.replies=all (deprecated



