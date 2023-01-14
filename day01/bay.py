def solution1(raw):
  elf_food_totals = []
  current_elf_total = 0

  for line in raw:
    if line == '\n':
      elf_food_totals.append(current_elf_total)
      current_elf_total = 0
    else:
      current_elf_total += int(line)

  return max(elf_food_totals)


def solution2(raw):
  elf_food_totals = []
  current_elf_total = 0

  for line in raw:
    if line == '\n':
      elf_food_totals.append(current_elf_total)
      current_elf_total = 0
    else:
      current_elf_total += int(line)

  elf_food_totals.sort(reverse=True)
  return (sum(elf_food_totals[0:3]))


with open('input_bay.txt', 'r') as file:
  raw = file.readlines()
  print(solution1(raw))
  print(solution2(raw))
