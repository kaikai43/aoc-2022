outcome = {
  'win': 6,
  'draw': 3,
  'loss': 0,
}

matchup = {
  'A X': 'draw',
  'A Y': 'win',
  'A Z': 'loss',
  'B X': 'loss',
  'B Y': 'draw',
  'B Z': 'win',
  'C X': 'win',
  'C Y': 'loss',
  'C Z': 'draw',
}

shape = {
  'X': 1,
  'Y': 2,
  'Z': 3,
}

total = 0

with open('./day2/input.txt') as f:
  for line in f:
    total += outcome[matchup[line.strip('\n')]] + shape[line.strip('\n')[-1]]

print(total)