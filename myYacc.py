import ply.yacc as yacc
import myLex

tokens = myLex.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE'),
)

def p_block(p):
    '''
    block : construct block
          | construct
    '''
    p[0] = ('block', p[1], p[2] if len(p) > 2 else None)

def p_construct(p):
    '''
    construct : function_definition
              | variable_declaration
              | hash_definition
              | case_statement
              | while_loop
              | puts_statement
    '''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_expression(p):
    '''
    expression : term
               | expression term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('expression', '+', p[1], p[2])

def p_term(p):
    '''
    term : IDENTIFIER
         | INTEGER
         | FLOAT
         | TRUE
         | FALSE  
         | STRING
         | PLUS
         | MINUS
         | TIMES
         | DIVIDE
         | EQUALS
    '''
    p[0] = ('term', p[1], p.slice[1].type)


def p_variable_declaration(p):
    '''variable_declaration : IDENTIFIER EQUALS expression
                            | IDENTIFIER EQUALS hash_definition
    '''
    p[0] = ('variable_declaration', p[1], p[3])

def p_function_definition(p):
    'function_definition : DEF IDENTIFIER LPAREN parameter_list RPAREN block END'
    p[0] = ('function_definition', p[2], p[4], p[6])

def p_parameter_list(p):
    '''
    parameter_list : IDENTIFIER COMMA parameter_list
                   | IDENTIFIER
                   | empty
    '''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_hash_definition(p):
    'hash_definition : LBRACE key_value_pairs RBRACE'
    p[0] = ('hash_definition', p[2])

def p_key_value_pairs(p):
    '''
    key_value_pairs : key_value_pair COMMA key_value_pairs
                    | key_value_pair
    '''
    p[0] = ('key_value_pairs', p[1])

def p_key_value_pair(p):
    '''key_value_pair : IDENTIFIER COLON expression
                      | STRING EQUALS GT expression
                      | IDENTIFIER EQUALS GT expression
    '''
    p[0] = ('key_value_pair', p[1], p[3])

def p_case_statement(p):
    'case_statement : CASE IDENTIFIER case_clause else_clause END'
    p[0] = ('switch_statement', p[2], p[3], p[4])

def p_case_clause(p):
    '''case_clause : WHEN expression block
                   | case_clause WHEN expression block'''
    if len(p) == 4:
        p[0] = ('case_clause', p[2], p[3])
    else:
        p[0] = ('nested_case_clause', p[1], p[3], p[4])

def p_else_clause(p):
    'else_clause : ELSE block'
    p[0] = ('else_clause', p[2])

def p_while_loop(p):
    'while_loop : WHILE expression DO block END'
    p[0] = ('while_loop', p[2], p[4])

def p_puts_statement(p):
    '''puts_statement : PUTS STRING
                      | PUTS IDENTIFIER'''
    p[0] = ('puts_statement', p[2])

# Add more grammar rules here

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' in line {p.lineno}, position {p.lexpos}")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()

print("Enter your code (type '\\' on a new line to finish):")
while True:
    lines = []
    while True:
        line = input()
        if line.strip() == "\\":
            break
        lines.append(line)
    code = "\n".join(lines)

    result = parser.parse(code)
    print(result)

    # Condition to exit the outer loop
    exit_condition = input("Do you want to continue? (y/n): ")
    if exit_condition.lower() == 'n':
        break
