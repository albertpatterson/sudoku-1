from data.data import getBoards
from data.populate_data import addNewBoardData
import solver.solver as solver 
import utils.utils as utils

import time

# addNewBoardData()

allBoards = getBoards()
board = allBoards[-1]

tic = time.perf_counter()
sol = solver.solveBoard(board)
toc = time.perf_counter()
print(f'solved in {toc - tic:0.4f} seconds')

print(sol)
utils.printBoard(sol)