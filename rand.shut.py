print("")
print(" Loading...")
import time, os, random
loop = True
print(" Ready!")
prom1 = input("This program can shutdown, logout, or restart your device. Continue? (y/n) >> ")
while loop:
    if prom1 == "y":
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        random = random.randrange(1, 5)
        if random == 1:
            print("Congratulations! You are safe now!")
        elif random == 2:
            print("Say goodbye to your unsaved files...")
            os.system("shutdown /s /t 2.5") 
        elif random == 3:
            print("Type your password again..")
            time.sleep(2.5)
            os.system("shutdown -l")
        elif random == 4:
            print("Restart yourself.")
            os.system("shutdown /r /t 2.5")
        print("You survived!")
        loop = False
    else:
        print("Program ended. Enter \".restart\" to restart.")
        prom2 = input(">> ")
        if prom2 == ".restart":
            loop = True
        else:
            loop = False
