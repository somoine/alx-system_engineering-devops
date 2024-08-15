#!/usr/bin/python3
"""Script to obtain subscribers count from a subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    """Function to get subscriber count"""
    if not subreddit or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'my-alx-app/0.0.1 (contact: myemail@example.com)'}
    
    try:
        req = get(url, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            data = req.json()
            return data.get('data', {}).get('subscribers', 0)
    except Exception:
        pass
    
    return 0
