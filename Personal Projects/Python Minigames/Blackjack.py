import random
import os

cards = ["Club-A", "Club-2", "Club-3", "Club-4", "Club-5", "Club-6", "Club-7", "Club-8", "Club-9", "Club-10", "Club-J", "Club-Q", "Club-K", "Diamond-A", "Diamond-2", "Diamond-3", "Diamond-4", "Diamond-5", "Diamond-6", "Diamond-7", "Diamond-8", "Diamond-9", "Diamond-10", "Diamond-J", "Diamond-Q", "Diamond-K", "Heart-A", "Heart-2", "Heart-3", "Heart-4", "Heart-5", "Heart-6", "Heart-7", "Heart-8", "Heart-9", "Heart-10", "Heart-J", "Heart-Q", "Heart-K", "Spade-A", "Spade-2", "Spade-3", "Spade-4", "Spade-5", "Spade-6", "Spade-7", "Spade-8", "Spade-9", "Spade-10", "Spade-J", "Spade-Q", "Spade-K"]
dealer = []
player = []
turnNum = 0

def getCard(card):
  if card[len(card)-1:len(card)] == "0":
    return card[len(card)-2:len(card)]
  else:
    return card[len(card)-1:len(card)]

def getNum(cards):
  num1 = 0
  numAce = 0
  
  for x in range(0, len(cards)):
    if ((getCard(cards[x]) == "J") or (getCard(cards[x]) == "Q") or (getCard(cards[x]) == "K")):
      num1 += 10
    elif (getCard(cards[x]) == "A"):
      numAce += 1
    else:
      num1 += int(getCard(cards[x]))

  for y in range(0, numAce):
    if ((num1 + (11*(numAce-y)) + y) <= 21):
      num1 += (11*(numAce-y) + y)
      return num1
      
  num1 += numAce
  return num1
  
def printPlayer():
  handP = ""
  for x in range(0, len(player)):
    handP += player[x] + " "
  return handP
    
def printDealerHide():
  handDH = ""
  for x in range(0, len(dealer)-1):
    handDH += dealer[x] + " "
  return handDH
    
def printDealerFull():
  handDF = ""
  for x in range(0, len(dealer)):
    handDF += dealer[x] + " "
  return handDF
  
def printCurrent():
  print("D: " + printDealerHide() + "\n\n" + "P: " + printPlayer() + "\n" + str(getNum(player)) + "\n\n")
  
def endGame():
  print("D: " + printDealerFull() + "\n" + str(getNum(dealer)) + "\n\n" + "P: " + printPlayer() + "\n" + str(getNum(player)) + "\n\n")
  if getNum(dealer) < 17:
    addDealerCard()
    endGame()
  else:
    if getNum(dealer) > 21:
      print("Dealer Break, Gain Bet")
    elif getNum(dealer) < getNum(player):
      print("Gain Bet")
    elif getNum(dealer) > getNum(player):
      print("Lose Bet")
    else:
      print("Pass")
        
def endGameDD():
  print("D: " + printDealerFull() + "\n" + str(getNum(dealer)) + "\n\n" + "P: " + printPlayer() + "\n" + str(getNum(player)) + "\n\n")
  if getNum(dealer) < 17:
    addDealerCard()
    endGameDD()
  else:
    if getNum(dealer) > 21:
      print("Dealer Break, Gain Double Bet")
    elif getNum(dealer) < getNum(player):
      print("Gain Double Bet")
    elif getNum(dealer) > getNum(player):
      print("Lose Double Bet")
    else:
      print("Pass")

