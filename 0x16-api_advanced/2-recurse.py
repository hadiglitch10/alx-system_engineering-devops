#!/usr/bin/python3
"""A recursive function that queries the Reddit
API and returns a list containing the titles of
all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """returns a list containing the titles
    of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    
    if not posts:
        return hot_list
    
    for post in posts:
        hot_list.append(post["data"]["title"])
    
    after = data["data"]["after"]
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

# Example usage
result = recurse("programming")
if result is not None:
    print(len(result))
else:
    print("None")
