from scanner import *

def readRecord(s):                   # we pass the scanner in

    high = s.readtoken()    #discard            
    highTemp = s.readint()
    low = s.readtoken()    #discard
    lowTemp = s.readint()
    description = s.readstring()
    
    record = [None, None, None]
    record[0] = highTemp
    record[1] = lowTemp
    record[2] = description

    return record

def main():

    # TODO: read in a number of days from command line
    numDays= sys.argv[1]
    # make sure that number is <= 5
    if numDays > 5:
        print("Too many days!")
        return
    s = Scanner("weatherInfo.dat")
    records = []
    for i in range(numDays):
        record = readRecords(s)
        records.append(readRecor(s))
    # create scanner
    # read in number of days from file using readRecord
    # print out data
    with open("weatherInfo2.dat") as f:
        for record in records:
            print(record)
            for item in record:
                f.write(str(item))

    # write it back to another file
