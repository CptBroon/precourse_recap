# A guessing game using python

selected_number = 4
user_guess = int(input("I have chosen a number between 1 and 5 - please guess the number"))

if user_guess == selected_number:
    print("Well done! You have guessed correctly!")
else:
    print("Sorry, that was not correct.")