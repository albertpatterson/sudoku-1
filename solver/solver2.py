import solver.utils as utils
import check.check_nullable as check
from solver.prepare import prepareBoard


def solveFromCell(board, scalarBoard, col, row):

  if col==0 and row==8:
    print(col, row)

  values = board[row][col]
  (nextCol, nextRow) = utils.getNextCell(col, row)

  for value in values:
    scalarBoard[row][col] = value

    if not check.checkCell(scalarBoard, col, row):
      continue

    if col == 8 and row == 8:
      return True

    if solveFromCell(board, scalarBoard, nextCol, nextRow):
      return True

  scalarBoard[row][col] = None
  return False

def solveBoard(board):
  prepareBoard(board)
  scalarBoard = [[None for x in range(0, 9)] for y in range(0, 9)]
  solved = solveFromCell(board, scalarBoard, 0, 0)  
  return (solved, scalarBoard)

  