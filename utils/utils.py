def printBoard(board):
  for col in range(0, 9):
    for row in range(0, 9):
      print(col, row, board[row][col])