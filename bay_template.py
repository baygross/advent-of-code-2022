# Helper function to print 2D matrix. 
def prettyPrint(matrix, spacer=''): 
  print('\n'.join([spacer.join([str(cell) for cell in row]) for row in matrix]))
  return
  
# Our main logic function
def solve(input):
  print("hello")
  return


with open('input_bay.txt', 'r') as file:
  input = [line.rstrip() for line in file.readlines()]

  # COMPLEX 
  # instead of one-top level list with all strings inside it,
  # have two layers of lists where the inner layer breaks up the input by double line break
  input = file.read()
  input = input.split("\n\n")
  input = list( map(lambda s: s.split("\n"), input) ) 

  solve(input)