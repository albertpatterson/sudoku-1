import neighbors.neighbors as neighbors
import math

def checkCells(board, cells):
  values = set()

  for (col, row) in cells:
    value = board[row][col]
    if value in values:
      return False
    values.add(value)
  
  return True

def checkColumn(board, col, memo):

  if memo[col] == None:
    cells = neighbors.getColumnNeighbors(col, 0)
    memo[col] = checkCells(board, cells)

  return memo[col]

def checkRow(board, row, memo):
  if memo[row] == None:
    cells = neighbors.getRowNeighbors(0, row)
    memo[row] = checkCells(board, cells)

  return memo[row]

def getCubeIndex(col, row):
  cubeCol = math.floor(col/3)
  cubeRow = math.floor(row/3)

  return 3*cubeRow + cubeCol

def checkCube(board, col, row, memo):
  cubeIndex = getCubeIndex(col, row)
  if memo[cubeIndex] == None:
    cells = neighbors.getCubeNeighbors(col, row, True)
    memo[cubeIndex] = checkCells(board, cells)

  return memo[cubeIndex]

def checkCell(board, col, row, colMemo, rowMemo, cubeMemo):
  return checkCube(board, col, row, cubeMemo) and checkRow(board, row, rowMemo) and checkColumn(board, col, colMemo)

def checkBoard(board):
  colMemo = [None for x in range(0, 9)]
  rowMemo = [None for x in range(0, 9)]
  cubeMemo = [None for x in range(0, 9)]
  
  for col in range(0, 9):
    for row in range(0, 9):
      if not checkCell(board, col, row, colMemo, rowMemo, cubeMemo):
        return False

  return True