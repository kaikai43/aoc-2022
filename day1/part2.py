topCal = 0
secondCal = 0
thirdCal = 0

cumSum = 0

with open('./day1/input.txt') as f:
  for line in f:
    if line.strip('\n') == "" or not line:
      if cumSum > topCal:
        tmp = topCal
        topCal = cumSum
        thirdCal = secondCal
        secondCal = tmp
      elif cumSum > secondCal and cumSum < topCal:
        thirdCal = secondCal
        secondCal = cumSum
      elif cumSum > thirdCal and cumSum < secondCal:
        thirdCal = cumSum
      cumSum = 0
    else:
      cumSum += int(line.strip('\n'))

print(sum([topCal, secondCal, thirdCal]))
