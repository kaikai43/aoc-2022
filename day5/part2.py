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
    stacks[int(new_line[2]) - 1] += stacks[int(new_line[1]) - 1][-int(new_line[0]):]
    stacks[int(new_line[1]) - 1] = stacks[int(new_line[1]) - 1][:-int(new_line[0])]

print("".join([stack[-1] for stack in stacks]))