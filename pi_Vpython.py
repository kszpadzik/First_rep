import numpy as np
import math
from vpython import *
# import matplotlib.pyplot as plt -> delete
#size of a window
scene = canvas(widh=900,height=400)
#setting window title
scene.title = 'lets count pi number!'
#distanece between center of first and middle cube, distance between second cube (while counting from left) and closest point of a wall
l = 5.0
#setting how many numbers of pi number after coma we want to know
k = 3
#defining variable "time", which will 
t = 0
#we will define variable that will contain our calculate pi value as 0
p = 0
#lets define step of time that will be depended on k, on every another loop while our time will increase by "dt"
dt = 0.1*(0.1**k)
#cube side lenght
s = 2.5
#d = s/2 -> delete if it will work
#mass of a left side cube 
m =100**k
#m2 = 1.0 -> delete
#defining details of cubes and wall
#at the beggining cubes will have constanst velocity
ball_1 = box(pos=vector(0, 0, 0), velocity=vector(1, 0, 0), size=vector(s, s, s), mass=m, color = color.purple)
ball_2 = box(pos=vector(l, 0, 0), velocity=vector(0, 0, 0), size=vector(s, s, s), m=1, color = color.purple)
wall = box(pos=vector((l*2)+0.1, 0, 0), size=vector(0.2, 10, 10), color=color.cyan)

while(k==0):
    #setting maximum number of loops if program would have any issues
    rate(5000)
    dt = 0.001
    #lets change our cubes position, time of event is "dt", velocity is declared, distance that every cube has traveled is velocity of a cube and amount of time event
    ball_1.pos += ball_1.velocity * dt
    ball_2.pos += ball_2.velocity * dt
    #finding out if during event position of right cube have contact with wall, its about chcking if position of right cube is smaller or equal to left side of a wall
    if ball_2.pos.x >= (wall.pos.x - (s / 2)):
        #now cube will have opposite direction of velocity vector 
        ball_2.velocity.x = -ball_2.velocity.x
        #while cube touching wall "p" variable has to increase by 1
        p = p + 1

    #finding out if during event position of right cube have contact with left cube, its about chcking if position of center points of both cubes is equal to lenght of a side of a cube 
    if ball_1.pos.x >= (ball_2.pos.x - s):
        #using momentum conservation law we will simulate a perfectly elastic collision. mass of bouth cubes are equal, so while collision cubes exchange with themselves their velocity
        temp = ball_1.velocity.x
        ball_1.velocity.x = ball_2.velocity.x
        ball_2.velocity.x = temp
        #while cubes collision "p" variable has to increase by 1
        p = p + 1

    #program will end if right cube while left cube will cros their start position
    if ball_1.pos.x < 0:
        #in this case we dont have to divide "p" by anything, because (0.1**k) is equal to 1
        p = p * (0.1 ** k) # -> delete??
        print(p) # -> delete??
        p1 = str(p)
        #lets diplay label on a window that will display final result
        okno = label(pos=wall.pos, text=p1, space=50, xoffset=0, yoffset=50, height=20, color=color.white,
                     linecolor=color.blue)
        #making the cubes them stacionary in thheir orginal position
        ball_1.pos = vector(0, 0, 0)
        ball_2.pos = vector(0, 0, 0)
        #no need to continue loop, we arleady have or result of calculating pi number 
        break

while(k>0):
    #setting maximum number of loops if program would have any issues
    rate(5000)
    #lets change our cubes position, time of event is "dt", velocity is declared, distance that every cube has traveled is velocity of a cube and amount of time event
    ball_1.pos += ball_1.velocity * dt
    ball_2.pos += ball_2.velocity * dt
    #finding out if during event position of right cube have contact with wall, its about chcking if position of right cube is smaller or equal to left side of a wall
    if ball_2.pos.x >= (wall.pos.x-(s/2)):
        #if colision with wall "p" variable increases by 1 and velocity of right cube change vector cuurent to opposite
        ball_2.velocity.x = -ball_2.velocity.x
        #while cube touching wall "p" variable has to increase by 1
        p = p+1

     #finding out if during event position of right cube have contact with left cube, its about chcking if position of center points of both cubes is equal to lenght of a side of a cube
    if ball_1.pos.x >= (ball_2.pos.x - s):
        temp = ball_1.velocity.x
        #using momentum conservation law we will simulate a perfectly elastic collision we can calculate velocity vector of cubes
        ball_1.velocity.x = (((m - 1) / (m + 1)) * ball_1.velocity.x) + (2 * ball_2.velocity.x) / (m + 1)
        ball_2.velocity.x = ((2*m / (m + 1))*temp) + ((1 - m) * ball_2.velocity.x) / (m + 1)
        #while cubes collision "p" variable has to increase by 1
        p = p+1
        ''''
        if (ball_1.pos.x < 0) and (k == 0):
            p1 = str(p)
            okno = label(pos=wall.pos, text=p1, space=50, xoffset=50, yoffset=50, height=20, color=color.white,
                     linecolor=color.blue)
            ball_1.pos = vector(0, 0, 0)
            ball_2.pos = vector(0, 0, 0)
            print(p)
            break '''

    #program will end if right cube while left cube will cros their start position        
    if (ball_1.pos.x < 0):
        if (ball_1.velocity.x < ball_2.velocity.x) and (ball_2.velocity.x < 0):
            p = p*(0.1**k)
            p1 = str(p)
            #lets diplay label on a window that will display final result
            okno = label(pos=wall.pos, text=p1, space=50, xoffset=0, yoffset=50, height=20, color=color.white, linecolor=color.blue)
            #making the cubes them stacionary in thheir orginal position
            ball_1.pos = vector(0, 0, 0)
            ball_2.pos = vector(0, 0, 0)
            print(p)  # -> delete??
            #no need to continue loop, we arleady have or result of calculating pi number 
            break

