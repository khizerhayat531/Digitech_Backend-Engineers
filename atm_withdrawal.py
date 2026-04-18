def withdraw(balance, amount):
    # Check if amount is a multiple of 500
    if amount % 500 != 0:
        print("Error: Amount must be a multiple of 500.")
        return balance
    
    # Check if amount is valid and within balance limits
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrawal successful! Remaining balance: {balance}")
    else:
        print("Error: Invalid amount or insufficient funds.")
        
    return balance

# Initial Setup
CORRECT_PIN = "1234"
user_pin = input("Enter your PIN: ")

if user_pin != CORRECT_PIN:
    print("Wrong PIN. Access denied.")
else:
    current_balance = float(input("Enter your account balance: "))
    
    while True:
        try:
            withdraw_amount = float(input("\nEnter amount to withdraw (or 0 to exit): "))
            
            if withdraw_amount == 0:
                print("Exiting program.")
                break
                
            current_balance = withdraw(current_balance, withdraw_amount)
            
        except ValueError:
            print("Please enter a valid numeric value.")
