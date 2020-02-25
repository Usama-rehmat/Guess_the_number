import random
print("WELCOME TO GAME")
print("In this game you guess the number between 0 to 20 and you have 5 chance")
n=random.randint(0, 20)
i=0
while(i<5):
    g = int(input("Guess the number"))
    if n==g:
        print("You Won")
        break
    elif g>n and g<21:
        print("your number is greater and guess again")
        i=i+1
        rem = 5-i
        print("You have remaining", rem, "chance ", "\n\n")
    elif g<n and g>=0:
        print("your number is lesser and guess again")
        i=i+1
        rem = 5 - i
        print("You have remaining", rem,  "chance ", "\n\n")
    elif g>20 or g<0:
        print("You enter out of range number\n\n")
if(i>=5):
    print("You Lose the Game")
