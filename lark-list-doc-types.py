#coding:utf-8
import sys
import json

from lark_common import unicodeAlfredQuery, DocType, ITEM_TYPE_ICONNAME_MAPPING

items = {
    'items': [
        {
            'title': 'Create new Docs',
            'arg': DocType.DOC,
            'icon': {
                'path': "itemicons/" + ITEM_TYPE_ICONNAME_MAPPING.get(DocType.DOC)
            }
        },
        {
            'title': 'Create new Docx',
            'arg': DocType.DOCX,
            'icon': {
                'path': "itemicons/" + ITEM_TYPE_ICONNAME_MAPPING.get(DocType.DOCX)
            }
        },
        {
            'title': 'Create new Sheets',
            'arg': DocType.SHEET,
            'icon': {
                'path': "itemicons/" + ITEM_TYPE_ICONNAME_MAPPING.get(DocType.SHEET)
            }
        },
        {
            'title': 'Create new Mindnotes',
            'arg': DocType.MINDNOTE,
            'icon': {
                'path': "itemicons/" + ITEM_TYPE_ICONNAME_MAPPING.get(DocType.MINDNOTE)
            }
        },
        {
            'title': 'Create new Bitable',
            'arg': DocType.BITABLE,
            'icon': {
                'path': "itemicons/" + ITEM_TYPE_ICONNAME_MAPPING.get(DocType.BITABLE)
            }
        },
    ]
}
items_json = json.dumps(items)

print(items_json)
