import data.translation as translation

from testing.utils import compareArrays

def getTestSquares1():
 return [
   {"x": 0, "y": 0, "value": 4}, 
   {"x": 0, "y": 2, "value": 7}, 
   {"x": 0, "y": 3, "value": 1}, 
   {"x": 0, "y": 5, "value": 6}, 
   {"x": 0, "y": 8, "value": 8}, 
   {"x": 1, "y": 2, "value": 5}, 
   {"x": 1, "y": 3, "value": 8}, 
   {"x": 1, "y": 4, "value": 9}, 
   {"x": 1, "y": 5, "value": 7}, 
   {"x": 1, "y": 6, "value": 1},
   {"x": 2, "y": 0, "value": 1}, 
   {"x": 2, "y": 1, "value": 9}, 
   {"x": 2, "y": 5, "value": 2}, 
   {"x": 2, "y": 6, "value": 6}, 
   {"x": 3, "y": 0, "value": 9}, 
   {"x": 3, "y": 1, "value": 1}, 
   {"x": 3, "y": 5, "value": 5}, 
   {"x": 3, "y": 7, "value": 4}, 
   {"x": 3, "y": 8, "value": 6}, 
   {"x": 4, "y": 1, "value": 4}, 
   {"x": 4, "y": 3, "value": 3}, 
   {"x": 4, "y": 5, "value": 9},
   {"x": 4, "y": 6, "value": 7},
   {"x": 4, "y": 8, "value": 1}, 
   {"x": 5, "y": 1, "value": 5}, 
   {"x": 5, "y": 2, "value": 3}, 
   {"x": 5, "y": 3, "value": 6}, 
   {"x": 5, "y": 7, "value": 8}, 
   {"x": 6, "y": 0, "value": 6}, 
   {"x": 6, "y": 3, "value": 5}, 
   {"x": 6, "y": 4, "value": 4}, 
   {"x": 6, "y": 6, "value": 8}, 
   {"x": 7, "y": 0, "value": 5},
   {"x": 7, "y": 1, "value": 8}, 
   {"x": 7, "y": 4, "value": 6}, 
   {"x": 7, "y": 7, "value": 1}, 
   {"x": 7, "y": 8, "value": 7}, 
   {"x": 8, "y": 3, "value": 9}, 
   {"x": 8, "y": 4, "value": 7}, 
   {"x": 8, "y": 5, "value": 8}, 
   {"x": 8, "y": 6, "value": 4},
   ]

def test_translateBoard_1():
  squares = getTestSquares1()
  json = {"squares": squares}

  expected = [
    [[4],  [], [1], [9],  [],  [], [6], [5],  []],
    [ [],  [], [9], [1], [4], [5],  [], [8],  []],
    [[7], [5],  [],  [],  [], [3],  [],  [],  []],
    [[1], [8],  [],  [], [3], [6], [5],  [], [9]],
    [ [], [9],  [],  [],  [],  [], [4], [6], [7]],
    [[6], [7], [2], [5], [9],  [],  [],  [], [8]],
    [ [], [1], [6],  [], [7],  [], [8],  [], [4]],
    [ [],  [],  [], [4],  [], [8],  [], [1],  []],
    [[8],  [],  [], [6], [1],  [],  [], [7],  []],
  ]

  actual = translation.translateBoard(json)

  assert len(actual) == 9

  for row in range(0,9):
    print('actual  ',actual[row])
    print('expected',expected[row])

    compareArrays(actual[row], expected[row])
    