import random

while True:
    correct_number = random.randint(1, 67)
    input_number = int(input("Guess the number between 1 and 67: "))

    if input_number == correct_number:
        print("!!")

    else:
        print("??")
