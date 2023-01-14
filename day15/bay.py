def solve(input):
  TARGET_ROW = 2000000
  
  #
  # First we are going to process the input into Sensor/Beacon coordinate pairs
  pairs = []
  for line in input:
    sensor_raw, beacon_raw = line.split(":")
    sensor_x = int(sensor_raw.split("=")[1].split(",")[0]) 
    sensor_y = int(sensor_raw.split("=")[2]) 
    beacon_x = int(beacon_raw.split("=")[1].split(",")[0]) 
    beacon_y = int(beacon_raw.split("=")[2])
    sensor= (sensor_x, sensor_y)
    beacon= (beacon_x, beacon_y)
    pairs.append( [sensor, beacon] )
    
  #
  # Now create a set of all coordinates that are covered by the sensors
  coverage = set()
  for pair in pairs:
    sensor, beacon = pair[0], pair[1]
    xdis = abs(sensor[0]-beacon[0])
    ydis = abs(sensor[1]-beacon[1])
    max_dis = xdis+ydis
    
    # This code block is accurate but the set gets too massive for CPU
    # so instead i'm going to optimize by only adding coords to the row we care about 
    # 
    # for x in range(0,max_dis+1):
    #   for y in range(0, max_dis+1-x):
    #     coverage.add( (sensor[0]+x, sensor[1]+y) )
    #     coverage.add( (sensor[0]-x, sensor[1]+y) )
    #     coverage.add( (sensor[0]+x, sensor[1]-y) )
    #     coverage.add( (sensor[0]-x, sensor[1]-y) )

    # This is my new optimized code block just for target_row
    ydis=abs(TARGET_ROW-sensor[1])
    if ydis>max_dis:
      continue
    xdis=max_dis-ydis
    for x in range(-1*xdis,xdis+1):
      coverage.add( (sensor[0]+x, TARGET_ROW) )
    
  #
  # now remove the beacons from the covered positions tracker to make the answer key happy
  for pair in pairs:
    coverage.discard(pair[1])

    
  #
  # finally figure out coverage for the row we care about
  covered_spots = 0
  for coord in coverage:
    if coord[1]==TARGET_ROW:
      covered_spots += 1

  print(covered_spots)
    
  
with open('input_bay.txt', 'r') as file:
  input = [line.rstrip() for line in file.readlines()]
  solve(input)
