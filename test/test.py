from '../lexer' import lexer

def testNumbers():
  l = lexer();
  l.addToken('NUMBER', r'(?:[0-9]+)')
  l.tokenize('1')