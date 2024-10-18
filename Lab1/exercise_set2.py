"""Exercise Set 2: Data Structures"""
from winreg import SetValueEx

import numpy as np
import matplotlib as plt
from fontTools.merge.util import first


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    listOne = [3, 6, 9, 12, 15, 18, 21]

    listTwo = [4, 8, 12, 16, 20, 24, 28]

    index = 0
    list3 = []

    for i in range(len(listTwo)):
        if (i%2) != 0:
            list3.insert(index, listOne[i])
            index += 1
        elif (i%2) == 0:
            list3.insert(index, listTwo[i])
            index += 1
    print(list3)
# ex2
def exercise2():
    sampleList = [34, 54, 67, 89, 11, 43, 94]

    sampleList[1] = sampleList[1] + 11
    sampleList[len(sampleList) - 1] =  sampleList[len(sampleList) - 1] + 11
    sampleList.pop(4)
    print(sampleList)


def exercise3():
    sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    a = 3
    list1 = [0] * a
    list2 = [0] * a
    list3 = [0] * a

    for i in range(len(sampleList)):
        if i < 3:
            list1[i] = sampleList[i]
        elif i >= 3 and i < 6:
            list2[i - 3] = sampleList[i]
        else:
            list3[i - 6] = sampleList[i]
    list1.reverse()
    list2.reverse()
    list3.reverse()
    print(list1, list2, list3)

# ex4
def exercise4():
    sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]

    my_dictionary = {}
    for ele in sampleList:
        if ele in my_dictionary:
            my_dictionary[ele] += 1
        else:
            my_dictionary[ele] = 1

    print(my_dictionary)


# ex5
def exercise5():
    firstList = [2, 3, 4, 5, 6, 7, 8]

    secondList = [4, 9, 16, 25, 36, 49, 64]

    a = set(zip(firstList, secondList))
    print(a)



# ex6
def exercise6():
    firstSet = {23, 42, 65, 57, 78, 83, 29}

    secondSet = {57, 83, 29, 67, 73, 43, 48}

    print(firstSet - secondSet)


# ex7
def exercise7():
    firstSet = {57, 83, 29}

    secondSet = {57, 83, 29, 67, 73, 43, 48}

    if firstSet.issubset(secondSet):
        print("First set is subset of the second set")
    if secondSet.issuperset(firstSet):
        print("Second set is a superset of the firs set")



# ex8
# It seems the loop is not checking 95
def exercise8():
    rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]

    sampleDict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
    for i in rollNumber:
        if i not in sampleDict.values():
            rollNumber.remove(i)
    print(rollNumber)



# ex9
def exercise9():
    speed = {  'Jan':47,  'Feb':52, 'March':47, 'April':44, 'May':52, 'June':53, 'July':54, 'Aug':44, 'Sept':54}

    my_list = []
    for i in speed.values():
        if i not in my_list:
            my_list.append(i)
    print(my_list)






    # ex10
def exercise10():
    sampleList = [87, 52, 44, 53, 54, 87, 52, 53]

    a = set(sampleList)
    b = tuple(a)

    print(f"The tuple {b}")
    print(f"Minimum value {min(b)} and maximum value {max(b)}")



if __name__ == "__main__":
    print("EXERCISE SET 2: Data Structures")
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