#test case = 29

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

def astar(start, goal, graph):
  cost = 0
  visited = {}
  visited[tuple(start)] = cost
  pqueue = []
  pqueue.append([tuple(start), cost])

  while pqueue:
    pqueue = sorted(pqueue, key=lambda x: x[1])
    node, node_cost = pqueue.pop(0)
    if list(node) == goal:
      return node_cost
    new_cost = visited[node] + 1
    for n in get_n(node, graph):
      if tuple(n) not in visited or new_cost < visited[tuple(n)]:
        visited[tuple(n)] = new_cost
        pqueue.append([tuple(n), new_cost + man_dist(n, goal)])

with open('./day12/input.txt') as f:
  graph = []
  for line in f:
    new_l = line.strip('\n')
    graph.append(new_l)

  n_cols = len(graph[0])
  n_rows = len(graph)
  all_a = {}
  goal = []

  for i in range(n_rows):
    for j in range(n_cols):
      if graph[i][j] == 'a' or graph[i][j] == 'S':
        all_a[(j, i)] = None
      if graph[i][j] == 'E':
        goal = [j, i]
  
  start_all = {}
  for a in all_a.keys():
    res = astar(a, goal, graph)
    if res:
      start_all[a] = res

  print(sorted(start_all.items(), key=lambda x: x[1]))