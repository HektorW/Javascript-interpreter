import imp

token_definitions = imp.load_source('token_definitions', '../token_definitions.py')
lexer = imp.load_source('lexer', '../lexer.py').lexer

def testNumbers():
  l = lexer();
  l.addToken('NUMBER', token_definitions.NUMBER)

  def test(input, expected):
    assert(l.tokenize(input)['NUMBER']['next'].group(0) == expected)

  test('1', '1')
  test('2', '2')

  print('# All Number tests passed')


testNumbers()
