import sys
from itertools import cycle
if __name__ == '__main__':
 t="51,7,,50,10,,49,11,,48,13,,48,13,4,3,,48,12,1,11,,48,25,,49,25,,34,8,8,25,,32,10,10,22,,29,13,11,21,,29,13,10,20,,23,24,4,7,2,10,,19,38,,16,40,,14,44,,13,46,,12,48,,11,49,,10,51,,10,52,,9,13,3,15,3,19,,9,10,3,4,2,9,2,4,2,17,,9,10,1,8,1,6,2,8,1,16,,10,8,1,9,1,6,1,9,2,15,,10,8,1,10,1,5,1,10,1,15,,10,8,1,10,1,5,1,10,1,15,,8,10,1,10,1,5,1,10,1,17,,7,11,1,9,1,6,1,10,1,19,,6,13,1,8,1,7,2,7,2,20,,5,16,6,11,7,22,,4,63,,4,63,,4,63,,4,63,,5,61,,6,59,,7,58,,8,56,,9,53,,12,48,,16,39"
 c = cycle([' ', '*'])
 for g in t.split(','):
  if g == '':
   print ''
   continue
  d = next(c)
  sys.stdout.write(d * int(g))