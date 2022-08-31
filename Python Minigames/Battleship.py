import random
import os

LineNum = [1,2,3,4,5,6,7,8,9,10]

PlineA = [0,0,0,0,0,0,0,0,0,0]
PlineB = [0,0,0,0,0,0,0,0,0,0]
PlineC = [0,0,0,0,0,0,0,0,0,0]
PlineD = [0,0,0,0,0,0,0,0,0,0]
PlineE = [0,0,0,0,0,0,0,0,0,0]
PlineF = [0,0,0,0,0,0,0,0,0,0]
PlineG = [0,0,0,0,0,0,0,0,0,0]
PlineH = [0,0,0,0,0,0,0,0,0,0]
PlineI = [0,0,0,0,0,0,0,0,0,0]
PlineJ = [0,0,0,0,0,0,0,0,0,0]

PAlineA = [0,0,0,0,0,0,0,0,0,0]
PAlineB = [0,0,0,0,0,0,0,0,0,0]
PAlineC = [0,0,0,0,0,0,0,0,0,0]
PAlineD = [0,0,0,0,0,0,0,0,0,0]
PAlineE = [0,0,0,0,0,0,0,0,0,0]
PAlineF = [0,0,0,0,0,0,0,0,0,0]
PAlineG = [0,0,0,0,0,0,0,0,0,0]
PAlineH = [0,0,0,0,0,0,0,0,0,0]
PAlineI = [0,0,0,0,0,0,0,0,0,0]
PAlineJ = [0,0,0,0,0,0,0,0,0,0]

AIlineA = [0,0,0,0,0,0,0,0,0,0]
AIlineB = [0,0,0,0,0,0,0,0,0,0]
AIlineC = [0,0,0,0,0,0,0,0,0,0]
AIlineD = [0,0,0,0,0,0,0,0,0,0]
AIlineE = [0,0,0,0,0,0,0,0,0,0]
AIlineF = [0,0,0,0,0,0,0,0,0,0]
AIlineG = [0,0,0,0,0,0,0,0,0,0]
AIlineH = [0,0,0,0,0,0,0,0,0,0]
AIlineI = [0,0,0,0,0,0,0,0,0,0]
AIlineJ = [0,0,0,0,0,0,0,0,0,0]

verticalArray = [PlineA, PlineB, PlineC, PlineD, PlineE, PlineF, PlineG, PlineH, PlineI, PlineJ]
verticalArrayAttack = [PAlineA, PAlineB, PAlineC, PAlineD, PAlineE, PAlineF, PAlineG, PAlineH, PAlineI, PAlineJ]
verticalArrayAI = [AIlineA, AIlineB, AIlineC, AIlineD, AIlineE, AIlineF, AIlineG, AIlineH, AIlineI, AIlineJ]

attackedAI = []
attackedPlayer = []

def printPlayer():
  print("-", end =" "), print(LineNum)
  print("A", end =" "), print(PlineA)
  print("B", end =" "), print(PlineB)
  print("C", end =" "), print(PlineC)
  print("D", end =" "), print(PlineD)
  print("E", end =" "), print(PlineE)
  print("F", end =" "), print(PlineF)
  print("G", end =" "), print(PlineG)
  print("H", end =" "), print(PlineH)
  print("I", end =" "), print(PlineI)
  print("J", end =" "), print(PlineJ)
  
def printPlayerA():
  print("-", end =" "), print(LineNum)
  print("A", end =" "), print(PAlineA)
  print("B", end =" "), print(PAlineB)
  print("C", end =" "), print(PAlineC)
  print("D", end =" "), print(PAlineD)
  print("E", end =" "), print(PAlineE)
  print("F", end =" "), print(PAlineF)
  print("G", end =" "), print(PAlineG)
  print("H", end =" "), print(PAlineH)
  print("I", end =" "), print(PAlineI)
  print("J", end =" "), print(PAlineJ)
  print("\n")
  
def printBoard():
  os.system("clear")
  printPlayerA()
  printPlayer()
  
