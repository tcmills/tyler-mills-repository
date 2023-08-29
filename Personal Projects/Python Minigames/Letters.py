import os
import random
import sys
import time

cards = ["Guard 1", "Guard 1", "Guard 1", "Guard 1", "Guard 1", "Priest 2", "Priest 2", "Baron 3", "Baron 3", "Handmaid 4", "Handmaid 4", "Prince 5", "Prince 5", "King 6", "Countess 7", "Princess 8"]
global playerCards
playerCards = []
AICards = []
discardSeen = []
discardUnseen = ["-------"]
playerDiscard = []
AIDiscard = []
protectedPlayer = [False]
protectedAI = [False]
printed = []
playerCard = [0]


def addPlayerCard():
  cardNum = random.randint(0, len(cards)-1)
  playerCards.append(cards.pop(cardNum))
  
def addAICard():
  cardNum = random.randint(0, len(cards)-1)
  AICards.append(cards.pop(cardNum))
  
def addDiscard():
  cardNum = random.randint(0, len(cards)-1)
  discardSeen.append(cards.pop(cardNum))
  
def comparePlayer():
  highestP = "0"
  highestA = "0"
  for x in range(0, len(playerCards)):
    if int(highestP[-1]) < int(playerCards[x][-1]):
      highestP = playerCards[x][-1]
  for y in range(0, len(AICards)):
    if int(highestA[-1]) < int(AICards[x][-1]):
      highestA = AICards[x][-1]
  if int(highestP[-1]) > int(highestA[-1]):
    printGame()
    printExtra()
    sys.exit("You Win")
  elif int(highestP[-1]) < int(highestA[-1]):
    printGame()
    printExtra()
    sys.exit("You Lose")
  else:
    startAI()
    
def compareAI():
  highestP = "0"
  highestA = "0"
  for x in range(0, len(playerCards)):
    if int(highestP[-1]) < int(playerCards[x][-1]):
      highestP = playerCards[x][-1]
  for y in range(0, len(AICards)):
    if int(highestA[-1]) < int(AICards[x][-1]):
      highestA = AICards[x][-1]
  if int(highestP[-1]) > int(highestA[-1]):
    printGame()
    printExtra()
    sys.exit("You Win")
  elif int(highestP[-1]) < int(highestA[-1]):
    printGame()
    printExtra()
    sys.exit("You Lose")
  else:
    startPlayer()
  
def printGame():
  os.system("clear")
  print()
  print("-----")
  print("There are 16 cards in the game. At the start of the game, a card is immediately discarded from the deck. Each player starts with a card. On their turn, they draw a card, then discard one of their two cards. So, each player always has one card unless it is their turn.")
  print()
  print("(5) Guard 1: Guess the other player's card. If you are correct, you win this round. You can not guess Guard 1.")
  print("(2) Priest 2: Look at the other player's card.")
  print("(2) Baron 3: Compare your card with the other player's card. Whoever has the highest number wins. In the case of a tie, nothing happens.")
  print("(2) Handmaid 4: You are protected this round. The other player can not use any cards against you.")
  print("(2) Prince 5: Choose a player. Their hand is discarded, and they immediately draw a new card.")
  print("(1) King 6: Trade hands with the another player.")
  print("(1) Countess 7: If you have this card as well as the King or Prince, you must discard it. Otherwise, it does nothing.")
  print("(1) Princess 8: If you discard this card for any reason, you lose.")
  print("-----")
  print()
  print()
  print()
  print("Discarded Card: ", end=""), print(discardUnseen)
  print()
  print("Your Discard Pile: ", end=""), print(playerDiscard)
  print("Other Player's Discard Pile: ", end=""), print(AIDiscard)
  if printed == []:
    print()
  else:
    print("Priest Viewed Card: ", end=""), print(printed)
  print()
  print()
  print()
  print("Your Hand: ", end=""), print(playerCards)
  
def printExtra():
  print()
  print("Other Player's Hand: ", end=""), print(AICards)
  print()
  print("Discarded Card: ", end=""), print(discardSeen)
  print()
    
def startPlayer():
  if len(cards) == 0:
    if int(AICards[0][-1]) < int(playerCards[0][-1]):
      printGame()
      printExtra()
      sys.exit("You Win")
    elif int(AICards[0][-1]) > int(playerCards[0][-1]):
      printGame()
      printExtra()
      sys.exit("You Lose")
    else:
      printGame()
      printExtra()
      sys.exit("Draw")
  addPlayerCard()
  printGame()
  printed.clear()
  time.sleep(5)
  if (playerCards[0] == "Countess 7" and (playerCards[1] == "King 6" or playerCards[1] == "Prince 5")):
    playerTurn(0)
  elif ((playerCards[0] == "King 6" or playerCards[0] == "Prince 5") and playerCards[1] == "Countess 7"):
    playerTurn(1)
  else:
    answer()
    playerTurn(playerCard[0])

def answer():
  choice = input("Which card would you like to play (0 or 1): ")
  if choice == "0" or choice == "1":
    playerCard[0] = int(choice)
  else:
    answer()
    
