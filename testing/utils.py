def compareArrays(actual, expected):
  assert len(expected) == len(actual)
  
  for pair in zip(actual, expected):
    assert pair[0] == pair[1]
