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

        
        

    
