import setting
import requests
from time import sleep

from pathlib import Path
from slack import get_slack_headers, post_to_slack
from twitter import endpoint_url, get_params, get_twitter_headers
from utils import get_keywords, check_response, write_to_csv_file


def main():
    while True:
        keywords = get_keywords()
        for keyword in keywords:
            print('Fetching tweets for ' + keyword)
            response = requests.get(endpoint_url(), params=get_params(
                keyword), headers=get_twitter_headers(setting.BEARER_TOKEN))
            if check_response(response) == 0:
                write_to_csv_file(response, Path('data/recent_tweets.csv'))
                post_to_slack(response, setting.WEBHOOK)
        print("Sleeping for 10 hours")
        sleep(36000)  # 10 hours


if __name__ == "__main__":
    main()

# TODO: Dockerize
# TODO: Write unit tests
# TODO: Add a cache or in-memory database to avoid fetching old tweets
# TODO: Take different sleep time for different keywords
