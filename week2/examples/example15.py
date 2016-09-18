# coding=utf-8
# Пример импорта модуля

import requests

URL = "https://google.com"

response = requests.get(URL)

print("Status code", response.status_code)

print("Headers: ")
print(response.headers)
