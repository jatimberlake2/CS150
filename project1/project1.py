#####################################
#                                   #
#   Anthony Timberlake              #
#   CS 150, Project 1               #
#   Due September 28th, 2013        #
#                                   #
#   Let's play darts!               #
#                                   #
#####################################
import random
def main():
# darts variable dealing with challenge involving loops and throwing more
#    than 5 darts in general
    darts = int(input("How many darts to throw? "))
    exes = [0]*darts
    wise = [0]*darts
    dots = [0]*darts
# where exes is an array of all x values of coordinates
#       wise is an array of all y values of coordinates
#       dots is an array of coordinate distance from the origin
#       (sound out exes and wise, lol)
# the length of these arrays is determined by the user input
    i = 0
    while (i<darts):
        exes[i]=random.uniform(-1.5,1.5)
        wise[i]=random.uniform(-1.5,1.5)
        dots[i]=(exes[i]**2+wise[i]**2)**(1/2)
        i += 1
    i = 0
    oBox = 0
    oCircle = 0
    iCircle = 0
    while(i<darts):
        if(dots[i]>1):
            print("Outside the target! (x:",exes[i],"y:",wise[i],")")
            oCircle += 1
        if(exes[i] > 1 or exes[i] < -1 or wise[i] > 1 or wise[i] < -1):  
            oBox += 1
        elif(dots[i]<1):
            print("In the target! (x:",exes[i],"y:",wise[i],")")
            iCircle += 1
        i += 1
    print(iCircle,"dart(s) in the target.")
    print(oCircle,"dart(s) outside the target.")
    print(oBox,"dart(s) off the board.")
# Challenges
# Checking for two subsets of "within the target"
# middle ring is from .5 to .75
# innermost ring a circle with a radius of .5
# checking for "edge shots"
# where distance (value of dots[i]) is between .99 and 1.01
    i = 0
    n5to75 = 0
    nto5 = 0
    edge = 0
    while(i<darts):
        if(dots[i]<1.01 and dots[i]>.99):
            print("Edge shot! (x:",exes[i],"y:",wise[i],")")
            edge += 1
        elif(dots[i]<.75 and dots[i] > .5):
            print("between .5 and .75! (x:",exes[i],"y:",wise[i],")")
            n5to75 += 1
        elif(dots[i]<.5):
            print("less than .5 away! (x:",exes[i],"y:",wise[i],")")
            nto5 += 1
        i += 1
    print("Middle Ring Hits:",n5to75)
    print("Innermost Ring Hits:",nto5)
    print("Edge shots:",edge)

main()
