# Our main logic function
def solve(input):

  # process our input into a nice clean data structure
  rock_paths = []
  for line in input:
    path = []
    coords = line.split("->")
    for coord in coords:
      x = int ( coord.split(",")[0] )
      y = int ( coord.split(",")[1] )
      path.append( (x,y) )
    rock_paths.append( path )

  #
  # now make a set of all coordinates that rock goes through
  rock_locations = set()
  lowest_rock = 0
  for path in rock_paths:
    for i in range(len(path)-1):
      start = path[i]
      end = path[i+1]

      # figure out the range to walk from start to end
      if start[0]<=end[0]:
        xrange = range(start[0], end[0]+1, 1)
      else:
        xrange = range(start[0], end[0]-1, -1)

      if start[1]<=end[1]:
        yrange = range(start[1], end[1]+1, 1)
      else:
        yrange = range(start[1], end[1]-1, -1)

      # then walk it! (one of these loops will just be one step)
      # along the, keep track of lowest rock, we'll need it later
      for xstep in xrange:
        for ystep in yrange:
          rock_locations.add( (xstep, ystep) )
          if ystep > lowest_rock:
            lowest_rock = ystep
            
  #
  # now start pouring the sand!
  for sand_grain_number in range(1,100000000): #arbitrarily large, whatever
    sand_coord = (500, 0)
    
    while True:

      #FOR PART II: see if we reached the floor
      if (sand_coord[1]==lowest_rock+1):
        rock_locations.add( sand_coord )
        break 
      #END PART II
        
      down = (sand_coord[0], sand_coord[1]+1)
      diagleft =  (sand_coord[0]-1, sand_coord[1]+1)
      diagright = (sand_coord[0]+1, sand_coord[1]+1)

      if down not in rock_locations:
        sand_coord = down
        # FOR PART I
        # if sand_coord[1] > lowest_rock:
        #   print("Finished! The last grain that stuck was:", sand_grain_number-1)
        #   return
        continue

      if diagleft not in rock_locations:
        sand_coord = diagleft
        continue

      if diagright not in rock_locations:
        sand_coord = diagright
        continue

      # FOR PART II
      if sand_coord == (500,0):
        print("Finished! The last grain that stuck was:", sand_grain_number)
        return
      #
        
      rock_locations.add( sand_coord )
      break 
      
      
      


with open('input_bay.txt', 'r') as file:
  input = [line.rstrip() for line in file.readlines()]
  solve(input)