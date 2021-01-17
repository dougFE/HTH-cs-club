# Basic Python Demo


# Booleans
isButtonOn = True
isButtonOn = False

# Integers
numberOfFriends = 5
numberOfFriends = 0
numberOfFriends = -12

# Floating Point Numbers (Floats)
averageFriends = 5.3
averageFriends = -5.0

addNumbers = numberOfFriends + 5 # + is for addition
addNumbers = numberOfFriends - 5 # - is for subtraction
addNumbers = numberOfFriends * 5 # * is for multiplication
addNumbers = numberOfFriends / 5 # / is for division

# Strings
sentence = "How are you today good sir?"
sentence = 'I have 8 apples! '
#sentence = ''

#print('Hello world!')
#print(sentence)

# String concatenation
#print('Judy said '  + sentence)
#print(2 * sentence)

# Lists (unordered set of values)
list_of_names = ['Jack', 'John', 'James']
list_of_names.append('Jacob')
#list_of_names.append(3)
#print(list_of_names)


# Functions (chunk of reusable code usually takes an input and gives an output)

def sayGreeting(name):
    print("Hello there, " + name + "!")

sayGreeting('Doug')

# For Loop
for person in list_of_names:
    sayGreeting(person)

print('\n')

for character in sentence:
    print(character)









