import sys
import unicodedata
import os

from urlparse import urlparse

# config
session = os.environ['session']
larkDomain = os.environ['larkDomain']

cookie = "session={}".format(session)

parsedLarkDomain = urlparse(larkDomain)
larkDriveHome = "https://{}/drive/home/".format(parsedLarkDomain.netloc)


# Get query from Alfred
try:
    alfredQuery = str(sys.argv[1])
except Exception, e:
    alfredQuery = ''
unicodeAlfredQuery = unicodedata.normalize('NFC', alfredQuery.decode('utf-8', 'ignore'))

referer = larkDriveHome

# Call Space api
common_headers = {"Content-type": "application/json",
           "User-Agent": "lark-space-alfred-workflow",
           "Referer": referer,
           "Cookie": cookie}

class DocType:
    DOC = 2
    DOCX = 22
    SHEET = 3
    BITABLE = 8
    MINDNOTE = 11

ITEM_TYPE_ICONNAME_MAPPING = {
    2: 'doc.png',
    22: 'docx.png',
    3: 'sheet.png',
    8: 'bitable.png',
    11: 'mindnote.png',
}
