import re as _re


def exact_jp(string):
    _jponly = _re.compile('[亜-熙ぁ-んァ-ヶ]')
    return ''.join(_jponly.findall(string))


def exact_letters(string):
    _letters_only = _re.compile('[亜-熙ぁ-んァ-ヶa-zA-Z0-9]')
    return ''.join(_letters_only.findall(string))


def numberize(string):
    return _re.sub(r'\D', '', string)


def numberize_int(string):
    return int(numberize(string))
