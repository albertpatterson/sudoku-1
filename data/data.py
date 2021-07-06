import sys
sys.path.append("..")

import data.storage as storage
import data.translation as translation

def doTranslation(json):
  return translation.translateBoard(json)

def getBoards():
  allBoardData = storage.getCurrentData()['data']
  allData = list(map(doTranslation, allBoardData))
  return allData

