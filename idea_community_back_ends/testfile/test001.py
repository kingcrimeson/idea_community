import requests
import json

data = {
    'code':'hakbdk',
    'nickname':'?????'
}

respsonse = requests.post(url='http://127.0.0.1:8000/login',  json=data)
respsonse.content.decode('utf-8')
print(respsonse.json())