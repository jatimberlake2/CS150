import sys
from scanner import *

def writeOut(table):
    out = open("output","w")
    for i in range(0, len(table),1):
        record = table[i]
        tweeter = record[0]
        tweet = record[1]
        year = str(record[2])
        month = str(record[3])
        day = str(record[4])
        time = record[5]
        out.write(tweeter);
        out.write("\t")
        out.write(tweet)
        out.write("\t")
        out.write(year)
        out.write(" ")
        out.write(month)
        out.write(" ")
        out.write(day)
        out.write(" ")
        out.write(time)
        out.write("\n")
        if (i > len(table)-6 and i < len(table)):
            print(tweeter,tweet)
    out.close()
    return "Files written."        

def merge(array1,array2):
    array3 = []
    i = 0
    j = 0
    while (i < len(array1) and j < len(array2)):
        record1 = array1[i]
        record2 = array2[j]
        if (timeCompare(record1,record2)):
            array3.append(array1[i])
            i = i + 1
        else:
            array3.append(array2[j])
            j = j + 1
    return array3 + array1[i:] + array2[j:]

def timeCompare(record1, record2):
    year1 = record1[2]
    year2 = record2[2]
    month1 = record1[3]
    month2 = record2[3]
    day1 = record1[4]
    day2 = record2[4]
    time1 = record1[5]
    time2 = record2[5]
    hour1 = time1[0:2]
    hour2 = time2[0:2]
    min1 = time1[3:5]
    min2 = time2[3:5]
    sec1 = time1[6:8]
    sec2 = time2[6:8]
 
    if (year2 > year1):
        return False
    if (year2 == year1):
        if (month2 > month1):
            return False
    if (year2 == year1):
        if (month2 ==  month1):
            if (day2 > day1):
                return False
    if (year2 == year1):
        if (month2 ==  month1):
            if (day2 == day1):
                if (hour2 > hour1):
                    return False
    if (year2 == year1):
        if (month2 ==  month1):
            if (day2 == day1):
                if (hour2 == hour1):
                   if (min2 > min1):
                       return False
    if (year2 == year1):
       if (month2 ==  month1):
           if (day2 == day1):
               if (hour2 == hour1):
                  if (min2 == min1):
                      if (sec2 > sec1):
                          return False
    return True

def readTable(fileName):
    s = Scanner(fileName)
    table = []
    record = readRecord(s)
    while (record != ""):
        table.append(record)
        record = readRecord(s)
    s.close()            
    return table

def readRecord(s):
    tweeter = s.readtoken()
    if(tweeter == ""):
        return ""
    tweeter = tweeter.replace("@","")
    tweet = s.readstring()
    year = s.readint()
    month = s.readint()
    day = s.readint()
    time = s.readtoken()
    record = [None, None, None, None, None, None]
    record[0] = tweeter
    record[1] = tweet
    record[2] = year
    record[3] = month
    record[4] = day
    record[5] = time
    return record
    
def main():
    print("Reading files...")
    file1 = str(sys.argv[1])
    file2 = str(sys.argv[2])
    table1 = readTable(file1)
    table2 = readTable(file2)
    if (len(table1) > len(table2)):
        print(file1, "has the most tweets with",len(table1))
    elif (len(table1) < len(table2)):
        print(file2, "has the most tweets with",len(table2))
    elif (len(table1) == len(table2)):
        print("The files,",file1,"and",file2,"each have",len(table1),"tweets.")
    #tRecord1 = ["Anthony","This thing is due...",2013,26,10,"23:59:59"]
    #tRecord2 = ["Justin","Hello World!.",1994,6,7,"12:53:27"]
    #print(timeCompare(tRecord1,tRecord2))
    print("Merging files...")
    trueTable = merge(table1,table2)
    print("Writing files...")
    print("Files written. Displaying 5 earliest tweets.")
    writeOut(trueTable)

main()
