# Script that takes binary numbers and performs conversion and arithmetic operations


def heyVagmi(name):
    print('Sup ' + name)

name = 'Vagmi'
# print(name[0:2])
# print(name[:-5])

#for index in range(len(name)):
#    print(index)


# Func converting for binary to decimal

def toDecimal(inputNum):
    decimalSum = 0
    strNum = str(inputNum)
    for digit in range(len(strNum)):
        realVal = int(strNum[-(digit+1)]) * (2**digit)
        decimalSum += realVal

    return(decimalSum)


# Func for converting decimal to binary

def toBinary(inputNum):
    binarySum = ''
    while inputNum != 0:
        bitToAdd = inputNum % 2
        inputNum = inputNum // 2
        binarySum = str(bitToAdd) + binarySum
    return(int(binarySum))


# Func for calculation

def addBinary(firstNum, secondNum):
    outputType = input('What output type do you want, binary or decimal? ')
    firstNum = toDecimal(firstNum)
    secondNum = toDecimal(secondNum)
    numSum = firstNum + secondNum
    if outputType == 'binary' or outputType == 'Binary':
        return(toBinary(numSum))
    elif outputType == 'decimal' or outputType == 'Decimal':
        return(numSum)


print(addBinary(101101, 101))

"""
    Homework:
    - Make a version of the addBinary function that, instead of taking firstNum
    and secondNum as input variables, it asks the user for these variables at
    function call

    - Make a list of binary numbers, and use the function or another method
    to find the decimal and binary sum of all the items in the list. So, if
    you gave it a list containing [10,110,1], it would return 1001 as well
    as 9
"""