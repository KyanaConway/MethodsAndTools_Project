import hashlib
import os


clear = lambda: os.system('cls')


def main():
    clear()
    print("Welcome to The Bookstore!")
    print("***************************************")
    print()
    print("[A] Register  [B]Login  [C]exit ")
    print()
    print()
    print()
    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['A', 'B','C']:
            break
    if userChoice == 'A':
        Register()
    elif userChoice == 'B':
        Login()
    elif userChoice == 'C':
        print("Goodbye!")
        exit()
        
def Register():
    clear()
    print("Register new account")
    print("")
    print()
    while True:
        userName = input("Enter Your username: ").title()
        userFname =input("Enter your fullname: ")
        userEmail = input("Enter email: ")
        userAddy = input("Enter Address: ")
        userState = input("Enter State: ")
        userPayment = input("Will you be paying with cash or card? ")
        
        
        if userName != '':
            break
    userName = sanitizeName(userName)
    if userAlreadyExist(userName):
        displayUserAlreadyExistMessage()
        
    else:
        while True:
            userPassword = input("Enter Your Password: ")
            if userPassword != '':
                break
        while True:
            confirmPassword = input("Confirm Your Password: ")
            if confirmPassword == userPassword:
                print("You are now registered! You can Login now!")
                break
            else:
                print("Passwords Don't Match")
                print()

        if userAlreadyExist(userName, userPassword):
            while True:
                print()
                error = input("You Are Already Registered.\n\nPress (T) To Try Again:\nPress (L) To Login: ").lower()
                if error == 't':
                    Register()
                    break
                elif error == 'l':
                    Login()
                    break
        addUserInfo([userName,userFname,userPassword,userEmail,userAddy,userState,userPayment])

        print()
        print("Registered!")

def Login():
    clear()
    print("Login")
    usersInfo = {}
    with open('userInfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            usersInfo.update({line[0]: line[1]})

    while True:
        userName = input("Enter Your username: ").title()
        userName = sanitizeName(userName)
        if userName not in usersInfo:
            print("You Are Not Registered")
            print()
        else:
            break
    while True:
        userPassword = input("Enter Your Password: ")
        if not (userPassword, usersInfo[userName]):
            print("Login Not successful! Try Again.")
            
        else:
            print("Welcome Back! "+usersInfo[userName])
            print("What Would you like to do next?")
            print("See Account Info[A], Purchase a Book[B] Exit[C]")
            print()
            print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['A', 'B','C']:
            break
    if userChoice == 'A':
        print(" [User]   [Name]        [Password]   [Email]           [Address, State]   [Payment]")
        AccountInfo()
        userChoice = print("Goodbye,"+userName)
        #exit()  
        userChoice =print("Do you want to Purchase a book [B] or Logout[C]")
    if userChoice =='B':
            Purchase()
    elif userChoice == 'C':
            exit()

    elif userChoice == 'B':
        Purchase()
    elif userChoice == 'C':
        print("Goodbye!")
        exit()
            #break
            
def AccountInfo():
    with open('userInfo.txt','r') as file:
        f_contents = file.readline()
        print(f_contents)
        #for line in file:
            #line = file.readline()
        #file.close()

def Purchase():
    useropption = input("What book would you like?")

#def secmenu():
        #print("Welcome Back!")


            


def addUserInfo(userInfo: list):
    with open('userInfo.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')
        file.close()

def userAlreadyExist(userName, userPassword=None):
    if userPassword == None:
        with open('userInfo.txt', 'r') as file:
            for line in file:
                line = line.split()
                if line[0] == userName:
                    return True
        return False
    else:
        userPassword = (userPassword)
        usersInfo = {}
        with open('userInfo.txt', 'r') as file:
            for line in file:
                line = line.split()
                if line[0] == userName and line[1] == userPassword:
                    usersInfo.update({line[0]: line[1]})
        if usersInfo == {}:
            return False
        return usersInfo[userName] == userPassword
        file.close()
def displayUserAlreadyExistMessage():
    while True:
        print()
        error = input("You Are Already Registered.\n\nPress (T) To Try Again:\nPress (L) To Login: ").lower()
        if error == 't':
            Register()
            break
        elif error == 'l':
            Login()
            break

def sanitizeName(userName):
    userName = userName.split()
    userName = '-'.join(userName)
    return userName




main()