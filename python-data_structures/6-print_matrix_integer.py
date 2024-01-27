#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        n = 0
        for j in matrix[i]:
            print("{:d}".format(j), end="")
            if n < len(matrix[i]) - 1:
                print(end=" ")
            n += 1
        print()
