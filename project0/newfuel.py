# program for slugging percentage, by John C. Lusth 2012
#    
#     modified by Brandon Dixon, 2013, to compute fuel consumption
# 
# this program may be freely distributed and modified, as long as:
# 
# a) the authorship of any modifications is added
#
# b) the reason for modification is added
#
# c) the comments are updated to reflect modifications
#
# d) the original authorship and that of any previous modifiers is preserved.
#

def main():
    # get the fuel MPG, lap distance, cool down speed
    mpg,lapDistance,numLaps,coolDown = getFuelData()
    # compute the fuel used
    fuelUsed = (numLaps * lapDistance / mpg) + (2* lapDistance)/coolDown
    # compute the weight of the fuel
    fuelWeight = fuelUsed * 6.1
    # display the results
    displayResults(mpg, lapDistance, numLaps, fuelUsed, fuelWeight)

def getFuelData():
    mpg = float(input("Miles per gallon at race pace? "))
    ld = float(input("Lap distance? "))
    nl = int(input("Number of race laps? "))
    cds = float(input("Cool down speed? ")) 
    return mpg, ld, nl, cds

def displayResults(mpg, lapDistance, numLaps, fuelUsed, fuelWeight):
    print("for")
    print("   ",mpg,"race pace miles per gallon")
    print("   ",lapDistance,"lap distance")
    print("   ",numLaps,"laps")
    print("the fuel used will be",fuelUsed,"gallons")
    print("the weight of the fuel used was",fuelWeight,"pounds")

main()
