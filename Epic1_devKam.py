import json
user = {}
#Save username and password to user dictionary and to JSON
def saveUser(username, password):
    user[username] = password
    with open("user_file.json", "w") as outfile:
        json.dump(user, outfile)

#Helper: Used in login to return the number of users
def getNumUsers():
    return len(user)

#Helper: Used in login to check if valid login information
def checkLoginInfo(username, password):
    for i in user:
        if i == username and user[i] == password:
            return True
    return False #Not Found

def loadUsers():
    with open("user_file.json", 'r') as database:
        user = json.load(database)

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

#Helper: Unique username check
def uniqueUsernameCheck(username): #Possible name change to isUnqueUsername(username):
    for i in user:
        if i == username:
            return False #Username found
    return True #Username not found, is unique

#Helper: adds new account to users
#This does the same thing as saveUser, not sure if we need it
def addNewAccount(username, password):
    user[username] = password
    saveUser(username, password)
    return




    

