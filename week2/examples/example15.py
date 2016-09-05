# coding=utf-8
# Пример импорта модуля

import urllib2

URL = "https://google.com"

response = urllib2.urlopen(url=URL)

print "Status code", response.code

print "Headers: "
print response.info()
