import os #used for terminal clear with os.system('cls')
import json
user = {}

def clearScreen():
    os.system('cls')

#Save username and password to user dictionary and to JSON
def saveUser(username, password):
    user[username] = password
    with open("user_file.json", "w") as outfile:
        json.dump(user, outfile)

#Load users from json file to dictionary
def loadUsers():
    with open("user_file.json", 'r') as database:
        user = json.load(database)

#Password strength criteria check
def checkPasswordSecurity(password):
    #Minimum 8 characters - Maximum 12 Characters
    #At least 1 capital letter
    #At least 1 digit
    #At least 1 special character
    pLen = len(password) #might need to change name of variable
    if pLen < 8 or pLen > 12:
        return False #Password is either too short or too long
    
    capitalFlag = 0
    digitFlag = 0
    specialFlag = 0
    for i in range(pLen):
        if password[i].isnumeric(): #is a digit
            digitFlag = 1
        if password[i].isupper(): #is uppercase
            capitalFlag = 1
        if password[i].isascii() and not password[i].isalnum(): #is ascii but not alpha-numerical
            specialFlag = 1
    
    if capitalFlag == 1 and digitFlag == 1 and specialFlag == 1:
        return True #Password is valid
    else:
        return False #Password is invalid

#Helper: adds new account to users
#This does the same thing as saveUser, not sure if we need it
def addNewAccount(username, password):
    user[username] = password
    saveUser(username, password)
    return

#Menu: Login to user account
def printLoginScreen():
    #To Do
    loginAttempts = 0 #not used for Epic 1 but the wording in the requirements makes it seem like it might be implemented later
    while True:
        print("*** Login to InCollege ***")
        print("Username: ", end="")
        username = input()
        print("Password: ", end="")
        password = input()
        #User input recieved
        
        #match username and password
        if checkLoginInfo(username, password) == True: # and loginAttempts <= maximum attempts allowed
            #Valid Login
            print("You have successfully logged in")
        else:
            #Invalid Login
            print("Incorret username / password, please try again")
            loginAttempts = loginAttempts + 1


def printNewAccountScreen():
    #To Do

    return 0

#Welcome screen and input
def printInitialScreen():
    clearScreen()
    while True:
        print("*** Welcome to InCollege ***")
        print("1 - Login as exisitng user")
        print("2 - Create a new InCollege account")
        userInput = input()
        if userInput == "1":
            #Login as existing user. Go to Login page
            printLoginScreen()
            break
        elif userInput == "2":
            #Create a new account. Go to create account page
            printNewAccountScreen()
            break
        else:
            print("Invalid selection please input \"1\" or \"2\"")

#Helper: Used in login to return the number of users
def getNumUsers():
    return len(user)

#Helper: Used in login to check if valid login information
def checkLoginInfo(username, password):
    for i in user:
        if i == username and user[i] == password:
            return True
    return False #Not Found

#Helper: Unique username check
def uniqueUsernameCheck(username): #Possible name change to isUnqueUsername(username):
    for i in user:
        if i == username:
            return False #Username found
    return True #Username not found, is unique
