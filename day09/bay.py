def solve(raw):
  
  # create an array of all our (direction, int distance) tuples
  commands = []
  for line in raw: 
    dir = line.split(" ")[0]
    dist = int(line.split(" ")[1])
    commands.append( (dir, dist) )

  # we'll use this dictionary to map steps in each cardinal direction
  deltas = {
    'U': (0,1),
    'D': (0,-1),
    'R': (1,0),
    'L': (-1,0)
  }

  # we'll use this set to track locations (uniquely)
  locations = set()

  # start at base coordinates
  head = (0,0)
  tail = (0,0)
  
  for command in commands:
    dir = command[0]
    dist = command[1]
    
    for step in range( dist ):

      # move the head
      head = (head[0] + deltas[ dir ][0], head[1] + deltas[ dir ][1])
      
      # see if tail needs to move.  (That is, if any direction is more than 1 step away)
      move = ( abs(head[0]-tail[0])>1 or abs(head[1]-tail[1])>1 )

      # then if you're going to move, step both x and/or y one step as appropriate
      if move is True:
        if head[0]>tail[0]:
          tail = (tail[0]+1, tail[1])
        if head[0]<tail[0]:
          tail = (tail[0]-1, tail[1])
        if head[1]>tail[1]:
          tail = (tail[0], tail[1]+1)
        if head[1]<tail[1]:
          tail = (tail[0], tail[1]-1)

      # add tail location to set
      locations.add( tail )

  # now show how many places the tail went
  print( len(locations) )



def solve2(raw):
  
  # create an array of all our (direction, int distance) tuples
  commands = []
  for line in raw: 
    dir = line.split(" ")[0]
    dist = int(line.split(" ")[1])
    commands.append( (dir, dist) )

  # we'll use this dictionary to map steps in each cardinal direction
  deltas = {
    'U': (0,1),
    'D': (0,-1),
    'R': (1,0),
    'L': (-1,0)
  }

  # we'll use this set to track locations (uniquely)
  locations = set()

  # start at base coordinates
  head = (0,0)
  knots = [head]
  for i in range(9):
    knots.append( (0,0) )
  
  for command in commands:
    dir = command[0]
    dist = command[1]
    
    for step in range( dist ):

      # move the head
      head = knots[0]
      delta = deltas[ dir ]
      head = (head[0] + delta[0], head[1] + delta[1])
      knots[0] = head
      
      # move each knot
      for k in range(1, len(knots)):
        prev = knots[k-1]
        curr = knots[k]
        
        # see if knot needs to move.  (That is, if any direction is more than 1 step away)
        move = ( abs(prev[0]-curr[0])>1 or abs(prev[1]-curr[1])>1 )
  
        # then if you're going to move, step both x and/or y one step as appropriate
        if move is True:
          if prev[0]>curr[0]:
            curr = (curr[0]+1, curr[1])
          if prev[0]<curr[0]:
            curr = (curr[0]-1, curr[1])
          if prev[1]>curr[1]:
            curr = (curr[0], curr[1]+1)
          if prev[1]<curr[1]:
            curr = (curr[0], curr[1]-1)

        knots[k]=curr
        
      # add last knot location to set
      locations.add( knots[9] )

  # now show how many places the tail went
  print( len(locations) )

with open('input_bay.txt', 'r') as file:
  raw = file.read().splitlines()
  solve(raw)
  solve2(raw)

  
 

