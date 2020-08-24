import sys
import unicodedata
import os

from urlparse import urlparse
from enum import IntEnum

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
headers = {"Content-type": "application/json",
           "Referer": referer,
           "Cookie": cookie}

class DocType(IntEnum):
    DOC = 2
    SHEET = 3

    def __str__(self):
        return str(self.value)

ITEM_TYPE_ICONNAME_MAPPING = {
    2: 'doc.png',
    3: 'sheet.png',
}
