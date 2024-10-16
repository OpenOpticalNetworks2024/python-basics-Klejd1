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
    my_list = [1,2,4,23,21,5,4,89,56,1]
    for i in range(len(my_list)):
        b = my_list[i]
    def my_fun():
        if my_list[0] == b:
            return True
        else:
            return False
    print(my_fun())



# ex4
def exercise4():
    my_list = [10,20,30,33,21,67,55,34,60,70,88,66,102,43,25]
    for i in range(len(my_list)):
        if (my_list[i] % 5) == 0:
            print(my_list[i])

# ex5
def exercise5():
    my_string = "Emma is a good developer. Emma is also a writer."
    counter = 0
    for i in range(len(my_string)):
        if my_string[i:i+4] == "Emma":
            counter +=1

    print(f"The word 'Emma' has been used {counter} times")


# ex6
def exercise6():
    list1 = [1,3,5,10,24,32]
    list2 = [2,4,6,11,25,33]

    list3 = []

    for num in list1:
        if num % 2 != 0:
            list3.append(num)

    for num in list2:
        if num % 2 == 0:
            list3.append(num)

    print(list3)


# ex7
def exercise7():
    string_1 = "Python is fun to learn"
    string_2 = " is a programming language and "

    new_string = string_1[:6] + string_2 + string_1[6:]

    print(new_string)


# ex8
def exercise8():
    a = input("Put the first string: ")
    b = input("Put the second string: ")
    m = int(len(a) / 2)
    n = int(len(b) / 2)

    newString = a[0] + a[m] + a[int(len(a)) - 1] + b[0] + b[n] + b[int(len(b)) - 1]

    print(newString)


# ex9
def exercise9():
    a = input("Input the string: ")
    lower = 0
    upper = 0
    digit = 0
    special = 0
    for i in range(len(a)):
        if a[i].islower() == True:
            lower += 1
        elif a[i].isupper() == True:
            upper += 1
        elif a[i].isdigit() == True:
            digit += 1
        elif a[i].isalnum() == False:
            special += 1

    print(f"There are {lower} lower case characters\nThere are {upper} upper case characters \nThere are {digit} digit characters and {special} special characters")
# ex10
def exercise10():
    a = "USA is an ancronym of United States of America. There are 50 states in uSa and UsA is very advanced"
    b = a.lower()
    count = 0
    for i in range(len(a)):
        if b[i:i+3] == "usa":
            count += 1
    print(f"There are {count} ocurrencies of the word 'USA' ignoring the case")

# ex11
def exercise11():
    a = "Here are 2 apples, 3 oranges and 4 bananas"
    sum = 0
    counter = 0
    for i in range(len(a)):
        if a[i].isdigit() == True:
            sum = sum + int(a[i])
            counter += 1
    print(f"The sum is {sum} and the average is {sum / counter}")



# ex12
def exercise12():
    def count_characters(input_string):
        char_count = {}
        for char in input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
    input_string = "Ciao, this is an example string for the program"
    a = count_characters(input_string)
    print("Character counts:", a)


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
