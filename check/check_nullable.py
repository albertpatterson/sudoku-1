import neighbors.neighbors as neighbors

def checkCells(board, cells):
  values = set()

  for (col, row) in cells:
    value = board[row][col]
    if value in values:
      return False

    if value != None:
      values.add(value)
  
  return True

def checkColumn(board, col):
  cells = neighbors.getColumnNeighbors(col, 0, True)
  return checkCells(board, cells)

def checkRow(board, row):
  cells = neighbors.getRowNeighbors(0, row, True)
  return checkCells(board, cells)


def checkCube(board, col, row):
  cells = neighbors.getCubeNeighbors(col, row, True)
  return checkCells(board, cells)


def checkCell(board, col, row):
  return checkCube(board, col, row) and checkRow(board, row) and checkColumn(board, col)
