class SavingsAccount:
    def __Init__(self):
        self.balance = 0
        print("--- Account created with balance $0 ---")

    def Deposit(self, amount):
        try:
            # 1. Validate that input is a number
            if not isinstance(amount, (int, float)):
                return "Error: The amount must be a number."

            # 2. Validate that amount is positive
            if amount <= 0:
                return "Error: The amount must be greater than zero."

            # 3. Perform Deposit
            self.balance += amount
            return f"Success: Deposited ${amount}. New balance: ${self.balance}"

        except Exception as e:
            return f"System Error: {str(e)}"

#  MAIN EXECUTION BLOCK (For Testing) 
if __name__ == "__main__":
    # Create the account
    my_account = SavingsAccount()
    
    # Test: Deposit valid amount
    print(my_account.Deposit(500))
    
    # Test: Deposit invalid amount (text)
    print(my_account.Deposit("hello"))