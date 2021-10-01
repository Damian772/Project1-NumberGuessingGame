from random import randint
print("There is a random number between 1 and 100")
x=1
digit=randint(1,100)
a=int(input("Guess the random number: "))

while digit != a:

    if a < digit:
        print (a,"was too low! Try again.")
        a=int(input("Guess the random number: "))
        x=x+1
    elif a > digit:
        print(a,"was too high! Try again.")
        a=int(input("Guess the random number: "))
        x=x+1

if digit == a:
    print("Congradulations, You got it right! It took you",x,"guess(es)!")
