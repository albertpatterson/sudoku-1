import requests

def fetchBoard():
  payload = {'size': '9', 'level': '3'}
  response = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?', params=payload)
  jsonData = response.json()
  return jsonData
