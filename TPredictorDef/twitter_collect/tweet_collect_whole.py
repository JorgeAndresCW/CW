
def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        queries=list()
        with open(r"C:\Users\Roch\PycharmProjects\TPredictorDef\CandidateData\keywords_candidate_n.txt","r") as keywords: #file_path refers to a list of 2 paths (Keywords (0), Hashtags (1))
            infokey=keywords.readlines()
            num_keyword=len(infokey)
            listKeywords=[]
            for i in range (num_keyword):

                listKeywords=listKeywords+infokey[i].split(" ")

        with open(r"C:\Users\Roch\PycharmProjects\TPredictorDef\CandidateData\hashtag_candidate_n.txt","r") as hashtags :

            infohashtags=hashtags.readlines()
            num_hashtags=len(infohashtags)
            listHashtags=[]
            for j in range (num_hashtags):
                listHashtags=listHashtags+infohashtags[j].split(" ")

        listqueries=listKeywords+listHashtags

        for i in range (len(listqueries)):
            listqueries[i]=listqueries[i].replace("\n","")
        return listqueries



    except IOError:
        print("Wrong file path")
        return
        # TO COMPLETE

print(get_candidate_queries(1,1))
