from nltk.tree import *

def prints(s):
  print(s, end='')

def in_order_aux(t, c):
  res, list = Tree(t.label(), []), []
  for child in t:
    if type(child) is Tree:
      sub, c, l = in_order_aux(child, c)
      list += l
      res.append(sub)
    else:
      list.append(child)
      res.append(c)
      c += 1
  return res, c, list

def in_order(t):
  t, _, l = in_order_aux(t, 0)
  t.pretty_print(l)
  return t

def act(t):
  for child in t:
    if type(child) is Tree:
      act(child)
    else:
      if type(child) is str and (child[0], child[-1]) == ('{', '}'):
        exec(child[1:-1])