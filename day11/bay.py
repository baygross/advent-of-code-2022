import math


# load the puzzle input into array of monkey {}'s
def loadMonkeys(raw, monkeys):
  num_monkeys = int((len(raw) + 1) / 7)
  for monkey_id in range(0, num_monkeys):
    raw_monkey = raw[monkey_id * 7:(monkey_id + 1) * 7]
    monkey = {}
    monkey['id'] = monkey_id  # int
    monkey['items'] = raw_monkey[1][18:].split(',')  # array of strings
    monkey['items'] = list(map(lambda x: int(x),
                               monkey['items']))  # now as ints
    monkey['operation'] = raw_monkey[2].split("=")[1].strip()  # string exec command
    monkey['test_divisor'] = int(raw_monkey[3][21:].rstrip())  # int
    monkey['true_toss'] = int(raw_monkey[4][29:].rstrip())  # int
    monkey['false_toss'] = int(raw_monkey[5][30:].rstrip())  # int

    monkeys.append(monkey)


# run the monkey simulation
def solve1(monkeys):

  # initialize a counter for how many times a monkey touches each object
  monkey_counter = [0] * len(monkeys)

  # simulate rounds
  for round in range(0, 10000):

    # each round, loop through each monkey array in order
    for monkey in monkeys:

      # then loop through each item the monkey has
      for item in monkey['items']:
        old = item
        new = eval(monkey['operation'])
            
        #item = int(math.floor(new / 3)) # solution 1
        #item = new % (23 * 19 * 13 * 17) # solution 2 sample
        item = new % (19 * 13 * 5 * 7 * 17 * 2 * 3 * 11)   # solution 2 bay   

        if item % monkey['test_divisor'] == 0:
          monkeys[monkey['true_toss']]['items'].append(item)
        else:
          monkeys[monkey['false_toss']]['items'].append(item)

        monkey_counter[monkey['id']] += 1

      # empty the current monekys array at end of loop
      monkey['items'] = []

  monkey_counter.sort()
  print(monkey_counter)


with open('input_bay.txt', 'r') as file:
  raw = file.read().splitlines()
  monkeys = []
  loadMonkeys(raw, monkeys)
  print(monkeys)
  solve1(monkeys)
