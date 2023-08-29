import random
import os
import sys
import time
import math

world0 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world1 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world2 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world3 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world4 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world5 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world6 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world7 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world8 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world9 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world10 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world11 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world12 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world13 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world14 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world15 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world16 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world17 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world18 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
world19 = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

worlds = [world0, world1, world2, world3, world4, world5, world6, world7, world8, world9, world10, world11, world12, world13, world14, world15, world16, world17, world18, world19]

place = [False]
inside = [False]

city = ["C", "City"]
merchant = ["G", "Merchant"]
dungeon = ["D", "Dungeon"]
camp = ["E", "Monster Camp"]
schools = ["S", "School"]
trees = ["T", "Trees"]
water = ["W", "Water"]
mountain = ["M", "Mountain"]
empty = ["_", "Empty"]
house = ["H", "House"]
locations = [city, merchant, dungeon, camp, schools, trees, water, mountain, empty, house]

race = [""]
school = [""]
lvl = [0]
maxHp = [100]
hp = [0]
mp = [0]
xp = [0]
spells = []
abilities = [""]
potion = [0]
mana = [0]
damageAmt = [0]
passive = [""]
goldAmt = [0]
oreAmt = [0]
woodAmt = [0]
fishAmt = [0]

chop = [0]

fireBlock = [False]

house = [0, 0]
houseReal = [False]

multiplyer = [1]
perception = [0]

cooldown = [0]

boon = [False]
slide = [False]

monsterName = [""]
monsterHp = [0]
monsterMaxHp = [0]
monsterMp = [0]
monsterDamage = [0]
monsterSpell = [0]

monsterNum = [10]

goblin = ["Goblin", "20", "0", "6", "0"]
bandit = ["Bandit", "30", "10", "8", "8"]
ogre = ["Ogre", "40", "20", "8", "10"]
minotaur = ["Minotaur", "80", "0", "10", "0"]
lich = ["Lich", "200", "50", "20", "12"]
monsters = [goblin, goblin, goblin, bandit, bandit, ogre, ogre, minotaur, lich]

def printWorld():
  permLocations()
  permHouse()
  os.system("clear")
  print()
  print(world0)
  print(world1)
  print(world2)
  print(world3)
  print(world4)
  print(world5)
  print(world6)
  print(world7)
  print(world8)
  print(world9)
  print(world10)
  print(world11)
  print(world12)
  print(world13)
  print(world14)
  print(world15)
  print(world16)
  print(world17)
  print(world18)
  print(world19)
  print()
  printPlayer()
  
def addLocation(x, y, locationID):
  location = findA()
  if location[0] == x and location[1] == y and locationID == 6:
    boon[0] = True
  if location[0] == x and location[1] == y and locationID == 7:
    slide[0] = True
    
  if location [0] != x or location[1] != y:
    worlds[y][x] = locations[locationID][0]
    
def addPlayer(x, y):
  raceAnswer = input("What race would you like to play as (Human, Dwarf, Orc, Troll): ")
  schoolAnswer = input("What school would you like to learn from (Fire, Water, Earth, Air): ")
  worlds[y][x] = "A"
  lvl[0] = 1
  hp[0] = maxHp[0]
  mp[0] = 100
  damageAmt[0] = 6
  
  if raceAnswer.lower() == "human":
    race[0] = "Human"
  elif raceAnswer.lower() == "dwarf":
    race[0] = "Dwarf"
  elif raceAnswer.lower() == "orc":
    race[0] = "Orc"
  elif raceAnswer.lower() == "troll":
    race[0] = "Troll"
    
  if schoolAnswer.lower() == "fire":
    school[0] = "Fire"
  elif schoolAnswer.lower() == "water":
    school[0] = "Water"
  elif schoolAnswer.lower() == "earth":
    school[0] = "Earth"
  elif schoolAnswer.lower() == "air":
    school[0] = "Air"
    
  if race[0] == "Human":
    abilities[0] = "Perception"
  elif race[0] == "Dwarf":
    abilities[0] = "Upgrade"
  elif race[0] == "Orc":
    abilities[0] = "Rage"
  elif race[0] == "Troll":
    abilities[0] = "Regenerate"
  
  if school[0] == "Fire":
    passive[0] = "Fire Shield (Take less magic damage)"
  elif school[0] == "Water":
    passive[0] = "Luck of the Sea (Easier to catch fish (Activated by Posideon's Bounty))"
  elif school[0] == "Earth":
    passive[0] = "Quick Pick (Find ore while moving through rock (Activated by Earth Glide))"
  elif school[0] == "Air":
    passive[0] = "Wind Cutter (Instantly cut down trees)"
    
