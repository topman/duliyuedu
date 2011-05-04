# coding: utf-8

def strip_char(s):
    """strip chars
    """
    CHARS_NEED_STRIP = ["*", "\n", "\r"]
    for x in CHARS_NEED_STRIP:
        s = s.replace(x, "")
    return s

fh = open("1.html")
cont = fh.read()
fh.close()

import html2text
cont = html2text.html2text(cont)

import re
pattern = u"(《[^》]*》)"
all = re.findall(pattern, cont)
all = list(set(all))
all = [strip_char(x) for x in all]
for a in all:
    print a
