from lexer import lexer
import json
import token_definitions

str = 'x=1+2;'
# batman = "Array(5).join(+{})+'\u0061 \u0042\u0061\u0074\u006d\u0061\u006e'"

l = lexer()

l.addToken('IDENTIFIER', token_definitions.IDENTIFIER)
l.addToken('NUMBER', token_definitions.NUMBER) # only integers
l.addToken('OPERATOR', token_definitions.OPERATOR)

tokens = l.parse(str)

print(json.dumps(tokens, indent=2))