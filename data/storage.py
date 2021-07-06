import json

def getCurrentData():
  with open('data/sudokus.json', 'r') as file:
    currentData = json.load(file)
    return currentData

def writeCurrentData(newData):
  with open('data/sudokus.json', 'w') as file:
    print('current', newData)
    json.dump(newData, file)