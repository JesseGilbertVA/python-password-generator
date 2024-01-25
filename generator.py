import random
import string

class invalidInteger(Exception):
    pass

def getLetterCriteria():
    print('Would you like your password to have uppercase letters, lowercase letters, both, or none?')
    letterCasing = int(input('1. Uppercase only \n2. Lowercase only \n3. Both uppercase and lowercase \n4. No letters \n'))
    if letterCasing >= 5 or letterCasing <= 0:
        raise invalidInteger
    return letterCasing

def getNumberCriteria():
    print('Would you like your password to contain numbers?')
    containNumbers = int(input('1. Yes \n2. No\n'))
    if containNumbers >= 3 or containNumbers <=0:
        raise invalidInteger
    return containNumbers

def getSpecialCriteria():
    print('Would you like your password to contain special characters?')
    containSpecial = int(input('1. Yes \n2. No \n'))
    if containSpecial >= 3 or containSpecial <= 0:
        raise invalidInteger
    return containSpecial

def passwordLength():
    print('Lastly, please enter desired password length: ')
    lengthInput = int(input())
    if lengthInput <= 0:
        raise invalidInteger
    return lengthInput

def generatePassword(length):
    if letterCharactersInput == 1:
        letterCharacters = string.ascii_uppercase
    elif letterCharactersInput == 2:
        letterCharacters = string.ascii_lowercase
    elif letterCharactersInput == 3:
        letterCharacters = string.ascii_letters
    else:
        letterCharacters = ''
    if numberCharactersInput == 1:
        numberCharacters = string.digits
    else:
        numberCharacters = ''
    if specialCharactersInput == 1:
        specialCharacters = string.punctuation
    else:
        specialCharacters = ''
    if letterCharactersInput == 4 and numberCharactersInput == 2 and specialCharactersInput == 2:
        print('No password criteria specified. Terminating.')
        exit(1)

    characters = letterCharacters + numberCharacters + specialCharacters
    password = ''.join(random.choice(characters) for i in range(length))
    print('Your secure password is: ' + password)

print('Welcome to the strong password generator.')
while True:
    try:
        letterCharactersInput = getLetterCriteria()
    except:
        print('Invalid input. Please enter a valid integer.')
    else: break

while True:
    try:
        numberCharactersInput = getNumberCriteria()
    except:
        print('Invalid input. Please enter a valid integer.')
    else: break

while True:
    try:
        specialCharactersInput = getSpecialCriteria()
    except:
        print('Invalid input. Please enter a valid integer.')
    else: break

while True:
    try:
        totalChractersInput = passwordLength()
    except:
        print('Invalid input. Please enter a valid integer.')
    else: break

generatePassword(totalChractersInput)