from input import strategy

shapeScores = {"X": 1, "Y": 2, "Z": 3}
outcomeScores = {"A": {"X": 3, "Y": 6, "Z": 0},
                 "B": {"X": 0, "Y": 3, "Z": 6},
                 "C": {"X": 6, "Y": 0, "Z": 3}}

print(sum([outcomeScores[opp][me] + shapeScores[me] for [opp, me] in [round.split(" ")
      for round in strategy.split("\n")]]))
