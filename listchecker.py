

list_of_numbers = [4, 7, 9]
anotherList = [123123,1239793721,'d','a sentence about how lame vagmi is', 123123]

def length_of_list(first_input):
    print('The length of the input list is ' + str(len(first_input)))

length_of_list(list_of_numbers)
length_of_list(anotherList)


def list_length_manual(inputList):
    lengthCounter = 0

    for item in inputList:
        #lengthCounter = lengthCounter + 1
        lengthCounter += 1


    print('The length of the input list is ' + str(lengthCounter))


