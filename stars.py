#!/usr/bin/env python3
import turtle as ttl
import random
import math
from PIL import Image




def hodnoty():
    X=([])
    pocet_paru=random.randint(3,9)
    for i in range(pocet_paru):
        X.append([random.randint(10,50),random.randint(0,359)])
    return X

def klikatice(X,Y,Z):
    ttl.penup()
    ttl.setposition(Y,Z)
    ttl.pendown()
    for i in X:
        ttl.left(i[1])
        ttl.forward(i[0])
    ttl.penup()
    ttl.setposition(Y,Z)
    ttl.setheading(0)
    ttl.pendown()

def star(souradniceX,souradniceY):
    paprsku=(random.randint(5,24))
    X=hodnoty()
    Y=souradniceX
    Z=souradniceY
    for i in range(paprsku):
        ttl.left((360/paprsku)*(i-1))
        klikatice(X,Y,Z)

def test_vzdalenosti(rada,nove_souradnice):
    p1 = [nove_souradnice[0], nove_souradnice[1]]
    for i in rada:
        distance = math.sqrt( ((p1[0]-i[0])**2)+((p1[1]-i[1])**2) )
        if distance < 120:
            return False    
    return True

def coordinates(X):
    rada=([])
    wanted = X
    quantity_check=0
    while len(rada)!=X:
        new_coordinates = ([random.randint(-800,800),random.randint(-400,400)])
        if test_vzdalenosti(rada, new_coordinates)==True and quantity_check<10000:
                rada.append(new_coordinates)
        elif quantity_check==10000:
            print("Too many stars, I will draw only " + str(len(rada)) + " of " + str(wanted))
            break
        else:
            quantity_check += 1
    return rada

def sky(number_of_stars):
    X = coordinates(number_of_stars)
    for value in X:
        star(value[0],value[1])

try:
    how_many = int(input("How many stars: "))
except ValueError:
    print("Was not number, I will make only one!")
    how_many = 1
    
ttl.speed(0) # set turtle speed 0 = maximum
ttl.ht() # hide turtle

sky(how_many)

ttl.exitonclick()