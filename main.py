import setting
import requests
import json
import csv

# sample query with curl, Twitter API v2
# curl --location --request GET 'https://api.twitter.com/2/tweets/search/recent?query=nyc&tweet.fields=author_id,created_at,entities,geo,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source'


def endpoint_url():
    endpoint = 'https://api.twitter.com/2/tweets/search/recent'
    return endpoint


def get_params(query):
    params = (
        ('query', query),
        #  ('tweet.fields', 'author_id,created_at,entities,geo,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source')
        ('tweet.fields', 'author_id,entities')
    )
    return params


def get_twitter_headers():
    # authorization: Bearer $BEARER_TOKEN'
    headers = {'authorization': 'Bearer {}'.format(setting.BEARER_TOKEN)}
    return headers


def get_slack_headers():
    headers = {'Content-type': 'application/json'}
    return headers


def check_response(response):
    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        return 1
    return 0


def main():
    response = requests.get(endpoint_url(), params=get_params(
        'هوش مصنوعی'), headers=get_twitter_headers())
    if check_response(response) == 0:
        # print(json.dumps(response.json(), indent=4, sort_keys=True))
        with open('recent_tweets.csv', 'w', newline='', encoding="utf-8") as csvfile:
            csvw = csv.writer(csvfile)
            # csvw.writerow(['tweet_id','author_id','text','entities'])
            # simplify tweet for readablity
            csvw.writerow(['tweet_id', 'text'])
            for item in response.json()['data']:
                # csvw.writerow([item['id'],item['author_id'],item['text'],json.dumps(item.get('entities','N/A'))])
                csvw.writerow([item['id'], item['text']])
                # post to slack (the username in the link is not important, the id matters)
                tweet_link = "https://twitter.com/AminGheibi/status/{}".format(
                    item['id'])
                response = requests.post(url=setting.WEBHOOK,
                                         headers=get_slack_headers(),
                                         data=json.dumps({"text": tweet_link}))
                check_response(response)


if __name__ == "__main__":
    main()
