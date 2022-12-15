def find_closest(main, f):
  total = 43562874
  unused_space = 70000000 - total
  to_delete = 30000000 - unused_space
  closest = total
  for line in f:
    line_list = line.strip('\n').split(' ')
    if line_list[0] == '$':
      if line_list[1] == 'cd':
        if line_list[2] == '..':
          for key in main.keys():
            if key != 'size':
              main['size'] += main[key]['size']
          if main['size'] >= to_delete and main['size'] - to_delete < closest - to_delete:
              closest = main['size']
          return closest
        else:
          new_closest = find_closest(main[line_list[2]], f)
          if new_closest >= to_delete and new_closest - to_delete < closest - to_delete:
            closest = new_closest
      if line_list[1] == 'ls':
        continue
    elif line_list[0] == 'dir':
      main[line_list[1]] = { 'size': 0 }
    else:
      main['size'] += int(line_list[0])
  if list(main.keys())[0] != '/':
    for key in main.keys():
      if key == '/':
        break
      if key != 'size':
        main['size'] += main[key]['size']
    if main['size'] >= to_delete and main['size'] - to_delete < closest - to_delete:
      closest = main['size']
  return closest

with open('./day7/input.txt') as f:
  main = {
    '/' : { 
      'size': 0
    }
  }
  closest = find_closest(main, f)
  print(closest)