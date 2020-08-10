import random

num=random.randint(1,20)
round=0

while(round<5):
    yournum=int(input("Enter the number of your choice"))
    if(num==yournum):
        print("Yayyy you guessed the correct number")
    elif(yournum<num):
        print("Sorry your guess was too low")
    else:
        print("Try again your guess was too high")
    round+=1
print("You lose the game the number is" ,num)
