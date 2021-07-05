import math
from itertools import chain

def getRowNeighbors(col, row):
  return ((c, row) for c in range(0, 9) if c != col)


def getColumnNeighbors(col, row):
  return ((col, r) for r in range(0, 9) if r != row)

def getCubeNeighbors(col, row):
  r0 = 3 * math.floor(row / 3)
  c0 = 3 * math.floor(col / 3)

  cols = [c0+dc for dc in range(0, 3)]

  r1 = r0
  g1 = ((c, r1) for c in cols if not(r1==row or c==col))

  r2 = r0 + 1
  g2 = ((c, r2) for c in cols if not(r2==row or c==col))

  r3 = r0 + 2
  g3 = ((c, r3) for c in cols if not(r3==row or c==col))

  return chain(g1, g2, g3)

# def getNeighboars(col, row):
#   colNeighbors = getColumnNeighbors(col, row)
#   rowNeighbors = getRowNeighbors(col, row)
#   cubeNeighbors = getCubeNeighbors(col, row)

#   return chain(colNeighbors, rowNeighbors, cubeNeighbors)

# def isValid(board, col, row):
#   neighbors = getNeighboars(col, row)

#   for neighbor in neighbors:
    

# def isColValid(scalarBoard, col):
#   colValues = set()
#   for row in range(0, 9):
#     value = scalarBoard[row][col]
#     if value in colValues:
#       return False

#     colValues.add(value)
  
#   return True

# def isRowValid(scalarBoard, col):
#   colValues = set()
#   for row in range(0, 9):
#     value = scalarBoard[row][col]
#     if value in colValues:
#       return False

#     colValues.add(value)
  
#   return True  


def getCandidateValues(board, col, row):

  candidateValues = set([1,2,3,4,5,6,7,8,9])

  colNeighbors = getColumnNeighbors(col, row)
  rowNeighbors = getRowNeighbors(col, row)
  cubeNeighbors = getCubeNeighbors(col, row)

  allNeighbors = chain(colNeighbors, rowNeighbors, cubeNeighbors)

  for (col, row) in allNeighbors:
    if len(board[row][col]) == 1:
      candidateValues.discard(board[row][col][0])

  return candidateValues

def getBoard(initialValues):
  board = [[[] for x  in range(0,9)] for x  in range(0,9)]
  
  for (col, row) in initialValues:
    board[row][col] = [initialValues[(col, row)]]

  return board
  

def stepBoard(board):
  print(board)

  changed = False
  
  for col in range(0, 9):
    for row in range(0, 9):
      if (len(board[row][col]) != 1):
        print(col, row)
        print(board[row][col])

        previousLen = len(board[row][col])
        previousLen = 9 if previousLen == 0 else previousLen

        board[row][col] = list(getCandidateValues(board, col, row))
        newLen = len(board[row][col])

        # print(board[row][col])
        # print(previousLen, newLen)
        # print()

        changed = newLen < previousLen

  print('changed', changed)
  return changed
  

def printBoard(board):
  for col in range(0, 9):
    for row in range(0, 9):
      print(col, row, board[row][col])


def solveBoard(board):
  # board = getBoard(initialValues)
  changed = stepBoard(board)
  while(changed):
    changed = stepBoard(board)

  printBoard(board)
  # print('changed', changed)
