outcome = {
  'Z': 6,
  'Y': 3,
  'X': 0,
}

matchup = {
  'A X': 'scissors',
  'A Y': 'rock',
  'A Z': 'paper',
  'B X': 'rock',
  'B Y': 'paper',
  'B Z': 'scissors',
  'C X': 'paper',
  'C Y': 'scissors',
  'C Z': 'rock',
}

shape = {
  'rock': 1,
  'paper': 2,
  'scissors': 3,
}

total = 0

with open('./day2/input.txt') as f:
  for line in f:
    total += shape[matchup[line.strip('\n')]] + outcome[line.strip('\n')[-1]]

print(total)