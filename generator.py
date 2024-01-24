import random
import string

def passwordLength():
    print('Enter desired strong password length: ')
    userInput = int(input())
    return userInput

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print('Your secure password is: ' + password)

while True:
    try:
        inputLength = passwordLength()
    except:
        print('Invalid input. Please enter an integer.')
    else: break

generate_password(inputLength)