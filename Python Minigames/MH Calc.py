def parser(line):
  list = []
  for x in range(0, len(line), 2):
    if line[x:x+1] == "0":
      list.append(int(line[x+1:x+2]))
    else:
      list.append(int(line[x:x+2]))
  return list

def targetReward():
  target = input("What is the Target Reward percentage: ")
  targetFlip = (1.0-(int(target)/100.0))
  return targetFlip
  
def captureReward():
  capture = input("What is the Capture Reward percentage: ")
  captureFlip = (1-(int(capture)/100))
  captureFlipSmall = 1-((int(capture)/100)*0.69)
  return (captureFlip*captureFlip*captureFlipSmall)
  
def brokenReward():
  broken = input("What are the Broken Part Reward percentages (Dont seperate list, Ex.270543 for 27% 5% 43%): ")
  brokenList = parser(broken)
  answer = 1
  for x in range(0, len(brokenList)):
    answer *= (1-(brokenList[x]/100))
  return answer
  
def carveReward():
  carve = input("What is the Carved Material percent: ")
  carveFlip = (1-(int(carve)/100))
  return carveFlip*carveFlip*carveFlip
  
def dropReward():
  drop = input("What is the Dropped Material percent: ")
  dropFlip = (1-(int(drop)/100))
  return dropFlip*dropFlip*dropFlip

def run():
  target = targetReward()
  capture = captureReward()
  broken = brokenReward()
  carve = carveReward()
  drop = dropReward()
  print(1-target)
  print(1-capture)
  print(1-broken)
  print(1-carve)
  print(1-drop)
  print(str(1-(target*capture*broken*carve*drop)))

def main():
  run()
  
if __name__ == "__main__":
    main()