def choose(turnNum):
  if getNum(player) == 21:
    print("Natural!!!")
    endGame()
  elif (turnNum == 0):
    if (getCard(player[0]) == getCard(player[1])):
      answer = input("Would you like to: Hit, Stand, Double Down, or Split: ")
      if answer.lower() == "hit":
        turnNum += 1
        addPlayerCard()
        printCurrent()
        if getNum(player) == 21:
          print("Player BlackJack!")
          endGame()
        elif getNum(player) < 21:
          choose(turnNum)
        else:
          print("Player Break")
      elif answer.lower() == "stand":
        turnNum += 1
        endGame()
      elif answer.lower() == "double down":
        turnNum += 1
        addPlayerCard()
        printCurrent()
        if getNum(player) == 21:
          print("Player BlackJack!")
          endGameDD()
        elif getNum(player) < 21:
          endGameDD()
        else:
          print("Player Break")
      elif answer.lower() == "split":
        print("I'm not coding this")
        choose(turnNum)
      else:
        print("Please enter a valid response.")
        choose(turnNum)
    else:
      answer = input("Would you like to: Hit, Stand, or Double Down: ")
      if answer.lower() == "hit":
        turnNum += 1
        addPlayerCard()
        printCurrent()
        if getNum(player) == 21:
          print("Player BlackJack!")
          endGame()
        elif getNum(player) < 21:
          choose(turnNum)
        else:
          print("Player Break")
      elif answer.lower() == "stand":
        turnNum += 1
        endGame()
      elif answer.lower() == "double down":
        turnNum += 1
        addPlayerCard()
        printCurrent()
        if getNum(player) == 21:
          print("Player BlackJack!")
          endGameDD()
        elif getNum(player) < 21:
          endGameDD()
        else:
          print("Player Break")
      else:
        print("Please enter a valid response.")
        choose(turnNum)
  else:
    answer = input("Would you like to: Hit or Stand: ")
    if answer.lower() == "hit":
      addPlayerCard()
      printCurrent()
      if getNum(player) == 21:
        print("Player BlackJack!")
        endGame()
      elif getNum(player) < 21:
        choose(turnNum)
      else:
        print("Player Break")
    elif answer.lower() == "stand":
      endGame()
    else:
      print("Please enter a valid response.")
      choose(turnNum)
    

def addPlayerCard():
  cardNum = random.randint(0, len(cards)-1)
  player.append(cards.pop(cardNum))
  
def addDealerCard():
  cardNum = random.randint(0, len(cards)-1)
  dealer.append(cards.pop(cardNum))

def insurance():
  insuranceAnswer = input("Would you like to buy insurance? (Y/N): ")
  if insuranceAnswer.lower() == "y":
    if ((getCard(dealer[1]) == "10") or (getCard(dealer[1]) == "J") or (getCard(dealer[1]) == "Q") or (getCard(dealer[1]) == "K")):
      print("Dealer Blackjack")
      print("Insurance Bet Doubled")
      if getNum(player) == 21:
        print("Pass")
      else:
        print("Loose Initial Bet")
    else:
      print("Insurance Lost")
      choose(turnNum)
  elif insuranceAnswer.lower() == "n":
    if ((getCard(dealer[1]) == "10") or (getCard(dealer[1]) == "J") or (getCard(dealer[1]) == "Q") or (getCard(dealer[1]) == "K")):
      print("Dealer Blackjack")
      if getNum(player) == 21:
        print("Pass")
      else:
        print("Loose Bet")
    else:
      choose(turnNum)
  else:
    print("Please enter a valid response.")
    insurance()

def start():
  addPlayerCard()
  addDealerCard()
  addPlayerCard()
  addDealerCard()
  printCurrent()
  
  if ((getCard(dealer[0]) == "10") or (getCard(dealer[0]) == "J") or (getCard(dealer[0]) == "Q") or (getCard(dealer[0]) == "K")) and  (getCard(dealer[1]) == "A"):
    print("Dealer BLACKJACK!")
    if getNum(player) == 21:
      print("Pass")
    else:
      print("Loose Bet")
  elif (getCard(dealer[0]) == "A"):
    insurance()
  else:
    choose(turnNum)

def main():
  start()
  
if __name__ == "__main__":
    main()