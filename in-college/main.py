import os  # used for terminal clear with os.system('cls')


def clearScreen():
    os.system("cls")


# Password strength criteria check
def checkPasswordSecurity(password):
    # Minimum 8 characters - Maximum 12 Characters
    # At least 1 capital letter
    # At least 1 digit
    # At least 1 special character
    pLen = len(password)  # might need to change name of variable
    if pLen < 8 or pLen > 12:
        return False  # Password is either too short or too long

    capitalFlag = 0
    digitFlag = 0
    specialFlag = 0
    for i in range(pLen):
        if password[i].isnumeric():  # is a digit
            digitFlag = 1
        if password[i].isupper():  # is uppercase
            capitalFlag = 1
        if (
            password[i].isascii() and not password[i].isalnum()
        ):  # is ascii but not alpha-numerical
            specialFlag = 1

    if capitalFlag == 1 and digitFlag == 1 and specialFlag == 1:
        return True  # Password is valid
    else:
        return False  # Password is invalid


def addNewAccount():
    # To Do
    return 0


def printLoginScreen():
    # To Do
    return 0


def printNewAccountScreen():
    # To Do

    return 0


# Welcome screen and input
def printInitialScreen():
    clearScreen()
    while True:
        print("*** Welcome to InCollege ***")
        print("1 - Login as exisitng user")
        print("2 - Create a new InCollege account")
        userInput = input()
        if userInput == "1":
            # Login as existing user. Go to Login page
            printLoginScreen()
            break
        elif userInput == "2":
            # Create a new account. Go to create account page
            printNewAccountScreen()
            break
        else:
            print('Invalid selection please input "1" or "2"')
