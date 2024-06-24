def accept(s, cs):
  if len(s) == 0:
    raise Exception("Expected "+cs+", got empty string")
  elif len(s) < len(cs):
    raise Exception("Expected "+cs+", got " + s)
  elif s[:len(cs)] == cs:
    return s[len(cs):]
  else:
    raise Exception("Expected "+cs+", got " + s[:len(cs)])