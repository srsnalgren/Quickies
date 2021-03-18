#Works for 0 < num < 4000

romList = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

num = 0

def writeRoman(letter, n):
    global num
    while num>=n:
        num-=n
        print(letter, end = '')

def main():
    global num
    num = int(input('Enter a number: '))
    print('Roman Numeral: ', end = '')
    for item in romList:
        writeRoman(item[0], item[1])

main()
