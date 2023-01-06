# coding=utf-8

import http.client
import json
import urllib.request, urllib.parse, urllib.error
import sys

from .searchresult import SearchResult
from .lark_common import cookie, common_headers, parsedLarkDomain, unicodeAlfredQuery, cookie, referer, DocType

def build_create_payload(doc_type):
    data = {
        'parent_token': '',
        'type': doc_type,
        'name': '',
    }

    return urllib.parse.urlencode(data)

doc_type = DocType.DOC
try:
    doc_type = int(unicodeAlfredQuery)
except Exception as e:
    doc_type = DocType.DOC

payload = build_create_payload(doc_type)
headers = dict(common_headers)
headers.update({
    "Content-type": "application/x-www-form-urlencoded",
})

conn = http.client.HTTPSConnection(parsedLarkDomain.netloc)
conn.request("POST", "/space/api/explorer/create/",
             build_create_payload(unicodeAlfredQuery), headers)
response = conn.getresponse()

resData = response.read()
conn.close()

dataJson = json.loads(resData)
if dataJson['code'] == 0:
    doc_url = dataJson['data']['url']

    sys.stdout.write(doc_url)
