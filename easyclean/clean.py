import re


def test(n):
    msg = 'your test is '+n
    return msg


def rex(txt):
    txt = ' '.join(re.sub("(@[A-Za-z0-9]+)", " ", txt).split())
    txt.strip()
    return txt






