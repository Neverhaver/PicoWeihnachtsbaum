import requests
from project_settings import settings
from urllib import parse
from random import randint

url = "http://api.giphy.com/v1/gifs/search"


def get_gif(query):
    random_gif_result = ""
    while not random_gif_result:
        params = parse.urlencode({
            "q": query,
            "api_key": settings["giphy"]["api_key"],
            "limit": "5",
            "offset": randint(0, 50)
        })
        gifs = requests.get("".join((url, "?", params)))

        for gif in gifs.json()['data']:
            gif_url = gif['images']['original']['url']
            if '.gif' in gif_url:
                random_gif_result = gif_url
                title = gif['title']
                return random_gif_result, title
