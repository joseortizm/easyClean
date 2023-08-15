import re


def test(n):
    msg = 'your test is '+n
    return msg


def rex(txt):
    txt = ' '.join(re.sub('(@[A-Za-z0-9]+)', ' ', txt).split())
    txt = ' '.join(re.sub('[\.\,\«\»\!\¡\[\]\_\{\}\`\~\?\<\>\/\¿\:\;\@\&\$\%\#\+\^\-\=\)\(\*]', ' ',txt).split())
    #txt = ' '.join(re.sub('[\:D\:)\:(\:-)\;-)\:<})\:-||\:-(\:-))\:-*\:-P~\:-O\:-o\:-0\:-|\:-\:-/\=:O\=:o\=:0]', ' ',txt).split())
    #txt = ' '.join(re.sub('[\:D]', ' ',txt).split())
    #txt = ' '.join(re.sub('(\s?[A-Z])', ' ', txt).split())
    #txt = ' '.join(re.sub('([a-z]\s)', ' ', txt).split())
    txt = ' '.join(re.sub('(\s[A-Z]\s)', ' ', txt).split())#
    txt = ' '.join(re.sub('(\s[a-z]\s)', ' ', txt).split())
    txt = ' '.join(re.sub('(\s[a-zA-Z0-9]\s)', ' ', txt).split())
    txt = ' '.join(re.sub('(\s[A-Z]\s)', ' ', txt).split())
    #txt = ' '.join(re.sub('(\s[a-z]\s)', ' ', txt).split())
    txt.strip()
    return txt
#emoticons son quitados por la linea 2 de simbolos





