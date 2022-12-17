complete_op = {
  'addx': 2,
}

'''
Test answer:
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
'''

with open('./day10/input.txt') as f:
  pixels = ['' for i in range(6)]
  n_cycle = 1
  x = 1
  for line in f:
    cmd = line.strip('\n').split(' ')
    if cmd[0] == 'noop':
      pixels[(n_cycle-1) // 40] += ('#' if (n_cycle-1) % 40 in [x-1, x, x+1] else '.')
      n_cycle += 1
    else:
      instruction, v = cmd
      for i in range(complete_op[instruction]):
        pixels[(n_cycle-1) // 40] += ('#' if (n_cycle-1) % 40 in [x-1, x, x+1] else '.')
        n_cycle += 1
        if i == 1:
          x += int(v)
  for row in pixels:
    print(row)
