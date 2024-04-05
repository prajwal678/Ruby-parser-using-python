import ply.lex as lex

tokens = (
    'DEF',
    'END',
    'IDENTIFIER',
    'EQUALS',
    'COMMA',
    'LBRACE',
    'RBRACE',
    'COLON',
    'CASE',
    'WHEN',
    'ELSE',
    'WHILE',
    'DO',
    'LPAREN',
    'RPAREN',
    'INTEGER',
    'FLOAT',
    'LT',
    'GT',
    'LE',
    'GE',
    'EQ',
    'NE',
    'STRING',
    'PUTS',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'TRUE',
    'FALSE'
)

# Simple token rules
t_EQUALS = r'='
t_COMMA = r','
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

def t_DO(t):
    r'do'
    return t

def t_DEF(t):
    r'def'
    return t

def t_END(t):
    r'end'
    return t

def t_CASE(t):
    r'case'
    return t

def t_WHEN(t):
    r'when'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_PUTS(t):
    r'puts'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remove the double quotes
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Ignored characters
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()