import random
import math

green = {
    1:[0,''],
    2:[0,''],
    3:[1,''],
    4:[2,''],
    5:[1,'+'],
    6:[1,'+']
}

yellow = {
    1:[0,''],
    2:[1,''],
    3:[1,''],
    4:[3,''],
    5:[1,'+'],
    6:[2,'+']
}

red = {
    1:[0,''],
    2:[2,''],
    3:[3,''],
    4:[4,''],
    5:[1,'+'],
    6:[2,'+']
}

iterations = 500000
total = 0

for i in range(iterations):

    continueFlag = True
    sum = 0

    while (continueFlag):

        x = math.floor(random.uniform(1,7))

        result = green[x]
        # print(result)
        if result[1] != '+':
            continueFlag = False

        sum += result[0]


    # print('sum = ',sum)
    total += sum

average = float(total) / float(iterations)
print('average = '+ str(average))
