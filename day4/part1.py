contain = 0
with open('./day4/input.txt') as f:
  for line in f:
    pair = line.strip('\n').split(',')
    pair_split = [i.split('-') for i in pair]
    if int(pair_split[0][0]) <= int(pair_split[1][0]) and int(pair_split[0][1]) >= int(pair_split[1][1]) or \
      int(pair_split[1][0]) <= int(pair_split[0][0]) and int(pair_split[1][1]) >= int(pair_split[0][1]):
      contain += 1

print(contain)
