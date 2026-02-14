import random

correct_number = random.randint(1, 67)

while True:
    input_number = int(input("Guess the number between 1 and 67: "))

    if input_number == correct_number:
        print("!!")
        break
    elif input_number < correct_number:
        print("?? (Too low)")
    else:
        print("?? (Too high)")
