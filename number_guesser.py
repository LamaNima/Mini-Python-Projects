import random as rand

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Enter a positive number ")
        quit()
else:
    print("Enter a number next time")
    quit()
random_number = rand.randint(0,top_of_range)

guess_count = 0

while True:
    guess_count += 1
    user_guess = input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number please")
        continue

    if(user_guess == random_number):
        print("You guessed the number!")
        break
    elif(user_guess < random_number):
        print("The number is greater than the number you guessed!")
    else:
        print("The number is less than the number you guessed!")

print("You took", guess_count, "guesses.")
