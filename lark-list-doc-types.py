import sys

is_py2 = sys.version_info.major == 2

if is_py2:
  import py2.lark_list_doc_types
else:
  import py3.lark_list_doc_types
