from random import randint
num = randint(0,100)
guess = None

while guess != num:
    guess = int(input("Type your guess: "))
    if guess == num:
        break
    if guess > num:
        print("Decrease your number. \n")
        continue
    else:
        print("Increase your number.\n")
        continue
print("You won!")