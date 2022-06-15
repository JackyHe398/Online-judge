def getMin3(data):
  if len(data) < 3:
    print("NA")
    return
  min = data[:3]
  min.sort()
  for i in data[3:]:
    if min[0] > i:
      min[2], min[1], min[0] = min[1], min[0], i
    elif min[1] > i:
      min[2], min[1] = min[1], i
    elif min[2] > i:
      min[2] = i
  print(min[2])
