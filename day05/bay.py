def loadCrates(raw_crates):
  # set up a two dimensional array to represent crate stacks
  num_stacks = 9 #int(len(raw_crates[0])/4)   ## i hate whitespace and am giving up
  crates = []
  for i in range(0, num_stacks):
    crates.append([])

  # read in the initial state of crates
  for row in raw_crates:
    for s in range(0, num_stacks):
      if row[s*4] == "[":
        crates[s].insert(0,(row[s*4+1]))
  return(crates)

def loadMoves(raw_moves):  #amount, from, to
  moves = []
  for row in raw_moves:
    row = row.split(" ")
    moves.append([row[1], row[3], row[5]])
  return(moves)


def solve1(crates, moves):   #amount, from, to
  for move in moves:
    amt, frm, to = int(move[0]), int(move[1])-1, int(move[2])-1
    for _ in range(0, amt):
      crates[to].append( crates[frm].pop() )

def solve2(crates, moves):   #amount, from, to
  for move in moves:
    amt, frm, to = int(move[0]), int(move[1])-1, int(move[2])-1
    temp_stack = []
    for _ in range(0, amt):
      temp_stack.insert(0, crates[frm].pop())
    crates[to].extend(temp_stack)  
  
with open('input_bay.txt', 'r') as file:
  raw = "".join(file.readlines())
  raw_crates = raw.split("\n\n")[0].split("\n")
  raw_moves = raw.split("\n\n")[1].split("\n")

  crates = loadCrates(raw_crates)
  moves = loadMoves(raw_moves)
  solve2(crates, moves)
  tops = "".join(map(lambda stck: stck.pop(), crates))
  print(tops)