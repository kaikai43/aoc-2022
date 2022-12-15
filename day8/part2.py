
with open('./day8/input.txt') as f:
  trees = []
  for line in f:
    trees.append(line.strip('\n'))
  num_cols = len(trees[0])
  num_rows = len(trees)
  max_score = 0
  for i in range(num_rows):
    for j in range(num_cols):
      if i == 0 or i == num_rows - 1 or j == 0 or j == num_cols - 1:
        continue
      else:
        tree = int(trees[i][j])
        score_list = [0, 0, 0, 0]
        for direction in range(4): # 0 = up, 1 = down, 2 = left, 3 = right
          if direction == 0:
            for up in range(i-1, -1, -1):
              score_list[direction] += 1
              if int(trees[up][j]) >= tree:
                break
          elif direction == 1:
            for down in range(i+1, num_rows):
              score_list[direction] += 1
              if int(trees[down][j]) >= tree:
                break
          elif direction == 2:
            for left in range(j-1, -1, -1):
              score_list[direction] += 1
              if int(trees[i][left]) >= tree:
                break
          else:
            for right in range(j+1, num_cols):
              score_list[direction] += 1
              if int(trees[i][right]) >= tree:
                break
        score = 1
        for k in score_list:
          score *= k
        if score > max_score:
          max_score = score
  print(max_score)
