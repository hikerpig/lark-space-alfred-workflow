# coding=utf-8

import httplib
import json
import os
import os.path
import struct
import urllib
import re
import sys

from urlparse import urlparse
from datetime import datetime, date

from searchresult import SearchResult
from lark_common import cookie, larkDomain, larkDriveHome, parsedLarkDomain, unicodeAlfredQuery, cookie, referer, DocType

def build_create_payload(doc_type):
    data = {
        'parent_token': '',
        'type': doc_type,
        'name': '',
    }

    return urllib.urlencode(data)

doc_type = DocType.DOC
try:
    doc_type = int(unicodeAlfredQuery)
except Exception, e:
    doc_type = DocType.DOC

payload = build_create_payload(doc_type)
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Referer": referer,
           "Cookie": cookie}

conn = httplib.HTTPSConnection(parsedLarkDomain.netloc)
conn.request("POST", "/space/api/explorer/create/",
             build_create_payload(unicodeAlfredQuery), headers)
response = conn.getresponse()

resData = response.read()
conn.close()

# for debug
# resData = json.dumps({
#     'data': {
#         'url': 'https://namaraii.com/cheatsheet/notion.html'
#     }
# })

dataJson = json.loads(resData)
if dataJson['code'] == 0:
    doc_url = dataJson['data']['url']

    sys.stdout.write(doc_url)
