
import os #used for terminal clear with os.system('cls')

#Helper: Used to clear screen
def clearScreen():
    os.system('cls')

#Load Users from JSON
users = set()
def loadUsers():
    #To DO
    users.add(("a", "a"))
    users.add(("User1", "P@ssw0rd1"))
    users.add(("User2", "P@ssw0rd2"))
    users.add(("User3", "P@ssw0rd3"))
    return 0

#Helper: Used in login to return the number of users
def getNumUsers():
    loadUsers() #Delete me, the load users will be called earlier in finished product so it is loaded and ready, here only for testing
    return len(users)

#Helper: Used in login to check if valid login information
def checkLoginInfo(u, p):
    #(username, password)
    for i in users:
        if i[0] == u and i[1] == p:
            return True
    return False #Not Found

#Save Users to JSON
def saveUsers():
    #To Do
    return 0

#Menu: Login to user account
def printLoginScreen():
    #To Do
    clearScreen()
    loginAttempts = 0 #not used for Epic 1 but the wording in the requirements makes it seem like it might be implemented later
    while True:
        print("*** Login to InCollege ***")
        print("Username: ", end="")
        username = input()
        print("Password: ", end="")
        password = input()
        #User input recieved

        #match username and password
        if checkLoginInfo(username, password): # and loginAttempts <= maximum attempts allowed
            #Valid Login
            print("You have successfully logged in")
            return 0
        else:
            #Invalid Login
            print("Incorret username / password, please try again")
            loginAttempts = loginAttempts + 1

#Helper: Password strength criteria check
def checkPasswordSecurity(password):
    capitalFlag = 0 #At least 1 capital letter
    digitFlag = 0 #At least 1 digit
    specialFlag = 0 #At least 1 special character
    pLen = len(password) #might need to change name of variable
    if pLen < 8 or pLen > 12: #Minimum 8 characters - Maximum 12 Characters
        return False #Password is either too short or too long
    
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

#Helper: Unique username check
def uniqueUsernameCheck(username): #Possible name change to isUnqueUsername(username):
    for i in users:
        if i[0] == username:
            return False #Username found
    return True #Username not found, is unique

#Helper: adds new account to users
def addNewAccount(u, p):
    users.add((u, p))
    return

#Menu: Add new user account
def printNewAccountScreen():
    #clearScreen()
    if getNumUsers() <= 4: #Requirement for 5 accounts
        while True:
            print("*** Create a new user account ***")
            print("Username: ", end="")
            username = input() #Get username
            if uniqueUsernameCheck(username):
                print("Password: ", end="")
                password = input() #Get password
                if(checkPasswordSecurity(password)): #Is password secure
                    print("Confirm password: ", end="")
                    passwordConfirm = input() #Get password confirmation
                    if password == passwordConfirm: #Confirm passwords
                        addNewAccount(username, password) #Add new account
                        clearScreen()
                        printTempName() #Logged in menu
                    else:
                        print("Passwords do not match")
                else:
                    print("Password Requirements: minimum of 8 characters, maximum of 12 characters, at least 1 capital letter, at least 1 digit, at least 1 special character")
            else:
                print("This username is already in use.") #wordage taken from roblox.com
    else:
        print("All permitted accounts have been created, please come back later") #Requirement for 5 accounts response
        printInitialScreen() #Return to inital screen
    return -1

#Users have logged in menu
def printTempName():
    #To Do
    while True:
        print("*** Logged In Menu WIP ***")
        wait = input()

#Welcome screen and input
def printInitialScreen():
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

def main():
    loadUsers()
    printInitialScreen()
    
if __name__ == "__main__":
    main()