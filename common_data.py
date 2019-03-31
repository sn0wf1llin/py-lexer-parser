import re

tokens_literals = (
    'and', 'or', 'not', 'class', 'break', 'continue',
    'if', 'else', 'elif', 'while', 'for',
    'import', 'from', 'in',
    'return', 'print'
)

# 'MODULE', 'SUBMODULE',
tokens = tuple([i.upper() for i in tokens_literals]) + (
    'VAR', 'EQUAL', 'NOTEQUAL', 'LESSEQUAL', 'GREATEREQUAL', 'PLUSEQUAL', 'DEF',
    'MINUSEQUAL', 'MULTEQUAL', 'DIVEQUAL', 'MODEQUAL', 'COLON', 'COMMA', 'SEMICOLON', 'PLUS', 'MINUS', 'MULT', 'DIV',
    'AMPER', 'LESS', 'GREATER', 'DOT', 'MOD', 'BACKQUOTE', 'NUMBER', 'ASSIGN', 'DOUBLEQUOTE',
    'LPAR', 'RPAR', 'LBRACE', 'RBRACE', 'LSQUAREBRACKET', 'RSQUAREBRACKET', 'FALSE', 'TRUE')

t_EQUAL = r'\=='
t_ASSIGN = r'\='
t_NOTEQUAL = r'\!='
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_MULTEQUAL = r'\*='
t_DIVEQUAL = r'\/='
t_MODEQUAL = r'%='
t_COLON = r':'
t_COMMA = r','
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_AMPER = r'&'
t_LESS = r'<'
t_GREATER = r'>'
t_DOT = r'\.'
t_MOD = r'%'
t_BACKQUOTE = r'`'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'
t_DOUBLEQUOTE = r'\"'
