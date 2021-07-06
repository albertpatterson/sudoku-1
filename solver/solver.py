import sys
sys.path.append("..")

from itertools import chain
import neighbors.neighbors as neighbors

def getCandidateValues(board, col, row):

  candidateValues = set([1,2,3,4,5,6,7,8,9])

  colNeighbors = neighbors.getColumnNeighbors(col, row)
  rowNeighbors = neighbors.getRowNeighbors(col, row)
  cubeNeighbors = neighbors.getCubeNeighbors(col, row)

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
