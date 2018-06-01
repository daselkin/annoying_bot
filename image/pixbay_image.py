import requests
import random
import json
import shutil


#RETURN JSON OBJECT WITH 10 IMAGE URLS
def create_pixbay_request():
    pixbay_key = '9156919-388f355c8d5a7bf95ae55a5ca' #THIS IS PERSONAL KEY
    valid = 0

    while valid == 0:
        page_number = random.randint(1, 200)

        url = 'https://pixabay.com/api/'
        payload = {'key': pixbay_key
            , 'image_type': 'photo'
            , 'min_width': '0'
            , 'min_height': '0'
            , 'safesearch': 'true'
            , 'order': 'latest'
            , 'page': page_number
            , 'per_page': '10'
                   # , 'q':
                   # , 'lang':
                   # , 'response_group':
                   # , 'orientation':
                   # , 'category':
                   # ,'editors_choice':
                   # , 'callback':
                   # , 'pretty':
                   }
        r = requests.get(url, params=payload)

        if r.status_code == 200: #RESPONSE IS GOOD JSON FORMAT
            valid = 1
        else:
            valid = 0

    to_json = json.dumps(r.json())
    json_obj_req = json.loads(to_json)
    return json_obj_req


#SELECT ONE URLS FROM LIST
def get_pixbay_url():
    json_req = create_pixbay_request()
    urls = []
    for value in json_req[u'hits']:
        urls.append(value[u'largeImageURL'])

    i = random.randint(0, len(urls)-1)
    return urls[i]


