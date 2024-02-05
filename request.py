# https://python.civic-apps.com/http-request-post-get/

import requests

response = requests.get('http://www.example.com')

print(response.status_code)    # HTTPのステータスコード取得
print(response.text)    # レスポンスのHTMLを文字列で取得

response = requests.get('https://httpbin.org/get')
print(response.json())  # レスポンスのjsonをdict化して返す

