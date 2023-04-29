import requests
import json, os
from dotenv import load_dotenv

load_dotenv() 

isbn = "9784309226712"

apikey = os.getenv('WEBAPI_KEY')

def getbookdetails(isbn):
    baserequest = 'https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404'
    appid = '?applicationId=' + apikey
    value = '&isbnjan=' + isbn
    uri = baserequest + appid + value
    r = requests.get(uri)
    json_load = r.json()
    print(json.dumps(json_load, indent=2, ensure_ascii=False))
    info = {}
    info["title"] = json_load['Items'][0]['Item']['title']
    info['writer'] = json_load['Items'][0]['Item']['author']
    return info

# print(json.dumps(json_load, indent=2, ensure_ascii=False))

info = getbookdetails(isbn)

print("title:" + info['title'])

print('writer' + info['writer'])