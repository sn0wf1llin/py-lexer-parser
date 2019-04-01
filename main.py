from lexer import lex_process
from myparser import parse_process
import os


def read_file(fname):
    with open(fname, 'r') as f:
        data = f.read()

    return data


def run(code=None, fname=None):
    if code is None and fname is None:
        return None

    elif fname is not None and os.path.isfile(fname):
        code = read_file(fname)

    if code is not None:
        lexres = lex_process(code)
        parseres = parse_process(code)

        return lexres, parseres

    return None, None
