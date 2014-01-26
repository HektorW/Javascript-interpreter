from lexer import lexer
import json

str = 'x=1+2;'
# batman = "Array(5).join(+{})+'\u0061 \u0042\u0061\u0074\u006d\u0061\u006e'"

l = lexer()

l.addToken('IDENTIFIER', r'[A-z\_\$]+[A-z0-9\_\$]*')
l.addToken('NUMBER', r'[0-9]+') # only integers
l.addToken('OPERATOR', r'[\+\*\-\/\=]')
l.addToken('SEMICOLON', r';')

tokens = l.parse(str)

print(json.dumps(tokens, indent=2))