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
