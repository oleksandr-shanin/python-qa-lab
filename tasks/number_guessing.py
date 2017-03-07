from math import log2
from random import randint

upper_boundary = int(input('Set the upper boundary: '))
print("OK, I'm thinking of a number between 1 an", upper_boundary)
number = randint(1, upper_boundary)
# print(number)
max_tries_left = int(log2(upper_boundary))
print("Try to guess it. You've got", max_tries_left + 1, "tries to do it.")
suggestion = int(input())
while max_tries_left:
    if suggestion > number:
        print("Your guess is too high.", max_tries_left, "tries left.")
    elif suggestion < number:
        print("Your guess is too low.", max_tries_left, "tries left.")
    else:
        print("You're right! It's", number)
        break
    suggestion = int(input())
    max_tries_left -= 1
else:
    if suggestion == number:
        print("You're right! It's", number)
    else:
        print("Too much tries, it was ", number)
