import xml.etree.ElementTree as et
import requests

"""
Simple XML parser

"""
xml = et.fromstring(requests.get("https://habrahabr.ru/rss/hubs/all/30c40aa7d38d22d957ead830a042ac24/").content)

print(xml[0][2].tag)

for children in xml:
    for i in children:
        for k in i:
            if k.tag == 'title':
                print(k.text)
            if k.tag == 'description':
                print(k.text)
                print('\n\n')