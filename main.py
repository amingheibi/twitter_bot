import setting
import requests
import json

#sample query with curl, Twitter API v2
# curl --location --request GET 'https://api.twitter.com/2/tweets/search/recent?query=nyc&tweet.fields=author_id,created_at,entities,geo,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source'

def endpoint_url():
    endpoint = 'https://api.twitter.com/2/tweets/search/recent'
    return endpoint

def get_params(query):
    params = (
     ('query', query),
     ('tweet.fields', 'author_id,created_at,entities,geo,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source'),
    )
    return params

def get_headers():
    #authorization: Bearer $BEARER_TOKEN'
    headers = {'authorization': 'Bearer {}'.format(setting.BEARER_TOKEN)}
    return headers

response = requests.get(endpoint_url(),params=get_params('هوش مصنوعی'),headers=get_headers())
if response.status_code !=200:
    print(response.status_code)
    print(response.text)
else:
    print(json.dumps(response.json(), indent=4, sort_keys=True))

