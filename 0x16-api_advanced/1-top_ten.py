#!/usr/bin/python3
"""prints hosts on a given reddit subreddit"""

import requests

def top_ten(subreddit):
    """print the titles of the 10 hottest posts on a given subreddit."""
    #construct the URL for the subreddits in JSON
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    #define headers for the HTTP request
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }

    params = {
            "limit":10
            }

    #a GET request to the subreddit's post page
    response = requests.get(url, headers=headers, params=params,
            allow_redirects=False)

    #if the response status code indicates a not-found error(404)
    if response.status_code == 404:
        print("None")
        return

    #the JSON response and extract the data section
    results = response.json().get("data")

    #prints the title of the top 10 posts
    [print(c.get("data").get("title")) for c in results.get("children")]
