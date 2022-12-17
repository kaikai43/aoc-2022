"""
Test case 2 answer = 36

Similar to part one, now extend case where (rope segment) can move diagonally,

So if previous rope segment move diagonally, then current rope segment move diagonally 
"""
def sign(x):
  if x < 0:
    return -1
  elif x == 0:
    return 0
  else:
    return 1

with open('./day9/input.txt') as f:
  rope = [[0,0] for i in range(10)]
  mapping = {
    'U': 1,
    'D': -1,
    'L': -1,
    'R': 1,
  }
  moveset = set([tuple(rope[0])])
  for line in f:
    move = line.strip('\n').split(' ')
    for i in range(int(move[1])):
      if move[0] == 'U' or move[0] =='D':
        rope[0][1] += mapping[move[0]]
      else:
        rope[0][0] += mapping[move[0]]
      for j in range(1, 10):
        rel_vec = [a - b for a,b in zip(rope[j-1], rope[j])]
        man_dist = sum([abs(a) for a in rel_vec])
        if man_dist >= 3 or (man_dist == 2 and any(x == 0 for x in rel_vec)):
          rope[j] = [sign(a) + b for a,b in zip(rel_vec, rope[j])]
        if j == 9 and tuple(rope[j]) not in moveset:
          moveset.add(tuple(rope[j]))
  print(len(moveset))