def getHCoord(location):
  if location[2:3] == "0":
    Horizontal = location[1:3]
  else:
    Horizontal = location[1:2]
    
  if int(Horizontal) > 0  and int(Horizontal) < 11:
    return Horizontal
  else:
    raise ValueError('This is not a coordinate! Please restart.')
  
def placeRightGo(size, horizontal, line):
  for x in range(size):
    if x+int(horizontal)-1 < 0 or x+int(horizontal)-1 > 9:
      raise ValueError('Your ship fell off the world! Please restart.')
    if line[x+int(horizontal)-1] == 0:
      line[x+int(horizontal)-1] = 1
    else:
      raise ValueError('Your ships ran into each other! Please restart.')
  printBoard()
  
def placeLeftGo(size, horizontal, line):
  for x in range(size):
    if int(horizontal)-x-1 < 0 or int(horizontal)-x-1 > 9:
      raise ValueError('Your ship fell off the world! Please restart.')
    if line[int(horizontal)-x-1] == 0:
      line[int(horizontal)-x-1] = 1
    else:
      raise ValueError('Your ships ran into each other! Please restart.')
  printBoard()
  
def placeUpGo(size, horizontal, line):
  for x in range(size):
    if line-x < 0 or line-x > 9:
      raise ValueError('Your ship fell off the world! Please restart.')
    if verticalArray[line-x][int(horizontal)-1] == 0:
      verticalArray[line-x][int(horizontal)-1] = 1
    else:
      raise ValueError('Your ships ran into each other! Please restart.')
  printBoard()
  
def placeDownGo(size, horizontal, line):
  for x in range(size):
    if line+x < 0 or line+x > 9:
      raise ValueError('Your ship fell off the world! Please restart.')
    if verticalArray[line+x][int(horizontal)-1] == 0:
      verticalArray[line+x][int(horizontal)-1] = 1
    else:
      raise ValueError('Your ships ran into each other! Please restart.')
  printBoard()
    
  
def placeRight(size, location, copy):
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical.upper() == "A":
    placeRightGo(size, Horizontal, PlineA)
  elif Vertical.upper() == "B":
    placeRightGo(size, Horizontal, PlineB)
  elif Vertical.upper() == "C":
    placeRightGo(size, Horizontal, PlineC)
  elif Vertical.upper() == "D":
    placeRightGo(size, Horizontal, PlineD)
  elif Vertical.upper() == "E":
    placeRightGo(size, Horizontal, PlineE)
  elif Vertical.upper() == "F":
    placeRightGo(size, Horizontal, PlineF)
  elif Vertical.upper() == "G":
    placeRightGo(size, Horizontal, PlineG)
  elif Vertical.upper() == "H":
    placeRightGo(size, Horizontal, PlineH)
  elif Vertical.upper() == "I":
    placeRightGo(size, Horizontal, PlineI)
  elif Vertical.upper() == "J":
    placeRightGo(size, Horizontal, PlineJ)
  else:
    print("Invalid coodinate " + Vertical + Horizontal + "! Please try again.")
    if size == 5:
      placeMassive()
    elif size == 4:
      placeBig()
    elif size == 3 and copy == 1:
      placeMedium1()
    elif size == 3 and copy == 2:
      placeMedium2()
    elif size == 2:
      placeSmall()
  
def placeLeft(size, location, copy):
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical.upper() == "A":
    placeLeftGo(size, Horizontal, PlineA)
  elif Vertical.upper() == "B":
    placeLeftGo(size, Horizontal, PlineB)
  elif Vertical.upper() == "C":
    placeLeftGo(size, Horizontal, PlineC)
  elif Vertical.upper() == "D":
    placeLeftGo(size, Horizontal, PlineD)
  elif Vertical.upper() == "E":
    placeLeftGo(size, Horizontal, PlineE)
  elif Vertical.upper() == "F":
    placeLeftGo(size, Horizontal, PlineF)
  elif Vertical.upper() == "G":
    placeLeftGo(size, Horizontal, PlineG)
  elif Vertical.upper() == "H":
    placeLeftGo(size, Horizontal, PlineH)
  elif Vertical.upper() == "I":
    placeLeftGo(size, Horizontal, PlineI)
  elif Vertical.upper() == "J":
    placeLeftGo(size, Horizontal, PlineJ)
  else:
    print("Invalid coodinate " + Vertical + Horizontal + "! Please try again.")
    if size == 5:
      placeMassive()
    elif size == 4:
      placeBig()
    elif size == 3 and copy == 1:
      placeMedium1()
    elif size == 3 and copy == 2:
      placeMedium2()
    elif size == 2:
      placeSmall()
    
