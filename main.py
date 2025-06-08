import json
from expense_manager import ExpenseManager

def main():
    manager = ExpenseManager('expenses.json')
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == '1':
            category = input("Category: ")
            amount = float(input("Amount: "))
            manager.add_expense(category, amount)
            print("Expense added.")
        elif choice == '2':
            expenses = manager.get_expenses()
            if not expenses:
                print("No expenses recorded.")
            else:
                for e in expenses:
                    print(f"{e['category']}: ₹{e['amount']}")
        elif choice == '3':
            summary = manager.get_summary()
            print("Summary (Category: Total Amount):")
            for cat, total in summary.items():
                print(f"{cat}: ₹{total}")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