def findA():
  for y in range(0, 20):
    for x in range(0, 20):
      if worlds[y][x] == "A":
        return [x, y]
        
def getLocation(x, y):
  return worlds[y][x]
  
def nextTo(location):
  current = findA()
  left = getLocation(current[0] - 1, current[1])
  right = getLocation(current[0] + 1, current[1])
  up = getLocation(current[0], current[1] - 1)
  down = getLocation(current[0], current[1] + 1)
  if left == location or right == location or up == location or down == location:
    return True
  else:
    return False
    
#sell in cities
#buy in cities(heal, mana, weapon (higher prices))

#if stay in safe place, stay safe

#count the days
def playerRight():
  location = findA()
  if location[0] == 19:
    print("You must not leave the kingdom.")
    move()
  else:
    checkForLocation(worlds[location[1]][location[0]+1])
    if worlds[location[1]][location[0]+1] == "W" and boon[0] == True:
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]][location[0]+1] = "A"
    elif worlds[location[1]][location[0]+1] == "M" and slide[0] == True:
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]][location[0]+1] = "A"
    elif worlds[location[1]][location[0]+1] != "W" and worlds[location[1]][location[0]+1] != "M" and worlds[location[1]][location[0]+1] != "T":
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]][location[0]+1] = "A"
  printWorld()
  
def playerLeft():
  location = findA()
  if location[0] == 0:
    print("You must not leave the kingdom.")
    move()
  else:
    checkForLocation(worlds[location[1]][location[0]-1])
    if worlds[location[1]][location[0]-1] == "W" and boon[0] == True:
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]][location[0]-1] = "A"
    elif worlds[location[1]][location[0]-1] == "M" and slide[0] == True:
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]][location[0]-1] = "A"
    elif worlds[location[1]][location[0]-1] != "W" and worlds[location[1]][location[0]-1] != "M" and worlds[location[1]][location[0]-1] != "T":
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]][location[0]-1] = "A"
  printWorld()
  
def playerDown():
  location = findA()
  if location[1] == 19:
    print("You must not leave the kingdom.")
    move()
  else:
    checkForLocation(worlds[location[1]+1][location[0]])
    if worlds[location[1]+1][location[0]] == "W" and boon[0] == True:
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]+1][location[0]] = "A"
    elif worlds[location[1]+1][location[0]] == "M" and slide[0] == True:
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]+1][location[0]] = "A"
    elif worlds[location[1]+1][location[0]] != "W" and worlds[location[1]+1][location[0]] != "M" and worlds[location[1]+1][location[0]] != "T":
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]+1][location[0]] = "A"
  printWorld()
  
def playerUp():
  location = findA()
  if location[1] == 0:
    print("You must not leave the kingdom.")
    move()
  else:
    checkForLocation(worlds[location[1]-1][location[0]])
    if worlds[location[1]-1][location[0]] == "W" and boon[0] == True:
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]-1][location[0]] = "A"
    elif worlds[location[1]-1][location[0]] == "M" and slide[0] == True:
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]-1][location[0]] = "A"
    elif worlds[location[1]-1][location[0]] != "W" and worlds[location[1]-1][location[0]] != "M" and worlds[location[1]-1][location[0]] != "T":
      worlds[location[1]][location[0]] = "_"
      worlds[location[1]-1][location[0]] = "A"
  printWorld()
  
