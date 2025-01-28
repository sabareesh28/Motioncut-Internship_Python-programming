

import json
DATA_FILE = "expenses.json"
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

"""#ADD EXPENSES"""

from datetime import datetime


def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return

    try:
        amount = float(input("Enter the expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    category = input("Enter the category (e.g., Food, Transportation, Entertainment): ").strip()
    description = input("Enter a brief description of the expense: ").strip()

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
    }

    data = load_data()
    data.append(expense)
    save_data(data)
    print("Expense added successfully!")

"""#VIEW SUMMARY"""

def view_monthly_summary(data):
    monthly_expenses = {}
    for expense in data:
        month = expense["date"][:7]
        monthly_expenses[month] = monthly_expenses.get(month, 0) + expense["amount"]

    print("\nMonthly Expenses:")
    for month, total in sorted(monthly_expenses.items()):
        print(f"{month}: ${total:.2f}")

"""#CATEGORY SUMMARY"""

def view_category_summary(data):
    category_expenses = {}
    for expense in data:
        category = expense["category"]
        category_expenses[category] = category_expenses.get(category, 0) + expense["amount"]

    print("\nCategory-wise Expenses:")
    for category, total in sorted(category_expenses.items()):
        print(f"{category}: ${total:.2f}")

"""#VIEW SUMMARY"""

def view_summary():
    data = load_data()
    if not data:
        print("No expense data available.")
        return

    print("\nSummary Menu:")
    print("1. Monthly Summary")
    print("2. Category-wise Summary")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        view_monthly_summary(data)
    elif choice == "2":
        view_category_summary(data)
    else:
        print("Invalid choice.")

"""#MAIN FUNCTION"""

def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

"""#RUN THE PROGRAM"""

if __name__ == "__main__":
    print("Welcome to the Expense Tracker!")
    main_menu()