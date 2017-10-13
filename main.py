#steel bearing dilemna
import random
from random import shuffle

balls = [1,2,3,4,5,6,7,8,9,10]
shuffledBalls = [1,2,3,4,5,6,7,8,9,10]
shuffle(shuffledBalls)

print("--------------------")
print("1,2,3,4,5,6,7,8,9,10")
print("--------------------")
print(" ")
print("Think of one of the numbers and decide if it is heavier or lighter.")
print(" ")
print("Weighing scales:")
print(" ")
print("side 1  -  side 2")
print(str(shuffledBalls[0]) + ", " + str(shuffledBalls[1]) + ", " + str(shuffledBalls[2]) + " - " + str(shuffledBalls[3]) + ", " + str(shuffledBalls[4]) + ", " + str(shuffledBalls[5]))
