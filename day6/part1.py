seq = 4

with open('./day6/input.txt') as f:
  found = False
  marker = f.read(4)
  if len(set(marker)) == 4:
    found = True
  while not found:
    c = f.read(1)
    seq += 1
    if not c:
      break
    marker = marker[1:] + c
    if len(set(marker)) == 4:
      found = True

print(seq)

