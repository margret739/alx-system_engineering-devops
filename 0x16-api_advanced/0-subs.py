#!/usr/bin/python3
""" this queries subs on a given reddit subreddit"""

import requests


def number_of_subscribers(subreddit):
    """return the total number of subs on given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
