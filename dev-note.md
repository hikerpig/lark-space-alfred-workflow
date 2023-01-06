## Translate py2 code to py3

```sh
rsync -r py2/* py3
2to3 --output-dir=py3 -nw py2
```
