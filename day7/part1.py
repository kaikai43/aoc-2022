
def add_size(main, f):
  total = 0
  for line in f:
    line_list = line.strip('\n').split(' ')
    if line_list[0] == '$':
      if line_list[1] == 'cd':
        if line_list[2] == '..':
          for key in main.keys():
            if key != 'size':
              main['size'] += main[key]['size']
          if main['size'] <= 100000:
            total += main['size']
          return total
        else:
          total += add_size(main[line_list[2]], f)
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
    if main['size'] <= 100000:
      total += main['size']
  return total

with open('./day7/input.txt') as f:
  main = {
    '/' : { 
      'size': 0
    }
  }
  total = add_size(main, f)
  print(main)
  print(total)