def solution1(raw):
  # we'll track total score here
  total_score = 0

  # And we'll use these two dictionaries to easily convert to points value
  move_to_score_map = {"X": 1, "Y": 2, "Z": 3}
  outcome_to_score_map = {"WIN": 6, "DRAW": 3, "LOSE": 0}

  # And we'll use this dictionary to calculate outcomes.
  outcome_calculator = {
    "XA": "DRAW",
    "XB": "LOSE",
    "XC": "WIN",
    "YA": "WIN",
    "YB": "DRAW",
    "YC": "LOSE",
    "ZA": "LOSE",
    "ZB": "WIN",
    "ZC": "DRAW",
  }

  #
  # Now iterate through the rounds
  for round in raw:
    points_this_round = 0
    my_move = round[2]
    their_move = round[0]

    # add the points for whatever move you played
    points_this_round += move_to_score_map[my_move]

    # add the points for whatever outcome you had
    outcome = outcome_calculator[my_move + their_move]
    points_this_round += outcome_to_score_map[outcome]

    total_score += points_this_round

  #wrap up
  return total_score


def solution2(raw):
  # we'll track total score here
  total_score = 0

  # And we'll use these two dictionaries to easily convert to points value
  outcome_to_score_map = {"Z": 6, "Y": 3, "X": 0}
  move_to_score_map = {"A": 1, "B": 2, "C": 3}

  # And we'll use this dictionary to calculate my move.
  my_move_calculator = {
    "AX": "C",  #rock lose --> scissors
    "AY": "A",  #rock draw --> rock
    "AZ": "B",  #rock win --> paper
    "BX": "A",  #paper lose --> rock
    "BY": "B",  #paper draw --> paper
    "BZ": "C",  #paper win --> scissors
    "CX": "B",  #scissors lose --> paper
    "CY": "C",  #scissors draw --> scissors
    "CZ": "A"  #scissors win --> rock
  }

  #
  # Now iterate through the rounds
  for round in raw:
    points_this_round = 0
    outcome = round[2]
    their_move = round[0]

    #calculate my move based on outcome
    my_move = my_move_calculator[their_move + outcome]

    # add the points for the round
    points_this_round += outcome_to_score_map[outcome]
    points_this_round += move_to_score_map[my_move]

    total_score += points_this_round

  #wrap up
  return total_score


with open('input_bay.txt', 'r') as file:
  raw = file.readlines()
  print(solution1(raw))
  print(solution2(raw))
