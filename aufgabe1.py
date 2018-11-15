print "Gib Deine Noten gefolgt von Return ein. Lass die Eingabe leer, um zu beenden."
counter = 1
print str(counter) + ". Note: "
input = raw_input()
grades = []
grades.append(input)
sum = float(input)
while input != "":
    counter = counter + 1
    print str(counter) + ". Note: "
    input = raw_input()
    if input != "":
        grades.append(input)
        sum = sum + float(input)
    else:
        arithmeticMean = sum / len(grades)
        print "Das arithmetische Mittel ist " + str(arithmeticMean)
        grades = sorted(grades)
        middle = len(grades) / 2
        median = 0
        if len(grades) % 2 == 0:
            median = (float(grades[middle]) + float(grades[middle-1]))/2
        else :
            median = float(grades[middle])
        print "Der Median ist " + str(median)