def checkForLocation(location):
  if location == "C":
    place[0] = True
    if goldAmt[0] > 50:
      goldAmt[0] -= 50
      hp[0] = maxHp[0]
      mp[0] = 100
      cooldown[0] = 0
  elif location == "H":
    place[0] = True
    hp[0] = maxHp[0]
    mp[0] = 100
    cooldown[0] = 0
  elif location == "S":
    place[0] = True
    if len(spells) == 0 and lvl[0] >= 1 and lvl[0] < 5:
      if school[0] == "Fire":
        spells.append("Firebolt")
      elif school[0] == "Water":
        spells.append("Ball O' Water")
      elif school[0] == "Earth":
        spells.append("Rock Throw")
      elif school[0] == "Air":
        spells.append("Toss")
    elif len(spells) == 0 and lvl[0] >= 5 and lvl[0] < 10:
      if school[0] == "Fire":
        spells.append("Firebolt")
        spells.append("Flame Dash")
      elif school[0] == "Water":
        spells.append("Ball O' Water")
        spells.append("Posideon's Bounty")
      elif school[0] == "Earth":
        spells.append("Rock Throw")
        spells.append("Earth Glide")
      elif school[0] == "Air":
        spells.append("Toss")
        spells.append("Step of the Wind")
    elif len(spells) == 0 and lvl[0] >= 10:
      if school[0] == "Fire":
        spells.append("Firebolt")
        spells.append("Flame Dash")
        spells.append("Fireball")
      elif school[0] == "Water":
        spells.append("Ball O' Water")
        spells.append("Posideon's Bounty")
        spells.append("Tidal Wave")
      elif school[0] == "Earth":
        spells.append("Rock Throw")
        spells.append("Earth Glide")
        spells.append("Entomb")
      elif school[0] == "Air":
        spells.append("Toss")
        spells.append("Step of the Wind")
        spells.append("Tornado")
    elif len(spells) == 1 and lvl[0] >= 5 and lvl[0] < 10:
      if school[0] == "Fire":
        spells.append("Flame Dash")
      elif school[0] == "Water":
        spells.append("Posideon's Bounty")
      elif school[0] == "Earth":
        spells.append("Earth Glide")
      elif school[0] == "Air":
        spells.append("Step of the Wind")
    elif len(spells) == 1 and lvl[0] >= 10:
      if school[0] == "Fire":
        spells.append("Flame Dash")
        spells.append("Fireball")
      elif school[0] == "Water":
        spells.append("Posideon's Bounty")
        spells.append("Tidal Wave")
      elif school[0] == "Earth":
        spells.append("Earth Glide")
        spells.append("Entomb")
      elif school[0] == "Air":
        spells.append("Step of the Wind")
        spells.append("Tornado")
    elif len(spells) == 2 and lvl[0] >= 10:
      if school[0] == "Fire":
        spells.append("Fireball")
      elif school[0] == "Water":
        spells.append("Tidal Wave")
      elif school[0] == "Earth":
        spells.append("Entomb")
      elif school[0] == "Air":
        spells.append("Tornado")
  elif location == "G":
    place[0] = True
    print("Type 'leave' to leave without buying anything. The merchant will still leave the area.")
    print()
    answer = input("Would you like to buy a healing potion(20g), mana potion(30g), or weapon upgrade(10g) (Type the name of what you want to buy): ")
    if answer.lower() == "healing potion" and goldAmt[0] >= 20:
      goldAmt[0] -= 20
      potion[0] += 1
    elif answer.lower() == "mana potion" and goldAmt[0] >= 30:
      goldAmt[0] -= 30
      mana[0] += 1
    elif answer.lower() == "weapon upgrade" and goldAmt[0] >= 10:
      goldAmt[0] -= 10
      damageAmt[0] += 1
    elif answer.lower() == "leave":
      time.sleep(1)
    else:
      checkForLocation(location)
  elif location == "E":
    place[0] = True
    os.system("clear")
    monsterNum = random.randint(0, len(monsters)-2)
    setMonster(monsterNum)
    battle()
    os.system("clear")
    monsterNum = random.randint(0, len(monsters)-2)
    setMonster(monsterNum)
    battle()
  elif location == "D":
    place[0] = True
    inside[0] = True
    os.system("clear")
    monsterNum = random.randint(0, len(monsters)-2)
    setMonster(monsterNum)
    battle()
    os.system("clear")
    monsterNum = random.randint(0, len(monsters)-2)
    setMonster(monsterNum)
    battle()
    os.system("clear")
    monsterNum = random.randint(0, len(monsters)-2)
    setMonster(monsterNum)
    battle()
    os.system("clear")
    setMonster(len(monsters)-1)
    battle()
    sys.exit("You have saved the kingdom!!!")
    
def getOptions():
  options = []
  options.append("Left (a)")
  options.append("Right (d)")
  options.append("Up (w)")
  options.append("Down (s)")
  if potion[0] > 0:
    options.append("Use healing potion (heal)")
  if mana[0] > 0:
    options.append("Use mana potion (mana)")
  if nextTo("M"):
    options.append("Go mining (mine)")
  if nextTo("W"):
    options.append("Go fishing (fish)")
  if nextTo("T"):
    options.append("Try chopping a tree (chop)")
  if woodAmt[0] >= 30 and oreAmt[0] >= 10 and goldAmt[0] >= 100 and nextTo("_"):
    options.append("Build a house (build)")
  if race[0] == "Dwarf":
    if cooldown[0] == 0 and oreAmt[0] > 0:
      options.append("Use ability (upgrade)")
  else:
    if cooldown[0] == 0:
      options.append("Use ability (" + abilities[0].lower() + ")")
  if school[0] == "Water" and len(spells) >= 2 and nextTo("W") and boon[0] == False:
    options.append("Cast Posideon's Bounty (posideon's bounty)")
  if school[0] == "Earth" and len(spells) >= 2 and nextTo("M") and slide[0] == False:
    options.append("Cast Earth Glide (earth glide)")
  options.append("Rest (rest)")
  return options
  
