# Python number guessing game
import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guess = int(input("What do you think the number is?: "))

while True:
    if guess > answer:
        print("Too high! Try again!")
        guess = int(input("What do you think the number is?: "))
    elif guess < answer:
        print("Too low! Try again!")
        guess = int(input("What do you think the number is?: "))
    else:
        print("Correct! You win!")
        break