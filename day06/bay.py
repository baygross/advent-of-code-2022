def solve1(line):
  for i in range(4,len(line)):
      substr = line[i-4:i]
      if len(set(substr))==4:
        return(i)

def solve2(line):
  for i in range(14,len(line)):
      substr = line[i-14:i]
      if len(set(substr))==14:
        return(i)

with open('input_bay.txt', 'r') as file:
  raw = "".join(file.readlines()).split('\n')
  
  print( solve2(raw[0]) )
  
  
  


