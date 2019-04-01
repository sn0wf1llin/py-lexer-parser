from mynode import Node
from common_data import *
import ply.yacc as yacc


def p_body(p):
    '''body :
            | body line '''

    if len(p) > 1:
        if p[1] is None:
            p[1] = Node('body', [])
        p[0] = p[1].add_parts([p[2]])
    else:
        p[0] = Node('body', [])


def p_line(p):
    '''line : BREAK
            | assign
            | expr
            | inplace_expr
            | condition
            | func LPAR args RPAR'''
    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 5:
        print(p.slice)
        p[0] = Node('func', [p[3]])


def p_func(p):
    '''func : PRINT
            | VAR'''

    p[0] = p[1]


def p_args(p):
    '''args :
            | term
            | term COMMA args'''

    if len(p) == 1:
        p[0] = Node('args', [])

    elif len(p) == 2:
        p[0] = Node('args', [p[1]])

    else:
        p[0] = p[3].add_parts([p[1]])


def p_condition_operator(p):
    '''condition_operator : WHILE
                          | IF'''

    p[0] = Node('condition_operator', [p[1]])

def p_condition(p):
    '''condition : ELSE COLON
                 | condition_operator TRUE COLON
                 | condition_operator fact COLON
                 | IF LPAR fact RPAR COLON'''

    if len(p) == 3:
        p[0] = p[1]

    elif len(p) == 4:
        p[0] = p[1].add_parts([p[2]])

    elif len(p) == 6:
        p[0] = p[1].add_parts([p[3]])


def p_assign(p):
    '''assign : VAR ASSIGN term
              | VAR ASSIGN expr'''
    p[0] = Node('assign', [p[3], p[1]])


def p_term(p):
    '''term : NUMBER
            | VAR
            | DOUBLEQUOTE VAR DOUBLEQUOTE
            | LPAR VAR RPAR
            | LSQUAREBRACKET VAR RSQUAREBRACKET'''

    if len(p) == 2:
        p[0] = Node('term', [p[1]])

    elif len(p) == 4:
        p[0] = Node('term', [p[2]])


def p_inplace_expr(p):
    '''inplace_expr : VAR PLUSEQUAL term
            | VAR MINUSEQUAL term
            | VAR MULTEQUAL term
            | VAR DIVEQUAL term'''

    p[0] = Node('inplace_expr', [p[2], p[1], p[3]])


def p_expr(p):
    '''expr : term
            | term PLUS term
            | term MINUS term
            | term MULT term
            | term DIV term'''

    if len(p) == 2:
        p[0] = Node('expr', [p[1]])
    else:
        p[0] = Node('expr', [p[2], p[1], p[3]])


def p_fact(p):
    '''fact : TRUE
            | FALSE
            | term EQUAL term
            | term GREATEREQUAL term
            | term LESSEQUAL term
            | term LESS term
            | term GREATER term
            | expr LESS expr
            | term EQUAL LPAR expr RPAR
            | term LESS LPAR expr RPAR
            | term GREATER LPAR expr RPAR
            | term LESSEQUAL LPAR expr RPAR
            | term GREATEREQUAL LPAR expr RPAR'''

    if len(p) == 2:
        p[0] = Node('fact', [p[1]])

    elif len(p) == 4:
        p[0] = Node('fact', [p[2], p[1], p[3]])

    elif len(p) == 6:
        p[0] = Node('fact', [p[2], p[1], p[4]])

def p_error(p):
    print("\nPARSER: Unexpected token: <{}>".format(p))


def parse_process(data):
    parser = yacc.yacc()

    return parser.parse(data)
