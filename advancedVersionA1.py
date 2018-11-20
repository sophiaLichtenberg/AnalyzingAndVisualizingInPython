counter = 1
grades = []
sum
#functions

def checkInput (input):
    if not(input.isdigit()):
        if input == "":
            return input
        print("Kein integer! Nochmal eingeben:")
        input = checkInput(raw_input())
        return input
    else:
        if input > "6" or input < "1":
            print("Keine valide Note! Nochmal eingeben:")
            input = checkInput(raw_input())
            return input
        else:
            return input

def calcArithmeticMean(grades):
    global sum
    arithmeticMean = sum / len(grades)
    return arithmeticMean

def calcMedian(grades):
    grades = sorted(grades)
    middle = len(grades) / 2
    if len(grades) % 2 == 0:
        median = (float(grades[middle]) + float(grades[middle - 1])) / 2
    else:
        median = float(grades[middle])
    return median

def checkIfReadyToCalc():
    global sum
    global counter
    global grades
    print "Jetzt berechnen ? (y/n)"
    answer = raw_input()
    if answer == "y":
        print "Das arithmetische Mittel ist " + str(calcArithmeticMean(grades))
        print "Der Median ist " + str(calcMedian(grades))
    elif answer == "n":
        counter = counter + 1
        print str(counter) + ". Note: "
        input = checkInput(raw_input())
        if input == "":
            checkIfReadyToCalc()
        else:
            grades.append(input)
            sum = sum + float(input)
            start(input)
    else:
        checkIfReadyToCalc()

def start(input):
    global sum
    global counter
    global grades
    while input != "":
        counter = counter + 1
        print str(counter) + ". Note: "
        input = checkInput(raw_input())
        if input != "":
            grades.append(input)
            sum = sum + float(input)
        else:
            checkIfReadyToCalc()

#Start of program

print "Gib Deine Noten gefolgt von Return ein. Lass die Eingabe leer, um zu beenden."
print str(counter) + ". Note: "
input = checkInput(raw_input())
grades.append(input)
sum = float(input)
start(input)




