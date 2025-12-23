import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
Player_Scores = [0 for _ in range(players)]

while max(Player_Scores) < max_score:  
    for player_idx in range(players):
       print("\nPlayer number", player_idx + 1,"turn has just started!\n")
       print("your total score is:", Player_Scores[player_idx])
       current_score = 0

       while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower()!='y':
             break
  
            value = roll()
            if value == 1:
               print("You rolled a 1! Turn done!.")
               current_score = 0
               break
            else:
               current_score += value
               print("You rolled a:", value)

            print("Your score is:", current_score)   
  
       Player_Scores[player_idx] += current_score  
       print("Your total score is:", Player_Scores[player_idx])

max_score_value = max(Player_Scores)
winning_idx = Player_Scores.index(max_score_value)
print("player number", winning_idx + 1, 
      " is the winner with a score of", max_score_value)      