# ** Pattern Recognition
# ** Task description:
'''
The daily life of Shri Ram in Gurukul includes Education sessions from the Guru, Sparring to increase experience in Sastra-Vidya and Strict meals in between. Sometimes though, Sree Ram gets free time and this happened to be one such time. While enjoying one such free time with his friends, one of his friends suggested Shri Ram and the others play a game he had recently learned.
Make that game so that Shri Ram and his friends can enjoy it.

'''

# ** Task details:
'''
Create a “Guess the Number” game on Python.
When the game starts, it will prompt the user to enter the name of the player and the range (both upper and lower limit) of the number within which the user will have to guess.
Following this, the game will generate a random number under the range and prompt the user to insert their guess.
Now, the guess is checked with the original number and the user will be informed if their guess was “Too High” or “Too Low”.
The users will be appointed 100 points at the start of the Game.
If they get the guess wrong, a total of 5 points will be deducted from the user's Total Points.
These points need to be tracked till the end of the number of rounds that the user entered when the game started and will be shown to the user during and at the end of the game.
The game ends if the user gets the correct guess for the number or if they run out of points.
'''

import random

print("please enter your name to start the Guess the Number game: ")
string = input()
print("hello, " + string + " let's start the game")
print("enter the range so that we can start the game: ")
var1 = int(input("enter the first number: "))
var2 = int(input("enter the second number: "))

n = random.randrange(var1,var2)
count = 100
print("ok, so now that you have entered the range you can start guessing: ")

while(count > 0):
    guess = int(input("enter the number: "))
    if(guess == n):
        print("hurray, you guessed the number right")
        break;
    else:
        if(guess < n):
            print("Too low")
            count-=5
        else:
            print("Too high")
            count-=5

if(count <= 0):
    print("sorry, you can't play further as you dont have points left to further go in this game")    