import requests

response = requests.get(
    "https://reddit.com/r/gifs.json",
    headers = {"User-Agent":"not-requests"}
    )
children = response.json()["data"]['children']

for post in children:
    title = post['data']['title']
    url = post["data"]['url']
    if 'imgur.com/' in url:
        print(title,url)
