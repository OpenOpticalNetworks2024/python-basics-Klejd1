"""Exercise Set 3: Numpy Exercises"""

import numpy as np

import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    a = np.arange(8).reshape(4,2)
    print(a)
    print(f"Number of dimensions {a.ndim}")
    print(f"Size of the array {a.size}")
    print(f"Shape of the numpy array {a.shape}")

# ex2
def exercise2():
    a = np.arange(100,200,10).reshape(5,2)
    print(a)

# ex3
def exercise3():
    a = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
    print(a)
    b = []
    for i in range(3):
        c = int(a[i,2])
        b.append(c)

    print(f"The array: {b} ")


# ex4
def exercise4():
    a = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

    print(a)
    b = []
    even_col = []
    for i in range(5):
        if (i % 2) != 0:
            for m in range(4):
                c = int(a[i,m])
                b.append(c)
        for m in range(4):
            if (m%2) == 0:
                c = int(a[i,m])
                even_col.append(c)

    print(f"The array of the odd rows: {b} \nThe array of even coloums: {even_col}")

# ex5
def exercise5():
    a = np.array([[5, 6, 9], [21, 18, 27]])

    b = np.array([[15, 33, 24], [4, 7, 1]])

    c = np.add(a,b)
    print(c)

    print(np.sqrt(c))

# ex6
def exercise6():
    a = np.array([[34,43,73],[82,22,12],[53,94,66]])

    print(np.sort(a))


# ex7
def exercise7():
    a = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

    print(f"The maximum of axis 0: {np.amax(a[0])}")
    print(f"The min of axis 1: {np.amin(a[1])}")


# ex8
def exercise8():
    a = np.array([[34,43,73],[82,22,12],[53,94,66]])
    print(a)

    for i in range(3):
        a[i,1] = 10

    print(f"Modified \n{a}")



if __name__ == "__main__":
    print("EXERCISE SET 3: NumPy Exercises")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
