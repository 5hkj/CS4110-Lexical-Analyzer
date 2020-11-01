import ply.lex as lex
import trietable as trie

# 1. keywords/reserved words incl. 7. boolean constant
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

# 8. operators & punctuation
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

# 4. integer constant
t_INTCONSTANT = r'0[xX][0-9a-fA-F]+|[0-9]+(?!\.)'
# 5. double constant
t_DOUBLECONSTANT = r'[0-9]+\.[0-9]*([eE]([+-])?[0-9]+)?'
# 6. string constant
t_STRINGCONSTANT = r'\"(\\.|[^"\\])*\"'

# 3. white spaces
t_ignore_SPACE = r'\s'
t_ignore_TAB = r'\t'
# t_ignore_NEWLINE = r'\n'

# 9. comments
t_ignore_COMMENT = r'\//.*'
t_ignore_BLOCK_COMMENT = r'\/\*(.|\n)*\*\/'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    # check to see if it is a keyword
    t.type = keyword.get(t.value, 'ID')
    return t

def t_NEWLINE(t):
    r'\n'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



lexer = lex.lex()
t = trie.TrieTable()
input  = open("toy_program.txt", "r", encoding='utf-8')
output = open("output.txt", "w", encoding='utf-8')
lexer.input(input.read())
for tok in lexer:
    if tok.type=='NEWLINE':
        output.write("\n")
    else:
        output.write(tok.type.lower() + " ")
        t.searchAndCreateIDs(tok.value)
output.write("\n")
t.printTrieToFile(output)

input.close()
output.close()
