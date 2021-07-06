from data.data import getBoards
from data.populate_data import addNewBoardData
import solver.solver as solver 
import solver.solver2 as solver2 

import utils.utils as utils

import time

# addNewBoardData()

allBoards = getBoards()
board = allBoards[-1]

tic = time.perf_counter()
(solved, sol) = solver2.solveBoard(board)
toc = time.perf_counter()
print(f'solved in {toc - tic:0.4f} seconds')

print(solved)
print(sol)
utils.printBoard(sol)