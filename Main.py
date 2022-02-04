import collections
import numpy as np
import pandas as pd

array_one = [[0 for x in range(3)] for y in range(3)]
array_two = [[0 for x in range(3)] for y in range(3)]
array_three = [[0 for x in range(3)] for y in range(3)]
array_four = [[0 for x in range(3)] for y in range(3)]
array_five = [[0 for x in range(3)] for y in range(3)]
array_six = [[0 for x in range(3)] for y in range(3)]
array_seven = [[0 for x in range(3)] for y in range(3)]
array_eight = [[0 for x in range(3)] for y in range(3)]
array_nine = [[0 for x in range(3)] for y in range(3)]

square_list = [array_one, array_two, array_three, array_four, array_five, array_six, array_seven, array_eight, array_nine]

another_num = "Y"

while another_num.upper() == "Y":
    indicator = 0
    square_num = 0

    while indicator == 0:
        try:
            square_num = int(input("Enter the number of the square the given number is in (left to right, 1-9): "))
            indicator = 1
        except:
            print("Invalid input. Answer is not an integer")

    while square_num > 9 or square_num < 1:
        print("Invalid input. Number is either too low or too high")
        square_num = int(input("Enter the number of the square the given number is in (left to right, 1-9): "))


    given_num = input("Enter the spot of the number in the square (ex. a number in the top middle spot in the square would be 1 2): ")
    given_num = given_num.strip()

    while len(given_num) != 3:
        print("Invalid input. Answer is too long")
        given_num = input("Enter the spot of the number in the square (ex. a number in the top middle spot in the square would be 1 2): ")

    indicator = 0
    row = 0
    column = 0

    while indicator == 0:
        try:
            row = int(given_num[0])
            column = int(given_num[2])
            indicator = 1
        except:
            print("Invalid input. Answer is not an integer")

            given_num = input("Enter the spot of the number in the square (ex. a number in the top middle spot in the square would be 1 2): ")
            given_num = given_num.strip()

            while len(given_num) != 3:
                print("Invalid input. Answer is too long")
                given_num = input("Enter the spot of the number in the square (ex. a number in the top middle spot in the square would be 1 2): ")


    indicator = 0
    num = 0

    while indicator == 0:
        try:
            num = int(input("What is the given number? "))
            indicator = 1
        except:
            print("Invalid input. Answer is not an integer")

    while num > 9 or num < 1:
        print("Invalid input. Number is either too low or too high")
        indicator = 0
        while indicator == 0:
            try:
                num = int(input("What is the given number? "))
                indicator = 1
            except:
                print("Invalid input. Answer is not an integer")


    if square_num == 1:
        array_one[row][column] = num
    elif square_num == 2:
        array_two[row][column] = num
    elif square_num == 3:
        array_three[row][column] = num
    elif square_num == 4:
        array_four[row][column] = num
    elif square_num == 5:
        array_five[row][column] = num
    elif square_num == 6:
        array_six[row][column] = num
    elif square_num == 7:
        array_seven[row][column] = num
    elif square_num == 8:
        array_eight[row][column] = num
    elif square_num == 9:
        array_nine[row][column] = num

    another_num = input("Do you want to enter another given value? (Y/N) ")


def solver(list):
    for index, i in enumerate(list):
        arr1 = np.array(i[0])
        arr2 = np.array(i[1])
        arr3 = np.array(i[2])
        arr = np.concatenate((arr1, arr2, arr3))

        if len(pd.Series(arr)[pd.Series(arr).duplicated()].values) > 0:
            print(i)
            break
        if index == len(list)-1:
            print("TEST")



solver(square_list)

