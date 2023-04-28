import requests
import json, os, time
from dotenv import load_dotenv

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
    return r

r = getbookdetails(isbn)

json_load = r.json()

print(type(r))

print(type(json_load))

print(json.dumps(json_load, indent=2, ensure_ascii=False))

print(json_load['Items'][0]['Item']['title'])