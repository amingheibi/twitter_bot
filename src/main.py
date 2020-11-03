import setting
import requests
import json
import csv
from pathlib import Path
from slack import get_slack_headers
from twitter import endpoint_url, get_params, get_twitter_headers
from utils import get_keywords, check_response


def main():
    keywords = get_keywords()
    for keyword in keywords:
        print('Fetching tweets for ' + keyword)
        response = requests.get(endpoint_url(), params=get_params(
            keyword), headers=get_twitter_headers(setting.BEARER_TOKEN))
        if check_response(response) == 0:
            # print(json.dumps(response.json(), indent=4, sort_keys=True))
            with open(Path('data/recent_tweets.csv'), 'w', newline='', encoding="utf-8") as csvfile:
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
