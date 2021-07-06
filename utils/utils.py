def printBoard1(board):
  for col in range(0, 9):
    for row in range(0, 9):
      print(col, row, board[row][col])

def printBoard(board):
  for row in range(0, 9):
    s = ' '.join(map(lambda x:str(x), board[row]))
    print(s)
