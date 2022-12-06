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

shared_badges = ''
elf_num = 1
group = []
with open('./day3/input.txt') as f:
  for line in f:
    new_line = line.strip('\n')
    group.append(new_line)
    if elf_num == 3:
      found = False
      for i in group[0]:
        for j in group[1]:
          if i == j:
            for k in group[2]:
              if i == k:
                shared_badges += i
                found = True
                break
          if found:
            break
        if found:
          break
      group = []
      elf_num = 1
    else:
      elf_num += 1

priority_sum = 0
for i in shared_badges:
  priority_sum += priority_map[i]

print(priority_sum)