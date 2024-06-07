import turtle
from time import sleep
import os
def setup():
    print("Are you ready for the Windows 10 Setup?")
    sleep(1)
    print("Good!")
    sleep(0.5)
    username = input("What will be your usernmae?: ")
    password = input("What will be your password?: ")
    print("Done? Alright!")
    sleep(0.5)
    print("We will give you a quiz, wait for 15 seconds.")
    sleep(1)
    print("Before we start, this quiz is for forgetting your password, or not.")
    sleep(1)
    print("Here we go!")
    sleep(1)
    clear = lambda: os.system("cls")
    clear()
    print("Please wait for the quiz...")
    sleep(15)
    print("The quiz is ready!")
    sleep(1)
    while True:
        question1 = input("What is your username that you typed in?: ")
        if question1 == username:
            print("Good.")
            sleep(1)
            question2 = input("What is your password that you typed in, too?: ")
            if question2 == password:
                print("Great job! You are ready to go! Just type in ./index.html to get to Windows 10.")
                sleep(2)
                exit = input("If you are done reading this, or if you are on it, do you want to close this setup? Y/N: ")
                if exit == "Y":
                    clear()
                    print("It is now safe to close this setup.")
                    sleep(2)
                    clear()
                else:
                    print("Okay! You can stay there all you want!")
                break
            else:
                print("You messed up! Try again.")
                continue
        else:
            print("You messed up! Try again.")
            continue
print("Welcome to Setup!")
sleep(1)
print("Loading Setup...")
setup()