import datetime
import json

expenses = []

def addExpense():
    
    date = input("Please enter the date (DD-MM-YYYY): ")
    category = input("Please Write your category here: ")
    description = input("please provide description: ")
    amount = int(input("Please enter amount(💲): "))

    expense = {
    "date": date,
    "category": category,
    "description": description,
    "amount": amount
    }
    expenses.append(expense)
    

    print("✅ Expense added Successfully: ")


def viewAllExpense():
    for expense in expenses:
        print(expense)

def viewTotalSpending():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\n========================")
    print("💰 Total Spending")
    print("========================")
    print(f"Total Expenses: ₹{total}")
    print("========================")

while True:
    print("\n Welcome to Expense Tracker: 💸\n")
    print("======= MENU =======")
    print("1 Add Expense: ")
    print("2 View All Expense: ")
    print("3 View total spending: ")
    print("4 Exit: \n")

    choice = int(input("\nEnter your choice between 1 to 4: "))

    match choice:
        case 1:
            addExpense()
        case 2:
            viewAllExpense()    
        case 3:
            viewTotalSpending()
        case 4:
            break
        case _:
            print("\n Invalid choice")   
        
        

    