def move():
  movement = input("What would you like to do: ")
  if mp[0] < 100:
    mp[0] += 5
    if mp[0] > 100:
      mp[0] = 100
  if movement.lower() == "a":
    chop[0] = 0
    playerLeft()
  elif movement.lower() == "d":
    chop[0] = 0
    playerRight()
  elif movement.lower() == "w":
    chop[0] = 0
    playerUp()
  elif movement.lower() == "s":
    chop[0] = 0
    playerDown()
  elif movement.lower() == "heal":
    if potion[0] > 0:
      healing = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + 4
      hp[0] += healing
      potion[0] -= 1
      if hp[0] > maxHp[0]:
        hp[0] = maxHp[0]
    printWorld()
  elif movement.lower() == "mana":
    if mana[0] > 0:
      regen = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + 4
      mp[0] += regen
      mana[0] -= 1
      if mp[0] > 100:
        mp[0] = 100
    printWorld()
  elif movement.lower() == "rest":
    if goldAmt[0] >= 10:
      goldAmt[0] -= 10
      if hp[0] < maxHp[0]:
        if fishAmt[0] > 0:
          fishAmt[0] -= 1
          hp[0] += 20
          if hp[0] > maxHp[0]:
            hp[0] = maxHp[0]
        else:
          hp[0] += 10
          if hp[0] > maxHp[0]:
            hp[0] = maxHp[0]
    printWorld()
  elif movement.lower() == "perception" and race[0] == "Human" and cooldown[0] == 0:
    perception[0] = 11
    cooldown[0] = 16
    printWorld()
  elif movement.lower() == "upgrade" and race[0] == "Dwarf" and cooldown[0] == 0 and oreAmt[0] > 0:
    damageAmt[0] += 3
    oreAmt[0] -= 1
    cooldown[0] = 16
    printWorld()
  elif movement.lower() == "regenerate" and race[0] == "Troll" and cooldown[0] == 0:
    hp[0] += 50
    if hp[0] > maxHp[0]:
      hp[0] = maxHp[0]
    cooldown[0] = 16
    printWorld()
  elif movement.lower() == "mine" and nextTo("M"):
    chance = random.randint(1, 3)
    if chance == 3:
      numOre = random.randint(0, 3)
      oreAmt[0] += numOre
      xp[0] += numOre * 2
    printWorld()
  elif movement.lower() == "fish" and nextTo("W"):
    if boon[0] == True:
      chance = random.randint(1, 3)
      xp[0] += 1
      if chance == 3:
        fishAmt[0] += 1
        xp[0] += random.randint(1, 5)
        maxHp[0] += 5
    else:
      chance = random.randint(1, 5)
      xp[0] += 1
      if chance == 5:
        fishAmt[0] += 1
        xp[0] += random.randint(1, 8)
        maxHp[0] += 5
    printWorld()
  elif movement.lower() == "chop" and nextTo("T"):
    chop[0] += 1
    if chop[0] == 1 and school[0] == "Air":
      chop[0] = 0
      current = findA()
      tree = input("Which tree do you want to fell? (Left(a), Right(d), Up(w), Down(s))")
      if tree.lower() == "a" and getLocation(current[0] - 1, current[1]) == "T":
        addLocation(current[0] - 1, current[1], 8)
        woodAmt[0] += random.randint(3, 8)
        xp[0] += random.randint(1, 3)
      elif tree.lower() == "d" and getLocation(current[0] + 1, current[1]) == "T":
        addLocation(current[0] + 1, current[1], 8)
        woodAmt[0] += random.randint(3, 8)
        xp[0] += random.randint(1, 3)
      elif tree.lower() == "w" and getLocation(current[0], current[1] - 1) == "T":
        addLocation(current[0], current[1] - 1, 8)
        woodAmt[0] += random.randint(3, 8)
        xp[0] += random.randint(1, 3)
      elif tree.lower() == "s" and getLocation(current[0], current[1] + 1) == "T":
        addLocation(current[0], current[1] + 1, 8)
        woodAmt[0] += random.randint(3, 8)
        xp[0] += random.randint(1, 3)
    elif chop[0] == 3:
      chop[0] = 0
      current = findA()
      tree = input("Which tree do you want to fell? (Left(a), Right(d), Up(w), Down(s)): ")
      if tree.lower() == "a" and getLocation(current[0] - 1, current[1]) == "T":
        addLocation(current[0] - 1, current[1], 8)
        woodAmt[0] += random.randint(3, 8)
        xp[0] += random.randint(1, 3)
      elif tree.lower() == "d" and getLocation(current[0] + 1, current[1]) == "T":
        addLocation(current[0] + 1, current[1], 8)
        woodAmt[0] += random.randint(3, 8)
        xp[0] += random.randint(1, 3)
      elif tree.lower() == "w" and getLocation(current[0], current[1] - 1) == "T":
        addLocation(current[0], current[1] - 1, 8)
        woodAmt[0] += random.randint(3, 8)
        xp[0] += random.randint(1, 3)
      elif tree.lower() == "s" and getLocation(current[0], current[1] + 1) == "T":
        addLocation(current[0], current[1] + 1, 8)
        woodAmt[0] += random.randint(3, 8)
        xp[0] += random.randint(1, 3)
    printWorld()
  elif movement.lower() == "build" and nextTo("_"):
    if woodAmt[0] >= 30 and oreAmt[0] >= 10 and goldAmt[0] >= 100:
      place = input("Where do you want to build your house?  (Left(a), Right(d), Up(w), Down(s)): ")
      current = findA()
      if place.lower() == "a" and getLocation(current[0] - 1, current[1]) == "_":
        house[0] = current[0] - 1
        house[1] = current[1]
        houseReal[0] = True
        permHouse()
      elif place.lower() == "d" and getLocation(current[0] + 1, current[1]) == "_":
        house[0] = current[0] + 1
        house[1] = current[1]
        houseReal[0] = True
        permHouse()
      elif place.lower() == "w" and getLocation(current[0], current[1] - 1) == "_":
        house[0] = current[0]
        house[1] = current[1] - 1
        houseReal[0] = True
        permHouse()
      elif place.lower() == "s" and getLocation(current[0], current[1] + 1) == "_":
        house[0] = current[0]
        house[1] = current[1] + 1
        houseReal[0] = True
        permHouse()
      else:
        move()
      woodAmt[0] -= 30
      oreAmt[0] -= 10
      goldAmt[0] -= 100
    printWorld()
  elif movement.lower() == "posideon's bounty" and school[0] == "Water" and len(spells) > 1 and nextTo("W") and boon[0] == False:
    if mp[0] < 20:
      print("Not enough MP")
    else:
      mp[0] -= 20
      boon[0] = True
      swim = input("Which way?  (Left(a), Right(d), Up(w), Down(s)): ")
      if swim.lower() == "a":
        playerLeft()
      elif swim.lower() == "d":
        playerRight()
      elif swim.lower() == "w":
        playerUp()
      elif swim.lower() == "s":
        playerDown()
    printWorld()
  elif movement.lower() == "earth glide" and school[0] == "Earth" and len(spells) > 1 and nextTo("M") and slide[0] == False:
    if mp[0] < 20:
      print("Not enough MP")
    else:
      mp[0] -= 20
      slide[0] = True
      glide = input("Which way?  (Left(a), Right(d), Up(w), Down(s)): ")
      if glide.lower() == "a":
        playerLeft()
      elif glide.lower() == "d":
        playerRight()
      elif glide.lower() == "w":
        playerUp()
      elif glide.lower() == "s":
        playerDown()
    printWorld()
  else:
    print("Invalid action")
    move()
    
