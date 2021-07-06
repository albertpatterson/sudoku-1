import sys
sys.path.append("..")

from testing.utils import compareArrays
import neighbors.neighbors as neighbors


def test_getRowNeighbors_0_0():
  actual = list(neighbors.getRowNeighbors(0, 0))  
  expected = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
  compareArrays(actual, expected)


def test_getRowNeighbors_3_7():
  actual = list(neighbors.getRowNeighbors(3, 7))  
  expected = [(0, 7), (1, 7), (2, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)]
  compareArrays(actual, expected)

def test_getColumnNeighbors_0_0():
  actual = list(neighbors.getColumnNeighbors(0, 0))  
  expected = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]
  compareArrays(actual, expected)


def test_getColumnNeighbors_8_5():
  actual = list(neighbors.getColumnNeighbors(8, 5))  
  expected = [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 6), (8, 7), (8, 8)]
  compareArrays(actual, expected)


def test_getCubeNeighbors_0_0():
  actual = list(neighbors.getCubeNeighbors(0,0))  
  expected = [(1,1),(2,1),(1,2),(2,2)]
  compareArrays(actual, expected) 


def test_getCubeNeighbors_8_3():
  actual = list(neighbors.getCubeNeighbors(8,3))  
  expected = [(6, 4),(7, 4),(6, 5),(7, 5)]
  compareArrays(actual, expected) 