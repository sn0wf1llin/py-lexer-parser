from lexer import lex_process
from parser import parse_process
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
        print(lexres)
        print("-"*33)
        parseres = parse_process(code)
        print("="*33)
        print(parseres)
        print("-"*33)

if __name__ == "__main__":
    run(fname='code_to_analyze.py')


