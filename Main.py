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
row = 0
column = 0

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
        print("Invalid input. Answer is either too long or too short")
        given_num = input("Enter the spot of the number in the square (ex. a number in the top middle spot in the square would be 1 2): ")

    indicator = 0

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
                print("Invalid input. Answer is either too long or too short")
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

    row = row-1
    column = column-1

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
    switch = 0

    # Base case
    for index, i in enumerate(list):
        arr1 = np.array(i[0])
        arr2 = np.array(i[1])
        arr3 = np.array(i[2])
        arr = np.concatenate((arr1, arr2, arr3))

        if len(pd.Series(arr)[pd.Series(arr).duplicated()].values) > 0:
            switch = 1

    if switch == 0:
        arr1 = np.array([0, 0, 0])
        arr2 = np.array([0, 0, 0])
        arr3 = np.array([0, 0, 0])
        if row == 0:
            arr1 = np.array(list[0][0])
            arr2 = np.array(list[1][0])
            arr3 = np.array(list[2][0])
        elif row == 1:
            arr1 = np.array(list[0][1])
            arr2 = np.array(list[1][1])
            arr3 = np.array(list[2][1])
        elif row == 2:
            arr1 = np.array(list[0][2])
            arr2 = np.array(list[1][2])
            arr3 = np.array(list[2][2])
        elif row == 3:
            arr1 = np.array(list[3][0])
            arr2 = np.array(list[4][0])
            arr3 = np.array(list[5][0])
        elif row == 4:
            arr1 = np.array(list[3][1])
            arr2 = np.array(list[4][1])
            arr3 = np.array(list[5][1])
        elif row == 5:
            arr1 = np.array(list[3][2])
            arr2 = np.array(list[4][2])
            arr3 = np.array(list[5][2])
        elif row == 6:
            arr1 = np.array(list[6][0])
            arr2 = np.array(list[7][0])
            arr3 = np.array(list[8][0])
        elif row == 7:
            arr1 = np.array(list[6][1])
            arr2 = np.array(list[7][1])
            arr3 = np.array(list[8][1])
        elif row == 8:
            arr1 = np.array(list[6][2])
            arr2 = np.array(list[7][2])
            arr3 = np.array(list[8][2])

        row_arr = np.concatenate((arr1, arr2, arr3))
        if len(pd.Series(row_arr)[pd.Series(row_arr).duplicated()].values) > 0:
            switch = 1

    if switch == 0:
        arr = 0
        if column == 0:
            arr1 = list[0][0][0]
            arr2 = list[0][1][0]
            arr3 = list[0][2][0]
            arr4 = list[3][0][0]
            arr5 = list[3][1][0]
            arr6 = list[3][2][0]
            arr7 = list[6][0][0]
            arr8 = list[6][1][0]
            arr9 = list[6][2][0]
            arr = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])
        elif column == 1:
            arr1 = list[0][0][1]
            arr2 = list[0][1][1]
            arr3 = list[0][2][1]
            arr4 = list[3][0][1]
            arr5 = list[3][1][1]
            arr6 = list[3][2][1]
            arr7 = list[6][0][1]
            arr8 = list[6][1][1]
            arr9 = list[6][2][1]
            arr = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])
        elif column == 2:
            arr1 = list[0][0][2]
            arr2 = list[0][1][2]
            arr3 = list[0][2][2]
            arr4 = list[3][0][2]
            arr5 = list[3][1][2]
            arr6 = list[3][2][2]
            arr7 = list[6][0][2]
            arr8 = list[6][1][2]
            arr9 = list[6][2][2]
            arr = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])
        elif column == 3:
            arr1 = list[1][0][0]
            arr2 = list[1][1][0]
            arr3 = list[1][2][0]
            arr4 = list[4][0][0]
            arr5 = list[4][1][0]
            arr6 = list[4][2][0]
            arr7 = list[7][0][0]
            arr8 = list[7][1][0]
            arr9 = list[7][2][0]
            arr = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])
        elif column == 4:
            arr1 = list[1][0][1]
            arr2 = list[1][1][1]
            arr3 = list[1][2][1]
            arr4 = list[4][0][1]
            arr5 = list[4][1][1]
            arr6 = list[4][2][1]
            arr7 = list[7][0][1]
            arr8 = list[7][1][1]
            arr9 = list[7][2][1]
            arr = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])
        elif column == 5:
            arr1 = list[1][0][2]
            arr2 = list[1][1][2]
            arr3 = list[1][2][2]
            arr4 = list[4][0][2]
            arr5 = list[4][1][2]
            arr6 = list[4][2][2]
            arr7 = list[7][0][2]
            arr8 = list[7][1][2]
            arr9 = list[7][2][2]
            arr = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])
        elif column == 6:
            arr1 = list[2][0][0]
            arr2 = list[2][1][0]
            arr3 = list[2][2][0]
            arr4 = list[5][0][0]
            arr5 = list[5][1][0]
            arr6 = list[5][2][0]
            arr7 = list[8][0][0]
            arr8 = list[8][1][0]
            arr9 = list[8][2][0]
            arr = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])
        elif column == 7:
            arr1 = list[2][0][1]
            arr2 = list[2][1][1]
            arr3 = list[2][2][1]
            arr4 = list[5][0][1]
            arr5 = list[5][1][1]
            arr6 = list[5][2][1]
            arr7 = list[8][0][1]
            arr8 = list[8][1][1]
            arr9 = list[8][2][1]
            arr = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])
        elif column == 8:
            arr1 = list[2][0][2]
            arr2 = list[2][1][2]
            arr3 = list[2][2][2]
            arr4 = list[5][0][2]
            arr5 = list[5][1][2]
            arr6 = list[5][2][2]
            arr7 = list[8][0][2]
            arr8 = list[8][1][2]
            arr9 = list[8][2][2]
            arr = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])

        if len(pd.Series(arr)[pd.Series(arr).duplicated()].values) > 0:
            switch = 1

    if switch == 0:
        return list


    # Recursive case
    for index_one, i in enumerate(list):
        count = 0
        for index_two, j in enumerate(i):
            for index_three, k in enumerate(j):
                list[index_one][index_two][index_three] = count
                solver(list)
                count = count + 1
                list[index_one][index_two][index_three] = 0
                solver(list)




solver(square_list)

