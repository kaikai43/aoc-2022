place = 1
maxPlace = -1
cumSum = 0
max = 0

with open('./day1/input.txt') as f:
  for line in f:
    if line.strip('\n') == "" or not line:
      if max < cumSum:
        max = cumSum
        maxPlace = place
      cumSum = 0
      place += 1
    else:
      cumSum += int(line.strip('\n'))

print(place, max)
