import sudoku
from testing.utils import compareArrays
# def compareArrays(actual, expected):
#   assert len(expected) == len(actual)
  
#   for pair in zip(actual, expected):
#     assert pair[0] == pair[1]


def test_getRowNeighbors_0_0():
  actual = list(sudoku.getRowNeighbors(0, 0))  
  expected = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
  compareArrays(actual, expected)


def test_getRowNeighbors_3_7():
  actual = list(sudoku.getRowNeighbors(3, 7))  
  expected = [(0, 7), (1, 7), (2, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)]
  compareArrays(actual, expected)

def test_getColumnNeighbors_0_0():
  actual = list(sudoku.getColumnNeighbors(0, 0))  
  expected = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]
  compareArrays(actual, expected)


def test_getColumnNeighbors_8_5():
  actual = list(sudoku.getColumnNeighbors(8, 5))  
  expected = [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 6), (8, 7), (8, 8)]
  compareArrays(actual, expected)


def test_getCubeNeighbors_0_0():
  actual = list(sudoku.getCubeNeighbors(0,0))  
  expected = [(1,1),(2,1),(1,2),(2,2)]
  compareArrays(actual, expected) 


def test_getCubeNeighbors_8_3():
  actual = list(sudoku.getCubeNeighbors(8,3))  
  expected = [(6, 4),(7, 4),(6, 5),(7, 5)]
  compareArrays(actual, expected) 

#    0 1 2 3 4 5 6 7 8
#-----------------------
# 0| _ _ _ _ 1 _ _ 7 _
# 1| _ _ _ _ _ _ _ _ _
# 2| 2 _ 5 _ _ _ _ _ _
# 3| _ _ _ _ _ _ _ _ _
# 4| _ _ _ _ _ _ _ _ _
# 5| 3 _ _ _ _ _ _ _ _
# 6| _ _ _ _ _ _ _ _ _
# 7| _ _ _ _ _ _ _ _ _
# 8| _ _ _ _ _ _ _ _ _
def getTestBoard1():
  return sudoku.getBoard({
    (4, 0):1,
    (7, 0):7,
    (0, 2):2,
    (2, 2):5,
    (0, 5): 3,
    })

def test_getCandidateValues_1_1():
  board = getTestBoard1()

  actual = sudoku.getCandidateValues(board, 0, 0)
  expected = [4, 6, 8, 9]
  compareArrays(actual, expected) 

def test_getCandidateValues_1_2():
  board = getTestBoard1()

  actual = sudoku.getCandidateValues(board, 8, 0)
  expected = [2,3,4,5,6,8,9]
  compareArrays(actual, expected) 

def test_getCandidateValues_1_3():
  board = getTestBoard1()

  actual = sudoku.getCandidateValues(board, 3,3)
  expected = [1,2,3,4,5,6,7,8,9]
  compareArrays(actual, expected)   




#    0 1 2 3 4 5 6 7 8
#-----------------------
# 0| _ _ _ _ _ _ _ 2 1
# 1| _ 9 6 _ 5 _ _ _ _
# 2| _ _ _ _ _ _ _ _ _
# 3| _ _ _ 5 _ _ 9 1 _
# 4| _ _ _ 7 _ _ _ _ _
# 5| _ _ _ _ _ _ _ _ _
# 6| _ 5 _ _ _ 8 _ 7 _
# 7| _ _ 8 _ _ _ 1 _ _
# 8| _ _ _ _ _ _ _ _ _
def getTestBoard2():
  return sudoku.getBoard({
    (7, 0):2,
    (8, 0):1,
    (1, 1):9,
    (2, 1):6,
    (4, 1):5,
    (3, 3):5,
    (6, 3):9,
    (7, 3):1,
    (3, 4):7,
    (1, 6):5,
    (5, 6):8,
    (7, 6):7,
    (2, 7):8,
    (6, 7):1,
    })

def test_getCandidateValues_2_1():
  board = getTestBoard2()

  actual = sudoku.getCandidateValues(board, 0, 0)
  expected = [3,4,5,7,8]
  compareArrays(actual, expected) 

def test_getCandidateValues_2_2():
  board = getTestBoard2()

  actual = sudoku.getCandidateValues(board, 5, 5)
  expected = [1,2,3,4,6,9]
  # expected = [1,2,3,4,5,6,7,8,9]
  compareArrays(actual, expected)  

def test_getCandidateValues_2_3():
  board = getTestBoard2()

  actual = sudoku.getCandidateValues(board, 6, 5)
  expected = [2,3,4,5,6,7,8]
  compareArrays(actual, expected)     


def test_getCandidateValues_2_4():
  board = getTestBoard2()

  actual = sudoku.getCandidateValues(board, 8, 1)
  expected = [3,4,7,8]
  compareArrays(actual, expected)   


#    0 1 2 3 4 5 6 7 8
#-----------------------
# 0| _ _ _ _ _ _ _ 2 1
# 1| _ 9 6 _ 5 _ _ _ _
# 2| _ _ _ _ _ _ _ _ _
# 3| _ _ _ 5 _ _ 9 1 _
# 4| _ _ _ 7 _ _ 6 _ _
# 5| _ _ _ _ _ _ _ _ _
# 6| _ 5 _ _ _ 8 _ 7 _
# 7| _ _ 8 _ _ _ 1 _ _
# 8| _ _ _ _ _ _ _ 3 2
def getTestBoard3():
  return sudoku.getBoard({
    (7, 0):2,
    (8, 0):1,
    (1, 1):9,
    (2, 1):6,
    (4, 1):5,
    (3, 3):5,
    (6, 3):9,
    (7, 3):1,
    (3, 4):7,
    (6, 4):6,
    (1, 6):5,
    (5, 6):8,
    (7, 6):7,
    (2, 7):8,
    (6, 7):1,
    (7, 8):3,
    (8, 8):2,
    })


# def test_stepBoard():
#   board = getTestBoard3()
#   sudoku.solveBoard(board)
#   assert False