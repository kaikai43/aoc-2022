complete_op = {
  'addx': 2,
}

flag = [20, 60, 100, 140, 180, 220]

# test = 13140
with open('./day10/input.txt') as f:
  signal = []
  n_cycle = 1
  x = 1
  for line in f:
    cmd = line.strip('\n').split(' ')
    if cmd[0] == 'noop':
      if n_cycle in flag:
        signal.append(n_cycle * x)
      n_cycle += 1
    else:
      instruction, v = cmd
      for i in range(complete_op[instruction]):
        if n_cycle in flag:
          signal.append(n_cycle * x)
        n_cycle += 1
        if i == 1:
          x += int(v)
  print(sum(signal))
  

