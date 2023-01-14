from functools import cmp_to_key

def compare(l, r):

  # INT INT
  if type(l) == int and type(r) == int:
    if l<r: 
      return 1 #succeed
    if l==r: 
      return 0 # inconclusive
    if l>r: 
      return -1  #fail 

  # INT LIST
  if type(l)==int and type (r) == list:
    return compare([l], r)
  if type(l)==list and type (r) == int:
    return compare(l, [r])

  # LIST LIST
  i = 0 # iterator
  while True:
    if i>= len(l) and i>=len(r):
      return 0 # inconclusive
    if i>=len(l):
      return 1 # succeed
    if i>=len(r):
      return -1 #fail

    result = compare(l[i], r[i])
    if result == 0:
      i+=1
      continue
    return result
    
  
#   
# Main puzzle logic starts here
def solve(input):
  correct_pairs = []

  # iterate over each pair
  for pair_idx in range(len(input)): 
    pair = input[pair_idx]
    left = eval(pair[0])
    right = eval(pair[1])

    if compare(left, right) == 1:
      correct_pairs.append(pair_idx + 1) #remember they start at 1 not 0

  # total the indexes of ones that were correct
  print (sum(correct_pairs))


#   
# Main puzzle logic starts here
def solve2(input):

  input.append("[[2]]")
  input.append("[[6]]")
  input = [eval(line) for line in input]

  # sort input list
  output = sorted(input, key=cmp_to_key(compare), reverse=True) 

  a = output.index([[2]]) + 1
  b = output.index([[6]]) + 1
  print(a * b)

with open('input_bay.txt', 'r') as file:

  # read in the file as a list of lists of strings
  # segmented by double line breaks
  raw = file.read()
  input = raw.split("\n\n")
  input = list( map(lambda s: s.split("\n"), input) ) 
  solve(input)

  # read in the file as a list of strings
  # deleting all spaced line breaks they no longer matter
  input = raw.splitlines()
  input = list( filter(lambda line: line != "", input) )
  solve2(input)