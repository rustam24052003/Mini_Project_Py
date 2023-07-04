import random

num = random.randint(1, 100)
print("Welcome to Numerical Guessing Game")


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100


def is_num_valid():
    while True:
        guess = input()
        if is_valid(guess):
            return int(guess)
        else:
            print("Please use number in range [0,100]")


def compare_num():
    while True:
        n = is_num_valid()
        if n > num:
            print("Please type number less than yours")
        elif n < num:
            print("Please type number greater than yours")
        else:
            print("Good job,you guessed it")
            break

compare_num()
