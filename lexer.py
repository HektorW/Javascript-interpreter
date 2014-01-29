import re, sys

class lexer:
  def __init__(self):
    self._tokens = []

  def addToken(self, name, rgx):
    token = {
      'name': name,
      'regex': rgx,
      'compiled': re.compile(rgx)
    }
    self._tokens.append(token)

  def parse(self, str):
    matched = self.tokenize(str)
    ordered = self.order(matched)
    return ordered;

  def getTokenType(self, str):
    for token in self._tokens:
      rgx = token['compiled']
      if rgx.search(str):
        return token['name']
    return None

  def getToken(self, token_name):
    for token in self._tokens:
      if token['name'] == token_name:
        return token
    return None

  def getTokenValue(self, str, token_name):
    token = self.getToken(token_name)
    if token:
      match = token['compiled'].search(str)
      if match:
        return match.group(0)
    return None


  def tokenize(self, str):
    matches = {}
    for token in self._tokens:
      obj = {
        'name': token['name'],
        'iter': token['compiled'].finditer(str)
      }
      try:
        obj['next'] = next(obj['iter'])
        obj['empty'] = False
      except StopIteration:
        obj['next'] = None
        obj['empty'] = True
      matches[token['name']] = obj
    return matches

  def order(self, matches):
    ordered = []
    while True:
      minval = sys.maxsize
      choosen = None
      for name, obj in matches.items():
        if obj['empty']:
          continue

        match = obj['next']
        if match.start() < minval:
          minval = match.start()
          choosen = name

      if choosen is not None:
        try:
          obj = matches[choosen]
          match = obj['next']
          ordered.append({
            'name': choosen,
            'value': match.group(),
            'start': match.start(),
            'end': match.end(),
            # 'match': match
          })
          obj['next'] = next(obj['iter'])

        except StopIteration:
          obj['empty'] = True

      if len([x for x in matches if not matches[x]['empty']]) == 0:
        break

    return ordered

    

class AST:
  def __init__(self):
    pass