import os #used for terminal clear with os.system('cls')
import json

MAXUSERS = 5
DATABASE = "users.json"

def clearScreen():
    os.system('cls')

#Adds new account to users dict and saves
def addNewAccount(username, password):
    users.append({"user":username, "pass":password})
    saveUsers()
    return 0

#Removes existing account from users dict and saves
def removeAccount(username):
    for index, account in enumerate(users):
        if account["user"] == username:
            users.pop(index)
            saveUsers()
            return 0
    return -1

#Save users dictionary to JSON
def saveUsers():
    os.chdir(os.path.dirname(__file__))
    jsonUsers = {"users":users}
    with open(DATABASE, "w") as database:
        json.dump(jsonUsers, database)
    return 0

#Load users from json file to dictionary
def loadUsers():
    global users
    os.chdir(os.path.dirname(__file__))
    try:
        with open(DATABASE, 'r') as database:
            jsonUsers = json.load(database)
            users = jsonUsers["users"]
            return 0
    except (FileNotFoundError, json.JSONDecodeError):
        users = []
        return -1

#Welcome screen and input
def printInitialScreen():
    clearScreen()
    while True:
        print("*** Welcome to InCollege ***")
        print("1 - Login as existing user")
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

#Menu: Login to user account
def printLoginScreen():
    loginAttempts = 0 #not used for Epic 1 but the wording in the requirements makes it seem like it might be implemented later
    login = False
    while True:
        clearScreen()
        print("*** Login to InCollege ***")
        print("Username: ", end="")
        username = input()
        print("Password: ", end="")
        password = input()
        #user input recieved
        
        #match username and password
        if isUser(username, password): # and loginAttempts <= maximum attempts allowed
            #Valid Login
            print("You have successfully logged in")
            login = True
            input()
            break
        else:
            #Invalid Login
            print("Incorrect username / password, please try again")
            loginAttempts = loginAttempts + 1
            input()

    if login:
        printMainMenu()
    else:
        printInitialScreen()

#Menu: Add new user account
def printNewAccountScreen():
    clearScreen()
    login = False
    if getNumUsers() < MAXUSERS: #Requirement for 5 accounts
        while True:
            print("*** Create a new user account ***")
            print("Username: ", end="")
            username = input() #Get username
            if isUniqueUser(username):
                print("Password: ", end="")
                password = input() #Get password
                if(checkPasswordSecurity(password)): #Is password secure
                    print("Confirm password: ", end="")
                    passwordConfirm = input() #Get password confirmation
                    if password == passwordConfirm: #Confirm passwords
                        addNewAccount(username, password) #Add new account
                        login = True
                        break
                    else:
                        print("Passwords do not match")
                else:
                    print("Password Requirements: minimum of 8 characters, maximum of 12 characters, at least 1 capital letter, at least 1 digit, at least 1 special character")
            else:
                print("This username is already in use.") #wordage taken from roblox.com
        if login:
            printMainMenu()
        else:
            printInitialScreen()
    else:
        print("All permitted accounts have been created, please come back later") #Requirement for 5 accounts response
        printInitialScreen() #Return to inital screen
    return -1

#Helper: Used in login to return the number of users
def getNumUsers():
    return len(users)

#Helper: Used in login to check if valid login information
def isUser(username, password):
    for i in users:
        if i["user"] == username and i["pass"] == password:
            return True
    return False #Not Found

#Helper: Unique username check
def isUniqueUser(username):
    for i in users:
        if i["user"] == username:
            return False #Username found
    return True #Username not found, is unique

#Helper: Password strength criteria check
def checkPasswordSecurity(password):
    capitalFlag = 0 #At least 1 capital letter
    digitFlag = 0 #At least 1 digit
    specialFlag = 0 #At least 1 special character
    pLen = len(password) #might need to change name of variable
    if pLen < 8 or pLen > 12: #Minimum 8 characters - Maximum 12 Characters
        return False #Password is either too short or too long
    
    for char in password:
        if char.isnumeric(): #is a digit
            digitFlag = 1
        if char.isupper(): #is uppercase
            capitalFlag = 1
        if char.isascii() and not char.isalnum(): #is ascii but not alpha-numerical
            specialFlag = 1
    
    if capitalFlag and digitFlag and specialFlag:
        return True #Password is valid
    else:
        return False #Password is invalid

#User has logged in menu
def printMainMenu():
    clearScreen()
    while True:
        print("*** Main Menu ***")
        print("1 - Search for a job")
        print("2 - Find someone that you know")
        print("3 - Learn a skill")
        userInput = input()
        if userInput == "1":
            printJobSearchScreen()
        elif userInput == "2":
            print("under construction")
            printFriendSearchScreen()
        elif userInput == "3":
            printSkillScreen()
        else:
            print("Invalid selection please input \"1\" or \"2\" or \"3\"")

#user selected to find someone that you know
def printFriendSearchScreen():
    clearScreen()
    print("*** Find A Friend ***")
    print("under construction, input anything to return")
    userInput = input()
    printMainMenu() #Delete me

#user selected to do a job search
def printJobSearchScreen():
    clearScreen()
    print("*** Job Search ***")
    print("under construction, input anything to return")
    userInput = input()
    printMainMenu() #Delete me
    
#user has selected to "Learn a skill"
def printSkillScreen():
    clearScreen()
    while True:    
        print("*** Learn a skill ***")
        print("1 - Learn how to skate")
        print("2 - Learn how to cook")
        print("3 - Learn how to drive")
        print("4 - Learn how to paint")
        print("5 - Learn how to whistle")
        print("6 - Return to main menu")
        userInput = input()
        if userInput == "1":
            printSkill1Screen()
        elif userInput == "2":
            printSkill2Screen()
        elif userInput == "3":
            printSkill3Screen()
        elif userInput == "4":
            printSkill4Screen()
        elif userInput == "5":
            printSkill5Screen()
        elif userInput == "6":
            printMainMenu()
        else:
            print("Invalid selection please input \"1\" or \"2\" or \"3\" or \"4\" or \"5\" or \"6\"")

#Used with printSkillScreen below To Do in future sprints
def printSkill1Screen():
    clearScreen()
    print("*** Learn Skating ***")
    print("under construction, input anything to return")
    userInput = input()
    printSkillScreen()
    
def printSkill2Screen():
    clearScreen()
    print("*** Learn Cooking ***")
    print("under construction, input anything to return")
    userInput = input()
    printSkillScreen()

def printSkill3Screen():
    clearScreen()
    print("*** Learn Driving ***")
    print("under construction, input anything to return")
    userInput = input()
    printSkillScreen()

def printSkill4Screen():
    clearScreen()
    print("*** Learn Painting ***")
    print("under construction, input anything to return")
    userInput = input()
    printSkillScreen()

def printSkill5Screen():
    clearScreen()
    print("*** Learn Whistling ***")
    print("under construction, input anything to return")
    userInput = input()
    printSkillScreen()

def main():
    loadUsers()
    printInitialScreen()
    return 0

main()