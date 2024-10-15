"""Exercise Set 1: Python Basics"""

#import numpy as np

#import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions

# ex1
def exercise1():
    def calc(a,b):
      if a * b > 1000:
        return a+b
      else:
          return a * b
    a = int(input("Put the first number: "))
    b = int(input("Put the second number: "))

    print(calc(a,b))


# ex2
def exercise2():
    a = [10,20,30,40,50,60,70,80,90,100]

    i = int(input("Put the index from where the iteration will start: "))

    for i in range(10):
        b = a[i]

    print("The sum is:", b + a[i-1])


# ex3
def exercise3():
    pass


# ex4
def exercise4():
    pass


# ex5
def exercise5():
    pass


# ex6
def exercise6():
    pass


# ex7
def exercise7():
    pass


# ex8
def exercise8():
    pass


# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


# ex11
def exercise11():
    pass


# ex12
def exercise12():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 1")
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
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()
