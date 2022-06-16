import random
import characters

length = int(input("How long do you want your password to be?\n"))
letters = -1
numbers = -1
symbols = -1
password = ""


def get_next(num_letters, num_numbers, num_symbols):
    pick_list = [get_random_letter(), get_random_number(), get_random_symbol()]

    if num_letters > 0:
        if num_numbers > 0:
            if num_symbols > 0:
                rand_pick = random.randint(0, 2)
            else:
                rand_pick = random.randint(0, 1)
        else:
            rand_pick = 0
    elif num_numbers > 0:
        if num_symbols > 0:
            rand_pick = random.randint(1, 2)
        else:
            rand_pick = 1
    else:
        rand_pick = 2

    return pick_list[rand_pick]


def get_random_letter():
    random_index = int(random.random() * len(characters.letters))
    return characters.letters[random_index]


def get_random_number():
    random_index = int(random.random() * len(characters.numbers))
    return characters.numbers[random_index]


def get_random_symbol():
    random_index = int(random.random() * len(characters.symbols))
    return characters.symbols[random_index]


if input("Do you want to pick the number of letters, numbers, and symbols? (Y or N)").lower() == 'y':
    while letters > length or letters < 0:
        letters = int(input(f"How many letters do you want in your password? Max: {length}\n"))
    if letters < length:
        while letters + numbers > length or numbers < 0:
            numbers = int(input(f"How many numbers do you want in your password? Max: {length - letters}\n"))
    else:
        numbers = 0

    symbols = length - letters - numbers

else:
    letters = int(random.random() * length)
    numbers = int(random.random() * (length - letters))
    symbols = length - letters - numbers

print(f"Letters: {letters} Numbers: {numbers} Symbols: {symbols}")

while len(password) < length:
    new_char = get_next(letters, numbers, symbols)
    if new_char in characters.letters:
        letters -= 1
    elif new_char in characters.numbers:
        numbers -= 1
    else:
        symbols -= 1
    password += new_char

print(f"Your random password is: {password}")