def printMonster():
  print()
  print(monsterName[0])
  print("HP: " + str(monsterHp[0]))
  print("MP: " + str(monsterMp[0]))
  print()
  print()
  print()
  print()
  print()

def printPlayer():
  print("Level " + str(lvl[0]) + " " + str(school[0]) + " " + str(race[0]))
  print("HP: " + str(hp[0]))
  print("MP: " + str(mp[0]))
  print("XP: " + str(xp[0]))
  print()
  if len(spells) != 0:
    print("Spells:")
    for x in range(0, len(spells)):
      print("      " + spells[x])
  print("Ability: " + str(abilities[0]))
  print("Ability Cooldown: " + str(cooldown[0]) + " turns")
  print("Passive: " + str(passive[0]))
  print("Healing Potions: " + str(potion[0]))
  print("Mana Potions: " + str(mana[0]))
  print("Weapon Damage: " + str(damageAmt[0]))
  print("Gold: " + str(goldAmt[0]))
  print("Resources:")
  print("     Ore: " + str(oreAmt[0]))
  print("     Wood: " + str(woodAmt[0]))
  print("     Fish: " + str(fishAmt[0]))
  print()
  if (len(spells) == 0) or (len(spells) == 1 and lvl[0] >= 5) or (len(spells) == 2 and lvl[0] >= 10):
    print("A new spell is available for you to learn from any School")
  print()
  
