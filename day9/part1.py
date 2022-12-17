"""
Easy case: Solve for Head movement first (test2)
Test answer easy case = 4

Test case 1 answer = 13

T can be in any square 1 distance away from H:
1    2    3
4    H(5) 6
7    8    9

If T in 1:
- Does not move if H move up/left
- Move diagonally to 5 if H move right/down
Apply similar logic to other corners (3, 7, 9)

If T in 2:
- Does not move if H move up/left/right
- Move in same direction if H move down
Apply similar logic to other neighbours (4, 6,8 )

If T in 5, do not move regardless of H.

Can use manhattan(H, T) to identify T position:
- 2 for corners
- 1 for neighbour
- 0 for overlap
Direction
- positive = up or right
- negative = down or left
"""
def sign(x):
  if x < 0:
    return -1
  elif x == 0:
    return 0
  else:
    return 1

with open('./day9/input.txt') as f:
  head = [0,0]
  tail = [0,0]
  mapping = {
    'U': 1,
    'D': -1,
    'L': -1,
    'R': 1,
  }
  moveset = set([tuple(head)])
  for line in f:
    move = line.strip('\n').split(' ')
    for i in range(int(move[1])):
      if move[0] == 'U' or move[0] =='D':
        head[1] += mapping[move[0]]
      else:
        head[0] += mapping[move[0]]
      rel_vec = [a - b for a,b in zip(head, tail)]
      man_dist = sum([abs(a) for a in rel_vec])
      if man_dist == 3 or (man_dist == 2 and any(x == 0 for x in rel_vec)):
        tail = [sign(a) + b for a,b in zip(rel_vec, tail)]
      if tuple(tail) not in moveset:
        moveset.add(tuple(tail))
  print(len(moveset))


