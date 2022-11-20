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


gif_links = {
    'start': [
        'https://media.giphy.com/media/l2JecCAExsqUC4HDy/giphy.gif',
        'https://media.giphy.com/media/SyP24XyDVsavNPECoR/giphy.gif',
        'https://media.giphy.com/media/3o6MbrQELrt6NcJm5W/giphy.gif',
        'https://media.giphy.com/media/mxDZecDOOsWCA/giphy.gif',
        'https://media.giphy.com/media/3o6MbeNr6v9XW7HNFS/giphy.gif',
        'https://media.giphy.com/media/xT1XGZAyEPjHNhOtRm/giphy.gif',
        'https://media.giphy.com/media/0DYipdNqJ5n4GYATKL/giphy.gif',
        'https://media.giphy.com/media/tdoUaMmgtgSqc/giphy.gif',
        'https://media.giphy.com/media/JLbTqEU5B8Z2w/giphy.gif',
        'https://media.giphy.com/media/AEqFAlx5VWY0M/giphy.gif',
        'https://media.giphy.com/media/5evtRzjLCov28/giphy.gif',
        'https://media.giphy.com/media/OIDxfuHdmcbqAOTqaY/giphy.gif'
    ],
    'white': [
        'https://media.giphy.com/media/ZqUVtxTTbd6Cc/giphy.gif',
        'https://media.giphy.com/media/s0k30jjI04THq/giphy.gif',
        'https://media.giphy.com/media/18RZ90FUGRRgRtAzp9/giphy.gif',
        'https://media.giphy.com/media/3hxwL6XGWnUI1aNlhT/giphy.gif',
        'https://media.giphy.com/media/TOUo1lBam8N2w/giphy.gif'
    ],
    'working': [
        'https://media.giphy.com/media/UYmY3vRnWpHHO/giphy.gif',
        'https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif',
        'https://media.giphy.com/media/l0K4hO8mVvq8Oygjm/giphy.gif',
        'https://media.giphy.com/media/13rQ7rrTrvZXlm/giphy.gif',
        'https://media.giphy.com/media/cg5FwpvDmhIcM/giphy.gif',
        'https://media.giphy.com/media/tn3kTJo4P4y1G/giphy.gif',
        'https://media.giphy.com/media/QK21sAsxnJATS/giphy.gif',
        'https://media.giphy.com/media/10mbtDA1OCEgDK/giphy.gif',
        'https://media.giphy.com/media/4oHyOIBIt57ag/giphy.gif',
        'https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif',
        'https://media.giphy.com/media/55m7FOTd2wneLu2mqd/giphy.gif',
        'https://media.giphy.com/media/YIXnEGNfdG4cE/giphy.gif',
        'https://media.giphy.com/media/1dHy0JSmsIfJgTgXEF/giphy.gif'

    ],
    'finish': [
        'https://media.giphy.com/media/3oEjHUf7j0aFDce0dG/giphy.gif',
        'https://media.giphy.com/media/3o7qDEq2bMbcbPRQ2c/giphy.gif',
        'https://media.giphy.com/media/11GWLm7bE2fibC/giphy.gif',
        'https://media.giphy.com/media/Ajhi3tsHaGBB6/giphy.gif',
        'https://media.giphy.com/media/muCo9BLS7vjErTON27/giphy.gif',
        'https://media.giphy.com/media/QMsS2IxP812wbn4WeE/giphy.gif',
        'https://media.giphy.com/media/8YBm95B5JNIXTWp5on/giphy.gif'
    ],
    'error': [
        'https://media.giphy.com/media/8EmeieJAGjvUI/giphy.gif',
        'https://media.giphy.com/media/3o6Zt6ML6BklcajjsA/giphy.gif',
        'https://media.giphy.com/media/nVTa8D8zJUc2A/giphy.gif',
        'https://media.giphy.com/media/3oKIPs1EVbbNZYq7EA/giphy.gif',
        'https://media.giphy.com/media/3Zp8CshcNtX6Mtr2Oj/giphy.gif',
        'https://media.giphy.com/media/dlMIwDQAxXn1K/giphy.gif',
        'https://media.giphy.com/media/g79am6uuZJKSc/giphy.gif',
        'https://media.giphy.com/media/13d2jHlSlxklVe/giphy.gif',
        'https://media.giphy.com/media/3o7TKxCX1CMPsUBE3e/giphy.gif',
        'https://media.giphy.com/media/3orifalzpkYYe8Mxy0/giphy.gif',
        'https://media.giphy.com/media/l2Je5IMLrZSbFD63S/giphy.gif',
        'https://media.giphy.com/media/eImrJKnOmuBDmqXNUj/giphy.gif',
        'https://media.giphy.com/media/YO7P8VC7nlQlO/giphy.gif',
        'https://media.giphy.com/media/4ZvxJSvzjmGg9yvolw/giphy.gif',
        'https://media.giphy.com/media/3o6UBiAQ9Ws8UWdmqA/giphy.gif',
        'https://media.giphy.com/media/l0MYrBjH940fhs96o/giphy.gif',
        'https://media.giphy.com/media/KBPFlXF4adtZdVis0c/giphy.gif',
        'https://media.giphy.com/media/l2Je8n1SgbvuEjs8U/giphy.gif',
        'https://media.giphy.com/media/Lo2hZm2etXjJm/giphy.gif',
        'https://media.giphy.com/media/3o6MbfihCsqYtqD0xW/giphy.gif',
        'https://media.giphy.com/media/3ohze456U9AIzUbex2/giphy.gif',
        'https://media.giphy.com/media/oQgDpLtsIQl1e/giphy.gif',
        'https://media.giphy.com/media/jS87uGldWwfh6SzCsg/giphy.gif',
        'https://media.giphy.com/media/9rAqb4kMwrGlqBnOq1/giphy.gif',
        'https://media.giphy.com/media/phJ6eMRFYI6CQ/giphy.gif',
        'https://media.giphy.com/media/xT5LMToUWkh57aUs3m/giphy.gif',
        'https://www.wykop.pl/cdn/c3201142/comment_sy6yVJAtOALo2mS39mbcMv5DybD7dTlA.gif',
        'https://media.giphy.com/media/YzskBcDFyH22k/giphy.gif',
        'https://media.giphy.com/media/lngjGVdDD6bEqFoAO9/giphy.gif',
        'https://media.giphy.com/media/Ahw40HZzrd0yN9ndH5/giphy.gif',
        'https://media.giphy.com/media/jsIEObYXbHdMv1fVQO/giphy.gif',
        'https://media.giphy.com/media/3orifckBVb4KdqpUqs/giphy.gif',
        'https://media.giphy.com/media/KBPFlXF4adtZdVis0c/giphy.gif',
        'https://media.giphy.com/media/xT5LMuMsf1GphZrB9C/giphy.gif',
        'https://media.giphy.com/media/HUkOv6BNWc1HO/giphy.gif',
        'https://media.giphy.com/media/nrXif9YExO9EI/giphy.gif',
        'https://media.giphy.com/media/KmTnUKop0AfFm/giphy.gif',
        'https://media.giphy.com/media/joV1k1sNOT5xC/giphy.gif',
        'https://media.giphy.com/media/J3MJAf2FbKO8oaTaTv/giphy.gif',
        'https://media.giphy.com/media/KcnIdXKOuvxNjLqYc1/giphy.gif',
        'https://media.giphy.com/media/An4MkAbxeiyqY/giphy.gif',
        'https://media.giphy.com/media/UTw9wnoyP8Pcs/giphy.gif',
        'https://media.giphy.com/media/xT9IgAhIUlEb5oXhAY/giphy.gif',
        'https://media.giphy.com/media/3o751XCnKoIwchqtEs/giphy.gif',
    ],
    'other': [
        'https://media.giphy.com/media/citBl9yPwnUOs/giphy.gif',
        'https://media.giphy.com/media/1136UBdSNn6Bu8/giphy.gif',
        'https://media.giphy.com/media/1d7F9xyq6j7C1ojbC5/giphy.gif',
        'https://media.giphy.com/media/3o6Zt3KyN0vd1S97d6/giphy.gif',
        'https://media.giphy.com/media/1dLiJGblBWmRqNV4fJ/giphy.gif',
        'https://media.giphy.com/media/100QWMdxQJzQC4/giphy.gif',
        'https://media.giphy.com/media/3boPPdHk2ueo8/giphy.gif',
        'https://media.giphy.com/media/BLeTkfK6TbjTa/giphy.gif',
        'https://media.giphy.com/media/47HLuGXkNVrUIHAtQW/giphy.gif',
        'https://media.giphy.com/media/LfTMESsJpxdZu/giphy.gif',
    ]
}