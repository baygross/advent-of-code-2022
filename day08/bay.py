def solve1(raw):
  num_rows = len(raw)
  num_cols = len(raw[0])
  print("This forest is dimensions:", num_rows, "x", num_cols)

  # initialize our main forest arrwy
  trees = []
  for row in raw:
    trees.append(list(row))

  # initialize num visible trees to the outer edge
  num_visible_trees = (num_rows +
                       num_cols) * 2 - 4  # dont double count corners
  print("Added the", num_visible_trees, "outside trees")

  # now loop over the inner cells only
  for r in range(1, num_rows - 1):
    for c in range(1, num_cols - 1):

      can_be_seen = False

      # check left
      if max(trees[r][:c]) < trees[r][c]:
        can_be_seen = True

      # check right
      if max(trees[r][c + 1:]) < trees[r][c]:
        can_be_seen = True

      # check up
      if max(map(lambda x: x[c], trees[:r])) < trees[r][c]:
        can_be_seen = True

      # check down
      if max(map(lambda x: x[c], trees[r + 1:])) < trees[r][c]:
        can_be_seen = True

      if can_be_seen:
        num_visible_trees += 1
        print("Added tree:", r, c)

  print(num_visible_trees)


def solve2(raw):
  num_rows = len(raw)
  num_cols = len(raw[0])
  print("This forest is dimensions:", num_rows, "x", num_cols)

  # initialize our main forest arrwy
  trees = []
  for row in raw:
    trees.append(list(row))

  best_view_so_far = 0

  # now loop over the inner cells only
  for row in range(1, num_rows - 1):
    for col in range(1, num_cols - 1):

      # check left
      line_of_sight_left = 0
      for c in range(col - 1, -1, -1):
        line_of_sight_left += 1  # it counts no matter what
        if trees[row][col] <= trees[row][c]:
          break
          # but stop counting now and break if equal or larger

      # check right
      line_of_sight_right = 0
      for c in range(col + 1, num_cols, 1):
        line_of_sight_right += 1  # it counts no matter what
        if trees[row][col] <= trees[row][c]:
          break
          # but stop counting now and break if equal or larger

      # check up
      line_of_sight_up = 0
      for r in range(row - 1, -1, -1):
        line_of_sight_up += 1  # it counts no matter what
        if trees[row][col] <= trees[r][col]:
          break
          # but stop counting now and break if equal or larger

      # check down
      line_of_sight_down = 0
      for r in range(row + 1, num_rows, 1):
        line_of_sight_down += 1  # it counts no matter what
        if trees[row][col] <= trees[r][col]:
          break
          # but stop counting now and break if equal or larger

      current_view = line_of_sight_left * line_of_sight_right * line_of_sight_down * line_of_sight_up
      best_view_so_far = max([best_view_so_far, current_view])

  print(best_view_so_far)


with open('input_bay.txt', 'r') as file:
  raw = file.read().splitlines()
  solve1(raw)
  solve2(raw)
