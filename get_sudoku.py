import requests
import json

def getCurrentData():
  with open('sudokus.json', 'r') as file:
    currentData = json.load(file)
    return currentData

def writeCurrentData(newData):
  with open('sudokus.json', 'w') as file:
    print('current', newData)
    json.dump(newData, file)

def getBoard():
  payload = {'size': '9', 'level': '1'}
  response = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?', params=payload)
  jsonData = response.json()
  print(jsonData)

  currentData = getCurrentData()

  currentData['data'].append(jsonData)

  writeCurrentData(currentData)

  # with open('sudokus.json', 'r') as file:
  #   currentData = json.load(file)
  #   print('current', currentData)

  # with open('sudokus.json', 'w') as file:
  #   currentData = json.load(file)
  #   print('current', currentData)

  #   print('new', jsonData)

  #   currentData['data'].append(jsonData)
  #   json.dump(currentData, file)
    

def translateBoard(json):
  board = [[[] for x  in range(0,9)] for x in range(0,9)]
  squares = json['squares']
  for square in squares:
    col = square['x']
    row = square['y']
    value = square['value']
    board[row][col] = [value]

  return board

def writeBoard(json):
  with open('sudokus.json', 'w+') as file:
    current = json.load(file)
    print(current)
    new = json.loads(json)
    allData = current.append(new)
    json.dump(allData, file)
    

