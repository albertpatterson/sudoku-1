import math
from itertools import chain

def getRowNeighbors(col, row, includeAll=False):
  return ((c, row) for c in range(0, 9)) if includeAll else ((c, row) for c in range(0, 9) if c != col)


def getColumnNeighbors(col, row, includeAll=False):
  return ((col, r) for r in range(0, 9)) if includeAll else ((col, r) for r in range(0, 9) if r != row)

def getCubeNeighbors(col, row, includeAll=False):
  r0 = 3 * math.floor(row / 3)
  c0 = 3 * math.floor(col / 3)

  cols = [c0+dc for dc in range(0, 3)]

  r1 = r0
  g1 = ((c, r1) for c in cols) if includeAll else ((c, r1) for c in cols if not(r1==row or c==col))

  r2 = r0 + 1
  g2 = ((c, r2) for c in cols) if includeAll else ((c, r2) for c in cols if not(r2==row or c==col))

  r3 = r0 + 2
  g3 = ((c, r3) for c in cols) if includeAll else ((c, r3) for c in cols if not(r3==row or c==col))

  return chain(g1, g2, g3)
