#!/usr/bin/env python3
"""
short code to draw given number of "stars" using turtle graphics
with random size, shape and possition 
"""
import turtle
import random
import math

def beam_parts_pairs():
    """
    function to generate random quantity of pairs 
    first number for distance and the seccond for angle
    """
    pairs=([])
    for _ in range(random.randint(3,9)): # minimum and maximum beam segments ("_" unused variable)
        pairs.append([random.randint(10,50),random.randint(0,359)])
    return pairs

def zig_zag(beam,X,Y):
    """
    drawing single star beam from given coordinates
    returning back to the same place and reset heading
    to basic direction
    """
    ttl.penup()
    ttl.setposition(X,Y)
    ttl.pendown()
    for i in beam:
        ttl.left(i[1])
        ttl.forward(i[0])
    ttl.penup()
    ttl.setposition(X,Y)
    ttl.setheading(0)
    ttl.pendown()

def star(coord_X,coord_Y):
    """
    function to draw star in a given coordinates,
    with random amount of beams 
    """
    B = beam_parts_pairs() # call for random beam 
    X = coord_X
    Y = coord_Y
    beams = random.randint(3,24) # random amount of beams

    for i in range(beams): 
        ttl.left((360/beams)*(i-1)) # turn left for portion of 360°
        zig_zag(B,X,Y) # call for single beam drawing

def distance_check(all_coordinates,new_coordinates):
    """
    calculating distance of new coordinates against all existing coordinates,
    returning boolean
    """
    p1 = [new_coordinates[0], new_coordinates[1]]
    for i in all_coordinates:
        distance = math.sqrt( ((p1[0]-i[0])**2)+((p1[1]-i[1])**2) )
        if distance < 120: # minimal star center distance set to 120 px
            return False    
    return True

def coordinates(X):
    """
    random coordinates generator,
    with check for stars not to be too close to each other
    """
    all_coordinates=([])
    wanted = X
    quantity_check=0
    while len(all_coordinates)!=X:
        # new random coordinates with distance check, limited to square 800x800px
        new_coordinates = ([random.randint(-400,400),random.randint(-400,400)])
        if distance_check(all_coordinates, new_coordinates)==True and quantity_check<10000:
            all_coordinates.append(new_coordinates)
        elif quantity_check==10000:
            # insurance for the loop to stop, if there is too many stars
            print("Too many stars, I will draw only " + str(len(all_coordinates)) + " of " + str(wanted))
            break
        else:
            quantity_check += 1
    return all_coordinates

def sky(number_of_stars):
    """
    function with call for given number of coordinates
    and call for function, which will draw the stars
    """
    X = coordinates(number_of_stars)
    for value in X:
        star(value[0],value[1])

try:
    # user input, with check if it's int
    how_many = int(input("How many stars: "))
except ValueError:
    print("Was not number, I will make only one!")
    how_many = 1
    
ttl = turtle.Turtle()
ttl.speed(0) # set turtle speed, 0 = maximum
ttl.ht() # hide turtle

sky(how_many) # final call to draw stars

turtle.Screen().exitonclick() # a bit ugly way to close canvas after drawing

# better way of end turtle graphics
# turtle.done() 