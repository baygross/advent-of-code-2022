# Going to use tuples in this code
# syntax: coord = (x, y)
# helpful because they are immutable

# helper function from stack overflow to pretty print 2d matrix
def prettyPrint(matrix):
  print('\n'.join([''.join([str(cell) for cell in row]) for row in matrix]))


def solve(grid):
  # read in the grid
  #prettyPrint(grid)
  height = len(grid)
  width = len(grid[0])
  
  # find start and end
  # and also make them normal heights so you dont have funky base case  
  for r in range(height):
    for c in range(width):
        if grid[r][c] == 'S':
            start = (r, c)
            grid[r][c] = 'a'
        if grid[r][c] == 'E':
            end = (r, c)
            grid[r][c] = 'z'
  
  # now run Dijkstra's 
  # --> this is a simplified version since all edges are just +1, it's easy
  # --> position in queue effectively means it is a shorter path, because it was added sooner
  queue = [ (start, 0) ]  # will be an array of (coordinate, distance) pairs
  seen = []

  while len(queue) > 0:
    coord, distance = queue.pop(0)
    r, c = coord
    
    # base cases
    if coord == end:
      print("finished at", distance)
      grid[r][c]='E' # reset for solution2 cycles
      return distance
    if coord in seen:
      continue

    # default case
    seen.append( coord )


    # add four cardinal directions to queue, but only if you can actually step that way
    if (r-1>=0 and ord(grid[r-1][c]) <= ord(grid[r][c])+1 ): 
      queue.append( ((r-1, c), distance+1) )
    if (r+1<height and ord(grid[r+1][c]) <= ord(grid[r][c])+1 ):
      queue.append( ((r+1, c), distance+1) )
    if (c-1>=0 and ord(grid[r][c-1]) <= ord(grid[r][c])+1 ):
      queue.append( ((r, c-1), distance+1) )
    if (c+1<width and ord(grid[r][c+1]) <= ord(grid[r][c])+1 ):
      queue.append( ((r, c+1), distance+1) )

  grid[ end[0] ][ end[1] ]='E' # reset for solution2 cycles that don't succeed

with open('input_bay.txt', 'r') as file:
  raw = file.read().splitlines()
  grid = [list(line.strip()) for line in raw]

  # solution 1
  #solve(grid)

  # soution 2
  height = len(grid)
  width = len(grid[0])

  # wipe the starting point
  for r in range(height):
    for c in range(width):
      if(grid[r][c] == 'S'):
        grid[r][c] = 'a'

 # then solve for each possible starting point
  distances = []
  for r in range(height):
    for c in range(width):
      if (grid[r][c] == 'a'):

        # add the starting point (and remove after this round)
        grid[r][c] = 'S' 
        d = solve(grid)
        grid[r][c] = 'a'

        # not all starting points have a solution! but if it did, add it to our list to check for min at end
        if d is not None:
          distances.append(d)

  print("minimum is:", min(distances))
  