def setMonster(num):
  monsterName[0] = monsters[num][0]
  monsterHp[0] = int(monsters[num][1])
  monsterMaxHp[0] = int(monsters[num][1])
  monsterMp[0] = int(monsters[num][2])
  monsterDamage[0] = int(monsters[num][3])
  monsterSpell[0] = int(monsters[num][4])

def battle():
  run = False
  os.system("clear")
  if cooldown[0] != 0:
    cooldown[0] -= 1
  printMonster()
  printPlayer()
  action = input("What would you like to do (Attack, Heal, Mana, Run, or Cast a Spell): ")
  if action.lower() == "attack":
    damage = random.randint(1, damageAmt[0])
    monsterHp[0] -= damage * multiplyer[0]
    multiplyer[0] = 1
  elif action.lower() == "heal":
    if potion[0] > 0:
      healing = random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + 6
      hp[0] += healing
      potion[0] -= 1
      if hp[0] > maxHp[0]:
        hp[0] = maxHp[0]
  elif action.lower() == "mana":
    if mana[0] > 0:
      regen = random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4) + 6
      mp[0] += regen
      mana[0] -= 1
      if mp[0] > 100:
        mp[0] = 100
  elif action.lower() == "rage" and race[0] == "Orc" and cooldown[0] == 0:
    multiplyer[0] = 2
    cooldown[0] = 16
  elif action.lower() == "firebolt" and school[0] == "Fire" and len(spells) > 0:
    if mp[0] < 10:
      print("Not enough MP")
    else:
      mp[0] -= 10
      damage = random.randint(1, 8) + random.randint(1, 8)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
  elif action.lower() == "flame dash" and school[0] == "Fire" and len(spells) > 1:
    if mp[0] < 20:
      print("Not enough MP")
    else:
      mp[0] -= 20
      damage = random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
  elif action.lower() == "fireball" and school[0] == "Fire" and len(spells) > 2:
    if mp[0] < 40:
      print("Not enough MP")
    else:
      mp[0] -= 40
      damage = random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
  elif action.lower() == "ball o' water" and school[0] == "Water" and len(spells) > 0:
    if mp[0] < 10:
      print("Not enough MP")
    else:
      mp[0] -= 10
      damage = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
  elif action.lower() == "tidal wave" and school[0] == "Water" and len(spells) > 2:
    if mp[0] < 40:
      print("Not enough MP")
    else:
      mp[0] -= 40
      damage = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
  elif action.lower() == "rock throw" and school[0] == "Earth" and len(spells) > 0:
    if mp[0] < 10:
      print("Not enough MP")
    else:
      mp[0] -= 10
      damage = random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
  elif action.lower() == "entomb" and school[0] == "Earth" and len(spells) > 2:
    if mp[0] < 40:
      print("Not enough MP")
    else:
      mp[0] -= 40
      damage = random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8) + random.randint(1, 8)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
      if monsterHp[0] <= (monsterMaxHp[0] * 0.375):
        monsterHp[0] = 0
  elif action.lower() == "toss" and school[0] == "Air" and len(spells) > 0:
    if mp[0] < 10:
      print("Not enough MP")
    else:
      mp[0] -= 10
      damage = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
  elif action.lower() == "step of the wind" and school[0] == "Air" and len(spells) > 1:
    if mp[0] < 20:
      print("Not enough MP")
    else:
      mp[0] -= 20
      damage = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
  elif action.lower() == "tornado" and school[0] == "Air" and len(spells) > 2:
    if mp[0] < 40:
      print("Not enough MP")
    else:
      mp[0] -= 40
      damage = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
      monsterHp[0] -= damage * multiplyer[0]
      multiplyer[0] = 1
      if monsterHp[0] <= (monsterMaxHp[0] * 0.375):
        monsterHp[0] = 0
  elif action.lower() == "run":
    roll = random.randint(1, 30)
    if roll > (monsterDamage[0] * 2) and inside[0] == False:
      run = True
    else:
      print("You could not get away.")
  
  monsterChoice = random.randint(0, 2)
  if monsterMp[0] > 0 and monsterChoice != 0:
    monsterAttack = random.randint(1, monsterSpell[0]) + random.randint(1, monsterSpell[0])
    monsterMp[0] -= 5
    if school[0] == "Fire":
      fireBlock[0] = True
  else:
    monsterAttack = random.randint(1, monsterDamage[0])
    
  if (action.lower() != "flame dash" or school[0] != "Fire") and (action.lower() != "step of the wind" or school[0] != "Air"):
    if fireBlock[0] == False:
      hp[0] -= monsterAttack
    else:
      newMonsterAttack = monsterAttack/2
      hp[0] -= math.ceil(newMonsterAttack)
      fireBlock[0] = False
  
  if hp[0] < 1:
    os.system("clear")
    sys.exit("You Lose")
  elif run:
    printWorld()
    multiplyer[0] = 1
    print("You got away")
  elif monsterHp[0] <= 0:
    printWorld()
    multiplyer[0] = 1
    print("You Win")
    if monsterName[0] == "Goblin":
      money = random.randint(1, 15)
      xpAmt = random.randint(3, 7)
      print("You found " + str(money) + " gold on the Goblin")
      goldAmt[0] += money
      xp[0] += xpAmt
    elif monsterName[0] == "Bandit":
      money = random.randint(15, 25)
      xpAmt = random.randint(7, 12)
      print("You found " + str(money) + " gold on the Bandit")
      goldAmt[0] += money
      xp[0] += xpAmt
    elif monsterName[0] == "Ogre":
      money = random.randint(10, 30)
      xpAmt = random.randint(12, 17)
      print("You found " + str(money) + " gold on the Ogre")
      goldAmt[0] += money
      xp[0] += xpAmt
    elif monsterName[0] == "Minotaur":
      money = random.randint(25, 60)
      xpAmt = random.randint(17, 22)
      print("You found " + str(money) + " gold on the Minotaur")
      goldAmt[0] += money
      xp[0] += xpAmt
    time.sleep(5)
  else:
    battle()
    