def placeUp(size, location, copy):
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical.upper() == "A":
    placeUpGo(size, Horizontal, 0)
  elif Vertical.upper() == "B":
    placeUpGo(size, Horizontal, 1)
  elif Vertical.upper() == "C":
    placeUpGo(size, Horizontal, 2)
  elif Vertical.upper() == "D":
    placeUpGo(size, Horizontal, 3)
  elif Vertical.upper() == "E":
    placeUpGo(size, Horizontal, 4)
  elif Vertical.upper() == "F":
    placeUpGo(size, Horizontal, 5)
  elif Vertical.upper() == "G":
    placeUpGo(size, Horizontal, 6)
  elif Vertical.upper() == "H":
    placeUpGo(size, Horizontal, 7)
  elif Vertical.upper() == "I":
    placeUpGo(size, Horizontal, 8)
  elif Vertical.upper() == "J":
    placeUpGo(size, Horizontal, 9)
  else:
    print("Invalid coodinate " + Vertical + Horizontal + "! Please try again.")
    if size == 5:
      placeMassive()
    elif size == 4:
      placeBig()
    elif size == 3 and copy == 1:
      placeMedium1()
    elif size == 3 and copy == 2:
      placeMedium2()
    elif size == 2:
      placeSmall()
    
def placeDown(size, location, copy):
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical.upper() == "A":
    placeDownGo(size, Horizontal, 0)
  elif Vertical.upper() == "B":
    placeDownGo(size, Horizontal, 1)
  elif Vertical.upper() == "C":
    placeDownGo(size, Horizontal, 2)
  elif Vertical.upper() == "D":
    placeDownGo(size, Horizontal, 3)
  elif Vertical.upper() == "E":
    placeDownGo(size, Horizontal, 4)
  elif Vertical.upper() == "F":
    placeDownGo(size, Horizontal, 5)
  elif Vertical.upper() == "G":
    placeDownGo(size, Horizontal, 6)
  elif Vertical.upper() == "H":
    placeDownGo(size, Horizontal, 7)
  elif Vertical.upper() == "I":
    placeDownGo(size, Horizontal, 8)
  elif Vertical.upper() == "J":
    placeDownGo(size, Horizontal, 9)
  else:
    print("Invalid coodinate " + Vertical + Horizontal + "! Please try again.")
    if size == 5:
      placeMassive()
    elif size == 4:
      placeBig()
    elif size == 3 and copy == 1:
      placeMedium1()
    elif size == 3 and copy == 2:
      placeMedium2()
    elif size == 2:
      placeSmall()
  
def place(size, location, copy):
  if "Down" in location or "down" in location:
    placeDown(size, location, copy)
  elif "Up" in location or "up" in location:
    placeUp(size, location, copy)
  elif "Right" in location or "right" in location:
    placeRight(size, location, copy)
  elif "Left" in location or "left" in location:
    placeLeft(size, location, copy)
  else:
    print("Invalid direction " + location + "! Please try again.")
    if size == 5:
      placeMassive()
    elif size == 4:
      placeBig()
    elif size == 3 and copy == 1:
      placeMedium1()
    elif size == 3 and copy == 2:
      placeMedium2()
    elif size == 2:
      placeSmall()
    
def placeMassive():
  Massive = input("Where would you like to place the 5 long ship (Input coordinate(A1 - J10) and direction(Up, Down, Left, Right) Ex. A1 Down): ")
  place(5, Massive, 0)
  
