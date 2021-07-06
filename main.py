from data.data import getBoards
# from data.populate_data import addNewBoardData
import solver.solver as solver 

# addNewBoardData()

allBoards = getBoards()
board = allBoards[0]
stepped = solver.stepBoard(board)
print(stepped)