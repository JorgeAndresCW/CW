import json
import tweepy
from Credentials2 import*

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

def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 30)
    for status in statuses:
        print(status)
    print(len(statuses))
    return statuses



def store_tweets(tweets,filename):

    with open(filename+".json","w") as f:
        json.dump(tweets,f,indent=4)


    return

tweets=collect_by_user("@AlexandreDubou3")

#L=[1,"ee",34]
print(json.dumps(tweets,indent=4))

#il nous donne un erreur de que notre structure de tweets est pas serializable
