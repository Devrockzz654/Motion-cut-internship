class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def view_expenses(self):
        total = 0
        print("Expense Tracker")
        print("----------------")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")
            total += amount
        print("----------------")
        print(f"Total: ${total}")

    def delete_expense(self, category):
        if category in self.expenses:
            del self.expenses[category]
            print(f"{category} expense deleted successfully.")
        else:
            print(f"No expense found for {category}.")

# Sample usage
def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully.")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            category = input("Enter category to delete: ")
            tracker.delete_expense(category)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()