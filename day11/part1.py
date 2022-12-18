# Test answer: 10605
'''
lvl_biz = product of 2 most active (#items inspected) monkeys
'''
import math

with open('./day11/input.txt') as f:
  monkeys = {}
  for line in f:
    new_l = line.strip('\n')
    if new_l.split(' ')[0] == 'Monkey':
      monkey_id = int(new_l.split(' ')[1].strip(':'))
      monkeys[monkey_id] = {}
      monkeys[monkey_id]['active'] = 0
      monkeys[monkey_id]['items'] = [int(i) for i in f.readline().strip('\n').strip('Starting items: ').split(', ')]
      op_l = f.readline().strip('\n').replace('Operation: new = old ', '').replace('  ', '').split(' ')
      monkeys[monkey_id]['op'] = op_l[0]
      monkeys[monkey_id]['amnt'] = op_l[1]
      monkeys[monkey_id]['div'] = int(f.readline().strip('\n').strip('Test: divisible by '))
      monkeys[monkey_id]['true'] = int(f.readline().strip('\n').strip('If true: throw to monkey '))
      monkeys[monkey_id]['false'] = int(f.readline().strip('\n').strip('If false: throw to monkey '))
  for i in range(20):
    for monkey_id in monkeys.keys():
      while len(monkeys[monkey_id]['items']) != 0:
        monkeys[monkey_id]['active'] += 1
        item = monkeys[monkey_id]['items'][0]
        monkeys[monkey_id]['items'] = monkeys[monkey_id]['items'][1:]
        new_item = 0
        if monkeys[monkey_id]['op'] == '*':
          if monkeys[monkey_id]['amnt'] == 'old':
            new_item = item * item
          else:
            new_item = item * int(monkeys[monkey_id]['amnt'])
        else:
          new_item = item + int(monkeys[monkey_id]['amnt'])
        new_item = math.floor(new_item / 3)
        if new_item % monkeys[monkey_id]['div'] == 0:
          monkeys[monkeys[monkey_id]['true']]['items'].append(new_item)
        else:
          monkeys[monkeys[monkey_id]['false']]['items'].append(new_item)
  arr_sort = sorted([monkeys[monkey_id]['active'] for monkey_id in monkeys.keys()], reverse=True)
  print(arr_sort[0] * arr_sort[1])



