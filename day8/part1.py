
with open('./day8/input.txt') as f:
  trees = []
  for line in f:
    trees.append(line.strip('\n'))
  num_cols = len(trees[0])
  num_rows = len(trees)
  visible = 0
  for i in range(num_rows):
    for j in range(num_cols):
      if i == 0 or i == num_rows - 1 or j == 0 or j == num_cols - 1:
        visible += 1
      else:
        tree = int(trees[i][j])
        is_visible = False
        for direction in range(4): # 0 = up, 1 = down, 2 = left, 3 = right
          if direction == 0:
            is_up_visible = True
            for up in range(i):
              if int(trees[up][j]) >= tree:
                is_up_visible = False
                break
            is_visible = is_up_visible
          elif direction == 1:
            is_down_visible = True
            for down in range(i+1, num_rows):
              if int(trees[down][j]) >= tree:
                is_down_visible = False
                break
            is_visible = is_down_visible
          elif direction == 2:
            is_left_visible = True
            for left in range(j):
              if int(trees[i][left]) >= tree:
                is_left_visible = False
                break
            is_visible = is_left_visible
          else:
            is_right_visible = True
            for right in range(j+1, num_cols):
              if int(trees[i][right]) >= tree:
                is_right_visible = False
                break
            is_visible = is_right_visible
          if is_visible:
            visible += 1
            break
  print(visible)
