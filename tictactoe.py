import numpy as np


def x_solved(lst):
    flag = 0
    for i in range(0, 3):
        for j in range(1):
            if lst[i][j] == "x" and lst[i][j + 1] == "x" and lst[i][j + 2] == "x":
                return True
                flag = 1
                break
            else:
                continue
    if flag != 1:
        for i in range(3):
            for j in range(1):
                if lst[j][i] == "x" and lst[j + 1][i] == "x" and lst[j + 2][i] == "x":
                    return True
                    flag = 1
                    break
                else:
                    continue
    if flag != 1:
        if lst[0][0] == "x" and lst[1][1] == "x" and lst[2][2] == "x":
            return True
        elif lst[0][2] == "x" and lst[1][1] == "x" and lst[2][0] == "x":
            return True
        else:
            return False


def o_solved(lst):
    flag = 0
    for i in range(0, 3):
        for j in range(1):
            if lst[i][j] == "o" and lst[i][j + 1] == "o" and lst[i][j + 2] == "o":
                return True
                flag = 1
                break
            else:
                continue
    if flag != 1:
        for i in range(3):
            for j in range(1):
                if lst[j][i] == "o" and lst[j + 1][i] == "o" and lst[j + 2][i] == "o":
                    return True
                    flag = 1
                    break
                else:
                    continue
    if flag != 1:
        if lst[0][0] == "o" and lst[1][1] == "o" and lst[2][2] == "o":
            return True
        elif lst[0][2] == "o" and lst[1][1] == "o" and lst[2][0] == "o":
            return True
        else:
            return False


lst = [[None, None, None],
       [None, None, None],
       [None, None, None]]

d_lst = np.array(lst)

ref_lst = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
ref_lst = np.array(ref_lst)
f2 = 0
for i in range(0, 9):
    d_list = np.array(lst)
    if i % 2 == 0:
        print("Current Board:\n", d_list)
        print("Choose the number to put 'x':\n", ref_lst)
        x = int(input())
        if x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7 or x == 8 or x == 9:
            for i in range(0, 3):
                for j in range(0, 3):
                    if ref_lst[i][j] == x:
                        lst[i][j] = "x"
                    else:
                        continue
        if x_solved(lst):
            print("'X' IS THE WINNER")
            d_list = np.array(lst)
            print(d_list)
            f2 = 1
            break

    else:
        print("Current Board:\n", d_list)
        print("Choose the number to put '0':\n", ref_lst)
        x = int(input())
        if x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7 or x == 8 or x == 9:
            for i in range(0, 3):
                for j in range(0, 3):
                    if ref_lst[i][j] == x:
                        lst[i][j] = "o"
                    else:
                        continue
        if o_solved(lst):
            print("'O' IS THE WINNER")
            d_list = np.array(lst)
            print(d_list)
            f2 = 1
            break

if f2 == 0:
    d_list = np.array(lst)
    print("Match Drawn\n", d_list)
