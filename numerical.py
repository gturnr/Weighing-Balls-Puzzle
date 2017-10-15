from random import shuffle
import random

print("This will determine which ball is odd and if it is heavier or lighter in 3 iterations.")

def menu():
    print(" ")
    input("Hit enter when you are ready to calculate which ball is odd")
    print(" ")
    main()

def main():
    oddWeights = [-1, 1]
    shuffleBalls = [1,2,3,4,5,6,7,8,9,10]
    shuffleBallWeights = [0,0,0,0,0,0,0,0,0,0]
    print(shuffleBalls)
    shuffle(shuffleBalls)
    print("Generating a random ball and it's weight...")
    chosenBall = random.choice(shuffleBalls)
    chosenWeight = random.choice(oddWeights)
    shuffleBallWeights[shuffleBalls.index(chosenBall)] = chosenWeight

    print("ball " + str(chosenBall))
    print("weight " + str(chosenWeight))
    print(" ")


    print(" ")

    print("Weighing scales: ")
    print(str(shuffleBalls[0]) + ", " + str(shuffleBalls[1]) + ", " + str(shuffleBalls[2]) + " <-> " + str(shuffleBalls[3]) + ", " + str(shuffleBalls[4]) + ", " + str(shuffleBalls[5]))
    side1 = shuffleBallWeights[0] + shuffleBallWeights[1] + shuffleBallWeights[2]
    side2 = shuffleBallWeights[3] + shuffleBallWeights[4] + shuffleBallWeights[5]

    if side2 > side1:
        print("Right side heavier")
        print(str(shuffleBalls[6]) + ", " + str(shuffleBalls[7]) + ", " + str(shuffleBalls[8]) + " <-> " + str(shuffleBalls[3]) + ", " + str(shuffleBalls[4]) + ", " + str(shuffleBalls[5]))
        side1 = shuffleBallWeights[6] + shuffleBallWeights[7] + shuffleBallWeights[8]
        side2 = shuffleBallWeights[3] + shuffleBallWeights[4] + shuffleBallWeights[5]

        if side2 > side1:
            print("Right side heavier")
            print(str(shuffleBalls[3]) + " <-> " + str(shuffleBalls[4]))
            if shuffleBallWeights[4] > shuffleBallWeights[3]:
                print("Your ball is number " + str(shuffleBalls[4]) + " and it is heavier")
            elif shuffleBallWeights[4] < shuffleBallWeights[3]:
                print("Your ball is number " + str(shuffleBalls[3]) + " and it is heavier")
            elif shuffleBallWeights[4] == shuffleBallWeights[3]:
                print("Your ball is number " + str(shuffleBalls[5]) + " and it is heavier")

        elif side2 < side1:
            print("Left side heavier")
            print("Not possible!!!")

        elif side2 == side1:
            print("Sides equal")
            print(str(shuffleBalls[0]) + " <-> " + str(shuffleBalls[1]))
            if shuffleBallWeights[1] > shuffleBallWeights[0]:
                print("Your ball is number " + str(shuffleBalls[0]) + " and it is lighter")
            elif shuffleBallWeights[1] < shuffleBallWeights[0]:
                print("Your ball is number " + str(shuffleBalls[1]) + " and it is lighter")
            elif shuffleBallWeights[1] == shuffleBallWeights[0]:
                print("Your ball is number " + str(shuffleBalls[2]) + " and it is lighter")


    elif side2 < side1:
        print("Left side heavier")
        print(str(shuffleBalls[6]) + ", " + str(shuffleBalls[7]) + ", " + str(shuffleBalls[8]) + " <-> " + str(shuffleBalls[3]) + ", " + str(shuffleBalls[4]) + ", " + str(shuffleBalls[5]))
        side1 = shuffleBallWeights[6] + shuffleBallWeights[7] + shuffleBallWeights[8]
        side2 = shuffleBallWeights[3] + shuffleBallWeights[4] + shuffleBallWeights[5]

        if side2 > side1:
            print("Right side heavier")
            print("Not possible!!!")

        elif side2 < side1:
            print("Left side heavier")
            print(str(shuffleBalls[3]) + " <-> " + str(shuffleBalls[4]))
            if shuffleBallWeights[4] > shuffleBallWeights[3]:
                print("Your ball is number " + str(shuffleBalls[3]) + " and it is lighter")
            elif shuffleBallWeights[4] < shuffleBallWeights[3]:
                print("Your ball is number " + str(shuffleBalls[4]) + " and it is lighter")
            elif shuffleBallWeights[4] == shuffleBallWeights[3]:
                print("Your ball is number " + str(shuffleBalls[5]) + " and it is lighter")

        elif side2 == side1:
            print("Sides equal")
            print(str(shuffleBalls[0]) + " <-> " + str(shuffleBalls[1]))
            if shuffleBallWeights[1] > shuffleBallWeights[0]:
                print("Your ball is number " + str(shuffleBalls[1]) + " and it is heavier")
            elif shuffleBallWeights[1] < shuffleBallWeights[0]:
                print("Your ball is number " + str(shuffleBalls[0]) + " and it is heavier")
            elif shuffleBallWeights[1] == shuffleBallWeights[0]:
                print("Your ball is number " + str(shuffleBalls[2]) + " and it is heavier")

    

    elif side1 == side2:
        print("Sides equal")
        print(str(shuffleBalls[0]) + ", " + str(shuffleBalls[1]) + ", " + str(shuffleBalls[2]) + " <-> " + str(shuffleBalls[6]) + ", " + str(shuffleBalls[7]) + ", " + str(shuffleBalls[8]))
        side1 = shuffleBallWeights[0] + shuffleBallWeights[1] + shuffleBallWeights[2]
        side2 = shuffleBallWeights[6] + shuffleBallWeights[7] + shuffleBallWeights[8]
        if side2 > side1:
            print("Right side heavier")
            print(str(shuffleBalls[6]) + " <-> " + str(shuffleBalls[7]))
            if shuffleBallWeights[7] > shuffleBallWeights[6]:
                print("Your ball is number " + str(shuffleBalls[7]) + " and it is heavier")
            elif shuffleBallWeights[7] < shuffleBallWeights[6]:
                print("Your ball is number " + str(shuffleBalls[6]) + " and it is heavier")
            elif shuffleBallWeights[7] == shuffleBallWeights[6]:
                print("Your ball is number " + str(shuffleBalls[8]) + " and it is heavier")


        elif side2 < side1:
            print("Left side heavier")
            print(str(shuffleBalls[6]) + " <-> " + str(shuffleBalls[7]))
            if shuffleBallWeights[7] > shuffleBallWeights[6]:
                print("Your ball is number " + str(shuffleBalls[6]) + " and it is lighter")
            elif shuffleBallWeights[7] < shuffleBallWeights[6]:
                print("Your ball is number " + str(shuffleBalls[7]) + " and it is lighter")
            elif shuffleBallWeights[7] == shuffleBallWeights[6]:
                print("Your ball is number " + str(shuffleBalls[8]) + " and it is lighter")

        elif side2 == side1:
            print("Sides equal")
            print(str(shuffleBalls[0]) + " <-> " + str(shuffleBalls[9]))
            if shuffleBallWeights[9] > shuffleBallWeights[0]:
                print("Your ball is number " + str(shuffleBalls[9]) + " and it is heavier")

            elif shuffleBallWeights[9] < shuffleBallWeights[0]:
                print("Your ball is number " + str(shuffleBalls[9]) + " and it is lighter")

    menu()
menu()