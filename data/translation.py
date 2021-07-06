def translateBoard(json):
  board = [[[] for x  in range(0,9)] for x in range(0,9)]
  squares = json['squares']
  for square in squares:
    col = square['x']
    row = square['y']
    value = square['value']
    board[row][col] = [value]

  return board