def placeBig():
  Big = input("Where would you like to place the 4 long ship (Input coordinate(A1 - J10) and direction(Up, Down, Left, Right) Ex. A1 Down): ")
  place(4, Big, 0)
  
def placeMedium1():
  Medium1 = input("Where would you like to place a 3 long ship (Input coordinate(A1 - J10) and direction(Up, Down, Left, Right) Ex. A1 Down): ")
  place(3, Medium1, 1)
  
def placeMedium2():
  Medium2 = input("Where would you like to place a 3 long ship (Input coordinate(A1 - J10) and direction(Up, Down, Left, Right) Ex. A1 Down): ")
  place(3, Medium2, 2)
  
def placeSmall():
  Small = input("Where would you like to place the 2 long ship (Input coordinate(A1 - J10) and direction(Up, Down, Left, Right) Ex. A1 Down): ")
  place(2, Small, 0)
  
def placePieces():
  placeMassive()
  placeBig()
  placeMedium1()
  placeMedium2()
  placeSmall()
  
def placeAIRightGo(size, horizontal, line):
  for x in range(size):
    if x+int(horizontal)-1 < 0 or x+int(horizontal)-1 > 9:
      raise ValueError('The AIs ship fell off the world! Please restart.')
    if line[x+int(horizontal)-1] == 0:
      line[x+int(horizontal)-1] = 1
    else:
      raise ValueError('The AIs  ships ran into each other! Please restart.')
  printBoard()
  
def placeAILeftGo(size, horizontal, line):
  for x in range(size):
    if int(horizontal)-x-1 < 0 or int(horizontal)-x-1 > 9:
      raise ValueError('The AIs  ship fell off the world! Please restart.')
    if line[int(horizontal)-x-1] == 0:
      line[int(horizontal)-x-1] = 1
    else:
      raise ValueError('The AIs  ships ran into each other! Please restart.')
  printBoard()
  
def placeAIUpGo(size, horizontal, line):
  for x in range(size):
    if line-x < 0 or line-x > 9:
      raise ValueError('The AIs  ship fell off the world! Please restart.')
    if verticalArrayAI[line-x][int(horizontal)-1] == 0:
      verticalArrayAI[line-x][int(horizontal)-1] = 1
    else:
      raise ValueError('The AIs ships ran into each other! Please restart.')
  printBoard()
  
def placeAIDownGo(size, horizontal, line):
  for x in range(size):
    if line+x < 0 or line+x > 9:
      raise ValueError('The AIs  ship fell off the world! Please restart.')
    if verticalArrayAI[line+x][int(horizontal)-1] == 0:
      verticalArrayAI[line+x][int(horizontal)-1] = 1
    else:
      raise ValueError('The AIs  ships ran into each other! Please restart.')
  printBoard()
    
  
def placeAIRight(size, location):
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical == "A":
    placeAIRightGo(size, Horizontal, AIlineA)
  elif Vertical == "B":
    placeAIRightGo(size, Horizontal, AIlineB)
  elif Vertical == "C":
    placeAIRightGo(size, Horizontal, AIlineC)
  elif Vertical == "D":
    placeAIRightGo(size, Horizontal, AIlineD)
  elif Vertical == "E":
    placeAIRightGo(size, Horizontal, AIlineE)
  elif Vertical == "F":
    placeAIRightGo(size, Horizontal, AIlineF)
  elif Vertical == "G":
    placeAIRightGo(size, Horizontal, AIlineG)
  elif Vertical == "H":
    placeAIRightGo(size, Horizontal, AIlineH)
  elif Vertical == "I":
    placeAIRightGo(size, Horizontal, AIlineI)
  elif Vertical == "J":
    placeAIRightGo(size, Horizontal, AIlineJ)
  else:
    print("This AI sucks! " + Vertical + Horizontal + ". Please try again.")
  
