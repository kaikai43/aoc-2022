# initialise priority map
priority_map = {}

alphabet = 'a'
for i in range(1,27):
    priority_map[alphabet] = i
    alphabet = chr(ord(alphabet) + 1)

alphabet = 'A'
for i in range(27, 53):
  priority_map[alphabet] = i
  alphabet = chr(ord(alphabet) + 1)

shared_items = ''
with open('./day3/input.txt') as f:
  for line in f:
    line_set = set(())
    new_line = line.strip('\n')
    mid = len(new_line) // 2
    for i in range(mid):
      for j in range(mid, len(new_line)):
        if new_line[i] == new_line[j]:
          line_set.add(new_line[i])
    for i in line_set:
      shared_items += i

priority_sum = 0
for i in shared_items:
  priority_sum += priority_map[i]

print(priority_sum)
