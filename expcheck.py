# EXPENSE CHECKER

import datetime
import numpy as np
import pandas as pd
# import pandas as pd
# while n(1)

# Create empty list
GOODS_OR_SERVICES = []
PRICE = []
DATES = []
EXPENSE_TYPE = []
BUDGET_LEFT = []


# create a function to add the expenses to the list and organize the data
def add_expense(good_or_service, price, date, expense_type):
    GOODS_OR_SERVICES.append(good_or_service)
    PRICE.append(price)
    DATES.append(date)
    EXPENSE_TYPE.append(expense_type)


print("Enter Your Budget:")
budget = int(input())
initial_budget = budget


option = -1
while (option != 0):
    print("Expense Checker:")

    print("1. Add Food Expense")
    print("2. Add Household Expense")
    print("3. Add Entertainment Expense")
    print("4. Show And Save The Expense Report")
    print("0. Exit")
    option = int(input("Chose an option:\n"))

    print()

    if option == 0:
        print("exiting the Program")
        break
    elif option == 1:
        print("Adding Food")
        expense_type = "FOOD"
    elif option == 2:
        print("Adding Household")
        expense_type = "HOUSEHOLD"
    elif option == 3:
        print("Adding Entertainment")
        expense_type = "ENTERTAINMENT"
    elif option == 4:

        #a data frame and add the expenses

        expense_report = pd.DataFrame()
        expense_report['GOODS_OR_SERVICES'] = GOODS_OR_SERVICES
        expense_report['PRICE'] = PRICE
        expense_report['DATES'] = DATES
        expense_report['EXPENSE_TYPE'] = EXPENSE_TYPE

        # save the expense report
        expense_report.to_csv('expense.csv')
        # show the expense report
        print(expense_report)
    else :
        print("You choose an incorrect option.Pleas select from option 0,1,2,3 or 4")
    # allow the user to enter the good or service and the price
    if option == 1 or option == 2 or option == 3 or option == 4:
        good_or_service = input('Enter the good or service for the expense type' + expense_type + ':\n')
        price = float(input('Enter the price of good or service:\n'))

        budget = budget - price
        print("You have left amount Rs.", budget)
        if budget == (0.1 * initial_budget):
            print("WARNING!!!!ONLY 10% AMOUNT IS LEFT THAT IS:", budget)

        today = datetime.date.today()
        add_expense(good_or_service, price, today, expense_type)

    print()
