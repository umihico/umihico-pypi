import codecs as _codecs
import ast as _ast
from pprint import pformat as _pformat


def save_as_txt(filename, data, mode='w'):
    with _codecs.open(filename, mode, 'utf-8') as f:
        f.write(_pformat(data))


def load_from_txt(filename):
    with _codecs.open(filename, 'r', 'utf-8') as f:
        return _ast.literal_eval(f.read())
