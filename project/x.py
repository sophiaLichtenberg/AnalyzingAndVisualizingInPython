def solve(input):
    even = []
    odd = []
    letter1 = input[0][0]
    letter2 = input[0][1]
    changes = 0
    for j in range(len(input)):
        for k in range(len(input[0])):
            if j % 2 == 0:
                if k % 2 == 0:
                    odd.append(input[j][k])
                if k % 2 != 0:
                    even.append(input[j][k])
            else:
                if k % 2 != 0:
                    odd.append(input[j][k])
                if k % 2 == 0:
                    even.append(input[j][k])

    if letter1 == letter2:
        letter1 = odd[1]
    if letter2 == letter1:
        letter2 = even[1]
    print even
    print odd
    for x in odd:
        if x != letter1:
            changes+=1

    for y in even:
        if y != letter2:
            changes+=1

    return changes


print solve(['abcdxy', 'yxyxyx', 'xyxyxy', 'yxyxyx', 'xyxyxy', 'yxyxyx'])
