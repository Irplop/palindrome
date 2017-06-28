# which palindromes when multiplied by 11 make another palindrome
# what about 111

# build palindrome list
# Generate all palindromic numbers less than n
# A Python program to generate palindromic numbers
# less than n.
def createPalindrome(inp, b, isOdd):
    n = inp
    palin = inp

    # checks if number of digits is odd or even
    # if odd then neglect the last digit of input in
    # finding reverse as in case of odd number of
    # digits middle element occur once
    if (isOdd):
        n = n / b

    # Creates palindrome by just appending reverse
    # of number to itself
    while (n > 0):
        palin = palin * b + (n % b)
        n = n / b
    return palin


# Function to print decimal palindromic number
def generatePaldindromes(n):
    palindromeList = []

    # Run two times for odd and even length palindromes
    for j in range(2):
        # Creates palindrome numbers with first half as i.
        # Value of j decided whether we need an odd length
        # of even length palindrome.
        i = 1
        while (createPalindrome(i, 10, j % 2) < n):
            # print createPalindrome(i, 10, j % 2),
            palindromeList.append(createPalindrome(i, 10, j % 2))
            i = i + 1
    return palindromeList




def getPercentPalindrome(digits, elevens):
    countPalins = 0

    n = pow(10,digits)

    palindromeList = generatePaldindromes(n)

    # print palindromeList

    for palind in palindromeList:

        newpalind = palind * elevens

        if str(newpalind) == str(newpalind)[::-1]:
            countPalins += 1
            print(newpalind,' is a palindrome')

    return [countPalins, palindromeList.__len__()]




for a in range(2,5):
    ans = getPercentPalindrome(a, 11)
    print(a,ans[0],ans[1])

# print getPercentPalindrome(7, 11)
# print getPercentPalindrome(7, 111)
# print getPercentPalindrome(7, 1111)
# print getPercentPalindrome(7, 11111)
# print getPercentPalindrome(7, 111111)
# print getPercentPalindrome(7, 1111111)
# print getPercentPalindrome(7, 11111111)
# print
# print getPercentPalindrome(6, 11)
# print getPercentPalindrome(6, 111)
# print getPercentPalindrome(6, 1111)
# print getPercentPalindrome(6, 11111)
# print getPercentPalindrome(6, 111111)
# print getPercentPalindrome(6, 1111111)
# print getPercentPalindrome(6, 11111111)
# print
# print getPercentPalindrome(5, 11)
# print getPercentPalindrome(5, 111)
# print getPercentPalindrome(5, 1111)
# print getPercentPalindrome(5, 11111)
# print getPercentPalindrome(5, 111111)
# print getPercentPalindrome(5, 1111111)
# print getPercentPalindrome(5, 11111111)
# print
# print getPercentPalindrome(4, 11)
# print getPercentPalindrome(4, 111)
# print getPercentPalindrome(4, 1111)
# print getPercentPalindrome(4, 11111)
# print getPercentPalindrome(4, 111111)
# print getPercentPalindrome(4, 1111111)
# print getPercentPalindrome(4, 11111111)
# print
# print getPercentPalindrome(3, 11)
# print getPercentPalindrome(3, 111)
# print getPercentPalindrome(3, 1111)
# print getPercentPalindrome(3, 11111)
# print getPercentPalindrome(3, 111111)
# print getPercentPalindrome(3, 1111111)
# print getPercentPalindrome(3, 11111111)
# print
# print getPercentPalindrome(2, 11)
# print getPercentPalindrome(2, 111)
# print getPercentPalindrome(2, 1111)
# print getPercentPalindrome(2, 11111)
# print getPercentPalindrome(2, 111111)
# print getPercentPalindrome(2, 1111111)
# print getPercentPalindrome(2, 11111111)