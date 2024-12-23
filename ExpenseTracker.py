import os

# Define the filename for storing expenses
expense_file = "expenses.csv"

def add_expense():
    """Adds a new expense to the CSV file."""
    # Collect expense details from the user
    date = input("Date (DD-MM-YYYY): ")
    category = input("Category (e.g., Food, Travel): ")
    description = input("Description: ")
    amount = input("Amount: ")

    # Create a new expense entry formatted as CSV
    expense = f"{date},{category},{description},{amount}\n"

    # Open the file in append mode to add the new expense
    with open(expense_file, 'a') as file:
        file.write(expense)
    
    print("Expense added!")

def view_expenses():
    """Displays all recorded expenses."""
    # Check if the expense file exists
    if not os.path.exists(expense_file):
        print("No expenses recorded.")
        return

    # Open the file in read mode
    with open(expense_file, 'r') as file:
        print("Date       | Category   | Description       | Amount")
        print("-" * 50)

        # Read and display each expense
        for line in file:
            # Split the line into components
            date, category, description, amount = line.strip().split(",")
            print(f"{date}  | {category:10} | {description:15} | {amount}")

def filter_by_category():
    """Filters and displays expenses by category."""
    # Check if the expense file exists
    if not os.path.exists(expense_file):
        print("No expenses found.")
        return

    # Ask the user for the category to filter
    category = input("Category to filter by: ")
    total = 0  # Initialize total amount for the filtered category

    # Open the file in read mode
    with open(expense_file, 'r') as file:
        print("Date       | Category   | Description       | Amount")
        print("-" * 50)

        # Read and display expenses that match the category
        for line in file:
            date, cat, description, amount = line.strip().split(",")
            # Check if the category matches (case insensitive)
            if cat.lower() == category.lower():
                print(f"{date}  | {cat:10} | {description:15} | {amount}")
                total += float(amount)  # Sum up the amounts

    print(f"\nTotal in {category}: {total}")  # Display total amount for the category

def delete_expense():
    """Deletes an expense based on the provided date."""
    # Check if the expense file exists
    if not os.path.exists(expense_file):
        print("No expenses to delete.")
        return

    view_expenses()  # Display all expenses to the user
    date_to_delete = input("Date of the expense to delete (DD-MM-YYYY): ")

    # Open the file to read existing expenses
    with open(expense_file, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    # Open the file in write mode to rewrite without the deleted expense
    with open(expense_file, 'w') as file:
        deleted = False  # Flag to check if an expense was deleted
        for line in lines:
            # If the line doesn't contain the date to delete, keep it
            if date_to_delete not in line:
                file.write(line)
            else:
                deleted = True  # Set the flag if an expense was deleted

    if deleted:
        print(f"Expense on {date_to_delete} deleted.")  # Confirm deletion
    else:
        print("No matching expense found.")  # No expense found for deletion

def edit_expense():
    """Edits an existing expense based on the provided date."""
    # Check if the expense file exists
    if not os.path.exists(expense_file):
        print("No expenses to edit.")
        return

    view_expenses()  # Display all expenses to the user
    date_to_edit = input("Date of the expense to edit (DD-MM-YYYY): ")

    # Open the file to read existing expenses
    with open(expense_file, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    # Open the file in write mode to rewrite with updated expense information
    with open(expense_file, 'w') as file:
        updated = False  # Flag to check if an expense was updated
        for line in lines:
            # If the line contains the date to edit, prompt for new values
            if date_to_edit in line:
                category = input("New category: ")
                description = input("New description: ")
                amount = input("New amount: ")
                # Create a new formatted expense entry
                updated_expense = f"{date_to_edit},{category},{description},{amount}\n"
                file.write(updated_expense)  # Write the updated expense
                updated = True  # Set the flag indicating an update
            else:
                file.write(line)  # Keep the original line

    if updated:
        print("Expense updated.")  # Confirm update
    else:
        print("No matching expense found.")  # No expense found for editing

def total_expense():
    """Calculates and displays the total of all expenses."""
    # Check if the expense file exists
    if not os.path.exists(expense_file):
        print("No expenses recorded.")
        return

    total = 0  # Initialize total amount
    with open(expense_file, 'r') as file:
        # Sum up all expense amounts
        for line in file:
            _, _, _, amount = line.strip().split(",")
            total += float(amount)  # Add to total

    print(f"Total expenses: {total}")  # Display total expenses

def clear_all_expenses():
    """Clears all expenses from the CSV file."""
    # Check if the expense file exists
    if not os.path.exists(expense_file):
        print("No expenses to clear.")
        return

    confirm = input("Are you sure you want to clear all expenses? (yes/no): ")
    if confirm.lower() == 'yes':
        # Clear the file content by opening it in write mode
        with open(expense_file, 'w'):
            pass
        print("All expenses cleared.")  # Confirm clearing
    else:
        print("Action cancelled.")  # Cancelled by the user

def main():
    """Main loop for the expense tracker application."""
    while True:
        # Display the menu options to the user
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

        # Call the corresponding function based on user choice
        if choice == "1":
            add_expense()  # Add a new expense
        elif choice == "2":
            view_expenses()  # View all expenses
        elif choice == "3":
            filter_by_category()  # Filter expenses by category
        elif choice == "4":
            delete_expense()  # Delete an expense
        elif choice == "5":
            edit_expense()  # Edit an existing expense
        elif choice == "6":
            total_expense()  # View total expenses
        elif choice == "7":
            clear_all_expenses()  # Clear all expenses
        elif choice == "8":
            print("Goodbye!")  # Exit message
            break
        else:
            print("Invalid option. Try again.")  # Invalid choice handling

# Run the main function to start the program
main()
