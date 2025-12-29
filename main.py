# Phase 1
# ✨ Goal — Basic Input, Variables & Simple Math ✨

# ANSI color/style codes for terminals (works on most Linux/macOS terminals)
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
BLUE_BLACK = "\033[34m"
MAGENTA = "\033[35m"
RED = "\033[31m"

def format_currency(value):
    return f"${value:,.2f}"

def read_float(prompt):
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print(f"{RED}Please enter a valid number.{RESET}")

def main():
    print(f"{BOLD}{CYAN}💰 SIMPLE EXPENSE TRACKER 💰{RESET}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # 1. Get user input for salary (with validation)
    salary = read_float(f"{BLUE_BLACK}Enter your total monthly salary: {RESET}")

    # 2. Get expense details
    expense_name = input(f"{BLUE_BLACK}What did you buy? {RESET}")
    expense_amount = read_float(f"{BLUE_BLACK}How much did the {expense_name} cost? {RESET}")

    # 3. The Logic (Math)
    remaining_balance = salary - expense_amount

    # 4. Output the nicely formatted result
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Income:   {GREEN}{format_currency(salary)}{RESET}")
    print(f"Spent:    {RED}{format_currency(expense_amount)}{RESET} on {BOLD}{expense_name}{RESET}")
    print(f"Balance:  {MAGENTA}{format_currency(remaining_balance)}{RESET}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# This line runs the program
if __name__ == "__main__":
    main()