# Phase 1
# Goal: Basic Input, Variables, and Math

def main():
    print("💰 SIMPLE EXPENSE TRACKER 💰")
    print("----------------------------")

    # 1. Get user input for salary
    salary = input("Enter your total monthly salary: ")
    
    # 2. Convert string to a number
    salary = float(salary)

    # 3. Get expense details
    expense_name = input("What did you buy? ")
    expense_amount = float(input(f"How much did the {expense_name} cost? "))

    # 4. The Logic (Math)
    remaining_balance = salary - expense_amount

    # 5. Output the result
    print("\n----------------------------")
    print(f"Income:   ${salary}")
    print(f"Spent:    ${expense_amount} on {expense_name}")
    print(f"Balance:  ${remaining_balance}")
    print("----------------------------")

# This line runs the program
if __name__ == "__main__":
    main()