def solution1(raw):
  num_pairs_with_full_overlap = 0
  
  for pair in raw:

    # prepare my inputs
    pair = ''.join(pair)
    e1, e2 = pair.split(",")[0], pair.split(",")[1]
    e1 = e1.split("-")
    e2 = e2.split("-")
    e1 = list(map(int, e1))
    e2 = list(map(int, e2))

    if (e1[0]<= e2[0] and e1[1]>= e2[1]):
      num_pairs_with_full_overlap += 1
    elif(e1[0]>= e2[0] and e1[1]<= e2[1]):
      num_pairs_with_full_overlap += 1

  return num_pairs_with_full_overlap
      
  
def solution2(raw):
  num_pairs_with_full_overlap = 0
  
  for pair in raw:
    # prepare my inputs
    pair = ''.join(pair)
    e1, e2 = pair.split(",")[0], pair.split(",")[1]
    e1 = e1.split("-")
    e2 = e2.split("-")
    e1 = list(map(int, e1))
    e2 = list(map(int, e2))

    if (e1[0]<= e2[1] and e1[1]>= e2[0]):
      num_pairs_with_full_overlap += 1

  return num_pairs_with_full_overlap
     

with open('input_sample.txt', 'r') as file:
  raw = file.readlines()
  print(solution1(raw))
  print(solution2(raw))