def placeAILeft(size, location):
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical == "A":
    placeAILeftGo(size, Horizontal, AIlineA)
  elif Vertical == "B":
    placeAILeftGo(size, Horizontal, AIlineB)
  elif Vertical == "C":
    placeAILeftGo(size, Horizontal, AIlineC)
  elif Vertical == "D":
    placeAILeftGo(size, Horizontal, AIlineD)
  elif Vertical == "E":
    placeAILeftGo(size, Horizontal, AIlineE)
  elif Vertical == "F":
    placeAILeftGo(size, Horizontal, AIlineF)
  elif Vertical == "G":
    placeAILeftGo(size, Horizontal, AIlineG)
  elif Vertical == "H":
    placeAILeftGo(size, Horizontal, AIlineH)
  elif Vertical == "I":
    placeAILeftGo(size, Horizontal, AIlineI)
  elif Vertical == "J":
    placeAILeftGo(size, Horizontal, AIlineJ)
  else:
    print("This AI sucks! " + Vertical + Horizontal + ". Please try again.")
    
def placeAIUp(size, location):
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical == "A":
    placeAIUpGo(size, Horizontal, 0)
  elif Vertical == "B":
    placeAIUpGo(size, Horizontal, 1)
  elif Vertical == "C":
    placeAIUpGo(size, Horizontal, 2)
  elif Vertical == "D":
    placeAIUpGo(size, Horizontal, 3)
  elif Vertical == "E":
    placeAIUpGo(size, Horizontal, 4)
  elif Vertical == "F":
    placeAIUpGo(size, Horizontal, 5)
  elif Vertical == "G":
    placeAIUpGo(size, Horizontal, 6)
  elif Vertical == "H":
    placeAIUpGo(size, Horizontal, 7)
  elif Vertical == "I":
    placeAIUpGo(size, Horizontal, 8)
  elif Vertical == "J":
    placeAIUpGo(size, Horizontal, 9)
  else:
    print("This AI sucks! " + Vertical + Horizontal + ". Please try again.")
    
def placeAIDown(size, location):
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical == "A":
    placeAIDownGo(size, Horizontal, 0)
  elif Vertical == "B":
    placeAIDownGo(size, Horizontal, 1)
  elif Vertical == "C":
    placeAIDownGo(size, Horizontal, 2)
  elif Vertical == "D":
    placeAIDownGo(size, Horizontal, 3)
  elif Vertical == "E":
    placeAIDownGo(size, Horizontal, 4)
  elif Vertical == "F":
    placeAIDownGo(size, Horizontal, 5)
  elif Vertical == "G":
    placeAIDownGo(size, Horizontal, 6)
  elif Vertical == "H":
    placeAIDownGo(size, Horizontal, 7)
  elif Vertical == "I":
    placeAIDownGo(size, Horizontal, 8)
  elif Vertical == "J":
    placeAIDownGo(size, Horizontal, 9)
  else:
    print("This AI sucks! " + Vertical + Horizontal + ". Please try again.")
  
def placeAI(size, location):
  if "Down" in location:
    placeAIDown(size, location)
  elif "Up" in location:
    placeAIUp(size, location)
  elif "Right" in location:
    placeAIRight(size, location)
  elif "Left" in location:
    placeAILeft(size, location)
  else:
    print("This AI sucks! " + location + ". Please try again.")
    placeAIPieces()
  
def placeAIPieces():
  placeAI(5, "B2 Right")
  placeAI(4, "I9 Up")
  placeAI(3, "G2 Right")
  placeAI(3, "C6 Down")
  placeAI(2, "I5 Down")
  
def attackGoPlayer(array, hori, vert):
  if int(hori) < 1 or int(hori) > 10:
    print('The AIs  ship fell off the world! Please restart.')
    playerAttack()
  if array[vert][int(hori)-1] == 0:
    array[vert][int(hori)-1] = 8
    verticalArrayAttack[vert][int(hori)-1] = 8
    print("Miss!")
  elif array[vert][int(hori)-1] == 1:
    array[vert][int(hori)-1] = 7
    verticalArrayAttack[vert][int(hori)-1] = 7
    print("Hit!")
  else:
    raise ValueError('You already attacked there! Please restart.')
    
