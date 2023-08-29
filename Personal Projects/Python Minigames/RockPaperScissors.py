import random

def go():
  choiceAI = random.randint(0, 2)
  choicePlayer = input("Rock, Paper, Scissors: ")
  if choicePlayer.lower() == "rock":
    if choiceAI == 0:
      print("Rock! Draw")
      go()
    elif choiceAI == 1:
      print ("Paper! You Lose")
    elif choiceAI == 2:
      print ("Scissors! You Win")
  elif choicePlayer.lower() == "paper":
    if choiceAI == 0:
      print("Rock! You Win")
    elif choiceAI == 1:
      print ("Paper! Draw")
      go()
    elif choiceAI == 2:
      print ("Scissors! You Lose")
  elif choicePlayer.lower() == "scissors":
    if choiceAI == 0:
      print("Rock! You Lose")
    elif choiceAI == 1:
      print ("Paper! You Win")
    elif choiceAI == 2:
      print ("Scissors! Draw")
      go()
  else:
    print("Please input a valid response.")
    go()

def main():
  go()
  
if __name__ == "__main__":
    main()