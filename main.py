from random import shuffle

print("This will determine which ball is odd and if it is heavier or lighter in 3 iterations.")
print(" ")

shuffleBalls = [1,2,3,4,5,6,7,8,9,10]
print(shuffleBalls)
shuffle(shuffleBalls)

print("Mentally pick a numbered ball between 1-10 and decide if it is heavier or lighter.")
print("All other balls have an equal weight")
print(" ")
print("Weighing scales: ")
print(str(shuffleBalls[0]) + ", " + str(shuffleBalls[1]) + ", " + str(shuffleBalls[2]) + " <-> " + str(shuffleBalls[3]) + ", " + str(shuffleBalls[4]) + ", " + str(shuffleBalls[5]))
decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")

if decision == "1":
    print(" ")
    print(str(shuffleBalls[6]) + ", " + str(shuffleBalls[7]) + ", " + str(shuffleBalls[8]) + " <-> " + str(shuffleBalls[3]) + ", " + str(shuffleBalls[4]) + ", " + str(shuffleBalls[5]))
    decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")
    if decision == "1":
        print(" ")
        print(str(shuffleBalls[3]) + " <-> " + str(shuffleBalls[4]))
        decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")
        if decision == "1":
            print("Your ball is number " + str(shuffleBalls[4]) + " and it is heavier")
        elif decision == "2":
            print("Your ball is number " + str(shuffleBalls[3]) + " and it is heavier")
        elif decision == "3":
            print("Your ball is number " + str(shuffleBalls[5]) + " and it is heavier")

    elif decision == "2":
        print("Not possible!!!")

    elif decision == "3":
        print(" ")
        print(str(shuffleBalls[0]) + " <-> " + str(shuffleBalls[1]))
        decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")
        if decision == "1":
            print("Your ball is number " + str(shuffleBalls[0]) + " and it is lighter")
        elif decision == "2":
            print("Your ball is number " + str(shuffleBalls[1]) + " and it is lighter")
        elif decision == "3":
            print("Your ball is number " + str(shuffleBalls[2]) + " and it is lighter")


elif decision == "2":
    print(" ")
    print(str(shuffleBalls[6]) + ", " + str(shuffleBalls[7]) + ", " + str(shuffleBalls[8]) + " <-> " + str(shuffleBalls[3]) + ", " + str(shuffleBalls[4]) + ", " + str(shuffleBalls[5]))
    decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")
    if decision == "1":
        print("Not possible!!!")

    elif decision == "2":
        print(" ")
        print(str(shuffleBalls[3]) + " <-> " + str(shuffleBalls[4]))
        decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")
        if decision == "1":
            print("Your ball is number " + str(shuffleBalls[3]) + " and it is lighter")
        elif decision == "2":
            print("Your ball is number " + str(shuffleBalls[4]) + " and it is lighter")
        elif decision == "3":
            print("Your ball is number " + str(shuffleBalls[5]) + " and it is lighter")

    elif decision == "3":
        print(" ")
        print(str(shuffleBalls[0]) + " <-> " + str(shuffleBalls[1]))
        decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")
        if decision == "1":
            print("Your ball is number " + str(shuffleBalls[1]) + " and it is heavier")
        elif decision == "2":
            print("Your ball is number " + str(shuffleBalls[0]) + " and it is heavier")
        elif decision == "3":
            print("Your ball is number " + str(shuffleBalls[2]) + " and it is heavier")

    

elif decision == "3":
    print(" ")
    print(str(shuffleBalls[0]) + ", " + str(shuffleBalls[1]) + ", " + str(shuffleBalls[2]) + " <-> " + str(shuffleBalls[6]) + ", " + str(shuffleBalls[7]) + ", " + str(shuffleBalls[8]))
    decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")
    if decision == "1":
        print(" ")
        print(str(shuffleBalls[6]) + " <-> " + str(shuffleBalls[7]))
        decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")
        if decision == "1":
            print("Your ball is number " + str(shuffleBalls[7]) + " and it is heavier")
        elif decision == "2":
            print("Your ball is number " + str(shuffleBalls[6]) + " and it is heavier")
        elif decision == "3":
            print("Your ball is number " + str(shuffleBalls[8]) + " and it is heavier")


    elif decision == "2":
        print(" ")
        print(str(shuffleBalls[6]) + " <-> " + str(shuffleBalls[7]))
        decision = input("Is the right side 1) Heavier, 2) Lighter, or 3) The same weigh as the left? ")
        if decision == "1":
            print("Your ball is number " + str(shuffleBalls[6]) + " and it is lighter")
        elif decision == "2":
            print("Your ball is number " + str(shuffleBalls[7]) + " and it is lighter")
        elif decision == "3":
            print("Your ball is number " + str(shuffleBalls[8]) + " and it is lighter")

    elif decision == "3":
        print(" ")
        print(str(shuffleBalls[0]) + ", " + str(shuffleBalls[1]) + ", " + str(shuffleBalls[2]) + " <-> " + str(shuffleBalls[9]) + ", "+ str(shuffleBalls[3]) + ", " + str(shuffleBalls[4]))
        decision = input("Is the right side 1) Heavier, or 2) Lighter? ")
        if decision == "1":
            print("Your ball is number " + str(shuffleBalls[9]) + " and it is heavier")

        elif decision == "2":
            print("Your ball is number " + str(shuffleBalls[9]) + " and it is lighter")

        