import requests
import json
from .utils import check_response


def get_slack_headers():
    headers = {'Content-type': 'application/json'}
    return headers


def post_to_slack(response, slack_web_hook):
    for item in response.json()['data']:
        # post to slack (the username in the link is not important)
        tweet_link = "https://twitter.com/AminGheibi/status/{}".format(
            item['id'])
        response = requests.post(url=slack_web_hook,
                                 headers=get_slack_headers(),
                                 data=json.dumps({"text": tweet_link}))
        check_response(response)
