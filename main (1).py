#Ghost house
from random import randint
print('Ghost house')
feeling_brave = True
score = 0
while feeling_brave:
  ghost_door = randint(1,3)
  print ('You stand in front of 3 doors')
  print ('In one door there is a ghost')
  print ('Which door do you open?')
  door = input('1,2,3,4,5 or 6 ?')
  door_num = int(door)
  if door_num == ghost_door:
    print('Ghost')
    feeling_brave = False
  else:
      print('No ghost!')
      print('When you go into the next room,')
      score = score + 0.1
      print('Run away!')
      print('Game over. Your score is', score)