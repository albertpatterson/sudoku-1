def printBoard1(board):
  for col in range(0, 9):
    for row in range(0, 9):
      print(col, row, board[row][col])

def toStr(value):
  return '_' if value == None else str(value)

def printBoard(board):
  for row in range(0, 9):
    s = ' '.join(map(toStr, board[row]))
    print(s)

def toScalarBoard(board):
  scalarBoard = []
  for row in range(0, 9):
    scalarRow = []
    for col in range(0, 9):
      values = board[row][col]
      next = None if len(values) == 0 else values[0]
      scalarRow.append(next)
    scalarBoard.append(scalarRow)

  return scalarBoard