def hit():
  attack = random.randint(1, 10)
  if attack == 1 and perception[0] == 0 and boon[0] == False:
    if slide[0] == True:
      chance = random.randint(0, 1)
      if chance == 0:
        os.system("clear")
        monsterNum[0] = random.randint(0, len(monsters)-2)
        setMonster(monsterNum[0])
        battle()
      else:
        oreAmt[0] += random.randint(1, 2)
        xp[0] += random.randint(1, 5)
    else:
      os.system("clear")
      monsterNum[0] = random.randint(0, len(monsters)-2)
      setMonster(monsterNum[0])
      battle()
  elif attack == 4 and slide[0] == True:
    oreAmt[0] += 1
  elif attack == 5 or attack == 6:
    print("Your travels have made you stronger")
    xp[0] += random.randint(1, 5)
  elif attack == 2:
    print("You found a healing potion")
    potion[0] += 1
  elif attack == 3:
    print("You found a mana potion")
    mana[0] += 1
  elif attack == 10:
    print("You found a stronger weapon")
    damageAmt[0] += random.randint(1, 3)
    
def checkXP():
  if xp[0] > (lvl[0] * 10):
    xp[0] -= (lvl[0] + 10)
    lvl[0] += 1
    maxHp[0] += 5
    hp[0] += 5
    if hp[0] > maxHp[0]:
      hp[0] = maxHp[0]
    print("Level Up!")
    time.sleep(5)
    checkXP()
    
def placeTrees(x, y, num):
  for n in range(0, num):
    worlds[y][x+n] = "T"
    
def permHouse():
  if houseReal[0] == True:
    addLocation(house[0], house[1], 9)
    