def attackGo(array, hori, vert):
  if int(hori) < 1 or int(hori) > 10:
    print('The AIs  ship fell off the world! Please restart.')
    playerAttack()
  if array[vert][int(hori)-1] == 0:
    array[vert][int(hori)-1] = 8
    print("Miss!")
  elif array[vert][int(hori)-1] == 1:
    array[vert][int(hori)-1] = 7
    print("Hit!")
  else:
    raise ValueError('You already attacked there! Please restart.')
  
def attackPlayer(location, array):
  os.system("clear")
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical == "A":
    attackGoPlayer(array, Horizontal, 0)
  elif Vertical == "B":
    attackGoPlayer(array, Horizontal, 1)
  elif Vertical == "C":
    attackGoPlayer(array, Horizontal, 2)
  elif Vertical == "D":
    attackGoPlayer(array, Horizontal, 3)
  elif Vertical == "E":
    attackGoPlayer(array, Horizontal, 4)
  elif Vertical == "F":
    attackGoPlayer(array, Horizontal, 5)
  elif Vertical == "G":
    attackGoPlayer(array, Horizontal, 6)
  elif Vertical == "H":
    attackGoPlayer(array, Horizontal, 7)
  elif Vertical == "I":
    attackGoPlayer(array, Horizontal, 8)
  elif Vertical == "J":
    attackGoPlayer(array, Horizontal, 9)
  else:
    print("This AI sucks! " + Vertical + Horizontal + ". Please try again.")
    
def attackAI(location, array):
  Vertical = location[0:1]
  Horizontal = getHCoord(location)
  if Vertical == "A":
    attackGo(array, Horizontal, 0)
  elif Vertical == "B":
    attackGo(array, Horizontal, 1)
  elif Vertical == "C":
    attackGo(array, Horizontal, 2)
  elif Vertical == "D":
    attackGo(array, Horizontal, 3)
  elif Vertical == "E":
    attackGo(array, Horizontal, 4)
  elif Vertical == "F":
    attackGo(array, Horizontal, 5)
  elif Vertical == "G":
    attackGo(array, Horizontal, 6)
  elif Vertical == "H":
    attackGo(array, Horizontal, 7)
  elif Vertical == "I":
    attackGo(array, Horizontal, 8)
  elif Vertical == "J":
    attackGo(array, Horizontal, 9)
  else:
    print("This AI sucks! " + Vertical + Horizontal + ". Please try again.")
    
def checkIfPlayerWin():
  ships = 0
  for x in range(0, len(verticalArrayAI)):
    for y in range(0,10):
      if verticalArrayAI[x][y] == "1":
        ships += 1
  if ships == "0":
    printBoardNoClear()
    print("You Win!!!")
    
def checkIfAIWin():
  ships = 0
  for x in range(0, len(verticalArray)):
    for y in range(0,10):
      if verticalArray[x][y] == "1":
        ships += 1
  if ships == "0":
    print("You Lose!!!")
  else:
    playGame()
    
def printBoardNoClear():
  printPlayerA()
  printPlayer()
  
def playerAttack():
  attackInput = input("Where would you like to strike (Input coordinate(A1 - J10)): ")
  attackPlayer(attackInput, verticalArrayAI)
  checkIfPlayerWin()
  
def randomCoord():
  letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
  randAttackVert = random.randint(0, 9)
  randAttackHori = random.randint(1, 10)
  randAttack = letters[randAttackVert] + str(randAttackHori)
  print(randAttack)
  if len(attackedAI) == 0:
    attackedAI.append(randAttack)
    return randAttack
  else:
    for x in attackedAI:
      if randAttack == x:
        randomCoord()
  attackedAI.append(randAttack)
  return randAttack
  
def AIAttack():
  attackAI(randomCoord(), verticalArray)
  printBoardNoClear()
  checkIfAIWin()
  
def playGame():
  playerAttack()
  AIAttack()
  
  
def start():
  printBoard()
  placePieces()
  placeAIPieces()
  playGame()

def main():
  start()
  
if __name__ == "__main__":
    main()