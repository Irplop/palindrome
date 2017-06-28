import math


class baseNumb:
    def __init__(self, numb, base):
        self.numb = numb # in base 10
        self.base = base

    def toString(self):
        size = math.floor(math.log(self.numb,self.base))
        tempStr = ''
        tempNumb = self.numb

        for i in reversed(range(size+1)):
            a = math.floor(tempNumb / pow(self.base, i))

            tempNumb -= a * pow(self.base, i)

            # generates a,b,c, ... for 10,11,12, ...
            if a >= 10:
                a = chr(97+a-10)

            tempStr += str(a)

        return tempStr

#
# palindromeList = []
# for i in range(1,pow(11,4)):
#     a = baseNumb(i, 11)
#     aString = a.toString()
#
#     if aString == aString[::-1]:
#         palindromeList.append(aString)
# print(palindromeList.__len__())


for i in [4,6,10,14,22,30,46,62,94,126,190]:
    a = baseNumb(i, 2)
    print(a.toString(),end=', ')
print()
for i in [10,16,34,52,106,160,322,484,970,1456,2914,4372]:
    a = baseNumb(i, 3)
    print(a.toString(),end=', ')
print()

for i in [18,30,78,126,318,510,1278,2046,5118,8190,20478,32766]:
    a = baseNumb(i, 4)
    print(a.toString(),end=', ')
print()


for i in [28,48,148,248,748,1248,3748,6248,18748,31248]:
    a = baseNumb(i, 5)
    print(a.toString(),end=', ')
print()


for i in [40,70,250,430,1510,2590,9070,15550,54430,93310,326590]:
    a = baseNumb(i, 6)
    print(a.toString(),end=', ')
print()

for i in [54,96,390,684,2742,4800,19206,33612,134454,235296,941190]:
    a = baseNumb(i, 7)
    print(a.toString(),end=', ')
print()



for i in [70,126,574,1022,4606,8190,36862,65534,294910,524286,2359294,4194302,18874366,33554430]:
    a = baseNumb(i, 8)
    print(a.toString(),end=', ')
print()

for i in [88,160,808,1456,7288,13120,65608]:
    a = baseNumb(i, 9)
    print(a.toString(),end=', ')

print()
for i in [130,240,1450,2660]:
    a = baseNumb(i, 11)
    print(a.toString(),end=', ')



maxBase = 9  # current maximum is 36
maxSize = 100


# for b in range(1,5):
#     palindromeList = []
#
#     for i in range(1,pow(b,6)):
#         a = baseNumb(i, b)
#         aString = a.toString()
#
#         if aString == aString[::-1]:
#             palindromeList.append(aString)
#
#     # print(palindromeList)
#     # print('Base ',b,' has ',palindromeList.__len__(),' palindromes below ',maxSize)
#     print(palindromeList.__len__())
