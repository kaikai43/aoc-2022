"""
Stacks

[N] [G]                     [Q]    
[H] [B]         [B] [R]     [H]    
[S] [N]     [Q] [M] [T]     [Z]    
[J] [T]     [R] [V] [H]     [R] [S]
[F] [Q]     [W] [T] [V] [J] [V] [M]
[W] [P] [V] [S] [F] [B] [Q] [J] [H]
[T] [R] [Q] [B] [D] [D] [B] [N] [N]
[D] [H] [L] [N] [N] [M] [D] [D] [B]
 1   2   3   4   5   6   7   8   9 
"""

stacks = [
  ['D', 'T', 'W', 'F', 'J', 'S', 'H', 'N'],
  ['H', 'R', 'P', 'Q', 'T', 'N', 'B', 'G'],
  ['L', 'Q', 'V'],
  ['N', 'B', 'S', 'W', 'R', 'Q'],
  ['N', 'D', 'F', 'T', 'V', 'M', 'B'],
  ['M', 'D', 'B', 'V', 'H', 'T', 'R'],
  ['D', 'B', 'Q', 'J'],
  ['D', 'N', 'J', 'V', 'R', 'Z', 'H', 'Q'],
  ['B', 'N', 'H', 'M', 'S']
]

with open('./day5/input.txt') as f:
  for line in f:
    new_line = line.strip('\n').strip('move ').replace('from ', '').replace('to ', '').split(' ')
    for i in range(int(new_line[0])):
      if len(stacks[int(new_line[1]) - 1]) != 0:
        stacks[int(new_line[2]) - 1].append(stacks[int(new_line[1]) - 1].pop())
      else:
        break

print("".join([stack[-1] for stack in stacks]))