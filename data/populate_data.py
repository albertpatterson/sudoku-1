import sys
sys.path.append("..")

import data.fetch as fetch
import data.storage as storage

def addNewBoardData():
  newBoardData = fetch.fetchBoard()

  currentData = storage.getCurrentData()

  currentData['data'].append(newBoardData)

  storage.writeCurrentData(currentData)