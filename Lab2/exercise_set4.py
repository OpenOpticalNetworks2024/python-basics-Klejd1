import pandas as pd
import matplotlib.pyplot as plt

from pandas import read_csv


#1. Read Total profit of all months and show it using a line plot
def exercise1():
    sales = pd.read_csv('sales_data.csv')
    print(sales["total_profit"])

    sales["total_profit"].plot()
    plt.xlabel('Months')
    plt.ylabel('Profit')
    plt.show()

#2. Get Total profit of all months and show line plot with the following Style properties:
#label = ’Profit data of last year’; color=’r’; marker=’o’;
#markerfacecolor=’k’; linestyle=’–’; linewidth=3.

def exercise2():
    sales = pd.read_csv("sales_data.csv")
    sales["total_profit"].plot(color='r', marker='o', markerfacecolor='k', linestyle='-')
    plt.title("Profit Data of Last Year")
    plt.show()
#3. Read all product sales data and show it using a multiline plot
def exercise3():
    sales = pd.read_csv("sales_data.csv")
    sales.iloc[0:12, 1:7].plot()
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.show()

#4. Read toothpaste sales data of each month and show it using a scatter plot
def exercise4():
    sales = pd.read_csv("sales_data.csv")
    plt.scatter(sales["month_number"], sales["toothpaste"])
    plt.show()

#5. Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
def exercise5():
    sales = read_csv("sales_data.csv")
    plt.bar(sales["month_number"], sales['bathingsoap'], color = 'red')
    plt.xlabel('Months')
    plt.ylabel('Sales')
    plt.show()
#6. Read the total profit of each month and show it using the histogram to see most common profit ranges
def exercise6():
    sales = read_csv('sales_data.csv')
    plt.hist(sales["total_profit"])
    plt.show()
#7. Read Bathing soap facewash of all months and display it using the Subplot
def exercise7():
    sales = read_csv('sales_data.csv')
    plt.subplot(1,2, 1)
    plt.plot(sales["month_number"], sales["bathingsoap"])
    plt.title("Sales from bathing soap")
    plt.subplot(1,2,2)
    plt.plot(sales["month_number"], sales["facewash"], color = 'r')
    plt.title("Sales from facewash")
    plt.show()

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
