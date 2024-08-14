import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyAPIProject/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    return 0
