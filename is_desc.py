def isDescending(data):
  for i in range(len(data)-1):
    if data[i] < data[i+1]:
      return False
  return True
