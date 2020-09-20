from sense_hat import SenseHat
import time

sense = SenseHat()

w = (255,255,255)
b = (0,0,0)
r = (255,0,0)
g = (0,255,0)
p = (0,0,255)


board =[[b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b] ]
        
board2 =[[r,r,r,b,b,b,b,r],
         [r,b,b,b,b,b,b,r],
         [b,b,b,b,b,r,b,r],
         [b,r,r,b,r,r,b,r],
         [b,b,b,b,b,b,b,b],
         [b,r,b,r,r,b,b,b],
         [b,b,b,r,b,b,g,r],
         [r,r,b,b,b,r,r,r] ]
             
             
pepe =  [[w,w,w,w,w,w,w,w],
         [w,g,g,w,w,g,g,w],
         [g,g,g,g,g,g,g,w],
         [g,g,w,b,g,w,b,w],
         [g,g,g,g,g,g,g,w],
         [p,g,r,r,r,r,r,w],
         [p,g,g,g,g,g,w,w],
         [p,p,p,p,p,p,w,w] ]

pepe2 = [[w,w,w,w,w,w,w,w],
         [w,g,g,w,w,g,g,w],
         [g,g,g,g,g,g,g,w],
         [g,g,g,g,g,g,g,w],
         [g,g,g,g,g,g,g,w],
         [p,g,r,r,r,r,r,w],
         [p,g,g,g,g,g,w,w],
         [p,p,p,p,p,p,w,w] ]        
         
y = 2
x = 2


def move_marble(pitch,roll,x,y):
  new_x = x
  new_y = y
  if 1 < pitch < 179 and x != 0:
    new_x -= 1
  elif 359 > pitch > 179 and x != 7:
    new_x += 1
    
  if 1 < roll < 179 and y != 7:
    new_y += 1
  elif 359 > roll > 179 and y != 0:
    new_y -= 1
  
  new_x, new_y = check_wall(x,y,new_x,new_y)
  return new_x, new_y
  
def check_wall(x,y,new_x,new_y): 
  if board2[new_y][new_x] != r:
    return new_x, new_y 
  elif board2[new_y][x] != r:
    return x, new_y
  elif board2[y][new_x] != r:
    return new_x, y 
  else:
    return x,y  
  
def checkObjective(x,y):
  if board2[y][x] == g:
    board2[y][x] = w
    sense.set_pixels(sum(board2,[])) 
    return True
  return False
  
def start():
  sense.clear()
  gameLoop()
  
def gameLoop():
  global x
  global y
  
  while True:
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    x,y = move_marble(pitch,roll,x,y)
    if checkObjective(x,y) == True:
      snakeAnimation()
      return
    board2[y][x] = w
    sense.set_pixels(sum(board2,[])) 
    time.sleep(0.03)
    board2[y][x] = b

def snakeAnimation():
  for i in range(0,len(board2)):
    for j in range(0,len(board2[0])):
      if(i % 2 == 0):
        board2[i][j] = w
      else:
        board2[i][len(board[0])-1-j] = w
      sense.set_pixels(sum(board2,[])) 
      time.sleep(0.02)
  crossAnimation(g)
  crossAnimation(b)
  pepeIdle()
  return 1
  
def pepeIdle():
  while True:
    sense.set_pixels(sum(pepe,[]))
    time.sleep(1)
    sense.set_pixels(sum(pepe2,[]))
    time.sleep(1)
  
def crossAnimation(color):
  roundCount = 0 
  extra = 0
  direction = 1
  i = 0
  j = -1
  for pixel in range(80):
    if direction == 1:
      if j == 7 - roundCount or j>=7:
        direction+=1
        continue
      else:
        j+=1
    elif direction == 2:
      if (i == 7 - roundCount) or (i>=7):
        direction+=1
        continue
      else:
        i+=1
    elif direction == 3:
      if j == 0  + roundCount or j<=0:
        direction += 1
        continue
      else:
        j-=1
    elif direction == 4:
      if i == 0 + roundCount+1 or i<=0:
        roundCount +=1
        direction = 1
        continue
      else:
        i-=1
        
    
    board2[i][j] = color
    sense.set_pixels(sum(board2,[])) 
    time.sleep(0.01)
  return 1

start()

