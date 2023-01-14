# helper function to calculate priority of a given character
def pval(c):
  c = ord(c)
  if (c>=65 and c<=90):  #A-Z
    c-=38
  else:
    c-=96 #a-z
  return c

def solution1(raw):
  return_total = 0
  
  for rucksack in raw:
    item_count = int(len(rucksack)/2)
    c1 = rucksack[0:(item_count)]
    c2 = rucksack[item_count:]
    
    duplicate_item = list(set(c1) & set(c2))[0]
    return_total += pval(duplicate_item)
    
  return return_total

  
def solution2(raw):
  return_total = 0
  groups = [raw[i:i+3] for i in range(0, len(raw), 3)]

  for c1, c2, c3 in groups:
    duplicate_item = list(set(c1) & set(c2) & set(c3))[0]
    return_total += pval(duplicate_item)
  
  return return_total


with open('input_bay.txt', 'r') as file:
  raw = [line.rstrip() for line in file.readlines()]  # cut trailing whitespace
  print(solution1(raw))
  print(solution2(raw))
