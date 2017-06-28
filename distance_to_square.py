import math

powersSet = set()
answ = []

maxNumb = 100

# # squares only
# for i in range(1, int(math.floor(math.sqrt(maxNumb)))):
#     powers.append(i * i)

# Other Powers too
for i in range(1, int(math.floor(math.sqrt(maxNumb)))):
    powersSet.add(int(math.pow(i,2)))
    powersSet.add(int(math.pow(i,3)))
    powersSet.add(int(math.pow(i,4)))
    powersSet.add(int(math.pow(i,5)))
    powersSet.add(int(math.pow(i,6)))
    powersSet.add(int(math.pow(i,7)))

powers = list(powersSet)
powers.sort()
# print(powers)
# print(powers.__len__())


for i in range(1, maxNumb):
    # basically insertion sort
    n0 = 0
    for n in powers:
        if n0 == n:
            print("dupe!: ", n)

        if i >= n0 and i<= n:
            # print(n)
            answ.append(min(i - n0, n - i))
            break
        n0 = n

print(answ)