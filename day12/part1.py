#test case = 31

def man_dist(a,b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_val(char):
  return ord('z') if char == 'E' else ord('a') if char == 'S' else ord(char)

def get_n(node, graph):
  directions = [[-1,0], [1,0], [0,1], [0,-1]]
  neighbors = []
  for i in directions:
    neighbor = [a + b for a,b in zip(node, i)]
    if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] < n_cols and neighbor[1] < n_rows:
      if (get_val(graph[neighbor[1]][neighbor[0]]) - get_val(graph[node[1]][node[0]])) <= 1:
        neighbors.append(neighbor)
  return neighbors

with open('./day12/input.txt') as f:
  graph = []
  start = []
  goal = []
  cost = 0
  for line in f:
    new_l = line.strip('\n')
    graph.append(new_l)
    if 'S' in new_l:
      start = [new_l.index('S'), len(graph)-1]
    if 'E' in new_l:
      goal = [new_l.index('E'), len(graph)-1]
  n_cols = len(graph[0])
  n_rows = len(graph)
  visited = {}
  visited[tuple(start)] = cost
  pqueue = []
  pqueue.append([tuple(start), cost])

  while pqueue:
    pqueue = sorted(pqueue, key=lambda x: x[1])
    node, node_cost = pqueue.pop(0)
    if list(node) == goal:
      print(node_cost)
      print('Goal reached')
      break
    new_cost = visited[node] + 1
    for n in get_n(node, graph):
      if tuple(n) not in visited or new_cost < visited[tuple(n)]:
        visited[tuple(n)] = new_cost
        pqueue.append([tuple(n), new_cost + man_dist(n, goal)])
