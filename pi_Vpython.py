import vpython as *

#size of a window
scene = canvas(widh=900,height=400)
#setting window title
scene.title = 'lets count pi number!'
#distanece between center of first and middle cube, distance between second cube (while counting from left) and closest point of a wall
center_cubes_distance = 5.0
#setting how many numbers of pi number after coma we want to know
decimal_accutacy = 3
#we will define variable that will contain our calculate pi value as 0
colision_counts = 0
#lets define step of time that will be depended on k, on every another loop while our time will increase by "dt"
dt = 0.1*(0.1**decimal_accutacy)
#cube side length, it is half of a distance between center of cubes 
side_length = 2.5
#d = s/2 -> delete if it will work
#mass of a left side cube 
left_cube_mass =100**decimal_accutacy
#m2 = 1.0 -> delete
#defining details of cubes and wall
#at the beggining left cube will have constanst velocity and right cube will be immobility
ball_1 = box(pos=vector(0, 0, 0), velocity=vector(1, 0, 0), size=vector(side_length, side_length, side_length), color = color.purple)
ball_2 = box(pos=vector(center_cubes_distance, 0, 0), velocity=vector(0, 0, 0), size=vector(side_length, side_length, side_length), color = color.purple)
wall = box(pos=vector((center_cubes_distance*2)+0.1, 0, 0), size=vector(0.2, 10, 10), color=color.cyan)

while(decimal_accutacy==0):
    #setting maximum number of loops if program would have any issues
    rate(5000)
    dt = 0.001
    #lets change our cubes position, time of event is "dt", velocity is declared, distance that every cube has traveled is velocity of a cube and amount of time event
    ball_1.pos += ball_1.velocity * dt
    ball_2.pos += ball_2.velocity * dt
    #finding out if during event position of right cube have contact with wall, its about chcking if position of right cube is smaller or equal to left side of a wall
    if ball_2.pos.x >= (wall.pos.x - (side_length / 2)):
        #now cube will have opposite direction of velocity vector 
        ball_2.velocity.x = -ball_2.velocity.x
        #while cube touching wall "p" variable has to increase by 1
        colision_counts = colision_counts + 1

    #finding out if during event position of right cube have contact with left cube, its about chcking if position of center points of both cubes is equal to lenght of a side of a cube 
    if ball_1.pos.x >= (ball_2.pos.x - side_length):
        #using momentum conservation law we will simulate a perfectly elastic collision. mass of bouth cubes are equal, so while collision cubes exchange with themselves their velocity
        temp = ball_1.velocity.x
        ball_1.velocity.x = ball_2.velocity.x
        ball_2.velocity.x = temp
        #while cubes collision "p" variable has to increase by 1
        colision_counts = colision_counts + 1

    #program will end if right cube while left cube will cros their start position
    if ball_1.pos.x < 0:
        #in this case we dont have to divide "p" by anything, because (0.1**k) is equal to 1
        calculated_pi_nuber = colision_counts * (0.1 ** decimal_accutacy)
        #lets diplay label on a window that will display final result
        okno = label(pos=wall.pos, text=str(calculated_pi_nuber), space=50, xoffset=0, yoffset=50, height=20, color=color.white,
                     linecolor=color.blue)
        #making the cubes them stacionary in thheir orginal position
        ball_1.pos = vector(0, 0, 0)
        ball_2.pos = vector(0, 0, 0)
        print("calculated pi number for chosen decimal_accutacy= ", decimal_accutacy, " is: ", calculated_pi_nuber)
        #no need to continue loop, we arleady have or result of calculating pi number 
        break

while(decimal_accutacy>0):
    #setting maximum number of loops if program would have any issues
    rate(5000)
    #lets change our cubes position, time of event is "dt", velocity is declared, distance that every cube has traveled is velocity of a cube and amount of time event
    ball_1.pos += ball_1.velocity * dt
    ball_2.pos += ball_2.velocity * dt
    #finding out if during event position of right cube have contact with wall, its about chcking if position of right cube is smaller or equal to left side of a wall
    if ball_2.pos.x >= (wall.pos.x-(side_length/2)):
        #if colision with wall "p" variable increases by 1 and velocity of right cube change vector cuurent to opposite
        ball_2.velocity.x = -ball_2.velocity.x
        #while cube touching wall "p" variable has to increase by 1
        colision_counts = colision_counts+1

     #finding out if during event position of right cube have contact with left cube, its about chcking if position of center points of both cubes is equal to lenght of a side of a cube
    if ball_1.pos.x >= (ball_2.pos.x - side_length):
        temp = ball_1.velocity.x
        #using momentum conservation law we will simulate a perfectly elastic collision we can calculate velocity vector of cubes
        ball_1.velocity.x = (((left_cube_mass - 1) / (left_cube_mass + 1)) * ball_1.velocity.x) + (2 * ball_2.velocity.x) / (left_cube_mass + 1)
        ball_2.velocity.x = ((2*left_cube_mass / (left_cube_mass + 1))*temp) + ((1 - left_cube_mass) * ball_2.velocity.x) / (left_cube_mass + 1)
        #while cubes collision "p" variable has to increase by 1
        colision_counts = colision_counts+1

    #program will end if right cube while left cube will cros their start position        
    if (ball_1.pos.x < 0):
        if (ball_1.velocity.x < ball_2.velocity.x) and (ball_2.velocity.x < 0):
            calculated_pi_nuber = colision_counts*(0.1**decimal_accutacy)
            #lets diplay label on a window that will display final result
            okno = label(pos=wall.pos, text=str(calculated_pi_nuber), space=50, xoffset=0, yoffset=50, height=20, color=color.white, linecolor=color.blue)
            #making the cubes them stacionary in thheir orginal position
            ball_1.pos = vector(0, 0, 0)
            ball_2.pos = vector(0, 0, 0)
            print("calculated pi number for chosen decimal_accutacy= ", decimal_accutacy, " is: ", calculated_pi_nuber)
            #no need to continue loop, we arleady have or result of calculating pi number 
            break

