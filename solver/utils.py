def getCandidateCounts(board):
  total = 1

  counts = [];
  for row in range(0, 9):
    rowCounts = []
    for col in range(0, 9):
      count = len(board[row][col])
      total = total*count
      rowCounts.append(count)
      print(count)
    counts.append(rowCounts)

  print('total', total)
  return counts

def getNextCell(col, row):
  if(col==8):
    return (0, row+1)

  return (col+1, row)

def getPreviousCell(col, row):
  if(col==0):
    return (8, row-1)

  return (col-1, row)

def incrementCandidateIndices(candidateCounts, candidateIndices, digitColIndex=8, digitRowIndex=8):
  currentCellIndex = candidateIndices[digitRowIndex][digitColIndex]
  currentCellIndexMax = candidateCounts[digitRowIndex][digitColIndex]-1
  if currentCellIndex == currentCellIndexMax:

    candidateIndices[digitRowIndex][digitColIndex] = 0
    (previousDigitColIndex, previousDigitRowIndex) = getPreviousCell(digitColIndex, digitRowIndex)

    # print(previousDigitColIndex, previousDigitRowIndex)
    incrementCandidateIndices(candidateCounts, candidateIndices, previousDigitColIndex, previousDigitRowIndex)
  else:
    candidateIndices[digitRowIndex][digitColIndex] += 1
  

def getScalarBoard(board, candidateIndices):
  scalarBoard = []
  for row in range(0, 9):
    scalarRow = []
    for col in range(0, 9):
      index = candidateIndices[row][col]
      try:
        candidates = board[row][col]
        value = candidates[index]
      except Exception:
        print('error')
        
      scalarRow.append(value)
    scalarBoard.append(scalarRow)

  return scalarBoard

def getScalarBoardNullable(board, candidateIndices):
  scalarBoard = []
  for row in range(0, 9):
    scalarRow = []
    for col in range(0, 9):
      index = candidateIndices[row][col]
      try:
        candidates = board[row][col]
        value = None if index == None else candidates[index]
      except Exception:
        print('error')
        
      scalarRow.append(value)
    scalarBoard.append(scalarRow)

  return scalarBoard

