import random
import os
import time

storeAI = [0]
storePlayer = [0]
boardAI = [4,4,4,4,4,4]
boardPlayer = [4,4,4,4,4,4]
turnInt = [0]

def printBoard():
  os.system("clear")
  print()
  print("Select a pit ordered from left to right on your side of the board")
  print("The number of seeds in that pit are dropped one by one in each pit going counter-clockwise around the board, skipping the other player's store.")
  print("If your last dropped seed lands in your store, you get to go again, and if you land on an empty pit on your side, both your seed and the other player's seeds on the opposite pit get moved into your store.")
  print("When there are no available moves on either player's side (by all pits being empty), the game ends and the remaining seeds on each side go into that side's store.")
  print("Whoever has the most seeds in their store wins.")
  print()
  print()
  print(" ", end =" "), print(boardAI)
  print(str(storeAI[0]) + "                    " + str(storePlayer[0]))
  print(" ", end =" "), print(boardPlayer)
  
def checkForWin():
  numPlayer = 0
  numAI = 0
  for x in range(0, 6):
    if boardPlayer[x] != 0:
      numPlayer += 1
    if boardAI[x] != 0:
      numAI += 1
  if numPlayer == 0 or numAI == 0:
    return True
    
def endGame():
  for x in range(0, len(boardAI)):
    storeAI[0] += boardAI[x]
    boardAI[x] = 0
  for x in range(0, len(boardPlayer)):
    storePlayer[0] += boardPlayer[x]
    boardPlayer[x] = 0
  printBoard()
  if storePlayer[0] > storeAI[0]:
    print("You Win!!!")
  elif storePlayer[0] < storeAI[0]:
    print("You Lose")
  else:
    print("Draw")
  
  
  
  
  
  
#AI Turn
def AIPull(pulled):
  if boardAI[pulled] == 1 and boardPlayer[pulled] != 0:
    storeAI[0] += boardAI[pulled]
    boardAI[pulled] = 0
    storeAI[0] += boardPlayer[pulled]
    boardPlayer[pulled] = 0

def PlayerLeft(amount):
  for x in range(0, len(boardAI)):
    if amount > 0:
      boardPlayer[x] += 1
      amount -= 1
  if amount > 0:
    AIRight(0, amount)
  else:
    printBoard()
    if checkForWin() == True:
      endGame()
    else:
      print(turnInt[0])
      time.sleep(3)
      playerTurn()
  
def addToAIStore(amount):
  storeAI[0] += 1
  amount -= 1
  if amount > 0:
    PlayerLeft(amount)
  else:
    if checkForWin() == True:
      endGame()
    else:
      printBoard()
      time.sleep(3)
      AITurn()
  
def AIRight(pit, amount):
  for x in range(len(boardAI)-pit-1, -1, -1):
    if amount > 0:
      boardAI[x] += 1
      amount -= 1
    if amount == 0 and boardAI[x] == 1:
      amount -= 1
      AIPull(x)
  if amount > 0:
    addToAIStore(amount)
  else:
    printBoard()
    if checkForWin() == True:
      endGame()
    else:
      print(turnInt[0])
      time.sleep(3)
      playerTurn()
  
def moveAI(pit):
  amount = boardAI[len(boardAI)-pit]
  boardAI[len(boardAI)-pit] = 0
  AIRight(pit, amount)
  
def randPit():
  turnInt[0] = random.randint(1,6)
  if boardAI[len(boardAI)-turnInt[0]] == 0:
    return randPit()
  else:
    return turnInt[0]

def AITurn():
  moveAI(randPit())
  
  
  
  
  
  
#Player Turn
def playerPull(pulled):
  if boardPlayer[pulled] == 1 and boardAI[pulled] != 0:
    storePlayer[0] += boardPlayer[pulled]
    boardPlayer[pulled] = 0
    storePlayer[0] += boardAI[pulled]
    boardAI[pulled] = 0

def AILeft(amount):
  for x in range(len(boardAI)-1, -1, -1):
    if amount > 0:
      boardAI[x] += 1
      amount -= 1
  if amount > 0:
    playerRight(0, amount)
  else:
    if checkForWin() == True:
      endGame()
    else:
      printBoard()
      time.sleep(3)
      AITurn()
  
def addToPlayerStore(amount):
  storePlayer[0] += 1
  amount -= 1
  if amount > 0:
    AILeft(amount)
  else:
    printBoard()
    if checkForWin() == True:
      endGame()
    else:
      time.sleep(3)
      playerTurn()
  
def playerRight(pit, amount):
  for x in range(pit, len(boardPlayer)):
    if amount > 0:
      boardPlayer[x] += 1
      amount -= 1
    if amount == 0 and boardPlayer[x] == 1:
      amount -=1
      playerPull(x)
  if amount > 0:
    addToPlayerStore(amount)
  else:
    if checkForWin() == True:
      endGame()
    else:
      printBoard()
      time.sleep(3)
      AITurn()
  
def movePlayer(pit):
  amount = boardPlayer[pit-1]
  boardPlayer[pit-1] = 0
  playerRight(pit, amount)
    

def playerTurn():
  turn = input("Which pit would you like to choose (1-6): ")
  if int(turn) == 1 and boardPlayer[0] != 0:
    movePlayer(1)
  elif int(turn) == 2 and boardPlayer[1] != 0:
    movePlayer(2)
  elif int(turn) == 3 and boardPlayer[2] != 0:
    movePlayer(3)
  elif int(turn) == 4 and boardPlayer[3] != 0:
    movePlayer(4)
  elif int(turn) == 5 and boardPlayer[4] != 0:
    movePlayer(5)
  elif int(turn) == 6 and boardPlayer[5] != 0:
    movePlayer(6)
  else:
    print("Please enter a valid response.")
    playerTurn()
    
    
    
    
    
    
    


def main():
  printBoard()
  playerTurn()
  
if __name__ == "__main__":
    main()