import sys

is_py2 = sys.version_info.major == 2

if is_py2:
  import py2.lark_search
else:
  import py3.lark_search
