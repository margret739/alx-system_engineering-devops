#!/usr/bin/python3
"""to query a list of all hot articles on agiven redddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """ retrieves a list of titles of all hot posts"""
    # construct the URL for the subreddit in JSON
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # headers for the HTTP request
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }

    # parameters for the request
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }

    # a GET request to the subreddits
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # if response status code indicates a not-found errer:
    if response.status_code == 404:
        return None
    # extract relevant files
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # append host titles to the hot-list
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # more post to retrieve, call the function recursively
    if ater is not None:
        return recourse(subreddit, hot_list, count, after)

    # returns the final list
    return hot_list
