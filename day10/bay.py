# helper function from stack overflow to pretty print 2d matrix
def prettyPrint(matrix):
  print('\n'.join([''.join([str(cell) for cell in row]) for row in matrix]))


# array-index (zero indexed counter)
# clock-cycle (one indexed counter)
# x-value (variable integer)
# signal strength (clock-cycle * x-value)
def solve(raw):

  # process the instructions list, and create an array showing each addition per clock cycle
  instructed_additions = []
  for line in raw:
    if line[0:4] == "noop":
      instructed_additions.append(0)
      continue
    # addx takes two cycles to run, so add a zero first
    instructed_additions.append(0)
    instructed_additions.append(int(line[5:]))

  # calculate the running total (aka: x-value) at each clock cycle
  x_values = []
  x_values.append(1)  # set the base case, always x=1
  for i in range(1, len(instructed_additions)):  # then loop forward
    x_values.append(x_values[i - 1] + instructed_additions[i])
  x_values.insert(0, 1)  # base case hack fix, idk

  # now multiple by x-value by clock cycle to get signal strength
  sig_strengths = []
  for i in range(0, len(x_values)):
    if (i + 1) in [20, 60, 100, 140, 180, 220]:
      print("cycle", i + 1, x_values[i], x_values[i] * (i + 1))
    sig_strengths.append(x_values[i] * (i + 1))

  # now find the specific cycle vals for ouput of solution 1
  output = 0
  for i in [20, 60, 100, 140, 180, 220]:
    output += sig_strengths[i - 1]
  print(output)  # solution 1!

  ##
  ## Solution 2

  # build the CRT
  crt = []
  for r in range(0, 6):
    crt.append([])
    for c in range(0, 40):
      crt[r].append(".")

  # now draw the sprints
  r = 0
  c = -1
  for i in range(1, len(x_values)):
    # loop through the array [r][c] using increment i
    # we want to draw the pixel represented at [r][c] at each cycle
    # we want to draw that pixel as a # if the x-value at that time i is within 1 pixel of c

    # increment pixel and handle wrapping
    c += 1
    if c == 40:
      c = 0
      r += 1

    # draw the pixel if sprite overlaps
    if (x_values[i] >= c and x_values[i] <= c + 2):
      crt[r][c] = "#"

  prettyPrint(crt)


with open('input_bay.txt', 'r') as file:
  raw = file.read().splitlines()
  solve(raw)
