import os

expense_file = "expenses.csv"

def add_expense():
    date = input("Date (DD-MM-YYYY): ")
    category = input("Category (e.g., Food, Travel): ")
    description = input("Description: ")
    amount = input("Amount: ")

    expense = f"{date},{category},{description},{amount}\n"

    with open(expense_file, 'a') as file:
        file.write(expense)
    
    print("Expense added!")

def view_expenses():
    if not os.path.exists(expense_file):
        print("No expenses recorded.")
        return

    with open(expense_file, 'r') as file:
        print("Date       | Category   | Description       | Amount")
        print("-" * 50)

        for line in file:
            date, category, description, amount = line.strip().split(",")
            print(f"{date}  | {category:10} | {description:15} | {amount}")

def filter_by_category():
    if not os.path.exists(expense_file):
        print("No expenses found.")
        return

    category = input("Category to filter by: ")
    total = 0

    with open(expense_file, 'r') as file:
        print("Date       | Category   | Description       | Amount")
        print("-" * 50)

        for line in file:
            date, cat, description, amount = line.strip().split(",")
            if cat.lower() == category.lower():
                print(f"{date}  | {cat:10} | {description:15} | {amount}")
                total += float(amount)

    print(f"\nTotal in {category}: {total}")

def delete_expense():
    if not os.path.exists(expense_file):
        print("No expenses to delete.")
        return

    view_expenses()
    date_to_delete = input("Date of the expense to delete (DD-MM-YYYY): ")

    with open(expense_file, 'r') as file:
        lines = file.readlines()

    with open(expense_file, 'w') as file:
        deleted = False
        for line in lines:
            if date_to_delete not in line:
                file.write(line)
            else:
                deleted = True

    if deleted:
        print(f"Expense on {date_to_delete} deleted.")
    else:
        print("No matching expense found.")

def edit_expense():
    if not os.path.exists(expense_file):
        print("No expenses to edit.")
        return

    view_expenses()
    date_to_edit = input("Date of the expense to edit (DD-MM-YYYY): ")

    with open(expense_file, 'r') as file:
        lines = file.readlines()

    with open(expense_file, 'w') as file:
        updated = False
        for line in lines:
            if date_to_edit in line:
                category = input("New category: ")
                description = input("New description: ")
                amount = input("New amount: ")
                updated_expense = f"{date_to_edit},{category},{description},{amount}\n"
                file.write(updated_expense)
                updated = True
            else:
                file.write(line)

    if updated:
        print("Expense updated.")
    else:
        print("No matching expense found.")

def total_expense():
    if not os.path.exists(expense_file):
        print("No expenses recorded.")
        return

    total = 0
    with open(expense_file, 'r') as file:
        for line in file:
            _, _, _, amount = line.strip().split(",")
            total += float(amount)

    print(f"Total expenses: {total}")

def clear_all_expenses():
    if not os.path.exists(expense_file):
        print("No expenses to clear.")
        return

    confirm = input("Are you sure you want to clear all expenses? (yes/no): ")
    if confirm.lower() == 'yes':
        with open(expense_file, 'w'):
            pass
        print("All expenses cleared.")
    else:
        print("Action cancelled.")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View expenses by category")
        print("4. Delete an expense")
        print("5. Edit an expense")
        print("6. View total expenses")
        print("7. Clear all expenses")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            edit_expense()
        elif choice == "6":
            total_expense()
        elif choice == "7":
            clear_all_expenses()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()