def permLocations():
  addLocation(12, 5, 0)
  addLocation(4, 10, 0)
  addLocation(16, 15, 0)
  addLocation(6, 4, 4)
  addLocation(18, 12, 4)
  addLocation(3, 17, 4)
  
  for y in range(3, 8):
    for x in range(2, 5):
      addLocation(x, y, 6)
      
  addLocation(3, 2, 6)
  addLocation(3, 8, 6)
  
  for y in range(12, 16):
    for x in range(11, 15):
      addLocation(x, y, 6)
      
  addLocation(13, 11, 6)
  addLocation(15, 15, 6)
  addLocation(13, 16, 6)
  addLocation(10, 14, 6)
  
  addLocation(7, 6, 7)
  addLocation(7, 7, 7)
  addLocation(6, 7, 7)
  addLocation(6, 8, 7)
  addLocation(6, 9, 7)
  addLocation(6, 10, 7)
  addLocation(5, 9, 7)
  addLocation(5, 10, 7)
  addLocation(5, 11, 7)
  addLocation(5, 12, 7)
  addLocation(5, 13, 7)
  addLocation(4, 12, 7)
  addLocation(4, 13, 7)
  addLocation(4, 14, 7)
  addLocation(3, 13, 7)
  addLocation(4, 14, 7)
  addLocation(3, 14, 7)
  addLocation(3, 15, 7)
  addLocation(2, 14, 7)
  addLocation(2, 15, 7)
  addLocation(1, 15, 7)
  addLocation(2, 16, 7)
  addLocation(1, 16, 7)
  
  addLocation(12, 2, 7)
  addLocation(13, 2, 7)
  addLocation(13, 3, 7)
  addLocation(14, 2, 7)
  addLocation(14, 3, 7)
  addLocation(14, 4, 7)
  addLocation(15, 3, 7)
  addLocation(15, 4, 7)
  addLocation(16, 4, 7)
  addLocation(16, 5, 7)
  addLocation(16, 6, 7)
  addLocation(17, 5, 7)
  addLocation(17, 6, 7)
  addLocation(17, 7, 7)
  addLocation(17, 8, 7)
  addLocation(17, 9, 7)
  addLocation(17, 10, 7)
  addLocation(16, 10, 7)
  addLocation(17, 11, 7)
  addLocation(18, 7, 7)
  addLocation(18, 8, 7)
  addLocation(18, 9, 7)
  
def play():
  boon[0] = False
  slide[0] = False
  if perception[0] != 0:
    perception[0] -= 1
  if cooldown[0] != 0 and perception[0] == 0:
    cooldown[0] -= 1
  printWorld()
  if nextTo("W") and boon[0] == True:
    hp[0] -= 5
    printWorld()
    if hp[0] < 1:
      sys.exit("You Drowned")
  options = getOptions()
  for o in range(0, len(options)):
    print(options[o])
  move()
  if place[0] == False:
    hit()
  place[0] = False
  checkXP()
  play()
  
def start():
  print()
  print("Welcome to Unearthed!")
  print("You are an Adventurer chosen to save the kingdom from the monster invasion.")
  print()
  print("'A' = You")
  print("'S' = Magic School")
  print("'C' = City")
  print("'G' = Merchant")
  print("'E' = Monster Encampment")
  print("'D' = Dungeon/ Boss' Lair")
  print("'W' = Water")
  print("'M' = Mountain")
  print("'T' = Tree")
  print("'H' = House")
  print()
  time.sleep(3)
  input("Press Enter to Begin.")
  addPlayer(9, 9)
  addLocation(random.randint(0, 19), 1, 1)
  addLocation(random.randint(8, 15), 6, 1)
  addLocation(random.randint(5, 10), 13, 1)
  addLocation(random.randint(3, 15), 18, 1)
  addLocation(random.randint(5, 19), 3, 3)
  addLocation(random.randint(7, 16), 8, 3)
  addLocation(random.randint(6, 12), 11, 3)
  addLocation(random.randint(3, 12), 16, 3)
  addLocation(random.randint(0, 19), 0, 2)
  placeTrees(0, 19, 20)
  placeTrees(0, 18, 3)
  placeTrees(16, 18, 4)
  placeTrees(0, 12, 3)
  placeTrees(0, 13, 1)
  placeTrees(0, 11, 3)
  placeTrees(0, 10, 2)
  placeTrees(0, 2, 1)
  placeTrees(0, 3, 2)
  placeTrees(0, 4, 1)
  placeTrees(19, 13, 1)
  placeTrees(18, 14, 2)
  placeTrees(19, 15, 1)
  placeTrees(17, 3, 3)
  placeTrees(18, 2, 2)
  placeTrees(19, 4, 1)
  printWorld()
  play()
  
  
  
def main():
  os.system("clear")
  start()
  

if __name__ == "__main__":
  main()
  
  