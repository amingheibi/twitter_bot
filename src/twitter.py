def endpoint_url():
    endpoint = 'https://api.twitter.com/2/tweets/search/recent'
    return endpoint


def get_params(query):
    params = (
        ('query', query),
        #  ('tweet.fields', 'author_id,created_at,entities,geo,
        #  in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source')
        ('tweet.fields', 'author_id,entities')
    )
    return params

# sample query with curl, Twitter API v2
# curl --location --request GET
# 'https://api.twitter.com/2/tweets/search/recent?query=nyc&
#  tweet.fields=author_id,created_at,entities,geo,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source'


def get_twitter_headers(token):
    # authorization: Bearer $BEARER_TOKEN'
    headers = {'authorization': 'Bearer {}'.format(token)}
    return headers
