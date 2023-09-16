import random

def roll():
    minValue = 1
    maxValue = 6
    roll = random.randint(minValue, maxValue)

    return roll
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again")

maxScore = 50
playerScores = [0 for _ in range(players)]

while max(playerScores) < maxScore:

    for playerIndex in range(players)
    print("\nplayer number", playerIndex + 1, "turn has just started!\n")
    currentScore = 0

    while True:
    shouldRoll = input("Would you like to toll (y)? ")
    if shouldRoll.lower() != "y":
        break

        value = roll()
    if value == 1:
        print("you rolled a 1! Turn done!")
        currentScore = 0
        break
    else:
        currentScore += value
        print("you rolled a: ", value)

    print("your score is: ", currentScore)

playerScores[playerIndex] == currentScore

print("your total score is: ", playerScores[playerIndex])