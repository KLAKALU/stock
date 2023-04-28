import requests
import json, os, time
from dotenv import load_dotenv

start = time.perf_counter()

load_dotenv() 

isbn = "9784309226712"

apikey = os.getenv('WEBAPI_KEY')

# pyaload = {"key1":"value1", "key2":"value2"}

def getbookdetails(isbn):
    baserequest = 'https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404'
    appid = '?applicationId=' + apikey
    value = '&isbnjan=' + isbn
    uri = baserequest + appid + value
    r = requests.get(uri)
    json_load = r.json()
    info = {}
    info["title"] = json_load['Items'][0]['Item']['title']
    info['writer'] = json_load['Items'][0]['Item']['author']
    return info

# print(json.dumps(json_load, indent=2, ensure_ascii=False))

info = getbookdetails(isbn)

print(info['title'])

print(info['writer'])