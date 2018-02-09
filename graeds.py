def topThreeGrades(gradeList):
        first = gradeList[0]
        second = gradeList[1]
        third = gradeList[2]
        if second > first:
                first, second = second, first
        if third > second:
                third, second = second, third
        if second > first:
                first, second = second, first
        for i in range(2, len(gradeList)):
                if gradeList[i] > first:
                        third = second
                        second = first
                        first = gradeList[i]
                elif gradeList[i] > second:
                        third = second
                        second = gradeList[i]
                elif gradeList[i] > third:
                        third = gradeList[i]
        return first, second, third
 
print(topThreeGrades([98, 32, 75, 100, 42, 47, 81, 89]))


