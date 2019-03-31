import ply.lex as lex
from ply.lex import TOKEN
import re
from common_data import *
from mytoken import MyToken


# it is an required variable
t_ignore = ' \r\n\t\f'


# error name in lowercase (!) because of a name convention
def t_error(t):
    r''
    print("\tIllegal character <{}>".format(t.value[0]))
    t.lexer.skip(1)


def t_COMMENT(t):
    # ignoring comments ; \043 is '#'
    r'[ ]*\043[^\n]*'  # ; otherwise PLY thinks it's an re comment
    pass


def t_TRUE(t):
    r'True'
    return  t


def t_FALSE(t):
    r'False'
    return  t


def t_AND(t):
    r'and'
    return t


def t_OR(t):
    r'or'
    return t


def t_NOT(t):
    r'not'
    return t


def t_CLASS(t):
    r'class'
    return t


def t_DEF(t):
    r'def'
    return t


def t_BREAK(t):
    r'break'
    return t


def t_CONTINUE(t):
    r'continue'
    return t


def t_IF(t):
    r'if'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_ELIF(t):
    r'elif'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_FOR(t):
    r'or'
    return t


def t_IMPORT(t):
    r'import'
    return t


def t_FROM(t):
    r'from'
    return t


def t_IN(t):
    r'in'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_PRINT(t):
    r'print'
    return t


def t_VAR(t):
    r'\w+'
    # value == something that was found with regular expr
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)  # value == smth that was found with regulat expr
    return t


def lex_process(data):
    lexer = lex.lex(reflags=re.UNICODE | re.DOTALL)
    result = []
    lexer.input(data)

    while True:
        try:
            tok = lexer.token()
            if not tok:
                break

            result.append(MyToken(tok))

        except Exception as e:
            break

    return result