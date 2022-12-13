from input import strategy

# X = Lose
# Y = Draw
# Z = Win

myShape = {"A": {"X": "Scissors", "Y": "Rock", "Z": "Paper"},  # Rock
           "B": {"X": "Rock", "Y": "Paper", "Z": "Scissors"},  # Paper
           "C": {"X": "Paper", "Y": "Scissors", "Z": "Rock"}}  # Scissors

shapeScores = {"Rock": 1, "Paper": 2, "Scissors": 3}
outcomeScores = {"X": 0,  # Lose
                 "Y": 3,  # Draw
                 "Z": 6}  # Win

print(sum([outcomeScores[outcome] + shapeScores[myShape[opp][outcome]] for [opp, outcome] in [round.split(" ")
      for round in strategy.split("\n")]]))
