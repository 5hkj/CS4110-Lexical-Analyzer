import ply.lex as lex

keyword = {
    'boolean':    'BOOLEAN',
    'break':      'BREAK',
    'class':      'CLASS',
    'double':     'DOUBLE',
    'else':       'ELSE',
    'extends':    'EXTENDS',
    'false':      'BOOLEANCONSTANT',
    'for':        'FOR',
    'if':         'IF',
    'implements': 'IMPLEMENTS',
    'int':        'INT',
    'interface':  'INTERFACE',
    'new':        'NEW',
    'newarray':   'NEWARRAY',
    'null':       'NULL',
    'println':    'PRINTLN',
    'readln':     'READLN',
    'return':     'RETURN',
    'string':     'STRING',
    'this':       'THIS',
    'true':       'BOOLEANCONSTANT',
    'void':       'VOID',
    'while':      'WHILE'
}

tokens = [
            'PLUS', 'MINUS', 'MULT', 'DIV', 'MOD', 'LESS', 'LESSEQUAL',
            'GREATER', 'GREATEREQUAL', 'EQUAL', 'NOTEQUAL', 'AND',
            'OR', 'NOT', 'ASSIGN', 'SEMICOLON', 'COMMA', 'PERIOD',
            'LEFTPAREN', 'RIGHTPAREN', 'LEFTBRACKET', 'RIGHTBRACKET',
            'LEFTBRACE', 'RIGHTBRACE', 'INTCONSTANT', 'DOUBLECONSTANT',
            'STRINGCONSTANT', 'ID', 'NEWLINE'
         ] + list(keyword.values())

# operators
t_PLUS         = r'\+'
t_MINUS        = r'\-'
t_MULT         = r'\*'
t_DIV          = r'\/'
t_MOD          = r'\%'
t_LESS         = r'\<'
t_LESSEQUAL    = r'\<='
t_GREATER      = r'\>'
t_GREATEREQUAL = r'\>='
t_EQUAL        = r'\=='
t_NOTEQUAL     = r'\!='
t_AND          = r'\&&'
t_OR           = r'\|\|'
t_NOT          = r'\!'
t_ASSIGN       = r'\='
t_SEMICOLON    = r'\;'
t_COMMA        = r'\,'
t_PERIOD       = r'\.'
t_LEFTPAREN    = r'\('
t_RIGHTPAREN   = r'\)'
t_LEFTBRACKET  = r'\['
t_RIGHTBRACKET = r'\]'
t_LEFTBRACE    = r'\{'
t_RIGHTBRACE   = r'\}'

t_INTCONSTANT = r'0[xX][0-9a-fA-F]+|[0-9]+(?!\.)'
t_DOUBLECONSTANT = r'[0-9]+\.[0-9]*([eE]([+-])?[0-9]+)?'
t_STRINGCONSTANT = r'\"(\\.|[^"\\])*\"'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = keyword.get(t.value, 'ID')
    return t

def t_NEWLINE(t):
    r'\n'
    return t

t_ignore_SPACE = r'\s'
t_ignore_TAB = r'\t'
# t_ignore_NEWLINE = r'\n'
t_ignore_COMMENT = r'\//.*'
t_ignore_BLOCK_COMMENT = r'\/\*(.|\n)*\*\/'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



lexer = lex.lex()
file = open("toy_program.txt", "r", encoding='utf-8')
lexer.input(file.read())
for tok in lexer:
    if tok.type=='NEWLINE':
        print()
    else:
        print(tok.type.lower(), end=" ")
