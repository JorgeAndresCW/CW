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
                listTweets = listTweets + tweet.text
        return listTweets

    except (tweepy.TweepError, tweepy.RateLimitError):
        print("There is a problem charging twitter")
        return


# in order to obtain the reponses , we have to fix the in reply to status id (the id of the message) and in reply to user id(the id of the owner of the message)
def get_retweets_of_candidate(num_candidate):

#comme obtenir le nombre du candidate?
    connexion = twitter_setup()
    tweets = connexion.search("RT",count=200)
#a retweet does not have user_mention, a retweet has retweet=True, retweeted_status.id (id of the message that i am retweeting) (problem: it does not allow me search with this criteria
    for tweet in tweets:
        print(tweet.text)
        print(tweet.created_at)
    print(len(tweets))



#for the streaming we need to know the id of the user, and the function follow user id will give us the repply and retweets
#By default @replies are only sent if the current user follows both the sender and receiver of the reply. For example, consider the case where Alice follows Bob, but Alice doesn’t follow Carol. By default, if Bob @replies Carol, Alice does not see the Tweet. This mimics twitter.com and api.twitter.com behavior. To have such Tweets returned in a streaming connection, specify replies=all when connecting.
#forget last comment, (deprecated)

list_streaming=[]

def collect_by_streaming(user_id):

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(follow=[user_id])




