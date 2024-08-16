#!/usr/bin/python3
""" Defines a function that queries the Reddit API and prints the
    first 10 hot posts listed for a given subreddit. Prints None if an
    invalid subreddit is given
"""

import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def top_ten(subreddit):
    """method doc"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