def playerTurn(num):
  card = playerCards.pop(num)
  playerDiscard.append(card)
  temp = []
  if protectedAI[0]:
    if card == "Handmaid 4":
      protectedPlayer[0] = True
    elif card == "Prince 5":
      protectedPrince()
    elif card == "Princess 8":
      printGame()
      printExtra()
      sys.exit("You Lose")
    protectedAI[0] = False
  else:
    if card == "Guard 1":
      guard()
    elif card == "Priest 2":
      printed.append(AICards[0])
    elif card == "Baron 3":
      comparePlayer()
    elif card == "Handmaid 4":
      protectedPlayer[0] = True
    elif card == "Prince 5":
      prince()
    elif card == "King 6":
      temp.append(playerCards[0])
      playerCards[0] = AICards[0]
      AICards[0] = temp[0]
    elif card == "Princess 8":
      printGame()
      printExtra()
      sys.exit("You Lose")
  startAI()

def guard():
  guess = input("What is your guess (2-8): ")
  if guess == "2" or guess == "3" or guess == "4" or guess == "5" or guess == "6" or guess == "7" or guess == "8":
    if AICards[0][-1] == guess:
      printGame()
      printExtra()
      sys.exit("You Win")
  else:
    guard()
    
def prince():
  who = input("Would you like to discard your hand or the other player's hand (0 for your hand or 1 for their hand): ")
  if who == "1":
    if AICards[0] == "Princess 8":
      AIDiscard.append(AICards[0])
      AICards.clear()
      printGame()
      printExtra()
      sys.exit("You Win")
    else:
      AIDiscard.append(AICards[0])
      AICards.clear()
      addAICard()
  elif who == "0":
    if playerCards[0] == "Princess 8":
      playerDiscard.append(playerCards[0])
      playerCards.clear()
      printGame()
      printExtra()
      sys.exit("You Lose")
    else:
      playerDiscard.append(playerCards[0])
      playerCards.clear()
      addPlayerCard()
  else:
    prince()
    
def protectedPrince():
  if playerCards[0] == "Princess 8":
    playerDiscard.append(playerCards[0])
    playerCards.clear()
    printGame()
    printExtra()
    sys.exit("You Lose")
  else:
    playerDiscard.append(playerCards[0])
    playerCards.clear()
    addPlayerCard()
      
def AITurn(num):
  card = AICards.pop(num)
  AIDiscard.append(card)
  temp = []
  if protectedPlayer[0]:
    if card == "Handmaid 4":
      protectedAI[0] = True
    elif card == "Prince 5":
      if AICards[0] == "Princess 8":
        AIDiscard.append(AICards[0])
        AICards.clear()
        printGame()
        printExtra()
        sys.exit("You Win")
      else:
        AIDiscard.append(AICards[0])
        AICards.clear()
        addAICard()
    elif card == "Princess 8":
      printGame()
      printExtra()
      sys.exit("You Win")
    protectedPlayer[0] = False
  else:
    if card == "Guard 1":
      guess = random.randint(2,8)
      if int(playerCards[0][-1]) == guess:
        printGame()
        printExtra()
        sys.exit("You Lose")
    elif card == "Baron 3":
      compareAI()
    elif card == "Handmaid 4":
      protectedAI[0] = True
    elif card == "Prince 5":
      who = random.randint(0,1)
      if who == 0:
        if AICards[0] == "Princess 8":
          AIDiscard.append(AICards[0])
          AICards.clear()
          printGame()
          printExtra()
          sys.exit("You Win")
        else:
          AIDiscard.append(AICards[0])
          AICards.clear()
          addAICard()
      elif who == 1:
        if playerCards[0] == "Princess 8":
          playerDiscard.append(playerCards[0])
          playerCards.clear()
          printGame()
          printExtra()
          sys.exit("You Lose")
        else:
          playerDiscard.append(playerCards[0])
          playerCards.clear()
          addPlayerCard()
    elif card == "King 6":
      temp.append(playerCards[0])
      playerCards[0] = AICards[0]
      AICards[0] = temp[0]
    elif card == "Princess 8":
      printGame()
      printExtra()
      sys.exit("You Win")
  startPlayer()

def startAI():
  if len(cards) == 0:
    if int(AICards[0][-1]) < int(playerCards[0][-1]):
      printGame()
      printExtra()
      sys.exit("You Win")
    elif int(AICards[0][-1]) > int(playerCards[0][-1]):
      printGame()
      printExtra()
      sys.exit("You Lose")
    else:
      printGame()
      printExtra()
      sys.exit("Draw")
  addAICard()
  printGame()
  time.sleep(5)
  if (AICards[0] == "Countess 7" and (AICards[1] == "King 6" or AICards[1] == "Prince 5")):
    AITurn(0)
  elif ((AICards[0] == "King 6" or AICards[0] == "Prince 5") and AICards[1] == "Countess 7"):
    AITurn(1)
  else:
    answer = random.randint(0,1)
    AITurn(answer)
    
def main():
  addPlayerCard()
  addAICard()
  addDiscard()
  startPlayer()
  
if __name__ == "__main__":
  main()